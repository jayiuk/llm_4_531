import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import json
import re

driver = webdriver.Chrome()

def crawling_tistory(url):
    contents = []
    try :
        driver.get(url)
        time.sleep(10)
        con = driver.find_elements(By.CLASS_NAME, "tt_article_useless_p_margin.contents_style")
        for c in con:
            texts = c.text
            contents.append(texts)
    except TimeoutError as e:
        print("크롤링이 안됩니다.", str(e))
        driver.quit()
    finally :
        driver.quit()
        
    return contents

def data_parse(data):
    pattern = r'(?P<heading>\d{1,2}\. .+?)\n(?P<content>.*?)(?=\n\d{1,2}\. |\Z)'
    matches = re.finditer(pattern, data, re.DOTALL)
    new_data = []
    for match in matches:
        title = match.group('heading').strip()
        contents = match.group('content').strip()
        new_data.append({'title' : title, 'content' : contents})
    return new_data