import pandas as pd
data = {
    'id': [1,2,3,4,5,6],
    'name': ['Ella','David','Zachary','Alice','Finn','Violet'],
    'email': ['emily@example.com', 'michael@example.com', 'sarah@example.com', 'john@example.com', 'john@example.com', 'alice@example.com']
}

df = pd.DataFrame(data)

#drop_duplicate(subset= , keep= , inplace= )
'''
subset: This is the column label or sequence of labels to 
        consider for identifying duplicate rows. 
        If not provided, it considers all columns in the DataFrame.
keep: This argument determines which duplicate row to retain.
    'first': (default) Drop duplicates except for the first occurrence.
    'last': Drop duplicates except for the last occurrence.
    False: Drop all duplicates.
inplace: If set to True, the changes are made directly to the object 
        without returning a new object. 
        If set to False (default), a new object with duplicates dropped will be returned.
'''
df.drop_duplicates(subset=['email'], keep='first', inplace=True)
print(df.head())
