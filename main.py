import requests
import json
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
from bidi.algorithm import get_display


def collect_data(plateNumber):
    ua = UserAgent()
    # plateNumber = "9476837"
    headers = {'Content-Type': 'application/json',
            'Accept': 'application/json',
            'User-Agent': f'{ua}'}
    try:
        r = requests.get(f'https://www.find-car.co.il/car/private/{plateNumber}',headers=headers )
        soup = BeautifulSoup(r.text, 'html.parser')
        items = []
        data = soup.find_all('div', class_ = ['flex flex_wrap table_conti base_details', 'flex flex_wrap table_conti important_details', 'flex flex_wrap table_conti more_details_tbl']  ) # 'flex flex_wrap table_conti base_details', 'flex flex_wrap table_conti important_details', 'flex flex_wrap table_conti more_details_tbl'
        if len(data) != 0:
            for row in data:
                for tag in row.find_all('li'):
                    for spanText in tag:
                        clearItem = " ".join(filter(None, spanText.text.strip().replace("\n", "").replace("\t", "").replace("\r", "").split(" ")))
                        if(len(clearItem) != 0):
                            items.append(clearItem)
                    if(tag.find('img', src = "/Resources/General/done_black_24dp.svg")):
                        items.append("כן")
                    elif(tag.find('img', src = "/Resources/General/close_black_24dp.svg")):
                        items.append("לא")
            items = dict(zip(items[::2], items[1::2]))
            keys_to_remove = ['1 2 3 4 5 6 7 8 9 10 11 12 13 14 15', '2', '4', '6', '8', '10', '12', '14', '1 2 3 4 5 6 7 8']
            items = {k: v for k, v in items.items() if k not in keys_to_remove}
        return items
    except: 
        return items

def collect_data_from_yad2(plateNumber):
    try:
        req = requests.get(f'https://gw.yad2.co.il/historical-pricelist-price/sub-model-by-plate/{plateNumber}')
        carData = req.json()
        if 'data' in carData:
            if 'subModelId' in carData['data']:
                subModelId = carData['data']['subModelId']
                year = carData['data']['year']
                with open('models.json', 'r', encoding='utf-8') as json_file:
                    models = json.load(json_file)
                for id in models['data']:
                    if 'models' in id:
                        for model in id['models']:
                            if 'subModels' in model:
                                for submodel in model['subModels']:
                                    if submodel['id'] == subModelId and submodel['year'] == year:
                                        return submodel
                
                                
            return carData['message']
        return None
    except:
        return None

def main():
    items = collect_data("9476837")
    # print(collect_data_from_yad2("9476837"))


if __name__ == "__main__":
    main()