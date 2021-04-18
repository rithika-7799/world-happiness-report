import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import matplotlib.pyplot as plt
import seaborn as sns
import scipy.stats as stats
import plotly as py # visualization library
from plotly.offline import init_notebook_mode, iplot # plotly offline mode
init_notebook_mode(connected=True) 
import plotly.graph_objs as go # plotly graphical object
import warnings
from countryinfo import CountryInfo
warnings.filterwarnings('ignore')
get_ipython().run_line_magic('pylab', 'inline')


# In[3]:

class Analysis:
    def __init__(self):
        data = pd.read_csv("C:\\Users\\Rithika\\Downloads\\data\\2019.csv")


        # In[4]:


        most=data.head()


        # In[5]:


        least=data.tail()


        # In[6]:


        d=[]
        d=data.iloc[[0,155]]



        # In[8]:



        #d= d.loc[['Overall rank','Score','GDP per capita','Social     support','Healthy life expectancy','Freedom to make life     choices','Generosity','Perceptions of corruption']]
        data_plot = d.loc[:,['Score','GDP per capita','Social support','Healthy     life expectancy','Freedom to make life choices','Generosity','Perceptions     of corruption']]
        data_plot.plot()


        # In[21]:


        f,ax = plt.subplots(figsize=(10, 10))
        sns.heatmap(data.corr(), annot=True, linewidths=.5, fmt= '.1f',ax=ax)
        plt.show()
        f.savefig("CorrPlot.jpg")


        # In[10]:


        plt.plot(data_plot.iloc[0])
        plt.plot(data_plot.iloc[1])


        # In[19]:


        fig, ax = plt.subplots(figsize=(8,8))
        width=0.35
        labels=['Score','GDP per capita','Social support','Healthy life 	    expectancy','Freedom to make life choices','Generosity','Perceptions of        corruption']
        x = np.arange(len(labels))
        rects1 = ax.bar(x - width/2, data_plot.iloc[0], width, label='Most happy     country')
        rects2 = ax.bar(x + width/2, data_plot.iloc[1], width, label='Least happy     country')
        plt.xticks(x, labels, fontsize=7, rotation=30)
        fig.show()
        fig.savefig("HappyVSUnhappy.jpg")


        # In[40]:


        data_plot = data.loc[:,['Score','GDP per capita','Social support','Healthy     life expectancy','Freedom to make life choices','Generosity','Perceptions     of corruption']]

        data_plot.plot().get_figure().savefig('AllParamsPlotAllData.jpg')


        # In[128]:


        countries= data['Country or region']
        #countries=pd.DataFrame(countries)
        region=[]
        for c in countries:
            try:
                region.append(CountryInfo(c).region())
            except:
                region.append(' ')
                    


        # In[129]:


        countries=pd.DataFrame(countries)
        scores=list(data['Score'])
        #scores=scores.to_frame()


        # In[130]:


        #len(scores)


        # In[131]:


        countries.insert(1, 'Region', region, allow_duplicates = True)
        countries.insert(0,'Score',scores,allow_duplicates=True)


        # In[ ]:





        # In[132]:


        countries=countries[countries['Region']!=' ']


        # In[133]:


        #len(countries)


        # In[167]:


        c1=countries.groupby('Region')['Score'].sum()


        # In[168]:




        # In[169]:


        c1.plot()
        c1=c1.to_frame()


        # In[170]:


        reg=['Africa','Americas','Asia','Europe','Oceania']


        # In[171]:




        # In[183]:

        try:
            fig=sns.barplot(x=reg,y=c1['Score'])
            fig.figure.savefig('CountryWise.jpg')
        except:
            print("")

        # In[188]:


        fig=sns.pairplot(data.iloc[:,[1,3,4,5,6,7,8]])
        fig.savefig('PairPlot.jpg')

        plt.show()


        # In[185]:





        # In[189]:


        happiness_score = data['Score'].astype(float)


        # In[198]:


        data1 = [dict(
                type='choropleth',
                colorscale = 'Rainbow',
                locations = data['Country or region'],
                z = happiness_score,
                locationmode = 'country names',
                text = data['Country or region'],
                colorbar = dict(
                title = 'Happiness Score', 
                titlefont=dict(size=25),
                tickfont=dict(size=18))
        )]
        layout = dict(
            title = 'Happiness Score',
            titlefont = dict(size=40),
            geo = dict(
                showframe = True,
                showcoastlines = True,
                projection = dict(type = 'equirectangular')
                )
        )
        choromap = go.Figure(data = data1, layout = layout)
        fig=iplot(choromap, validate=False)
        #choromap.savefig('world.jpg')


        # In[197]:




        # In[201]:


        choromap.write_image("WorldMapScore.png")


        # In[ ]:



obj = Analysis()

print("Python script executed")


