from string import ascii_letters
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import sql_client as sql

def corr_heatmap(df):
    # del df['labname']
    corr = df.corr()

    print(corr)
    fig, ax = plt.subplots(figsize=(10,5))
    ax.matshow(corr)
    # plt.matshow(corr, fignum=f.number)
    ax.set_xticks(range(df.shape[1]), minor=False)
    ax.set_xticklabels(df.columns, rotation=45, minor=False)
    # ax.xticks(range(df.shape[1]), df.columns, rotation=45)
    # ax.yticks(range(df.shape[1]), df.columns,)
    cb = plt.colorbar()
    cb.ax.tick_params(labelsize=14)
    plt.title('Correlation Matrix', fontsize=16);

    mask = np.triu(np.ones_like(corr, dtype=np.bool))
    # Set up the matplotlib figure
    # f, ax = plt.subplots(figsize=(100, 100))

    # ax.yxlabel('ylabel', fontsize=5)

    # Generate a custom diverging colormap
    # cmap = sns.diverging_palette(220, 10, as_cmap=True)
    
    # Draw the heatmap with the mask and correct aspect ratio
    # ax = sns.heatmap(corr, mask=mask, cmap=cmap, vmax=.3, center=0,
    #             square=True, linewidths=.5, cbar_kws={"shrink": .5})

    plt.show()
    print('plotted')

def count_histo(df):
    # pd.set_option('display.max_rows', None)
    
    histo = df.count()/df.shape[0]
    print(histo)
    ax = histo.plot.hist(bins=100, alpha=0.5)
    plt.show()


if __name__ == '__main__':
    print('running')
    sns.set(style="white")

    SERVER_NAME = "teamseven.ct4lx0aqwcg9.ca-central-1.rds.amazonaws.com"
    DATABASE_NAME = "eicu_demo"
    USERNAME = "admin"
    PASSWORD = "jXGiWT5FqVTyMQHXa74c"
    s = sql.SqlClient(SERVER_NAME, DATABASE_NAME, USERNAME, PASSWORD)
    # df = s.select('lab_squashed', select="*")
    df = s.select('lab_flat', select="*")
    count_histo(df)