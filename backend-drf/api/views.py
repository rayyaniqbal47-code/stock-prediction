from django.shortcuts import render
from api.Serializers import StockSerializer
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import yfinance as yf
from datetime import datetime
import tensorflow as tf
from sklearn.preprocessing import MinMaxScaler
import os
from django.conf import settings
from api.utils import save_plot
from keras.models import load_model
from sklearn.metrics import mean_squared_error , r2_score


# Create your views here.

class StockAPIView(APIView):

    def post(self , request):
        serializer = StockSerializer(data=request.data)
        if serializer.is_valid():
            ticker = serializer.validated_data['ticker']

            # fetch the data from yfinance
            now = datetime.now()
            start = datetime(now.year-10 , now.month , now.day)
            end = now
            df = yf.download(ticker , start , end)

            if df.empty:
                return Response({'error':'No data found for the given ticker' , 'status':status.HTTP_404_NOT_FOUND})
            

            df = df.reset_index()

            # generating basic plot
            plt.switch_backend('AGG')
            plt.figure(figsize=(12,5))
            plt.plot(df.Close , label='closing price')
            plt.title(f"closing price of {ticker}")
            plt.xlabel('Days')
            plt.ylabel('price')
            plt.legend()

            # save the plot to a file

            plot_img_path = f"{ticker}_plot.png"
            plot_img = save_plot(plot_img_path)

            # 100 days moving average 
            # ma = moving average
            ma100 = df.Close.rolling(100).mean()
            plt.switch_backend('AGG')
            plt.figure(figsize=(12,5))
            plt.plot(df.Close , label='closing price')
            plt.plot(ma100 , 'r', label='100 days ma')
            plt.title(f"100 days moving average of {ticker}")
            plt.xlabel('Days')
            plt.ylabel('price')
            plt.legend() 
            plot_img_path = f"{ticker}_100_days_ma.png"
            plot_100_days_ma = save_plot(plot_img_path)


            # 200 days moving average 
            # ma = moving average
            ma200 = df.Close.rolling(200).mean()
            plt.switch_backend('AGG')
            plt.figure(figsize=(12,5))
            plt.plot(df.Close , label='closing price')
            plt.plot(ma100 , 'r', label='100 days ma')
            plt.plot(ma200 , 'g', label='200 days ma')
            plt.title(f"200 days moving average of {ticker}")
            plt.xlabel('Days') 
            plt.ylabel('price')
            plt.legend() 
            plot_img_path = f"{ticker}_200_days_ma.png"
            plot_200_days_ma = save_plot(plot_img_path)


            # splitting data into training and testing datasets
            data_training = pd.DataFrame(df.Close[0:int(len(df)*0.7)])
            data_testing = pd.DataFrame(df.Close[int(len(df)*0.7):])

            # scaling down the data between 0 and 1
            scaler = MinMaxScaler(feature_range=(0,1))


            # load ML model
            model = load_model('stock_prediction_model.keras')


            # prepare test data
            past_100_days = data_training.tail(100)
            final_df = pd.concat([past_100_days , data_testing] , ignore_index=True)
            input_data = scaler.fit_transform(final_df)
            x_test = []
            y_test = []

            for i in range(100 , input_data.shape[0]):
                x_test.append(input_data[i-100:i])
                y_test.append(input_data[i, 0])

            x_test , y_test = np.array(x_test) , np.array(y_test)


            # making predictions
            y_predicted = model.predict(x_test)


            # revert the scaled prices to original prices
            y_predicted = scaler.inverse_transform(y_predicted.reshape(-1 , 1)).flatten()
            y_test = scaler.inverse_transform(y_test.reshape(-1 , 1)).flatten()


            # plot the final prediction
            plt.switch_backend('AGG')
            plt.figure(figsize=(12,5))
            plt.plot(y_test , 'b' , label='original price')
            plt.plot(y_predicted , 'r', label='predicted price')
            plt.title(f"final prediction for {ticker}")
            plt.xlabel('Days') 
            plt.ylabel('price')
            plt.legend() 
            plot_img_path = f"{ticker}_final_prediction.png"
            plot_final_prediction = save_plot(plot_img_path)

            # model evaluation

            # mean squared error (MSE)
            # lower MSE means your predictions is closer to the actual values

            mse = mean_squared_error(y_test , y_predicted)


            # root mean squared error (RMSE)
            # a lower RMSE incdicate that our model is good

            rmse = np.sqrt(mse)


            # r-squared 
            # r-squared measures how well your models predictions match the actual values 
            # so r-squared should be in between 0 and 1 if it is close to 1 it means our prediction is very good

            r2 = r2_score(y_test , y_predicted)


            return Response({
                'status':'success' , 
                'plot_img':plot_img ,
                'plot_100_days_ma':plot_100_days_ma,
                'plot_200_days_ma':plot_200_days_ma,
                'plot_final_prediction':plot_final_prediction,
                'mse':mse,
                'rmse':rmse,
                'r2':r2,
                })







