import pandas as pd

df = pd.read_csv(r"C:\Users\kon_p\Downloads\US1.XOM_211207_221207.csv", sep=';')
print(df.head())
print(df.info())
df1=df.drop(['<TICKER>', '<PER>', '<TIME>'], axis=1)
print(df1.head())

df1.index = pd.to_datetime(df1['<DATE>'], dayfirst=True)
df1['value'] = df1['<CLOSE>']
df2 = df1.drop(['<CLOSE>', '<DATE>'], axis=1)
print(df2.head())
print(df2.isnull().sum(axis=0))

prophetdf = pd.DataFrame()
prophetdf['ds'] = df2.index
prophetdf['y'] = df2['value'].values
prophetdf_train = prophetdf[:-20]
prophetdf_test = prophetdf[-20:]

from prophet import Prophet
from sklearn.metrics import  mean_absolute_error


def fb_prophet_function(data, **params):

    prophet_model = Prophet(**params)
    prophet_model.fit(data)
    future = prophet_model.make_future_dataframe(periods=20, freq='D')
    #pred = prophet_model.predict(future)
    return prophet_model


fbmodel = fb_prophet_function(data=prophetdf_train, weekly_seasonality=False, yearly_seasonality=False, changepoint_range=0.8,changepoint_prior_scale=0.8)


import pickle
with open ("models/fbmodel.pckl", 'wb') as f_out:
    pickle.dump(fbmodel, f_out)
    f_out.close()
with open('models/fbmodel.pckl', 'rb') as f_in:
    testmodel=pickle.load(f_in)

future=testmodel.make_future_dataframe(periods=20, freq='D')
fbforecast=testmodel.predict(future)
MAE=mean_absolute_error(prophetdf.y[-20:], fbforecast.yhat[-20:])
print("MAE=", MAE)
