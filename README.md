# django-forecasting-app
This web application forecasts future sales using the ARIMA model.

# How to Run

1. Clone the repository:
        git clone https://github.com/prabipradeep/forecasting_app.git
        
       

2. Navigate to the project directory and install requirements:
        
        cd forecasting_app
        pip install -r requirements.txt
3.Migrate the database and run the server:

	python manage.py migrate
	python manage.py runserver

4.Access the application at http://127.0.0.1:8000/


# Dataset and the forecasting model:-


    Dataset: The dataset used is a time series dataset containing daily sales data for a retail store. It includes two columns:
        Date: The date of the sales record.
        Sales: The total sales amount recorded on each date.

    The data file should be in CSV format and should be structured similarly to sample_sales_data.csv, provided as an example in the repository.

    Forecasting Model: 
    This application uses the ARIMA (AutoRegressive Integrated Moving Average) model to forecast future sales data. 
    The ARIMA model is suitable for time series data with trends or seasonality patterns, and it works by combining three main elements:
        AutoRegressive (AR): Uses past values to predict future values.
        Integrated (I): Differencing the data to remove any trends, making it stationary.
        Moving Average (MA): Accounts for errors from past forecasts to improve prediction accuracy.

    The model is dynamically trained using parameters (p=5, d=1, q=0) each time a user specifies a forecast horizon.

# Challenges Faced During Implementation

    Data Stationarity: One of the main challenges was ensuring the dataset was stationary. Time series models like ARIMA require the data to have no overall trend or seasonality. To address this, differencing was applied to the data to remove any trends.

    Model Parameter Tuning: Finding the optimal ARIMA parameters (p, d, q) for accurate forecasting required testing and adjusting. We used (5, 1, 0) as the default parameters, but other values may improve accuracy depending on the dataset.
