import requests
from bs4 import BeautifulSoup
import csv



def write_to_csv(data):
    with open('cars.csv', 'a') as file:
        writer = csv.writer(file)
        writer.writerow([data['title'], data['price'], data['img']])

def get_html(url):
    response = requests.get(url)
    return response.text

def get_total_pages(html):
    response = requests.get(url_)
    return requests.text

def get_total_pages(html):
    soup = BeautifulSoup(html, 'lxml')
    page_list = soup.find('div', class_ = 'pages fl').find_all('a')
    last_page = page_list[-2].text
    return last_page


def get_data(html):
    soup = BeautifulSoup(html, 'lxml')
    cars = soup.find('div', class_ = 'catalog-list').find_all('a', class_ = 'catalog-list-item')
#     print(cars)
    for car in cars:
        try:
            title = car.find('span', class_ = 'catalig-item-caption').text.strip()
        except:
            title = ''
            

        try:
            img = car.find('img', class_ = 'catalog-item-cover-img').get('src')
        except:
            img = ''
        try:
            price = car.find('span', class_ = 'catalog-item-price')
        except:
            price = ''

        data = {'title': title, 'price': price, 'img': img} 
        print(data)
        write_to_csv(data) 
        # print(price)

def main():
    url_ = 'https://cars.kg/offers'
    get_html(url_)
    html = get_html(url_)
#     get_data(html)
    number = int(get_total_pages(html))
    i = 1
    while i <= number:
        print(i)
        url_ = f'https://cars.kg/offers/{i}'
        html = get_html(url_)
        number = int(get_total_pages(html))
        if not BeautifulSoup(html, 'lxml')
        i += 1
        print(number) 

with open('cars.csv', 'w') as file:
    writer = csv.writer(file)
    writer.writerow(['title'])
main()

# git init
# git add . 
# git commit -m 'комент'
# git remote add origin <SSH>
# git push origin master