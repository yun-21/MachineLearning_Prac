from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

# ChromeDriver 경로 설정
service = Service('./chromedriver')  # 실제 경로로 수정

# WebDriver 초기화
driver = webdriver.Chrome(service=service)

# 예시로 구글 홈페이지 열기
driver.get('https://en.wikipedia.org/wiki/Main_Page')

elements = driver.find_elements(By.CSS_SELECTOR, 'div.MainPageBG.mp-box')

for element in elements:
    print(element.text)
# 종료
# driver.quit()
