import requests
from bs4 import BeautifulSoup
from write_to_db import write_to_db
import csv
                                
# with open('file.csv', 'w') as file: #  можно быстро посмотреть что парситься в файле file.csv 
#     """ открывает файл file.csv и 
#     записывает туда заголовки столбцов"""
#     writer = csv.writer(file, delimiter=',')
#     writer.writerow(['image', 'date', 'price', 'currency'])


# def write_to_csv(data):  #  открывает файл file.csv и записывает туда спарсенные даннные
#     with open('file.csv', 'a') as file:
#         writer = csv.writer(file)
#         writer.writerow([data['image'], data['date'], data['price'], data['currency']])


def get_html(url):  # возращает html код стр в виде строки
    response = requests.get(url)
    return response.text


def get_total_pages(html):   # возвращает общее кол-во страниц 
    soup = BeautifulSoup(html, 'lxml')
    page_list = soup.find('div', class_='pagination').find_all('a')
    last_page = page_list[-3].text
    return last_page


def get_data(html):   # вытаскивает нужные данные из стр и записывает в бд
    soup = BeautifulSoup(html, "lxml")
    houses = soup.find_all('div', class_='search-item')
    print(houses)
    for house in houses:
        try:
            image = house.find('div', class_='image').find('img').get('data-src')
        except:
            image = 'NUll'
        
        try:
            date = house.find('span', class_='date-posted').text
        except:
            date='NULL'
        
        try:
            price = house.find("div", class_="price").text.split()[0][1:]
        except:
            price = 'NULL'

        try:
            currency = house.find('div', class_='price').text.split()[0][0]
        except:
            currency = 'NULL'

        data = {'image':image, 
                'date':date,
                'price':price,
                'currency': currency
            }
        
        write_to_db(data)
        # write_to_csv(data)



def main():  # вызывает нужные функции
    url_ = "https://www.kijiji.ca/b-apartments-condos/city-of-toronto/c37l1700273"
    html = get_html(url_)
    get_data(html)
    number = int(get_total_pages(html))
    i = 1
    while i<= number:
        
        url =f'https://www.kijiji.ca/b-apartments-condos/city-of-toronto/page-{i}/c37l1700273'
        html = get_html(url)
        number = int(get_total_pages(html))
        if not BeautifulSoup(html, 'lxml').find_all('div', class_="search-item"):
            break
        get_data(html)
        i += 1


if __name__ == "__main__":
    main()




