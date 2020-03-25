import pandas as pd

url = "https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv"

df1 = pd.read_csv(url, error_bad_lines=False)

df_total_daily = df1.sum(axis=0)

print(df_total_daily)
print(df_total_daily.index)





