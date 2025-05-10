from crawling import crawling_tistory
from crawling import data_parse
base_url = 'https://burnfit.io/workout-program/jim-wendler-531-beginner/'
con = crawling_tistory(base_url)
print(con)
real_con = data_parse(con)
print(real_con)