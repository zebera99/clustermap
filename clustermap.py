!pip install seaborn==0.9.0
import pandas as pd
import seaborn as sns

df = pd.read_csv('data/young_survey.csv')

interest = df.loc[:, 'History': 'Pets']
corr = interest.corr()

sns.clustermap(corr)
