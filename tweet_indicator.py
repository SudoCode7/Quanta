import twitterscraper
import pandas as pd
import datetime as dt

d = dt.timedelta(days=2)
end_date = dt.datetime.now()
begin_date = end_date-d

limit = 100
lang = 'english'

