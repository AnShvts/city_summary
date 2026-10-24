from clients.weather import get_weather
from clients.rates import get_rate
from processing.preprocessing import add_weather_flags, add_rate_flags

def build_city_summary(city: str, currency: str = 'USD') -> dict:
    weather = get_weather(city)
    rate = get_rate(currency)
    
    rate_dict = {
        'currency': currency,
        'rate_to_rub': rate
    }
    
    weather = add_weather_flags(weather)
    rate_dict = add_rate_flags(rate_dict)
    
    return {
        'city': city,
        'weather': weather,
        'rates': rate_dict
    }
