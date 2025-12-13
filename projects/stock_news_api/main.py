import requests
from twilio.rest import Client
from env_vars import *


## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

def get_tsla_stock_price() -> list :
    tsla_stock_price = requests.get(url=VANTAGE_URL_FULL)
    tsla_stock_price.raise_for_status()
    tsla_data = tsla_stock_price.json()
    days_json = tsla_data['Time Series (Daily)']

    it = iter(days_json)
    first_key, second_key = next(it, None), next(it, None)

    first_value, second_value = days_json[first_key], days_json[second_key]
    first_day_close_val = float(first_value['4. close'])
    second_day_close_val = float(second_value['4. close'])
    return  first_day_close_val, second_day_close_val

def calculate_perc_change():
    ab = get_tsla_stock_price()
    change =  ((ab[0] - ab[1])  / ab[1]) * 100
    return round(change, 2)

## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME.
def get_news():
    news_dict = {}
    news_resp = requests.get(url=NEWS_URL, params=NEWS_PARAMS)
    news_resp.raise_for_status()
    news_data = news_resp.json()
    top_3_articles = news_data['articles'][:3]
    for idx, article in enumerate(top_3_articles,1):
        title = article['title']
        description = article["description"]
        url = article['url']
        news_dict[f"news_{idx}"] = [title, description, url]
    return news_dict

## STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number.
perc_change = calculate_perc_change()
print(perc_change)

try:
    if abs(perc_change) > 1.5:
        news = get_news()
        client = Client(username=TWILLIO_ACCOUNT_SID,
                        password=TWILLIO_AUTH_TOKEN)
        message = client.messages.create(
            messaging_service_sid=TWILLIO_MESSAGE_SID,
            body=f"\n{STOCK}: {perc_change}"
                 f"\n\nTitle: {news['news_1'][0]}"
                 f"\n\nBrief: {news['news_1'][1]}"
                 f"\n\nLink: {news['news_1'][-1]}",
            from_=TWILLIO_LINE,
            to=MAIN_LINE
        )
        # print(news)
        # print(message.error_message)
        print("Success")
    else:
        print("No shaking")
except Exception as e:
    print(e)


#Optional: Format the SMS message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""


