import argparse
import sys
from clients.weather import CityNotFoundError
from clients.rates import CurrencyNotFoundError
from clients.http import ExternalServiceError
from processing.service import build_city_summary

def main():
    parser = argparse.ArgumentParser(description='Сводка по городу')
    parser.add_argument('--city', required=True, help='Название города')
    parser.add_argument('--currency', default='USD', help='Код валюты (по умолчанию USD)')
    args = parser.parse_args()

    try:
        summary = build_city_summary(args.city, args.currency)
        
        print(f"Город: {summary['city']}")
        print(f"Погода: {summary['weather']['temp_c']}°C, {summary['weather']['description']}")
        print(f"Тёплая одежда: {'да' if summary['weather']['warm_clothes'] else 'нет'}")
        print(f"{summary['rates']['currency']}→RUB: {summary['rates']['rate_to_rub']}")
        print(f"Дорогой курс: {'да' if summary['rates']['expensive'] else 'нет'}")
        
    except CityNotFoundError as e:
        print(f'Ошибка: {e}', file=sys.stderr)
        sys.exit(3)
    except CurrencyNotFoundError as e:
        print(f'Ошибка: {e}', file=sys.stderr)
        sys.exit(3)
    except ExternalServiceError as e:
        print(f'Ошибка: {e}', file=sys.stderr)
        sys.exit(4)
    except Exception as e:
        print(f'Неизвестная ошибка: {e}', file=sys.stderr)
        sys.exit(2)

if __name__ == '__main__':
    main()
