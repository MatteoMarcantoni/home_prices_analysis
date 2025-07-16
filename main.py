from APIClient import get_odata

def main():
    target_url = "https://beta-odata4.cbs.nl/CBS/83765NED"

    # Downloaden van gehele tabel, duurt ongeveer 2 minuten
    target_url = target_url + "/Observations"
    # Downloaden van eerste 100 rijen uit de tabel

    # target_url = target_url + "/Observations?$top=100"
    data = get_odata(target_url)
    print(data.head())
    
if __name__ == "__main__":
    main()
