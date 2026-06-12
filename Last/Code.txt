#!/usr/bin/env python
# coding: utf-8

# # Importing of the Libraries

# In[1]:


#importing labraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from statsmodels.tsa.arima.model import ARIMA
from sklearn.model_selection import train_test_split
from keras.models import Sequential
from statsmodels.tsa.stattools import adfuller, kpss
from keras.layers import LSTM, Dense
from statsmodels.tsa.statespace.sarimax import SARIMAX
from sklearn.metrics import mean_squared_error, mean_absolute_error
from sklearn.metrics import r2_score
from sklearn.preprocessing import MinMaxScaler
import plotly.graph_objects as go
import math
import warnings
warnings.filterwarnings('ignore')


# # Amazon data Exploration

# In[2]:


Amazon_Data=pd.read_csv('AMZN.csv')


# In[3]:


Amazon_Data.head()


# In[4]:


Amazon_Data.shape


# In[5]:


Amazon_Data.info()


# In[6]:


Amazon_Data.describe()


# # Data Cleaning

# In[7]:


Amazon_Data.isnull().sum()


# In[8]:


Amazon_Data['Date'] = pd.to_datetime(Amazon_Data['Date'])


# # EDA

# In[9]:


#time Series plot
plt.figure(figsize=(8, 4))
plt.plot(Amazon_Data['Date'], Amazon_Data['Close'], label='Close Prices')
plt.title('Time Series Plot of Close Prices')
plt.xlabel('Date')
plt.ylabel('Close Prices')
plt.legend()
plt.show()


# In[10]:


#Candlestick Chart of Stock Prices
fig = go.Figure(data=[go.Candlestick(x=Amazon_Data['Date'],
                open=Amazon_Data['Open'],
                high=Amazon_Data['High'],
                low=Amazon_Data['Low'],
                close=Amazon_Data['Close'])])

fig.update_layout(title='Candlestick Chart of Stock Prices',
                  xaxis_title='Date',
                  yaxis_title='Stock Prices')
fig.show()


# In[11]:


#Histogram 
plt.figure(figsize=(7,4))
plt.hist(Amazon_Data['Volume'], bins=10, color='skyblue', edgecolor='black')
plt.title('Histogram of Volume')
plt.xlabel('Volume')
plt.ylabel('Frequency')
plt.show()


# In[12]:


#scatter plot for high and low price
plt.figure(figsize=(7,5))
plt.scatter(Amazon_Data['High'], Amazon_Data['Low'], color='orange', alpha=0.7)
plt.title('Scatter Plot between High and Low Prices')
plt.xlabel('High Prices')
plt.ylabel('Low Prices')
plt.show()


# In[13]:


Amazon_Data.set_index('Date', inplace=True)


# # Stationary test

# ## ADF Test
# 

# In[14]:


def adf_test(timeseries):
    result = adfuller(timeseries, autolag='AIC')
    print('ADF Statistic:', result[0])
    print('p-value:', result[1])
    print('Critical Values:', result[4])
    
    if result[1] <= 0.05:
        print("The time series is stationary")
    else:
        print("The time series is non-stationary")


# In[15]:


# ADF Test on closing prices
adf_test(Amazon_Data['Close'])


# ## KPSS Test
# 

# In[16]:


def kpss_test(timeseries):
    result = kpss(timeseries, regression='c', nlags="auto")
    print('KPSS Statistic:', result[0])
    print('p-value:', result[1])
    print('Critical Values:', result[3])
    
    if result[1] <= 0.05:
        print("The time series is non-stationary")
    else:
        print("The time series is stationary")


# In[17]:


# KPSS Test on closing prices
kpss_test(Amazon_Data['Close'])


# ### Difference the time series
# 

# In[18]:


AmazonClose=Amazon_Data['Close']


# In[19]:


returns  = np.diff(AmazonClose)


# ## ARIMA Model
# 

# In[20]:


# Split the data into training and testing sets
train_size = int(len(returns) * 0.8)
train, test = returns[:train_size], returns[train_size:]


# In[21]:


# Fit ARIMA model
order = (5, 1, 0)  # Example order (p, d, q)
Arima_model = ARIMA(train, order=order)
Arima_model_fit = Arima_model.fit()


# In[22]:


# Forecast using the trained model
arima_forecast = Arima_model_fit.forecast(steps=len(test))


# In[23]:


Arima_mae = mean_absolute_error(test, arima_forecast)
print(f'Mean Absolute Error: {Arima_mae}')


# In[24]:


Arima_rmse = math.sqrt(mean_squared_error(test, arima_forecast))
print(f'Root Mean Squared Error: {Arima_rmse}')


# # SARIMA

# In[25]:


order = (1, 0, 1)  # Example order (p, d, q)
seasonal_order = (1, 0, 1, 12)  # Example seasonal order (P, D, Q, m)
sarima_model = SARIMAX(train, order=order, seasonal_order=seasonal_order)
sarima_model_fit = sarima_model.fit()


# In[26]:


# Forecast using the trained model
sarima_forecast = sarima_model_fit.forecast(steps=len(test))


# In[27]:


sarima_rmse = math.sqrt(mean_squared_error(test, sarima_forecast))
print(f'Mean Squared Error (SARIMA): {sarima_rmse}')


# In[28]:


sarima_mae = mean_absolute_error(test, sarima_forecast)
print(f'Mean Absolute Error: {sarima_mae}')


# # LSTM

# In[29]:


# Function to create supervised dataset for LSTM
def create_dataset(dataset, look_back):
    dataX, dataY = [], []
    for i in range(len(dataset)-look_back):
        a = dataset[i:(i+look_back), 0]
        dataX.append(a)
        dataY.append(dataset[i + look_back, 0])
    return np.array(dataX), np.array(dataY)


# In[30]:


# Normalize the differenced series
scaler = MinMaxScaler(feature_range=(0, 1))
scaled_series = scaler.fit_transform(returns.reshape(-1, 1))


# In[31]:


# Create supervised dataset for LSTM
look_back = 1
X, y = create_dataset(scaled_series, look_back)


# In[32]:


# Reshape input data to be [samples, time steps, features]
X = np.reshape(X, (X.shape[0], X.shape[1],1))


# In[ ]:


# Build LSTM model
model = Sequential()
model.add(LSTM(50, input_shape=(1, look_back)))#timestep=1
model.add(Dense(1))
model.compile(loss='mean_squared_error', optimizer='adam')
model.fit(X, y, epochs=10, batch_size=1, verbose=1)


# In[ ]:


# Predict using the trained LSTM model
trainPredict = model.predict(X)


# In[ ]:


# Invert predictions to original scale
trainPredict = scaler.inverse_transform(trainPredict)
y_inverse = scaler.inverse_transform([y])


# In[ ]:


lstm_mae = mean_absolute_error(y_inverse[0], trainPredict[:, 0])
print(f'Mean Absolute Error: {lstm_mae}')


# In[ ]:


lstm_rmse = math.sqrt(mean_squared_error(y_inverse[0], trainPredict[:, 0]))
print(f'Root Mean Squared Error: {lstm_rmse}')


# In[ ]:


#comparison of RMSE with different model
data = [['LSTM', lstm_rmse], ['SARIMA', sarima_rmse], ['ARIMA', Arima_rmse]]
df = pd.DataFrame(data, columns=['Machine learning', 'RMSE'])

plt.figure(figsize=(7, 5))  
plt.xlim(0, 50)
sns.barplot(x='RMSE', y='Machine learning', data=df, palette='viridis')  
plt.xlabel('RMSE Values')
plt.ylabel('Machine Learning Models')
plt.title('Comparison of RMSE for Different Machine Learning Methods')
plt.show()


# In[ ]:




