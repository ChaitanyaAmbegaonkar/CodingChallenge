#https://www.sbir.gov/sbirsearch/award/all
import time

from selenium import webdriver
from bs4 import BeautifulSoup

def get_soup(browser, url):
    try:
        browser.get(url)
        html = browser.page_source.encode('utf-8')
        soup = BeautifulSoup(html, "lxml")
        return soup

    except:
        print("problem in generating the soup")
        return None


def fetch(browser,url):
    try:
        soup = get_soup(browser, url)
        links = soup.find_all('a')

        for i in links:
            if str(i).__contains__("/solr_print/award/all?"):
                url2 = "https://www.sbir.gov"+i.attrs['href']
                driver = browser.get(url2)
                time.sleep(5)
                submit_button = driver.find_elements_by_xpath('//*[@id="recaptcha-anchor"]/div[5]')[0]
                submit_button.click()
                submit_button2 = driver.find_elements_by_xpath('//*[@id="edit-submit"]')[0]
                submit_button2.click()
    except:
        print("fault")

# options = webdriver.ChromeOptions()
# options.add_argument('--ignore-certificate-errors')
# options.add_argument("--test-type")
# options.binary_location = "/Users/user/Documents/patent_code/match_2_SBIR_to_patents/chromedriver"
# brow = webdriver.Chrome(chrome_options=options)
brow = webdriver.Chrome(executable_path='/Users/user/Documents/patent_code/match_2_SBIR_to_patents/chromedriver')
fetch(brow,"https://www.sbir.gov/sbirsearch/award/all")
