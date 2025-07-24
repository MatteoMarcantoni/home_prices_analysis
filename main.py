import pandas as pd
from cbsodata_client import get_data, get_meta

TABLE_ID = '83625NED'

def get_house_prices():
    # Downloaden entire table
    return pd.DataFrame(get_data(TABLE_ID))
    # return data

def get_metadata_house_prices():
    # Download metadata from table
    return pd.DataFrame(get_meta(TABLE_ID, 'DataProperties'))

if __name__ == "__main__":
    house_prices = get_house_prices()
    print(house_prices.head())

    metadata = get_metadata_house_prices()
    print(metadata[['Key','Title']])
