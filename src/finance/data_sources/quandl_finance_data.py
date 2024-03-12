import quandl as qdl
from util.config_util import get_config

def get_quandl_api_key():                
    return get_config()['quandl']['api_key']

def get_quandl_data(dataset, start_date, end_date):
    qdl.ApiConfig.api_key = get_quandl_api_key()
    qdl_data = qdl.get(dataset, start_date=start_date, end_date=end_date)
    return qdl_data

if __name__ == "__main__":
    # dataset = "WIKI/AAPL"
    # start_date = "2024-01-01"
    # end_date = "2024-03-12"
    # data = get_quandl_data(dataset, start_date, end_date)
    # print(data.head())

    dataset = "BCHAIN/MKPRU"
    start_date = "2024-01-01"
    end_date = "2024-03-12"
    data = get_quandl_data(dataset, start_date, end_date)
    print(data.head())

