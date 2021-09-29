#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import seaborn as sns
import plotly.express as px
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.graph_objects as pg


# In[2]:


Medals=pd.read_excel('Medals.xlsx') #Carlos


# In[3]:


print(Medals.info())
Medals.head()


# In[4]:


import plotly.graph_objects as go


# In[5]:


Medals.rename(columns={'Team/NOC':'Team'},inplace=True)
fig= go.Figure()
fig.add_trace(go.Bar(x=Medals.Team, y=Medals['Gold'], name='Golden Medals', marker_color='#FFD700'))
fig.add_trace(go.Bar(x=Medals.Team, y=Medals['Silver'], name='Silver Medals', marker_color='#c0c0c0'))
fig.add_trace(go.Bar(x=Medals.Team, y=Medals['Bronze'], name='Bronze Medals', marker_color= '#cd7f32'))

fig.update_layout(
    title='Medals per Country', title_x=0.5,
    xaxis=dict(
        title='Country',
        titlefont_size=16,
        tickfont_size=10),
    yaxis=dict(
        title='Amount of medals',
        titlefont_size=16,
        tickfont_size=10),
    legend=dict(
        x=0.82,
        y=0.95,
        bgcolor='rgba(0, 0, 0, 0)',
        bordercolor='rgba(0, 0, 0, 0)'
    ),
    barmode='stack',
    bargap=0.15,
    bargroupgap=0.07)

methods='update'

fig.update_layout(
    updatemenus=[
        dict(
            type="buttons",
            buttons=[
                dict(label="Gold",
                     method=methods,
                     args=['visible', Medals.Gold]),
                dict(label="Silver",
                     method=methods,
                     args=['visible', Medals.Silver]),
                dict(label='Bronze',
                     method=methods,
                     args=['visible', Medals.Bronze]),
                dict(label="All",
                     method=methods,
                     args=['visible', Medals.Total])])])
                
                
fig.show()


# In[7]:


Medals.rename(columns={'Team/NOC':'Team'},inplace=True)
color_scheme={'Gold': '#FFD700', 'Silver': '#c0c0c0','Bronze': '#cd7f32'}

plot= pg.Figure(data=[go.Bar(
    name='Gold', x=Medals['Team'], y=Medals['Gold'], marker_color='#FFD700'
),
    go.Bar(
    name='Silver', x=Medals['Team'], y=Medals['Silver'], marker_color='#c0c0c0'
),
    go.Bar(
    name='Bronze', x=Medals['Team'], y=Medals['Bronze'], marker_color= '#cd7f32'
    ),
])
plot.update_layout(
    updatemenus=[
        dict(
            type="buttons",
            direction="down", x=-0.1,
            buttons=list([
                dict(label="Total medals",
                     method="update",
                     args=[{"visible": [True, True, True]},
                           {"title": "Both"}]),
                dict(label="Gold",
                     method="update",
                     args=[{"visible": [True, False, False]},
                           {"title": "Gold",
                            }]),
                dict(label="Silver",
                     method="update",
                     args=[{"visible": [False, True, False]},
                           {"title": "Silver",
                            }]),
                dict(label="Bronze",
                     method="update",
                     args=[{"visible": [False, False, True]},
                           {"title": "Bronze",
                            }]),]))])
plot.update_layout(
    title='Medals per Country', title_x=0.5,
    xaxis=dict(
        title='Country',
        titlefont_size=16,
        tickfont_size=10),
    yaxis=dict(
        title='Amount of medals',
        titlefont_size=16,
        tickfont_size=10),
    legend=dict(
        x=0.82,
        y=0.95,
        bgcolor='rgba(0, 0, 0, 0)',
        bordercolor='rgba(0, 0, 0, 0)'
    ),
    barmode='stack',
    bargap=0.15,
    bargroupgap=0.07
)                      
plot.show()


# In[8]:


Medals.rename(columns={'Team/NOC':'Team'},inplace=True)
color_scheme={'Gold': '#FFD700', 'Silver': '#c0c0c0','Bronze': '#cd7f32'}
px.bar(Medals, x='Team', y=['Gold', 'Silver', 'Bronze'], hover_data=['Total'],
            labels={'value':'Amount of medals', 'variable':'Medal', 'Total':'Total medals'}, barmode='stack', 
       color_discrete_map=color_scheme)


# In[98]:


Medals.rename(columns={'Team/NOC':'Team'},inplace=True)
fig= go.Figure()
fig.add_trace(go.Bar(x=Medals.Team, y=Medals['Gold'], name='Golden Medals', marker_color='#FFD700'))
fig.add_trace(go.Bar(x=Medals.Team, y=Medals['Silver'], name='Silver Medals', marker_color='#c0c0c0'))
fig.add_trace(go.Bar(x=Medals.Team, y=Medals['Bronze'], name='Bronze Medals', marker_color= '#cd7f32'))

fig.update_layout(
    title='Medals per Country', title_x=0.5,
    xaxis=dict(
        title='Country',
        titlefont_size=16,
        tickfont_size=10),
    yaxis=dict(
        title='Amount of medals',
        titlefont_size=16,
        tickfont_size=10),
    legend=dict(
        x=0.82,
        y=0.95,
        bgcolor='rgba(0, 0, 0, 0)',
        bordercolor='rgba(0, 0, 0, 0)'
    ),
    barmode='stack',
    bargap=0.15,
    bargroupgap=0.07
)
fig.show()


# In[ ]:





# In[4]:


Medals.rename(columns={'Team/NOC':'Team'},inplace=True) # renaming the Team/NOC column to Team
x = []
for team in Medals['Team']:
    x.append(team)
y = Medals['Gold']
plt.figure(figsize=(30,8))
plt.bar(x,y)
for index, value in enumerate(y):
    plt.text(index, value, str(value),color='blue',size=10,fontweight='bold')
plt.xlabel("Country",size=20)
plt.ylabel("Gold Medals", size=20)
plt.xticks(x,rotation='vertical',size=15)
plt.title("Gold Medals across Nations", size=20)
plt.show()


# In[11]:


Medals.rename(columns={'Team/NOC':'Team'},inplace=True) # renaming the Team/NOC column to Team
x = []
for team in Medals['Team']:
    x.append(team)
y = Medals['Silver']
plt.figure(figsize=(30,8))
plt.bar(x,y)
for index, value in enumerate(y):
    plt.text(index, value, str(value),color='black',size=10,fontweight='bold')
plt.xlabel("Country",size=20)
plt.ylabel("Silver Medals", size=20)
plt.xticks(x,rotation='vertical',size=15)
plt.title("Silver Medals across Nations", size=20)
plt.show()


# In[6]:


Medals.rename(columns={'Team/NOC':'Team'},inplace=True) # renaming the Team/NOC column to Team
x = []
for team in Medals['Team']:
    x.append(team)
y = Medals['Bronze']
plt.figure(figsize=(30,8))
plt.bar(x,y)
for index, value in enumerate(y):
    plt.text(index, value, str(value),color='blue',size=10,fontweight='bold')
plt.xlabel("Country",size=20)
plt.ylabel("Bronze Medals", size=20)
plt.xticks(x,rotation='vertical',size=15)
plt.title("Bronze Medals across Nations", size=20)
plt.show()


# In[7]:


Medals.rename(columns={'Team/NOC':'Team'},inplace=True) # renaming the Team/NOC column to Team
x = []
for team in Medals['Team']:
    x.append(team)
y = Medals['Total']
plt.figure(figsize=(30,8))
plt.bar(x,y)
for index, value in enumerate(y):
    plt.text(index, value, str(value),color='blue',size=10,fontweight='bold')
plt.xlabel("Country",size=20)
plt.ylabel("Total Medals", size=20)
plt.xticks(x,rotation='vertical',size=15)
plt.title("Total Medals across Nations", size=20)
plt.show()


# In[ ]:




