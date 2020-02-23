from splinter import Browser
from bs4 import BeautifulSoup
import pandas as pd
import os
import time
while True:
    executable_path = {'executable_path': 'C:/chromedriver.exe'}
    browser = Browser('chrome', **executable_path, headless=True)
    url = 'https://www.google.com/search?q=pro+wrestling+news&sxsrf=ACYBGNQRnT7i1rFugB-mIDIE7dRXis9utw:1579285550822&source=lnms&tbm=nws&sa=X&ved=2ahUKEwiCp4WSoYvnAhUIV80KHVS0DZ8Q_AUoAXoECA4QAw&biw=1920&bih=937'
    browser.visit(url)
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')
    articles = soup.find_all('div', class_='bkWMgd')
    number = 0
    headlines = []
    sources = []
    times = []
    excerpts = []
    links = []
    image_links = []
    for article in articles:
        if number == 11:
            break
        headlines.append((article.find('div', class_="phYMDf nDgy9d")).text.replace("\n", "").strip())
        sources.append((article.find('div', class_='pDavDe RGRr8e')).text)
        times.append((article.find('span', class_='eNg7of')).text)
        excerpts.append((article.find('div', class_='eYN3rb')).text.replace("\n", "").strip())
        links.append((article.find('div', class_='dbsr')).a['href'])
        image_links.append((article.find('img')['src']) + '\n')
        number = number + 1
    browser.quit()
    news_df = pd.DataFrame()
    news_df["Headline"] = headlines
    news_df["Source"] = sources
    news_df["Posted"] = times
    news_df["Excerpt"] = excerpts
    news_df["Link"] = links
    news_df["ImageLink"] = image_links
    news_df.to_csv("news.csv", index=False)
    time.sleep(1*60)