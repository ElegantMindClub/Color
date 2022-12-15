#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2020.1.2),
    on Tue Aug 18 12:46:08 2020
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

from __future__ import absolute_import, division

from psychopy import locale_setup
from psychopy import prefs
from psychopy import sound, gui, visual, core, data, event, logging, clock
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle
import os  # handy system and path functions
import sys  # to get file system encoding

from psychopy.hardware import keyboard



# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)

# Store info about the experiment session
psychopyVersion = '2020.1.2'
expName = 'DualColor_red_yellow'  # from the Builder filename that created this script
expInfo = {'gender (m/f)': '', 'age': '', 'participant': ''}
dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data' + os.sep + '%s_%s' %(expInfo['participant'], expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='/Users/megan/Downloads/ColorCenterExperiment2.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame

# Start Code - component code to be run before the window creation

# Setup the Window
win = visual.Window(
    size=[1920, 1080], fullscr=True, screen=0, 
    winType='pyglet', allowGUI=True, allowStencil=False,
    monitor='TV', color=[0,0,0], colorSpace='rgb',
    blendMode='avg', useFBO=True, 
    units='norm')
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard()

# Initialize components for Routine "Instructions"
InstructionsClock = core.Clock()
ExperimentInstructions = visual.TextStim(win=win, name='ExperimentInstructions',
    text="Press 'f' if you see red\nPress 'j' if you see yellow\nPress any key to continue",
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
ContinueColor = keyboard.Keyboard()

# Initialize components for Routine "GaborRoutine"
GaborRoutineClock = core.Clock()
import random
import numpy as np
random.seed()
Cross = visual.ShapeStim(
    win=win, name='Cross', vertices='cross',units='deg', 
    size=(1, 1),
    ori=0, pos=(0, 0),
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[1,1,1], fillColorSpace='rgb',
    opacity=1, depth=-1.0, interpolate=True)
polygon_2 = visual.Polygon(
    win=win, name='polygon_2',units='deg', 
    edges=999, size=(2.74,2.74), #change to 3.5cm diameter according to ruler
    ori=0, pos=(0, 0),
    lineWidth=1, lineColor=1.0, lineColorSpace='rgb255',
    fillColor=1.0, fillColorSpace='rgb255',
    opacity=1, depth=-2.0, interpolate=True)
key_resp_3 = keyboard.Keyboard()
trialNumber = 0
targetNumber = 100
trials = 0

# Initialize components for Routine "thanks"
thanksClock = core.Clock()
thanksText = visual.TextStim(win=win, name='thanksText',
    text='This is the end of the experiment.\n\nThanks!',
    font='arial',
    pos=[0, 0], height=0.3, wrapWidth=None, ori=0, 
    color=[1, 1, 1], colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "Instructions"-------
continueRoutine = True
# update component parameters for each repeat
ContinueColor.keys = []
ContinueColor.rt = []
_ContinueColor_allKeys = []
# keep track of which components have finished
InstructionsComponents = [ExperimentInstructions, ContinueColor]
for thisComponent in InstructionsComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
InstructionsClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "Instructions"-------
while continueRoutine:
    # get current time
    t = InstructionsClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=InstructionsClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *ExperimentInstructions* updates
    if ExperimentInstructions.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        ExperimentInstructions.frameNStart = frameN  # exact frame index
        ExperimentInstructions.tStart = t  # local t and not account for scr refresh
        ExperimentInstructions.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(ExperimentInstructions, 'tStartRefresh')  # time at next scr refresh
        ExperimentInstructions.setAutoDraw(True)
    
    # *ContinueColor* updates
    waitOnFlip = False
    if ContinueColor.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        ContinueColor.frameNStart = frameN  # exact frame index
        ContinueColor.tStart = t  # local t and not account for scr refresh
        ContinueColor.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(ContinueColor, 'tStartRefresh')  # time at next scr refresh
        ContinueColor.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(ContinueColor.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(ContinueColor.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if ContinueColor.status == STARTED and not waitOnFlip:
        theseKeys = ContinueColor.getKeys(keyList=None, waitRelease=False)
        _ContinueColor_allKeys.extend(theseKeys)
        if len(_ContinueColor_allKeys):
            ContinueColor.keys = _ContinueColor_allKeys[-1].name  # just the last key pressed
            ContinueColor.rt = _ContinueColor_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in InstructionsComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Instructions"-------
for thisComponent in InstructionsComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "Instructions" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
trials = data.TrialHandler(nReps=100, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=[None],
    seed=None, name='trials')
thisExp.addLoop(trials)  # add the loop to the experiment
thisTrial = trials.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
if thisTrial != None:
    for paramName in thisTrial:
        exec('{} = thisTrial[paramName]'.format(paramName))

for thisTrial in trials:
    currentLoop = trials
    # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
    if thisTrial != None:
        for paramName in thisTrial:
            exec('{} = thisTrial[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "GaborRoutine"-------
    continueRoutine = True
    # update component parameters for each repeat
    delay2=random.randint(300,800)/1000
    
    correctKey = ['f','j']
    
    color = random.randint(1,2)
    
    if  color == 1:
        r = 255
        g = 0
        b = 0
        correctKey = 'f'
    if color == 2:
        r = 255
        g = 255
        b = 0
        correctKey = 'j'
    polygon_2.setFillColor([r,g,b])
    polygon_2.setLineColor([r,g,b])
    key_resp_3.keys = []
    key_resp_3.rt = []
    _key_resp_3_allKeys = []
    
        
    # keep track of which components have finished
    GaborRoutineComponents = [Cross, polygon_2, key_resp_3]
    for thisComponent in GaborRoutineComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    GaborRoutineClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "GaborRoutine"-------
    while continueRoutine:
        # get current time
        t = GaborRoutineClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=GaborRoutineClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *Cross* updates
        if Cross.status == NOT_STARTED and tThisFlip >= 1.00-frameTolerance:
            # keep track of start time/frame for later
            Cross.frameNStart = frameN  # exact frame index
            Cross.tStart = t  # local t and not account for scr refresh
            Cross.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Cross, 'tStartRefresh')  # time at next scr refresh
            Cross.setAutoDraw(True)
        if Cross.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > Cross.tStartRefresh + 0.2-frameTolerance:
                # keep track of stop time/frame for later
                Cross.tStop = t  # not accounting for scr refresh
                Cross.frameNStop = frameN  # exact frame index
                win.timeOnFlip(Cross, 'tStopRefresh')  # time at next scr refresh
                Cross.setAutoDraw(False)
        
        # *polygon_2* updates
        if polygon_2.status == NOT_STARTED and tThisFlip >= 1.2+delay2-frameTolerance:
            # keep track of start time/frame for later
            polygon_2.frameNStart = frameN  # exact frame index
            polygon_2.tStart = t  # local t and not account for scr refresh
            polygon_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(polygon_2, 'tStartRefresh')  # time at next scr refresh
            polygon_2.setAutoDraw(True)
        
        # *key_resp_3* updates
        if key_resp_3.status == NOT_STARTED and t >= delay2+1.2-frameTolerance:
            # keep track of start time/frame for later
            key_resp_3.frameNStart = frameN  # exact frame index
            key_resp_3.tStart = t  # local t and not account for scr refresh
            key_resp_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_3, 'tStartRefresh')  # time at next scr refresh
            key_resp_3.status = STARTED
            # keyboard checking is just starting
            key_resp_3.clock.reset()  # now t=0
            key_resp_3.clearEvents(eventType='keyboard')
        if key_resp_3.status == STARTED:
            theseKeys = key_resp_3.getKeys(keyList=['f', 'j'], waitRelease=False)
            _key_resp_3_allKeys.extend(theseKeys)
            if len(_key_resp_3_allKeys):
                key_resp_3.keys = _key_resp_3_allKeys[0].name  # just the first key pressed
                key_resp_3.rt = _key_resp_3_allKeys[0].rt
                # was this correct?
                if (key_resp_3.keys == str(correctKey)) or (key_resp_3.keys == correctKey):
                    key_resp_3.corr = 1
                else:
                    key_resp_3.corr = 0
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in GaborRoutineComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "GaborRoutine"-------
    for thisComponent in GaborRoutineComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials.addData('polygon_2.started', polygon_2.tStartRefresh)
    trials.addData('polygon_2.stopped', polygon_2.tStopRefresh)
    # check responses
    if key_resp_3.keys in ['', [], None]:  # No response was made
        key_resp_3.keys = None
        # was no response the correct answer?!
        if str(correctKey).lower() == 'none':
           key_resp_3.corr = 1;  # correct non-response
        else:
           key_resp_3.corr = 0;  # failed to respond (incorrectly)
    # store data for trials (TrialHandler)
    trials.addData('key_resp_3.keys',key_resp_3.keys)
    trials.addData('key_resp_3.corr', key_resp_3.corr)
    if key_resp_3.keys != None:  # we had a response
        trials.addData('key_resp_3.rt', key_resp_3.rt)
    if (key_resp_3.keys == str(correctKey)) or (key_resp_3.keys == correctKey):
        trialNumber = trialNumber+1
    if trialNumber == 100:
        trials.finished = True
    # the Routine "GaborRoutine" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 100 repeats of 'trials'

# get names of stimulus parameters
if trials.trialList in ([], [None], None):
    params = []
else:
    params = trials.trialList[0].keys()
# save data for this loop
trials.saveAsExcel(filename + '.xlsx', sheetName='trials',
    stimOut=params,
    dataOut=['n','all_mean','all_std', 'all_raw'])

# ------Prepare to start Routine "thanks"-------
continueRoutine = True
routineTimer.add(2.000000)
# update component parameters for each repeat
# keep track of which components have finished
thanksComponents = [thanksText]
for thisComponent in thanksComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
thanksClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "thanks"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = thanksClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=thanksClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *thanksText* updates
    if thanksText.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        thanksText.frameNStart = frameN  # exact frame index
        thanksText.tStart = t  # local t and not account for scr refresh
        thanksText.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(thanksText, 'tStartRefresh')  # time at next scr refresh
        thanksText.setAutoDraw(True)
    if thanksText.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > thanksText.tStartRefresh + 2.0-frameTolerance:
            # keep track of stop time/frame for later
            thanksText.tStop = t  # not accounting for scr refresh
            thanksText.frameNStop = frameN  # exact frame index
            win.timeOnFlip(thanksText, 'tStopRefresh')  # time at next scr refresh
            thanksText.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in thanksComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "thanks"-------
for thisComponent in thanksComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)

# Flip one final time so any remaining win.callOnFlip() 
# and win.timeOnFlip() tasks get executed before quitting
win.flip()

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
