import pandas as pd

# create dataframe
data_table_df = pd.read_csv (r'/Resources/cities.csv')

# render dataframe as html
html = df_marks.to_html()
print(html)