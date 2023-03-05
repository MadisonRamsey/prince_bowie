import pandas as pd
from mwviews.api import PageviewsClient

# load wiki daily views data
client = PageviewsClient(user_agent="<madiramsey> prince_bowie")
views_data = client.article_views('en.wikipedia', ['Prince', 'David Bowie'], granularity='daily', start='20160101', end='20160131')

# load data into dataframe and clean row/column names
views_df = pd.DataFrame.from_dict(views_data, orient='index').reset_index(names='date')
views_df.rename(columns={col:col.lower().replace(' ','_') for col in views_df.columns}, inplace=True)




