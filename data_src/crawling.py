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
        con = driver.find_elements(By.CLASS_NAME, "entry-content.wp-block-post-content.is-layout-constrained.wp-block-post-content-is-layout-constrained")
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
    sentences = re.findall(r'.+?(?:[.!?](?=\s)|\Z)', data, flags=re.DOTALL)
    new_data = {}
    for j in range(1, len(sentences)+1):
        for i, s in enumerate(sentences):
            if s.strip().startswith('Q') and i + 1 < len(sentences):
                a = sentences[i + 1].strip()
                new_data['question'] = s
                new_data['answer'] = a
                path = f'tuning_531{j}.json'
                with open(path, 'w', encoding='UTF-8') as f:
                    json.dump(new_data, f, ensure_ascii=False)
    return new_data