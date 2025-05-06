import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

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