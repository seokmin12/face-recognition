from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from tqdm import tqdm

keyword = input('검색할 키워드를 입력하세요: ')

# 웹 접속 - 네이버 이미지 접속
print("접속중")
driver = webdriver.Chrome('/Users/seokmin/Desktop/python/chromedriver')
driver.implicitly_wait(30)

url = f'https://search.naver.com/search.naver?where=image&sm=tab_jum&query={keyword}'
driver.get(url)

# 페이지 스크롤 다운
body = driver.find_element_by_css_selector('body')
for i in range(10):
    body.send_keys(Keys.PAGE_DOWN)
    time.sleep(1)

# 이미지 링크 수집
imgs = driver.find_elements_by_css_selector('img._image')
result = []
for img in tqdm(imgs):
    if 'http' in img.get_attribute('src'):
        result.append(img.get_attribute('src'))
# print(result)

driver.close()
print("수집완료")

# 폴더생성
print("폴더생성")
import os
if not os.path.isdir('./{}'.format(keyword)):
    os.mkdir('./{}'.format(keyword))

# 다운로드
print("다운로드")
from urllib.request import urlretrieve
for index, link in tqdm(enumerate(result)):
    start = link.rfind('.')
    end = link.rfind('&')
    # print(link[start:end])
    filetype = link[start:end]  # .png

    urlretrieve(link, './{}/{}{}{}'.format(keyword, keyword, index, '.jpg'))

print("다운로드 완료")
