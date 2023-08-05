import pandas as pd
import seaborn as sns
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np

#// Import data
df = pd.read_csv("Data Analysis with Python\\Medical Data Visualizer\\medical_examination.csv") #! Change for replit
# df.info()

#// Add 'overweight' column
df['overweight'] = df.apply(lambda x : 1 if x['weight'] / ((x['height'] / 100) ** 2) > 25 else 0, axis=1)
# print(df[['overweight']].head())

#// Normalize data by making 0 always good and 1 always bad. If the value of 'cholesterol' or 'gluc' is 1, make the value 0. If the value is more than 1, make the value 1.
# print(df['gluc'].head(20))
df['cholesterol'] = df['cholesterol'].apply(lambda x: 0 if x == 1 else 1)
df['gluc'] = df['gluc'].apply(lambda x: 0 if x == 1 else 1)
# print(df['gluc'].head(20))

# Draw Categorical Plot
def draw_cat_plot():
    #// Create DataFrame for cat plot using `pd.melt` using just the values from 'cholesterol', 'gluc', 'smoke', 'alco', 'active', and 'overweight'.
    df_cat = pd.melt(df, id_vars=['cardio'], value_vars=['cholesterol', 'gluc', 'smoke', 'alco', 'active', 'overweight'])

    #// Group and reformat the data to split it by 'cardio'. Show the counts of each feature.
    #// You will have to rename one of the columns for the catplot to work correctly.
    df_cat = df_cat.groupby(['cardio', 'variable', 'value'])['value'].count().reset_index(name='total')
    df_cat = df_cat.rename(columns={'variable': 'variable_name'})
    # print(df_cat)
 
    #// Draw the catplot with 'sns.catplot()'
    g = sns.catplot(
        data=df_cat,
        x='variable_name',
        y='total',
        hue='value',
        col='cardio',
        kind='bar'
        )
    g.set_axis_labels('variable', 'total')
    g.set_titles('{col_name}')

    #// Get the figure for the output
    fig = g.fig

    # Do not modify the next two lines
    fig.savefig('Data Analysis with Python\\Medical Data Visualizer\\Plot\\catplot.png') #! Change for replit
    return fig

#// Draw Heat Map
def draw_heat_map():
    #// Clean the data
    df_heat = df.copy()
    df_heat = df_heat.loc[(df['ap_lo'] <= df['ap_hi']) 
                          & (df['height'] >= df['height'].quantile(0.025)) 
                          & (df['height'] <= df['height'].quantile(0.975))
                          & (df['weight'] >= df['weight'].quantile(0.025))
                          & (df['weight'] <= df['weight'].quantile(0.975))
                          ]

    #// Calculate the correlation matrix
    corr = df_heat.corr(method="pearson")
    # print(corr)

    #// Generate a mask for the upper triangle
    mask = np.triu(np.ones_like(corr, dtype=bool))

    #// Set up the matplotlib figure
    fig, ax = plt.subplots(figsize=(12,12))

    #// Draw the heatmap with 'sns.heatmap()'
    sns.heatmap(corr, linewidths=1, annot=True, mask=mask, center=0.08, square=True, fmt=".1f", cbar_kws={"shrink": 0.5})
    
    #// Do not modify the next two lines
    fig.savefig('Data Analysis with Python\\Medical Data Visualizer\\Plot\\heatmap.png') #! Change for replit
    return fig

if __name__=="__main__":
    #draw_cat_plot()
    fig = draw_heat_map()
    ax = fig.axes[0]
    actual = [text.get_text() for text in ax.get_default_bbox_extra_artists() if isinstance(text, mpl.text.Text)]
    print(actual)