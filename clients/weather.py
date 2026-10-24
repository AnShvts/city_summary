from clients.http import make_get_request, ExternalServiceError

class CityNotFoundError(Exception):
    pass

def get_weather(city: str) -> dict:
    API_KEY = 'e44b99648d5f217de7674fcc3294c4ff'
    url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric'
    
    try:
        data = make_get_request(url)
    except ExternalServiceError as e:
        if '404' in str(e):
            raise CityNotFoundError(f"Город '{city}' не найден")
        raise
    
    if 'main' not in data or 'temp' not in data['main']:
        raise ExternalServiceError('Неожиданный формат ответа от API погоды')
        
    temp_c = float(data['main']['temp'])
    description = data['weather'][0]['description'].lower()
    
    return {
        'temp_c': temp_c,
        'description': description
    }
