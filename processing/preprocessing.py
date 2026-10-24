def add_weather_flags(weather_data: dict) -> dict:
    temp = weather_data.get('temp_c', 0)
    weather_data['warm_clothes'] = temp < 0
    return weather_data

def add_rate_flags(rate_data: dict) -> dict:
    rate = rate_data.get('rate_to_rub', 0)
    rate_data['expensive'] = rate > 100
    return rate_data
