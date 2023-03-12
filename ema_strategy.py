def ema_strategy(FMA,SMA):
    from py5paisa import FivePaisaClient
    import pandas as pd
    import numpy as np
    import requests
    import time


    def check_internet_connection():
            internet = True
            while internet == True:
            # initializing URL
                url = "https://www.google.com/"
                timeout = 10
                try:
                    # requesting URL
                    request = requests.get(url, timeout=timeout)
                    # print("Internet is on")
                    internet = False

                # catching exception
                except (requests.ConnectionError, requests.Timeout) as exception:
                    print("Internet disconnected")
                    time.sleep(2)


    check_internet_connection()
    select_date = '2022-12-07'
    bank_nifty_data=client.historical_data('N','C',2885,'1m',f'{select_date}',f'{select_date}')
    bank_nifty_data['Close']
    date_time = bank_nifty_data['Datetime']
    x = bank_nifty_data['Close'].values
    # x
    bank_nifty_data
    reliance = bank_nifty_data['Close'].to_frame()
    reliance


    reliance['FMA']= round(reliance['Close'].rolling(FMA).mean(),2)
    reliance['SMA']= round(reliance['Close'].rolling(SMA).mean(),2)
    
    # print(reliance.to_string())
    latest_fast_moving_avg=reliance.iloc[-1][1]
    latest_slow_moving_avg = reliance.iloc[-1][2]

    print('FMA',latest_fast_moving_avg)
    print('SMA',latest_slow_moving_avg )

    if latest_fast_moving_avg>latest_slow_moving_avg:
        print("buy stock") #buy code


        
from py5paisa import FivePaisaClient
cred = {
    "APP_NAME": "",
    "APP_SOURCE": "",
    "USER_ID": "",
    "PASSWORD": "",
    "USER_KEY": "",
    "ENCRYPTION_KEY": ""
}

client = FivePaisaClient(email="",
                         passwd="", dob="", cred=cred)
client.login()

# ema_strategy(FMA,SMA)
ema_strategy(12,25)
