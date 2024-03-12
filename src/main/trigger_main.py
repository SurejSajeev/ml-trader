from src.finance.data_sources.eikon_finance_data import get_eikon_data


if __name__ == "__main__":
    instruments = ['AAPL.O', 'MSFT.O']
    parameters = ['TR.PriceClose', 'TR.Volume', 'TR.PriceLow', 'TR.PriceHigh', 'TR.PriceOpen', 'TR.Revenue']
    data = get_eikon_data(instruments, parameters)
    print(data.head())