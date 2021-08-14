import pandas as pd

df = dc_bikeshare_q1_2012.groupby(['bike_number'])['end_time'].max().to_frame('lastused').reset_index().sort_values(by='lastused', ascending = False)
