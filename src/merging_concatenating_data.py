import pandas as pd

from src.loading import results

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
bios = pd.read_csv('bios.csv')
nocs = pd.read_csv('noc_regions.csv')
print(bios[['name','born_country','NOC']].head())
print(nocs.head())

#merge() như trong sql
#on= là phép kết nối tự nhiên
bios_new = pd.merge(bios, nocs, left_on='born_country', right_on='NOC', how = 'left')
print(bios_new.head())
bios_new.rename(columns={'region':'born_country_full'}, inplace=True)
bios_new.drop(columns=['NOC_y'],inplace=True)
print(bios_new[bios_new['NOC_x'] != bios_new['born_country_full']][['name','born_country','NOC_x','born_country_full']].head())

#concat([df1,df2])
'''
pd.concat(): Used to concatenate DataFrames 
        either vertically (by rows) or horizontally (by columns).
The 'objs' parameter is a sequence or mapping of Series or DataFrame objects to be concatenated.
The 'axis' parameter determines the direction of concatenation:
        axis=0 is set as the default value, which means it will concatenate DataFrames vertically (by rows).
        axis=1 will concatenate DataFrames horizontally (by columns).
'''
usa = bios[bios['born_country'] == 'USA'].copy()
print(usa.head())
gbr = bios[bios['born_country'] == 'GBR'].copy()
print(gbr.head())
new_df = pd.concat([usa,gbr])
print(new_df.head())


