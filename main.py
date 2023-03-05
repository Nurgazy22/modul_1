import requests
from bs4 import BeautifulSoup
from write_to_db import write_to_db


def get_html(url):  # возращает html код стр в виде строки
    response = requests.get(url)
    return response.text


def get_total_pages(html):   # возращает общее кол-во страниц 
    soup = BeautifulSoup(html, 'lxml')
    page_list = soup.find('div', class_='pagination').find_all('a')
    last_page = page_list[-3].text
    return last_page


def get_data(html):   # вытаскивает нужные данные из стр и записывает в бд
    soup = BeautifulSoup(html, "lxml")
    houses = soup.find_all("div", class_="search-item")
    
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
            price = house.find("div", class_="price").text.split()[0]
        except:
            price = 'NULL'
        
        data = {'image':image, 
                'date':date,
                'price':price
            }
        
        write_to_db(data)


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




