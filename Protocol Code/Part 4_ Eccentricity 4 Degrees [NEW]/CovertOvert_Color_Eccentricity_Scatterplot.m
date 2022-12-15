%VA Color Experiment 4.5 (4, new): Covert/Overt RT vs. Eccentricity & Color 
%Created by Meera McAdam, 9/22/20
%Most recent edit: 9/22/20

%Takes raw data input and will display & save a graph of RT vs.
%Eccentricity. Can do any combination of color scenarios.

clear variables

    %%%STEP ONE: Put your .csv files in the same folder as the MATLAB script.
    %%%Pick which target color you are going to compare across experiments
    %%%(e.g. Blue for 2-choice, 3-choice and 4-choice experiment data)
    
    %%%CHANGE THE BELOW TWO VARIABLES TO YOUR NAME, AND THE COLOR.
      subjectname = "Megan";
      targetcolor = "Red";
      
    %%%STEP TWO: Set filenames to your data for the respective number of choices (1,2,3).
    %%%Remember to put .csv at the end.
      
      filename_overt = "Megan_Overt_red_09_21_Color_RT_Eccentricity.csv";
      filename_covert = "Megan_Covert_red_09_21_Color_RT_Eccentricity.csv";
      
      %Now press Run!
           
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

    %Set color variables equal to RGB strings in raw data
    %use targetcolor for string, use colorval.() for value

            
    %Import .csv data into MATLAB as tables
        RT_O_Table = readtable(filename_overt,'ReadVariableNames',0,'HeaderLines',1);
        RT_C_Table = readtable(filename_covert,'ReadVariableNames',0,'HeaderLines',1);
          
    %Extract the Direction, Eccentricity, & Reaction Time data columns,
    %discard any data that is not the target color,
    %and discard any data that has an incorrect key press.
        RT = cell(2,1); %cells to hold reaction time for overt(1), covert(2)
        RT{1} = RT_O_Table{RT_O_Table.Var5==1,[2,3,4,6]};
        RT{2} = RT_C_Table{RT_C_Table.Var5==1,[2,3,4,6]};
    
      
    for i=1:2
        %Multiply the third column by 1000 to make it milliseconds
        RT{i}(:,3) = RT{i}(:,3) * 1000;

        %Set eccentricity values as negative or positive depending on L/R direction
        RT{i}(:,2) = (RT{i}(:,1) - 1) .* RT{i}(:,2);

        %Remove direction column since it is no longer needed
        RT{i} = RT{i}(:,2:4);
    end
    
   %Create eccentricity vector and sort by eccentricity
   %creates a table with headers as eccentricity
   RT_stats = cell(2,3);
    for i=1:2 %overt/covert
        for col=1:3 %number of colors
        RT_stats{i,col} = [];
            for ecc_interv = -40:5:40 %eccentricities
                %Extract reaction times for specific number of colors and
                %eccentricity
                rownum = (RT{i}(:,1) == ecc_interv & RT{i}(:,3) == col);
                RT_ecc = RT{i}(rownum,2); 
                
                if ~isempty(RT_ecc)
                    %Remove outliers based on quartiles(Per eccentricity, per 
                    %number colors, and per overt/covert)
                    RT_ecc = rmoutliers(RT_ecc, 'quartiles');
                    %Statistical Analysis: mean, standard deviation, standard error
                    RT_mean = mean(RT_ecc);
                    RT_SD = std(RT_ecc);
                    RT_SE = RT_SD/sqrt(length(RT_ecc));
                    RT_stats{i,col} = [RT_stats{i,col},[ecc_interv;RT_mean;RT_SD;RT_SE]];
                end
            end
        end
    end
        

    
    %Make scatter plots
    p = cell(2,3);
    plot_colors = ['r','g','b';'m','k','c'];
    for ov = 1:2 %overt or covert
        for i=1:3 %1,2,3 colors 
            %plot data points
            scatter(RT_stats{ov,i}(1,:), RT_stats{ov,i}(2,:), 'filled', plot_colors(ov,i));
            hold on 
            errorbar(RT_stats{ov,i}(1,:), RT_stats{ov,i}(2,:), RT_stats{ov,i}(4,:), 'vertical', 'o', 'Color', plot_colors(ov,i));

            %draw line
            xline(0);

            %negative eccentricities using linear fit
            neg_cols = (RT_stats{ov,i}(1,:) <= 0);
            Best_fit_neg_i = polyfit(RT_stats{ov,i}(1,neg_cols), RT_stats{ov,i}(2,neg_cols) , 1); %slope and intercept
            fit_neg_i = Best_fit_neg_i(1)*RT_stats{ov,i}(1,neg_cols) + Best_fit_neg_i(2); %y=ax+b

            plot(RT_stats{ov,i}(1,neg_cols), fit_neg_i, 'Color', plot_colors(ov,i));

            %positive eccentricities using linear fit
            pos_cols = (RT_stats{ov,i}(1,:) >= 0);
            Best_fit_pos_i = polyfit(RT_stats{ov,i}(1,pos_cols), RT_stats{ov,i}(2,pos_cols), 1);
            fit_pos_i = Best_fit_pos_i(1)*RT_stats{ov,i}(1,pos_cols) + Best_fit_pos_i(2);

            %save line handle for legend 
            p{ov,i} = plot(RT_stats{i}(1,pos_cols),fit_pos_i, 'Color', plot_colors(ov,i));
        end
    end
        
    %Edit graph aesthetics 
        ylim([300 600]);
        xlim([-50 50]);

        title('RT vs Eccentricity and Color Decision-Making for ' + targetcolor );
        ylabel('Reaction Time (ms)');
        xlabel('Eccentricity (°)');   
       
    %Adjust legend to number of color choices  
        box off
        legend([p{1,1},p{1,2},p{1,3},p{2,1},p{2,2},p{2,3}], ... 
            "Overt, 1 Color", "Overt, 2 Colors", "Overt, 3 Colors", ...
                    "Covert, 1 Color", "Covert, 2 Colors", "Covert, 3 Colors",...
                    'location', 'northeastoutside');
        legend boxoff


    %Save graph to folder
        saveas(gcf,'Eccentricity&Color_MultipleScenario_' + targetcolor + '_' + subjectname + '.png')
        
    %you did it! :)
