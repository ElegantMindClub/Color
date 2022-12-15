

from __future__ import absolute_import, division
import psychopy
psychopy.useVersion('latest')
from psychopy import locale_setup, prefs, sound, gui, visual, core, data, event, logging, clock, monitors
import numpy as np
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle
from psychopy.hardware import keyboard
import os, time, csv, random

green= [0,255,0]
red= [255,0,0]
blue=[0,0,255]
yellow=[255,255,0]

angles = [0]
directions = [0, 2] #0 is right, 2 is left
colors=[yellow, red]
trials = 60

def csvOutput(output, fileName):
    with open(fileName, 'a', newline='') as csvFile:
        writer = csv.writer(csvFile)
        writer.writerow(output)
    csvFile.close()
    
def csvInput(fileName):
    with open(fileName) as csvFile:
        reader = csv.DictReader(csvFile, delimiter = ',')
        dict = next(reader)
    csvFile.close()
    return dict

_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)
gaborfile = os.path.join(os.getcwd(), 'eccentricity_monitor_calibration.csv')
if not os.path.isfile(gaborfile):
    print('You must run the eccentricity_calibration.py script to set up your monitor')
    time.sleep(5)
    core.quit()

tvInfo = csvInput(gaborfile)

distToScreen = float(tvInfo['Distance to screen'])
heightMult, spacer = float(tvInfo['height']), float(tvInfo['spacer'])
circleMult = float(tvInfo['circleRadius'])
centerX, centerY = float(tvInfo['centerx']), float(tvInfo['centery'])
rightXMult, leftXMult = float(tvInfo['rightx']), float(tvInfo['leftx'])
rightEdge, leftEdge = float(tvInfo['rightEdge']), float(tvInfo['leftEdge'])

def endExp():
    win.flip()
    logging.flush()
    win.close()
    core.quit()

datadlg = gui.Dlg(title='Record Data?', pos=None, size=None, style=None,\
     labelButtonOK=' Yes ', labelButtonCancel=' No ', screen=-1)
ok_data = datadlg.show()
recordData = datadlg.OK

if recordData:
    date = time.strftime("%m_%d")
    expName = 'RY Green Cue'
    expInfo = {'Subject Name': ''}
    
    dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
    if dlg.OK == False:
        core.quit()
    
    OUTPATH = os.path.join(os.getcwd(), 'Data')
    if not os.path.isdir(OUTPATH):
        os.mkdir(OUTPATH)
    
    fileName = os.path.join(OUTPATH,\
        (expInfo['Subject Name'] + '_' + date + '_' + expName + '.csv'))
        

    
headers = ['Color', 'Reaction Time (s)']
if not os.path.isfile(fileName):
    csvOutput(headers, fileName)

mon = monitors.Monitor('TV') # Change this to the name of your display monitor
mon.setWidth(float(tvInfo['Width (cm)']))
win = visual.Window(
    size=(int(tvInfo['Width (px)']), int(tvInfo['Height (px)'])), fullscr=True, screen=int(tvInfo['Screen number']), 
    winType='pyglet', allowGUI=True, allowStencil=False,
    monitor= mon, color='grey', colorSpace='rgb',
    blendMode='avg', useFBO=True, 
    units='cm')
    
def genDisplay(displayInfo):
    displayText = visual.TextStim(win=win,
    text= displayInfo['text'],
    font='Arial',
    pos=(displayInfo['xPos'], displayInfo['yPos']),
    height=displayInfo['heightCm'],
    wrapWidth=500,
    ori=0, 
    color=displayInfo['color'],
    colorSpace='rgb',
    opacity=1, 
    languageStyle='LTR',
    depth=0.0)
    return displayText
    
def displaceCalc(angle):
    angleRad = np.deg2rad(angle)
    xDisp = np.tan(angleRad)*distToScreen
    return xDisp
    
def checkcorrect(response, color):
    if response == 'escape':
        endExp()
    elif response == 'v':
        ans = [red]
    elif response == 'b':
        ans = [yellow]
    return (color in ans)

    
radius = displaceCalc(4)*circleMult
Circle = visual.Circle(
    win=win,
    units="cm",
    size = radius,
    opacity =1,
    depth=-1,
    lineColorSpace='rgb255',fillColorSpace='rgb255'
)    
Circle.contrast = 1

cue = visual.Circle(
    win=win, units='cm', 
    size=radius,
    ori=0, pos=(centerX, 0),
    lineWidth=1, lineColor=[0,255,0], lineColorSpace='rgb255',
    fillColor=[0,255,0], fillColorSpace='rgb255',
    opacity=1, depth=-1.0, interpolate=True)
cue.contrast=1

#grating = psychopy.visual.GratingStim(
#    win=win,
#    units="cm",
#    size = radius
#)    
#grating.sf = 5/radius
#grating.contrast = 1
#grating.mask = 'circle'


def instructions():
    genDisplay({'text': 'Press "V" when you see the color red',\
        'xPos': 0, 'yPos': centerY+3, 'heightCm': 1, 'color': 'white'}).draw()
    genDisplay({'text': 'and "B" when you see the color yellow',\
        'xPos': 0, 'yPos': centerY+1, 'heightCm': 1, 'color': 'white'}).draw()
    genDisplay({'text': 'Please keep your eyes fixed in the center',\
        'xPos': 0, 'yPos': centerY-1,'heightCm': 1, 'color': 'white'}).draw()
    genDisplay({'text': 'Press the spacebar to continue',\
        'xPos': 0, 'yPos': centerY-3,'heightCm': 1, 'color': 'white'}).draw()
    win.flip()
    keyy = event.waitKeys(keyList = ['space', 'escape']) 
    if keyy[0] == 'escape': 
        win.flip()
        logging.flush()
        win.close()
        core.quit()

def expBreak():
    dispInfo = {'text': 'Break', 'xPos': 0, 'yPos': centerY+4, 'heightCm': 3, 'color': 'white'}
    breakText = genDisplay(dispInfo)
    dispInfo = {'text': '', 'xPos': 0, 'yPos': centerY, 'heightCm': 3, 'color': 'white'}
    for i in range(20):
        breakText.draw()
        dispInfo['text'] = str(20-i) + ' seconds'
        genDisplay(dispInfo).draw()
        win.flip()
        time.sleep(1)
        
def inBounds(trialInfo):
    if trialInfo['dir'] == 0:
        if (centerX + displaceCalc(trialInfo['angle'])) > rightEdge:
            return False
    elif trialInfo['dir'] == 2:
        if (centerX - displaceCalc(trialInfo['angle'])) < (-leftEdge):
            return False
    return True

def genPairs():
    pairs = list(range(0))
    for i in range(trials):
        for j in range(len(angles)): # Loop through angles
            for k in range(len(directions)): # Loop through directions
                # Append (angle index * 10) + direction index to pairs
                pairs.append((j*10)+k) 
    shuffle(pairs) # Randomize the pairs list
    return pairs
    
def interpretPair(pair):
    direction = directions[int(pair%10)]
    color = random.choice(colors)
    return {'dir': direction, 'color': color, 'angle':0}
   
    
instructions()

pairs = genPairs()




#correct = 0
#incorrect = 1

run = 0
mistakes = 0

stimheight = displaceCalc(4)*heightMult

mistakedict = {}

for pair in pairs:
    win.flip()
    trialInfo = interpretPair(pair)
    if not inBounds(trialInfo):
        continue
        
        
    time.sleep(random.uniform(.3,.8))

    cue.pos = (0,centerY)
    cue.draw()
    win.flip()
    
    time.sleep(.2)
    win.flip()
    
    interstimulus = random.uniform(.3,.8)
    time.sleep(interstimulus)
    
    #interstimulus = random.uniform(.5,1)
    #time.sleep(interstimulus)
    Circle.lineColor = trialInfo['color']
    Circle.fillColor = trialInfo['color']
    displacement = 0
    if trialInfo['dir'] == 0:
        xPos = centerX + displacement*rightXMult
    elif trialInfo['dir'] ==2:
        xPos = centerX + displacement*leftXMult
    Circle.pos = (xPos, centerY)
    #Change to color, ShapeStim
    Circle.draw()
    
    times = {'start': 0, 'end': 0}
    win.timeOnFlip(times, 'start')
    win.flip()
    keys = event.waitKeys(timeStamped = True, keyList = ['b', 'v', 'escape'])
    key = keys[0]
    if key[0] == 'escape':
        endExp()
    times['end'] = key[1]
    reactionTime = times['end'] - times['start']
    buffer = 2.3 - interstimulus - reactionTime
    if buffer > 0:
        if checkcorrect(key[0], trialInfo['color']):
            output = (trialInfo['color'], reactionTime)
            csvOutput(output, fileName)
        else:
            mistakedict[mistakes] = trialInfo
            mistakes += 1
            output = (trialInfo['color'], 0)
            csvOutput(output, fileName)
    else:
        mistakedict[mistakes] = trialInfo
        mistakes += 1
        output = (trialInfo['color'], 0)
        csvOutput(output, fileName)
    run += 1
    win.flip()
    if run%52 == 0 and run != 208:
        expBreak()


run2 = 0
if mistakes > 0:
    genDisplay({'text': 'These trials are a make-up of your mistakes',\
        'xPos': 0, 'yPos': centerY+5, 'heightCm': 1, 'color': 'white'}).draw()
    genDisplay({'text': 'Please follow the same instructions',\
        'xPos': 0, 'yPos': centerY+3, 'heightCm': 1, 'color': 'white'}).draw()
    genDisplay({'text': 'and press Space to continue',\
        'xPos': 0, 'yPos': centerY+1, 'heightCm': 1, 'color': 'white'}).draw()
    win.flip()
    keyyy = event.waitKeys(keyList = ['space', 'escape'])
    if keyyy[0] == 'escape': 
        win.flip()
        logging.flush()
        win.close()
        core.quit()
    l = 0
    while l < mistakes:
        win.flip()
        trialInfo = mistakedict[l]
        if not inBounds(trialInfo):
            continue
            
        
        time.sleep(random.uniform(.3,.8))

        cue.pos = (0,centerY)
        cue.draw()
        win.flip()
    
        time.sleep(.2)
        win.flip()
    
        interstimulus = random.uniform(.3,.8)
        time.sleep(interstimulus)
    
        #interstimulus = random.uniform(.5,1)
        #time.sleep(interstimulus)
        
        Circle.lineColor = trialInfo['color']
        Circle.fillColor = trialInfo['color']
        displacement = 0
        if trialInfo['dir'] == 0:
            xPos = centerX + displacement*rightXMult
        elif trialInfo['dir'] ==2:
            xPos = centerX + displacement*leftXMult
        Circle.pos = (xPos, centerY)
        #Change to color, ShapeStim
        Circle.draw()
        times = {'start': 0, 'end': 0}
        win.timeOnFlip(times, 'start')
        win.flip()
        keys = event.waitKeys(timeStamped = True, keyList = ['b', 'v', 'escape'])
        key2 = keys[0]
        if key2[0] == 'escape':
            endExp()
        times['end'] = key2[1]
        reactionTime2 = times['end'] - times['start']
        buffer2 = 2.3 - interstimulus - reactionTime
        if buffer2 > 0:
            if checkcorrect(key2[0], trialInfo['color']):
                output = (trialInfo['color'], reactionTime2)
                csvOutput(output, fileName)
            else:
                mistakedict[mistakes] = trialInfo
                mistakes += 1
                output = (trialInfo['color'],0)
                csvOutput(output, fileName)
        else:
            mistakedict[mistakes] = trialInfo
            mistakes += 1
            output = (trialInfo['color'], 0)
            csvOutput(output, fileName)
        run2 += 1
        l += 1
        win.flip()
        if run2%52 == 0:
            expBreak()


strmistakes = str(mistakes)
print(strmistakes + ' mistakes')
endExp()


