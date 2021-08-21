#!/usr/bin/env python
import json
from newsapi import NewsApiClient
try:
    # For Python 3.0 and later
    from urllib.request import urlopen
except ImportError:
    # Fall back to Python 2's urllib2
    from urllib2 import urlopen



#Used to parse JSON data
def get_jsonparsed_data(url):
        response = urlopen(url)
        data = response.read().decode("utf-8")
        return json.loads(data)

#Return's -1 on failure
def countryname_to_abv(name):
    countriesDict = {'Argentina': 'ar', 'Greece': 'gr', 'Netherlands': 'nl', 'South Africa': 'za', 'Australia': 'au', 'Hong Kong': 'hk', 'New Zealand': 'nz', 'South Korea': 'kr', 'Austria': 'at', 'Hungary': 'hu', 'Nigeria': 'ng', 'Sweden': 'se', 'Belgium': 'be', 'India': 'in', 'Norway': 'no', 'Switzerland': 'ch', 'Brazil': 'br', 'Indonesia': 'id', 'Philippines': 'ph', 'Taiwan': 'tw', 'Bulgaria': 'bg', 'Ireland': 'ie', 'Poland': 'pl', 'Thailand': 'th', 'Canada': 'ca', 'Israel': 'il', 'Portugal': 'pt', 'Turkey': 'tr', 'China': 'cn', 'Italy': 'it', 'Romania': 'ro', 'UAE': 'ae', 'Colombia': 'co', 'Japan': 'jp', 'Russia': 'ru', 'Ukraine': 'ua', 'Cuba': 'cu', 'Latvia': 'lv', 'Saudi Arabia': 'sa', 'United Kingdom': 'gb', 'Czech Republic': 'cz', 'Lithuania': 'lt', 'Serbia': 'rs', 'United States': 'us','Egypt': 'eg', 'Malaysia': 'my', 'Singapore': 'sg', 'Venuzuela': 've', 'France': 'fr', 'Mexico': 'mx', 'Slovakia': 'sk', 'Germany': 'de', 'Morocco': 'ma', 'Slovenia': 'si'}
    for key in countriesDict.keys():
        lowerInput= name.lower()
        lowerKey = key.lower()
        if ((key == name) or (lowerKey == lowerInput)):
            return countriesDict[key]
    return -1



def get_news(countrySelec):
    # covidUrl = ("https://newsapi.org/v2/everything?country=" + country + "q=covid&apiKey=c52b171292aa4cb1a7f7aa858b6ff9d7")
    # #Now a parsed dict of covid news
    # covidUrl = get_jsonparsed_data(covidUrl)
    try:
        country_abv = countryname_to_abv(countrySelec)
        newsapi = NewsApiClient(api_key='c52b171292aa4cb1a7f7aa858b6ff9d7')
        # /v2/top-headlines
        top_headlines = newsapi.get_top_headlines(q="Covid-19", country=country_abv)

        print("TOP HEADLINES FOR", countrySelec.upper() + ": \n\n")
        print(top_headlines)

        print("\n\n EVERYTHING: \n\n")
        all_articles = newsapi.get_everything(q="Covid-19", sort_by='relevancy')
        print(all_articles)
        
    except Exception as e: 
        print("news_error")
        print(e)


exitFlag = 0
#Main loop
while (exitFlag==0):
    print("Type 0 to close program.")
    country = input("Please enter a countries name: ")
    if (country == "0"):
        exitFlag = 1
    else:
        try:
            get_news(country)
        except Exception as e: 
            print("search_error")
            print(e)