from bs4 import BeautifulSoup
import requests
import json


class ScrapeStrategy():
    def scrape(self, url):
        pass


class BeautifulSoupStrategy(ScrapeStrategy):
    def scrape(self, url, stock_symbol):
        response = requests.get(url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, 'html.parser')
            data = {}
            open_value_td = soup.find('td', {'data-test': 'OPEN-value'})
            close_value_td = soup.find('td', {'data-test': 'PREV_CLOSE-value'})
            volume_td = soup.find('td', {'data-test': 'TD_VOLUME-value'})
            market_cap_td = soup.find('td', {'data-test': 'MARKET_CAP-value'})
            data['stock_symbol'] = stock_symbol
            if open_value_td:
                data['open'] = open_value_td.text.strip()
            else:
                data['open'] = 'Open Value not found'
            if close_value_td:
                data['close'] = close_value_td.text.strip()
            else:
                data['close'] = 'Close Value not found'
            if volume_td:
                data['volume'] = volume_td.text.strip()
            else:
                data['volume'] = 'Volume Value not found'
            if market_cap_td:
                data['market_cap'] = market_cap_td.text.strip()
            else:
                data['market_cap'] = 'Market Cap Value not found'
            return data
        else:
            return f'Failed to retrieve the webpage, status code: {response.status_code}'


class SeleniumStrategy(ScrapeStrategy):
    def scrape(self, url):
        pass


class Context:
    def __init__(self, strategy):
        self._strategy = strategy

    def set_strategy(self, strategy):
        self._strategy = strategy

    def scrape(self, url, stock_symbol):
        return self._strategy.scrape(url, stock_symbol)


class introducir_beauti:
    context = Context(BeautifulSoupStrategy())
    values = context.scrape(url, stock_symbol)
    print('Values:', values)

    datos_requeridos1 = "datos_beautifulSoap.json"
    
    with open(datos_requeridos1, "w") as archivo:
        json.dump(values, archivo)


class introducir_beauti:
    datos_requeridos2 = "datos_seleniumStrategy.json"
    #with open(datos_requeridos2, "w") as archivo:
    #    json.dump(values, archivo)

def main():
    stock_symbol = input("Enter the stock symbol (e.g., TSLA for Tesla): ")
    url = f'https://finance.yahoo.com/quote/{stock_symbol}'
    
    
introducir_beauti
    


if __name__ == "__main__":
    main()
