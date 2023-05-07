import requests
import json
import time

menu = input("MENU\n1. World Wide news\n2. Top headlines from India\n\nEnter your choice : ")

if menu == "1":
    query = input("\nWhat type of news you want to read : ").lower()
    url = f"https://newsapi.org/v2/everything?q={query}&from=2023-04-06&sortBy=publishedAt&apiKey=eca97a922f584620ac87752994b31a92"

    r = requests.get(url)
    news = json.loads(r.text)

    print("\n")

    for article in news["articles"]:
        print(article["title"])
        print(article["description"])
        print("\n----------------------------------------------------------------------------------------------------------\n")

else:
    url = f"https://newsapi.org/v2/top-headlines?country=in&apiKey=eca97a922f584620ac87752994b31a92"

    r = requests.get(url)
    news = json.loads(r.text)

    print("\n")

    for article in news["articles"]:
        print(article["title"])
        print(article["description"])
        print("\n----------------------------------------------------------------------------------------------------------\n")
        time.sleep(0.5)