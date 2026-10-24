from clients.http import make_get_request, ExternalServiceError

class CurrencyNotFoundError(Exception):
    pass

def get_rate(currency: str) -> float:
    url = f'https://api.frankfurter.dev/v2/rate/{currency}/RUB'
    
    try:
        data = make_get_request(url)
    except ExternalServiceError as e:
        if '404' in str(e):
            raise CurrencyNotFoundError(f"Валюта '{currency}' не найдена")
        raise
    
    if not isinstance(data, dict) or 'rate' not in data:
        raise ExternalServiceError('Неожиданный формат ответа от API курсов')
        
    return float(data['rate'])
