import pandas as pd
import APIClient

def main():
    identifier = '83625NED'
    # Downloaden van gehele tabel (kan een halve minuut duren)
    data = pd.DataFrame(APIClient.get_data(identifier))
    print(data.head())
    
if __name__ == "__main__":
    main()
