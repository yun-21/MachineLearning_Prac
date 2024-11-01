import requests
from bs4 import BeautifulSoup
import pandas as pd

# 크롤링할 웹사이트 URL
url = 'http://books.toscrape.com'

# 웹 페이지 요청
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# 데이터 추출
books = []
for book in soup.find_all('article', class_='product_pod'):
    title = book.h3.a['title']
    price = book.select('p.price_color')[0].get_text()
    books.append({'title': title, 'price': price})

# 데이터 저장
# df = pd.DataFrame(books)
# df.to_csv('books.csv', index=False)
print(books)