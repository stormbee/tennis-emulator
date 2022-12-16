from genericpath import exists
import json
import os
import random
import re
import time
import requests
from bidi import algorithm as bidialg

for i in range(10):
    a = random.randint(1, 1000000)
    print(a)

# req = requests.get(f"https://gw.yad2.co.il/price-list/sub-model/price-calculation-options?subModelId=30556")
# priceCalculation = req.json()
# # ownershipPercent = [item['value'] for item in priceCalculation['data']['ownershipPercent'] if item['text'] == 'פרטי' ][-1]
# # print(ownershipPercent)

# warrantyType = [item['value'] for item in priceCalculation['data']['warrantyType'] if item['text'] == 'מנוע + הילוכים' ][0]
# print(warrantyType)
# if warrantyType == 0:
#     warrawarrantyPercentByType = 0
# else:
#     warrawarrantyPercentByType = [item['value'] for item in priceCalculation['data']['warrantyPercentByType'][f'{warrantyType}'] if item['text'] == '3 שנים' ][0]
# # for i in priceCalculation['data']['warrantyPercentByType'][f'{warrantyType}']:
# #     print(i)
# print(warrawarrantyPercentByType)    
    
# def getModels():
#     req = requests.get('https://gw.yad2.co.il/price-list/search-options/manufacturers')
#     manufacturers = req.json()
#     if 'data' in manufacturers:
#         manufacturers['data'] = sorted(manufacturers['data'], key=lambda k: k['id'])
#     manufacturersID = [manufacturer['id'] for manufacturer in manufacturers['data']]
#     for id in manufacturersID:
#         req = requests.get(f'https://gw.yad2.co.il/price-list/search-options/{id}/models/')
#         models = req.json()
#         if 'data' in manufacturers:
#             for manufacturer in manufacturers['data']:
#                 if 'data' in models:
#                     for model in models['data']:
#                         if manufacturer['id'] == model['manufacturerId']:
#                             manufacturer['models'] = models['data']
#                             # print(f"Id : {manufacturer['id']} was written")
#                             break
#     if 'data' in models:
#         for model in models['data']:
#             if 'models' in model:
#                 model['models'] = sorted(model['models'], key=lambda k: k['title'])

#     with open ('models.json', 'w', encoding='utf-8') as outfile:
#         json.dump(manufacturers, outfile, ensure_ascii=False, indent=4)
    


# def getSubmodels(models):
#     req = requests.get('https://gw.yad2.co.il/price-list/feed?family-type=7%2C4%2C9%2C6%2C8%2C3%2C2%2C10%2C1%2C5')
#     submodels = req.json()
    
#     if 'data' in submodels:
#         limit = submodels['data']['pagination']['limit']
#         total = submodels['data']['pagination']['total']
#         pagination = total // limit if total % limit == 0 else total // limit + 1
#         for k in range(pagination + 1):
#             print(f'Page {k+1}')
#             req = requests.get(f'https://gw.yad2.co.il/price-list/feed?family-type=7%2C4%2C9%2C6%2C8%2C3%2C2%2C10%2C1%2C5&page={k+1}')
#             submodels = req.json()
    
            
        
#             for i, id in enumerate(models['data']):
#                 if 'models' in id:
#                     for j, model in enumerate(id['models']):
#                         listOfModelsId = []
#                         for submodel in submodels['data']['models']:
#                             if model['id'] == submodel['modelId']:
#                                 for subsubmodel in submodel['subModels']:
                                
#                                     subsubmodel['year'] = submodel['year']
#                                     listOfModelsId.append(subsubmodel)
#                                 if 'subModels' in models['data'][i]['models'][j]:
#                                     models['data'][i]['models'][j]['subModels'] += listOfModelsId
#                                 else:
#                                     models['data'][i]['models'][j]['subModels'] = listOfModelsId
#                                 [dict(t) for t in {tuple(d.items()) for d in models['data'][i]['models'][j]['subModels']}]
                                
#         with open ('models.json', 'w', encoding='utf-8') as outfile:
#             json.dump(models, outfile, ensure_ascii=False, indent=4)            

                    
# def chechPrice(user_input):
#     # with open('data.json', 'r', encoding='utf-8') as json_file:
#     #     car = json.load(json_file)
#     req = requests.get(f'https://gw.yad2.co.il/historical-pricelist-price/sub-model-by-plate/{user_input}')
#     carData = req.json()
#     print(carData)
#     if 'data' in carData:
#         if 'subModelId' in carData['data']:
#             subModelId = carData['data']['subModelId']
#             ascentYearOnRoad = carData['data']['year']
#             req = requests.get(f'https://www.yad2.co.il/price-list/_next/data/GXlrm5jlf0Afk4xzgrUiT/sub-model/30556/2017.json?sub-model-id=30556&year=2017')
#             carPrice = req.json()
#             print(carPrice)
#             if 'data' in carPrice:
#                 if 'price' in carPrice['data']:
#                     return carPrice['data']['price']
#         else:
#             return None
#     else:
#         return None
#     parametrs = {
#         "subModelId": 30556, # done
#         "previousOwnershipPercent": 0, # done
#         "kilometers": 21500, # done
#         "ascentYearOnRoad": 2017, # done
#         "ascentMonthOnRoad": 1, # done
#         "price": 43300,
#         "ownersNumber": 1, # done
#         "currentOwnershipPercent": 0, # done
#         "appraiserReducePercent": 0, # done
#         "warrantyPercent": 0, # done
#         "hasLPGSystem": False # done
#     }
#     # link = f"https://gw.yad2.co.il/pricelist-calculator/calculate-price?subModelId={parametrs['subModelId']}&previousOwnershipPercent={parametrs['previousOwnershipPercent']}&kilometers={parametrs['subModelId']}&ascentYearOnRoad={parametrs['ascentYearOnRoad']}&ascentMonthOnRoad={parametrs['ascentMonthOnRoad']}&price={parametrs['price']}&ownersNumber={parametrs['ownersNumber']}&currentOwnershipPercent={parametrs['currentOwnershipPercent']}&appraiserReducePercent={parametrs['appraiserReducePercent']}&warrantyPercent={parametrs['warrantyPercent']}&hasLPGSystem={parametrs['hasLPGSystem']}"
    
                


 


# def main():
    
    # if not os.path.isfile('models.json'):
    #     getModels()
    # with open('models.json', 'r', encoding='utf-8') as json_file:
    #     models = json.load(json_file)
    # getSubmodels(models)


    # user_input = '9476837'
    # chechPrice(user_input)
    # i need to get how much time taking to get the data

    # start = time.time()
    # for i, id in enumerate(models['data']):
    #     if 'models' in id:
    #         for j, model in enumerate(id['models']):
    #             if 'subModels' in model:
    #                 for k, submodel in enumerate(model['subModels']):
    #                     if submodel['id'] == 30556 and submodel['year'] == 2017:
    #                         print(submodel)
    #                         end = time.time()
    #                         break


                            
    
    
    

# if __name__ == '__main__':
#     main()