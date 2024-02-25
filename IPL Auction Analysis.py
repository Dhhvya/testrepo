#!/usr/bin/env python
# coding: utf-8

# In[149]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# In[228]:


data=pd.read_csv("IPLData.csv")


# In[151]:


data


# In[152]:


data.describe().transpose()


# In[153]:


data.isna().sum()


# In[154]:


data.info()


# CLEANING THE DATA

# In[155]:


batters = data.loc[(data["Player_Type"] == "Batter")]
batters_new = batters.loc[(batters["Capped"] == 1)]
Capped_Batters = batters_new[['Player Name',
'Team',
'Nationality',
'Matches_Played',
'Runs',
'Average',
'Strike_Rate']]


# In[156]:


Capped_Batters.head(10)


# In[157]:


bowlers = data.loc[(data["Player_Type"] == "Bowler ")]
bowlers_new = bowlers. loc[(bowlers["Capped"] == 1)]
Capped_Bowlers = bowlers_new[['Player Name',
'Team',
'Nationality',
'Matches_Played',
'Wickets',
'Bowling_average',
'Economy',
'Bowling_Strike_Rate']]


# In[158]:


Capped_Bowlers.head(10)


# In[159]:


Keepers = data.loc[(data["Player_Type"] == "Keeper")]
Keepers_new = Keepers.loc[(Keepers["Capped"] == 1)]
Capped_Keepers = Keepers_new[['Player Name',
'Team',
'Nationality',
'Matches_Played',
'Runs',
'Average',
'Strike_Rate',
'Catches',
'Run_outs',
'Stumps']]


# In[160]:


Capped_Keepers.head(10)


# In[161]:


Allrounders = data.loc[(data["Player_Type"] == "Allrounder")]
Allrounders_new = Allrounders.loc[(Allrounders["Capped"] == 1)]
Capped_Allrounders = Allrounders_new[['Player Name',
'Team',
'Nationality',
'Matches_Played',
'Runs',
'Average',
'Strike_Rate',
'Wickets',
'Bowling_average',
'Economy',
'Bowling_Strike_Rate']]


# In[162]:


Capped_Allrounders.head(10)


# In[163]:


Capped_Batters = Capped_Batters.fillna(0)
Capped_Bowlers = Capped_Bowlers.fillna(0)
Capped_Allrounders = Capped_Allrounders.fillna(0)
Capped_Keepers = Capped_Keepers.fillna(0)


# In[164]:


print(Capped_Batters.isna().sum())
print(Capped_Bowlers.isna().sum())
print(Capped_Allrounders.isna().sum())
print(Capped_Keepers.isna().sum())


# INITIAL ANALYSIS

# In[165]:


#Narrowing our analysis to batters who have a batting average more than 32
top_batters = Capped_Batters.loc[(Capped_Batters["Average"] >= 32.0)]

#Sorting the data in descending order - with respect to each parameter
top_batters_average = top_batters. sort_values('Average', ascending=False)
top_batters_strike_rate = top_batters. sort_values ('Strike_Rate', ascending=False)
top_batters_runs = top_batters.sort_values ('Runs', ascending=False)
top_batters_matches = top_batters. sort_values ('Matches_Played', ascending=False)


# In[166]:


top_batters_average


# In[167]:


top_batters_strike_rate


# In[168]:


top_batters_runs


# In[169]:


top_batters_matches


# From our analysis, if we rank from 0-10, the top three batters that will come while analysis each of the above data are:
# 1. KL Rahul
# 2. David Warner
# 3. Virat Kohli

# In[170]:


#there we have narrowed our analysis based on the bowling averages of the players to be less than 24.0
top_bowlers = Capped_Bowlers.loc[(Capped_Bowlers ["Bowling_average"] <= 24.0)]
top_bowlers_average = top_bowlers.sort_values ('Bowling_average')
top_bowlers_strike_rate = top_bowlers.sort_values ('Bowling_Strike_Rate')
top_bowlers_wickets = top_bowlers.sort_values ('Wickets', ascending=False)
top_bowlers_economy = top_bowlers.sort_values ('Economy')
top_bowlers_matches = top_bowlers.sort_values ('Matches_Played', ascending=False)


# In[171]:


top_bowlers_average


# In[172]:


top_bowlers_strike_rate


# In[173]:


top_bowlers_wickets


# In[174]:


top_bowlers_economy


# In[175]:


top_bowlers_matches


# From the above analysis, if we rank down the parameters from 1-10. The top bowling options are as follows:
# 1. Kagiso Rabada
# 2. Jasprit Bumrah
# 3. Yuzvendra Chahal
# 4. Nathan Coulter-Nile

# Analyzing the Allrounder Data
# We narrowed our analysis by further segregating the allrounders based on strike rate equal to or more than 140.0.

# In[176]:


top_allrounders = Capped_Allrounders.loc[(Capped_Allrounders["Strike_Rate"] >= 140.0)]
top_allrounders_average = top_allrounders.sort_values('Average', ascending=False)
top_alrounders_strike_rate = top_allrounders.sort_values('Strike_Rate', ascending=False)
top_allrounders_runs = top_allrounders.sort_values('Runs', ascending=False)
top_allrounders_matches = top_allrounders.sort_values('Matches_Played', ascending=False)
top_allrounders_bowling_average = top_allrounders.sort_values('Bowling_average')
top_allrounders_bowling_strike_rate = top_allrounders.sort_values('Bowling_Strike_Rate')
top_allrounders_wickets = top_allrounders.sort_values('Wickets', ascending=False)
top_allrounders_economy = top_allrounders.sort_values ('Economy')
top_allrounders_matches = top_allrounders.sort_values ('Matches_Played', ascending=False)


# In[177]:


top_allrounders_average


# In[178]:


top_alrounders_strike_rate


# In[179]:


top_allrounders_runs


# In[180]:


top_allrounders_matches


# In[181]:


top_allrounders_bowling_average


# In[182]:


top_allrounders_bowling_strike_rate


# In[183]:


top_allrounders_wickets


# In[184]:


top_allrounders_economy


# From the above analysis, if we rank down the allrounders from 1-10 on various parameters. The top allrounder options are as follows
# 1. Andre Russell
# 2. Sunil Narine
# 3. Hardik Pandya
# 4. Jofra Archer

# In[185]:


#Analyzing the Keepers Data
#we have narrowed our analysis down to keepers averaging more than 25.0
top_keepers = Capped_Keepers.loc[(Capped_Keepers["Average"] >= 25.0)]

#Sorting the data in descending order - with respect to each parameter.
top_Keepers_average = top_keepers.sort_values ('Average', ascending=False)
top_Keepers_strike_rate = top_keepers.sort_values('Strike_Rate', ascending=False)
top_Keepers_runs = top_keepers.sort_values ('Runs', ascending=False)
top_Keepers_matches = top_keepers.sort_values( 'Matches_Played', ascending=False)
top_Keepers_catches = top_keepers.sort_values ('Catches', ascending=False)
top_Keepers_runouts = top_keepers.sort_values('Run_outs', ascending=False)
top_Keepers_stumps = top_keepers.sort_values ('Stumps', ascending=False)


# In[186]:


top_Keepers_average


# In[187]:


top_Keepers_strike_rate


# In[188]:


top_Keepers_runs


# In[189]:


top_Keepers_matches


# In[190]:


top_Keepers_catches


# In[191]:


top_Keepers_runouts


# In[192]:


top_Keepers_stumps 


# If we rank the keepers in order of 1-10 on the above parameters. The top 3 keepers will be
# 1. MS Dhoni
# 2. Dinesh Karthik
# 3. Rishabh Pant

# VISUALIZATION FOR ENHANCED ANALYSIS

# In[193]:


#Visualization of Batters Data
#the plot shows each of the top batters strike rate
plt.figure(figsize=(20,10))
sns.barplot(x='Player Name', y= 'Strike_Rate', data=top_batters) 



# In[194]:


#the plot shows each of the top batters runs
plt.figure(figsize=(20,10))
sns.barplot(x='Player Name', y= 'Runs', data=top_batters) 


# In[195]:


#the plot shows each of the top batters average
plt.figure(figsize=(20,10))
sns.barplot(x='Player Name', y= 'Average', data=top_batters) 


# In[196]:


#the plot shows each of the top batters matches played
plt.figure(figsize=(20,10))
sns.barplot(x='Player Name', y= 'Matches_Played', data=top_batters) 


# In[197]:


#visualization for bowlers
#the plot shows each of the top bowlers bowling average
plt.figure(figsize=(20,10))
sns.barplot(x='Player Name', y= 'Bowling_average', data=top_bowlers) 


# In[198]:


#the plot shows each of the top bowlers Economy
plt.figure(figsize=(20,10))
sns.barplot(x='Player Name', y= 'Economy', data=top_bowlers) 


# In[199]:


#the plot shows each of the top bowlers strike rate
plt.figure(figsize=(20,10))
sns.barplot(x='Player Name', y= 'Bowling_Strike_Rate', data=top_bowlers) 


# In[200]:


#the plot shows each of the top bowlers wickets
plt.figure(figsize=(20,10))
sns.barplot(x='Player Name', y= 'Wickets', data=top_bowlers) 


# In[201]:


#the plot shows each of the top bowlers matches played
plt.figure(figsize=(20,10))
sns.barplot(x='Player Name', y= 'Matches_Played', data=top_bowlers) 


# In[202]:


#Visualization for all rounders
#this plots show the strike rate for top allrounders
plt.figure(figsize=(20,10))
sns.barplot(x='Player Name', y= 'Strike_Rate', data=top_allrounders) 


# In[203]:


#this plots show top allrounders average
plt.figure(figsize=(20,10))
sns.barplot(x='Player Name', y= 'Average', data=top_allrounders) 


# In[204]:


#this plots show the matches played by top allrounders
plt.figure(figsize=(20,10))
sns.barplot(x='Player Name', y= 'Matches_Played', data=top_allrounders) 


# In[205]:


#this plots show top allrounders runs
plt.figure(figsize=(20,10))
sns.barplot(x='Player Name', y= 'Runs', data=top_allrounders) 


# In[206]:


#this plots show top allrounders bowling average
plt.figure(figsize=(20,10))
sns.barplot(x='Player Name', y= 'Bowling_average', data=top_allrounders) 


# In[207]:


#this plots show top allrounders economy
plt.figure(figsize=(20,10))
sns.barplot(x='Player Name', y= 'Economy', data=top_allrounders) 


# In[208]:


#this plots show top allrounders bowling strike rate
plt.figure(figsize=(20,10))
sns.barplot(x='Player Name', y= 'Bowling_Strike_Rate', data=top_allrounders) 


# In[209]:


#this plots show top allrounders matches played
plt.figure(figsize=(20,10))
sns.barplot(x='Player Name', y= 'Matches_Played', data=top_allrounders) 


# In[210]:


#this plots show top allrounders economy
plt.figure(figsize=(20,10))
sns.barplot(x='Player Name', y= 'Economy', data=top_allrounders) 


# In[211]:


#this plots show top allrounders wickets
plt.figure(figsize=(20,10))
sns.barplot(x='Player Name', y= 'Wickets', data=top_allrounders) 


# In[212]:


#Visualization for keepers
#this plots show keepers average
plt.figure(figsize=(20,10))
sns.barplot(x='Player Name', y= 'Average', data=top_keepers) 


# In[213]:


#this plots show keepers average
plt.figure(figsize=(20,10))
sns.barplot(x='Player Name', y= 'Average', data=top_keepers) 


# In[214]:


#this plots show keepers runs
plt.figure(figsize=(20,10))
sns.barplot(x='Player Name', y= 'Runs', data=top_keepers) 


# In[215]:


#this plots show keepers strike rate
plt.figure(figsize=(20,10))
sns.barplot(x='Player Name', y= 'Strike_Rate', data=top_keepers) 


# In[216]:


#this plots show keepers catches
plt.figure(figsize=(20,10))
sns.barplot(x='Player Name', y= 'Catches', data=top_keepers) 


# In[217]:


#this plots show keepers runouts
plt.figure(figsize=(20,10))
sns.barplot(x='Player Name', y= 'Run_outs', data=top_keepers) 


# In[218]:


#this plots show stump done by keepers 
plt.figure(figsize=(20,10))
sns.barplot(x='Player Name', y= 'Stumps', data=top_keepers) 


# In[219]:


#this plots show keepers matches played
plt.figure(figsize=(20,10))
sns.barplot(x='Player Name', y= 'Matches_Played', data=top_keepers) 


# Forming Our Best 11 for the Campaign based on the above analysis
# 1. We will consider the number of players from each category that the 120 world cup winning 
#    and the last year's IPL winning team played in their Final matches
#    
# 2. The Australia squad consisted of - 3 Batters, 3 Allrounders, 4 Bowlers with 1 spin option and 1 wicket keeper.
# 
# 3. The Chennai Squad Consisted of - 4 Batters, 3 Allrounders, 3 Bowlers and 1 Wicket Keeper.
# 
# 4. For our final analysis we will consider the ratio of players in the best 11 as follows:
#    3 Batters 
#    3 Allrounders
#    4 Bowlers with 2 Spin Options
#    1 Wicket Keeper

# In[220]:


#Batters for the Final 11 - KL Rahul, Virat Kohli, David Warner
#here, we are storing the values of each player in a separate dataframe to use for displaying using the barplot
top_batters.reset_index(drop=True)
matches_values = [top_batters.iloc[6]['Matches_Played'], top_batters.iloc[2]['Matches_Played'], top_batters.iloc[5]['Matches_Played']]
runs_values = [top_batters.iloc[6]['Runs'], top_batters.iloc[2]['Runs'],top_batters.iloc[5]['Runs']]
average_values = [top_batters.iloc[6]['Average'], top_batters.iloc[2]['Average'],top_batters.iloc[5]['Average']]
Strike_rate_values = [top_batters.iloc[6]['Strike_Rate'],top_batters.iloc[2]['Strike_Rate'], top_batters.iloc[5]['Strike_Rate']]
Labels = ['KL Rahul', 'David Warner', 'Virat Kohli']

fig, axes = plt. subplots(2,2, figsize=(10,10))
axes[0][0].set_title("Matches Played")
axes[0][1].set_title("Runs in the IPL Career")
axes[1][0].set_title("Strike Rate")
axes[1][1].set_title("Average")
sns.barplot(x=Labels, y=matches_values, ax=axes[0][0])
sns. barplot(x=Labels, y=runs_values, ax=axes[0][1])
sns. barplot(x=Labels, y=Strike_rate_values, ax=axes[1][0])
sns. barplot(x=Labels, y=average_values, ax=axes[1][1])


# In[221]:


top_allrounders.reset_index(drop=True)
matches_values = [top_allrounders.iloc[5]['Matches_Played'],top_allrounders.iloc[9]['Matches_Played'],top_allrounders.iloc[6]['Matches_Played']]
runs_values = [top_allrounders.iloc[5]['Runs'],top_allrounders.iloc[9]['Runs'], top_allrounders. iloc[6]['Runs']]
average_values = [top_allrounders.iloc[5]['Average'],top_allrounders.iloc[9]['Average'],top_allrounders.iloc[6]['Average']]
strike_rate_values = [top_allrounders.iloc[5]['Strike_Rate'],top_allrounders.iloc[9]['Strike_Rate'],top_allrounders.iloc[6]['Strike_Rate']]
bowling_strike_rate_values = [top_allrounders.iloc[5]['Bowling_Strike_Rate'],top_allrounders.iloc[9]['Bowling_Strike_Rate'],top_allrounders.iloc[6]['Bowling_Strike_Rate']]
bowling_average_values = [top_allrounders.iloc[5]['Bowling_average'],top_allrounders.iloc[9]['Bowling_average'], top_allrounders.iloc[6]['Bowling_average']]
wickets_values = [top_allrounders.iloc[5]['Wickets'],top_allrounders.iloc[9]['Wickets'], top_allrounders. iloc[6]['Wickets']]
economy_values = [top_allrounders.iloc[5]['Economy'], top_allrounders. iloc[9]['Economy'], top_allrounders. iloc[6]['Economy']]
Labels = ['Andre Russell','Sunil Narine', 'Hardik Pandya']
fig, axes = plt.subplots(4,2, figsize=(20,20))
axes[0][0].set_title("Matches")
axes[0][1].set_title("Runs")
axes[1][0].set_title("Average")
axes[1][1].set_title("Strike Rate")
axes[2][0].set_title("Bowling Strike Rate")
axes[2][1].set_title("Bowling Average")
axes[3][0].set_title("wickets")
axes[3][1].set_title("Economy")
sns.barplot(x=Labels, y=matches_values, ax=axes[0][0])
sns.barplot(x=Labels, y=runs_values, ax=axes[0][1])
sns.barplot(x=Labels, y=average_values, ax=axes[1][0]) 
sns.barplot(x=Labels, y=strike_rate_values, ax=axes[1][1])
sns.barplot(x=Labels, y=bowling_strike_rate_values, ax=axes[2][0])
sns.barplot(x=Labels, y=bowling_average_values, ax=axes[2][1])
sns.barplot(x=Labels, y=wickets_values, ax=axes[3][0])
sns.barplot(x=Labels, y=economy_values, ax=axes[3][1])


# In[222]:


top_bowlers.reset_index(drop=True)

matches_values = [top_bowlers.iloc[10]['Matches_Played'], top_bowlers.iloc[0]['Matches_Played'], top_bowlers.iloc[7]['Matches_Played'], top_bowlers.iloc[1]['Matches_Played']]
wickets_values = [top_bowlers.iloc[10]['Wickets'], top_bowlers.iloc[0]['Wickets'], top_bowlers.iloc[7]['Wickets'], top_bowlers.iloc[1]['Wickets']]
bowling_average_values = [top_bowlers.iloc[10]['Bowling_average'], top_bowlers.iloc[0]['Bowling_average'], top_bowlers.iloc[7]['Bowling_average'], top_bowlers.iloc[1]['Bowling_average']]
bowling_strike_rate_values = [top_bowlers.iloc[10]['Bowling_Strike_Rate'], top_bowlers.iloc[0]['Bowling_Strike_Rate'], top_bowlers.iloc[7]['Bowling_Strike_Rate'], top_bowlers.iloc[1]['Bowling_Strike_Rate']]
economy_values = [top_bowlers.iloc[10]['Economy'], top_bowlers.iloc[0]['Economy'], top_bowlers.iloc[7]['Economy'], top_bowlers.iloc[1]['Economy']]

Labels = ['Jasprit Bumrah', 'Keiso Rabada', 'Nathan Coulter-Nile', 'Yuzi Chahal']

fig, axes = plt.subplots(3, 2, figsize=(15, 15))
axes[0][0].set_title("Matches Played")
axes[0][1].set_title("Wickets")
axes[1][0].set_title("Bowling Average")
axes[1][1].set_title("Bowling Strike Rate")
axes[2][0].set_title("Economy")

sns.barplot(x=Labels, y=matches_values, ax=axes[0][0])
sns.barplot(x=Labels, y=wickets_values, ax=axes[0][1])
sns.barplot(x=Labels, y=bowling_average_values, ax=axes[1][0])
sns.barplot(x=Labels, y=bowling_strike_rate_values, ax=axes[1][1])
sns.barplot(x=Labels, y=economy_values, ax=axes[2][0])


# In[223]:


matches_values = [top_keepers.iloc[8]['Matches_Played'], top_keepers.iloc[8]['Runs']]
average_values = [top_keepers.iloc[8]['Average'], top_keepers.iloc[8]['Strike_Rate']]
keeping_values = [top_keepers.iloc[8]['Catches'], top_keepers.iloc[8]['Stumps'], top_keepers.iloc[8]['Run_outs']]
label1 = ['Matches', 'Runs']
label2 = ['Average', 'Strike Rate']
label3 = ['Catches', 'Stumps', 'Run_outs']

fig, axes = plt.subplots(1, 3, figsize=(20, 10))
axes[0].set_title("Matches And Runs")
axes[1].set_title("Average and Strike Rate")
axes[2].set_title("Keeping Stats")

sns.barplot(x=label1, y=matches_values, ax=axes[0])
sns.barplot(x=label2, y=average_values, ax=axes[1])
sns.barplot(x=label3, y=keeping_values, ax=axes[2])


# In[224]:


batter1 = top_batters.loc[(top_batters["Player Name"] == 'KL Rahul ')]
batter2 = top_batters.loc[(top_batters["Player Name"] == 'David Warner ')]
batter3 = top_batters.loc[(top_batters["Player Name"] == 'Virat Kohli')]

bowler1 = top_bowlers.loc[(top_bowlers["Player Name"] == 'Yuzvendra Chahal ')]
bowler2 = top_bowlers.loc[(top_bowlers["Player Name"] == 'Jasprit Bumrah')]
bowler3 = top_bowlers.loc[(top_bowlers["Player Name"] == 'Nathan Coulter-Nile')]
bowler4 = top_bowlers.loc[(top_bowlers["Player Name"] == 'Kagiso Rabada ')]

allrounder1 = top_allrounders.loc[(top_allrounders["Player Name"] == 'Andre Russell')]
allrounder2 = top_allrounders.loc[(top_allrounders["Player Name"] == 'Sunil Narine ')]
allrounder3 = top_allrounders.loc[(top_allrounders["Player Name"] == 'Hardik Pandya')]

keeper = top_keepers.loc[(top_keepers["Player Name"] == 'MS Dhoni')]


# In[225]:


final = [batter1, batter2, batter3, allrounder1, allrounder2, allrounder3, keeper, bowler1, bowler2, bowler3, bowler4]
final_team = pd.concat(final)
final_team = final_team.drop(labels=['Matches_Played', 'Runs', 'Average', 'Strike_Rate', 'Wickets', 
                                     'Bowling_average', 'Economy', 'Bowling_Strike_Rate', 
                                     'Catches', 'Run_outs', 'Stumps'], axis=1)

final_team.reset_index(drop=True)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




