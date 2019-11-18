import pandas as pd
from bs4 import BeautifulSoup
import csv
def get_tables(soup):
    try:
        return soup.find('a', {'class': 'downloadLink'})
    except:
        print "cannot find footer tables"
        return None


def get_soup(browser, url):
    try:
        browser.get(url)
        html = browser.page_source.encode('utf-8')
        soup = BeautifulSoup(html, "lxml")
        return soup
    except:
        print("problem in generating the soup")
        return None


def scraper():
    zipcode = ['90007', '10001', '93553']
    files = []
    from selenium import webdriver
    import time
    current = time.strftime('%Y-%m-%d-%H-%M-%S')
    files.append(str(current))
    browser = webdriver.Chrome(executable_path='/Users/user/Documents/patent_code/match_2_SBIR_to_patents/chromedriver')
    for i in zipcode:
        url = "https://www.redfin.com/zipcode/"+i+"/filter/include=sold-6mo"
        soup = get_soup(browser, url)
        link = str(get_tables(soup))
        link = link.split(" ")
        url = link[2].replace("\"","")
        url = url.replace("href=","")
        url = url.replace("amp;", "")
        url = "https://www.redfin.com"+url
        browser.get(url)
    current = time.strftime('%Y-%m-%d-%H-%M-%S')
    files.append(str(current))
    time.sleep(5)
    return files

def merge(timelimit):
    import os
    path = os.path.expanduser('~/Downloads')
    files = os.listdir(path)
    info = []
    info.append(('SOLD DATE', 'PROPERTY TYPE', 'ADDRESS', 'CITY', 'STATE', 'ZIP',
                 'PRICE', 'BEDS', 'BATHS', 'LOCATION', 'SQUARE FEET', 'LOT SIZE',
                 'YEAR BUILT', 'DAYS ON MARKET', '$/SQUARE FEET'))
    for filename in files:
        path1 = path + "/" + filename
        if filename.startswith("redfin"):
            if timelimit[0][:13] == filename[7:20]:
                try:
                    df1 = pd.read_csv(path1)
                    for ind,row in df1.iterrows():
                        info.append((row['SOLD DATE'],row['PROPERTY TYPE'],row['ADDRESS'],row['CITY'],row['STATE'],row['ZIP'],row['PRICE'],row['BEDS'],row['BATHS'],row['LOCATION'],row['SQUARE FEET'],row['LOT SIZE'],row['YEAR BUILT'],row['DAYS ON MARKET'],row['$/SQUARE FEET']))
                except:
                    print("Error occurred")
                os.remove(path1)
    with open('RedfinData.csv', mode='w') as employee_file:
        writer = csv.writer(employee_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        for i in info:
            writer.writerow(i)


files = scraper()
merge(files)