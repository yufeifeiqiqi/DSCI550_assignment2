import pandas as pd
import numpy as np
from detoxify import Detoxify
import os

os.environ['KMP_DUPLICATE_LIB_OK'] = 'True'

df = pd.read_csv('combine_add_geo.csv')
df['Toxicity'] = np.nan
df['Severe_Toxicity'] = np.nan
df['Obscenity'] = np.nan
df['Identity_Attack'] = np.nan
df['Insult'] = np.nan
df['Threat'] = np.nan
df['Sexual_Explicit'] = np.nan

for index, row in df.iterrows():
    results = Detoxify('unbiased').predict(str(row['rtg_translate']))
    df.loc[index, 'Toxicity'] = results['toxicity']
    df.loc[index, 'Severe_Toxicity'] = results['severe_toxicity']
    df.loc[index, 'Obscenity'] = results['obscene']
    df.loc[index, 'Identity_Attack'] = results['identity_attack']
    df.loc[index, 'Insult'] = results['insult']
    df.loc[index, 'Threat'] = results['threat']
    df.loc[index, 'Sexual_Explicit'] = results['sexual_explicit']

df.to_csv('final.tsv', sep='\t', index=False)
