import eikon as ek
from src.util.config_util import get_config
import eikon as ek

def get_app_key():
    return get_config()['eikon']['api_key']

def get_eikon_data(instruments, parameters):
    ek.set_app_key(get_app_key())
    eikon_data = ek.get_data(instruments=instruments, fields=parameters)
    return eikon_data

if __name__ == "__main__":
    instruments = ['AAPL.O', 'MSFT.O']
    parameters = ['TR.PriceClose', 'TR.Volume', 'TR.PriceLow', 'TR.PriceHigh', 'TR.PriceOpen', 'TR.Revenue']
    data = get_eikon_data(instruments, parameters)
    print(data.head())