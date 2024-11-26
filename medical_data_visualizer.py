import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# 1
df = df = pd.read_csv('medical_examination.csv')


# 2
df['bmi_temp'] = df['weight'] / (df['height'] / 100) ** 2

df['overweight'] = df['bmi_temp'].apply(lambda x: 1 if x > 25 else 0)

df = df.drop('bmi_temp', axis=1)

# 3
df['active'] = 1 - df['active']
df['cholesterol'] = df['cholesterol'].apply(lambda x: 0 if x == 1 else 1)
df['gluc'] = df['gluc'].apply(lambda x: 0 if x == 1 else 1)

# 4
def draw_cat_plot():
    # 5
    df_cat = pd.melt(df, id_vars=['id'], value_vars=['cholesterol', 'gluc', 'smoke', 'alco', 'active','overweight'],
                 var_name='variable', value_name='value')


    # 6
    df_cat = df_cat = pd.melt(df, id_vars=['cardio'], value_vars=['cholesterol', 'gluc', 'smoke', 'alco', 'active', 'overweight'], var_name='variable', value_name='value')

    

    # 7
    g = sns.catplot(x='variable', hue='value', col='cardio', data=df_cat, kind='count')
    g.set_axis_labels("variable", "total")


    # 8
    fig = g


    # 9
    fig.savefig('catplot.png')
    return fig


# 10
def draw_heat_map():
    # 11
    df_heat = df_heat = df[(df['ap_lo'] <= df['ap_hi']) &
             (df['height'] >= df['height'].quantile(0.025)) &
             (df['height'] <= df['height'].quantile(0.975)) &
             (df['weight'] >= df['weight'].quantile(0.025)) &
             (df['weight'] <= df['weight'].quantile(0.975))]

    # 12
    corr = df_heat.corr()

    # 13
    mask = np.triu(corr)



    # 14
    fig, ax = plt.subplots(figsize=(12, 10))

    # 15

    sns.heatmap(corr, annot=True, fmt='.1f', mask=mask, vmax=.3, center=0,
            square=True, linewidths=.5, cbar_kws={"shrink": .5})

    # 16
    fig.savefig('heatmap.png')
    return fig
