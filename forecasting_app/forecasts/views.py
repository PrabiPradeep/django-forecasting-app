from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from .utils import load_and_preprocess_data, build_arima_model, plot_forecast

def forecast_view(request):
    forecast_horizon = 12  
    if request.method == 'POST':
        forecast_horizon = int(request.POST.get('horizon', 12))  

    sales_data = load_and_preprocess_data()
    
    forecast = build_arima_model(sales_data['Sales'], steps=forecast_horizon)
    
    forecast_plot = plot_forecast(sales_data['Sales'], forecast)
    
    context = {
        'forecast_plot': forecast_plot,
        'forecast': forecast.to_dict(),
        'horizon': forecast_horizon
    }
    
    return render(request, 'forecasts/forecast_result.html', context)
