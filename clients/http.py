import time
import requests

MAX_RETRIES = 2
TIMEOUT = 9.5

class ExternalServiceError(Exception):
    pass

def make_get_request(url: str) -> dict | list:
    for attempt in range(MAX_RETRIES + 1):
        try:
            # Добавляем User-Agent, чтобы API не блокировали запрос
            headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'}
            response = requests.get(url, headers=headers, timeout=TIMEOUT)
            
            if response.status_code == 429:
                retry_after = response.headers.get('Retry-After')
                wait_time = int(retry_after) if retry_after and retry_after.isdigit() else 2 ** attempt
                time.sleep(wait_time)
                continue
            
            if response.status_code in (500, 502, 503, 504):
                response.raise_for_status()
                
            response.raise_for_status()
            
            try:
                return response.json()
            except requests.exceptions.JSONDecodeError:
                raise ExternalServiceError('Сервис вернул ответ не в формате JSON')
                
        except (requests.exceptions.Timeout, requests.exceptions.ConnectionError) as e:
            if attempt == MAX_RETRIES:
                raise ExternalServiceError(f'Внешний сервис недоступен после {MAX_RETRIES} попыток: {e}')
            time.sleep(2 ** attempt)
            
        except requests.exceptions.HTTPError as e:
            raise ExternalServiceError(f'Ошибка HTTP: {e}')
            
    raise ExternalServiceError('Не удалось выполнить запрос')
