import pandas as pd
from statsmodels.tsa.arima.model import ARIMA
import matplotlib.pyplot as plt
from io import BytesIO
import base64


def load_and_preprocess_data():
    df = pd.read_csv('forecasts/data/shampoo_sales.csv', parse_dates=['Month'], index_col='Month')
    df.fillna(method='ffill', inplace=True)

    return df

def build_arima_model(data, steps=12):
    model = ARIMA(data, order=(5, 1, 0))  
    model_fit = model.fit()
    
    forecast = model_fit.forecast(steps=steps)
    return forecast


def plot_forecast(data, forecast):
    plt.figure(figsize=(10, 6))
    plt.plot(data.index, data, label='Historical Sales')
    forecast_index = pd.date_range(data.index[-1], periods=len(forecast) + 1, freq='M')[1:]
    plt.plot(forecast_index, forecast, label='Forecasted Sales', color='orange')
    
    plt.fill_between(forecast_index, forecast - 1.96 * forecast.std(), forecast + 1.96 * forecast.std(), color='orange', alpha=0.3)
    plt.legend()
    plt.title('Sales Forecast')

    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    
    image_base64 = base64.b64encode(buffer.getvalue()).decode()
    buffer.close()
    
    return image_base64
