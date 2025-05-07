from crawling import crawling_tistory
from crawling import data_parse
base_url = 'https://hse30.tistory.com/798'
con = crawling_tistory(base_url)
real_con = data_parse(con)
print(real_con)