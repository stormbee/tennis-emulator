import asyncio
import json
import math
import re
from aiogram import Bot, Dispatcher, Router
from aiogram.types import KeyboardButton, Message, ReplyKeyboardMarkup, ReplyKeyboardRemove
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from aiogram.utils.markdown import hbold
from bidi import algorithm as bidialg
import requests
from settings import TOKEN
from main import collect_data, collect_data_from_yad2


class Form(StatesGroup):
    plateNumber = State()
    check_price = State()
    kilometers = State()
    ownersNumber = State()
    currentOwnershipPercent = State()
    previousOwnershipPercent = State()
    ascentYearOnRoad = State()
    ascentMonthOnRoad = State()
    warranty = State()
    warrantyPercent = State()
    hasLPGSystem = State()


 
bot = Bot(token=TOKEN, parse_mode="HTML")
dp = Dispatcher()
form_router = Router()
dp.include_router(form_router)
regex = r"^\d{7,8}$"
listOfOwners = ['פרטי', 'רכב ביבוא אישי ', 'חברה/ליסינג יד ראשונה  0 ק\"n  ', 
                'בעלות יבואן / רכב הדגמה', 'ליסינג רכב חדש עד 12 חודשי שימוש',
                'ליסינג פרטי', 'ליסינג נהג יחיד', 'ליסינג  מרובה נהגים',
                'ליסינג - קיבוצים, רשויות, אגודות שיתופיות, משטרה, ממשלתי וצהל',
                'חברת השכרה', 'רכב השכרה עד 12 חודשי שימוש ',
                'קיבוצים, רשויות, אגודות שיתופיות ,משטרה, ממשלתי וצהל', 'חברה/עמותה - נהג יחיד',
                'חברה/עמותה - מרובה נהגים', 'סיור תיור', 'דיפלומט', 'מונית', 'רכב לימוד נהיגה']


@form_router.message(Command(commands=["start"]))
async def command_start(message: Message, state: FSMContext) -> None:
    await state.clear()
    await state.set_state(Form.plateNumber)
    await message.answer(
        "Welcome To Israel Cars Info Bot.Here you can get information about any Israel car",
        reply_markup=ReplyKeyboardRemove(),
    )



@form_router.message(Form.plateNumber)
async def process_plateNumber(message: Message, state: FSMContext) -> None:
    user_input = message.text
    if re.match(regex, user_input):
        carData = collect_data(user_input)
        # before need to save carData in json file
        # with open('data.json', 'r', encoding='utf-8') as outfile:
        #     carData = json.load(outfile)
        card = []
        if len(carData) != 0:
            for key, value in carData.items():
                card.append(bidialg.get_display(f"{hbold(key)}" + ' : ' + value))
            await message.answer(bidialg.get_display("\n".join(card)))
            await state.update_data(plateNumber=message.text)
            await state.set_state(Form.check_price)

            await message.answer(
                f"Want to check price?",
                reply_markup=ReplyKeyboardMarkup(
                    keyboard=[
                        [
                            KeyboardButton(text="Yes"),
                            KeyboardButton(text="No"),
                        ]
                    ],
            resize_keyboard=True
            )
            ,)
            
        else:
            await message.answer("No results found\nTry again /start")
    else:
        await message.answer("Please enter a valid number or press /start to try again")
    



@form_router.message(Form.check_price)
async def process_get_kilometrs(message: Message, state: FSMContext, text = None) -> None:
    if message.text.casefold() == "no":
        await state.get_data()
        await state.clear()
        await message.answer("'Thank you for using our service!\nPress /start to check again'")
    elif message.text.casefold() == "yes" or text == "yes":
        await state.update_data(check_price=message.text)
        await state.set_state(Form.kilometers)
        await message.answer(
                    f"How much Kilometrs?",
                    reply_markup=ReplyKeyboardRemove(),
                )
    else:
        await message.answer("Please use buttons to interact with the bot")
    


@form_router.message(Form.kilometers)
async def process_ownersNumber(message: Message, state: FSMContext) -> None:
    if re.match(r"^\d{1,7}$", message.text):
        await state.update_data(kilometers=message.text)
        await state.set_state(Form.ownersNumber)

        await message.answer(
                    f"Number of owners?",
                    reply_markup=ReplyKeyboardMarkup(
                        keyboard=[
                            [
                                KeyboardButton(text="1"),
                                KeyboardButton(text="2"),
                                KeyboardButton(text="3")
                            ],
                            [
                                KeyboardButton(text="4"),
                                KeyboardButton(text="5"),
                                KeyboardButton(text="6"),
                                KeyboardButton(text="7 or more")
                            ]
                        ],
                resize_keyboard=True,
                one_time_keyboard=True
                )
                ,)
    else:
        return await process_get_kilometrs(message, state, "yes")



@form_router.message(Form.ownersNumber, lambda message : message.text in ['1', '2', '3', '4', '5', '6', '7 or more'])
async def process_currentOwnershipPercent(message: Message, state: FSMContext) -> None:
    keyboard=[
                        [
                            KeyboardButton(text="פרטי"),
                            KeyboardButton(text="רכב ביבוא אישי "),
                            KeyboardButton(text="חברה/ליסינג יד ראשונה  0 ק\"n  ")
                        ],
                        [
                            KeyboardButton(text="בעלות יבואן / רכב הדגמה"),
                            KeyboardButton(text="ליסינג רכב חדש עד 12 חודשי שימוש"),
                            KeyboardButton(text="ליסינג פרטי")
                        ],
                        [
                            KeyboardButton(text="ליסינג נהג יחיד"),
                            KeyboardButton(text="ליסינג  מרובה נהגים"),
                            KeyboardButton(text="ליסינג - קיבוצים, רשויות, אגודות שיתופיות, משטרה, ממשלתי וצהל")
                        ],
                        [    
                            KeyboardButton(text="חברת השכרה"),
                            KeyboardButton(text="רכב השכרה עד 12 חודשי שימוש "),
                            KeyboardButton(text="קיבוצים, רשויות, אגודות שיתופיות ,משטרה, ממשלתי וצהל")
                        ],
                        [    
                            KeyboardButton(text="חברה/עמותה - נהג יחיד"),
                            KeyboardButton(text="חברה/עמותה - מרובה נהגים"),
                            KeyboardButton(text="סיור תיור")
                        ],
                        [    
                            KeyboardButton(text="דיפלומט"),
                            KeyboardButton(text="מונית"),
                            KeyboardButton(text="רכב לימוד נהיגה")
                        ]
                    ]
    if "ownersNumber" not in  await state.get_data():
        if message.text == "1":
            await state.update_data(previousOwnershipPercent="פרטי")
        await state.update_data(ownersNumber=message.text[0])
        await state.set_state(Form.currentOwnershipPercent)
        await message.answer(
                    f"Current Owner?",
                    reply_markup=ReplyKeyboardMarkup(
                    keyboard=keyboard, 
                resize_keyboard=True,
                one_time_keyboard=True
                )
                ,)
    else:
        await state.set_state(Form.previousOwnershipPercent)
        await message.answer(
                    f"Previous Owner?",
                    reply_markup=ReplyKeyboardMarkup(
                    keyboard=keyboard, 
                resize_keyboard=True,
                one_time_keyboard=True
                )
                ,)
@form_router.message(Form.currentOwnershipPercent, lambda message : message.text in listOfOwners)
@form_router.message(Form.previousOwnershipPercent, lambda message : message.text in listOfOwners)
async def process_ascentMonthOnRoad(message: Message, state: FSMContext) -> None:
    if "previousOwnershipPercent" not in await state.get_data():
        await process_currentOwnershipPercent(message, state)
        await state.update_data(previousOwnershipPercent=message.text)
    else:
        number = (await state.get_data())['plateNumber']
        carInfo = collect_data(number)
        await state.update_data(currentOwnershipPercent=message.text, ascentYearOnRoad=carInfo["שנת יצור"])
        await state.set_state(Form.ascentMonthOnRoad)
        await message.answer(
                    f"Ascent Month On Road?",
                    reply_markup=ReplyKeyboardMarkup(
                        keyboard=[
                            [
                                KeyboardButton(text="1"),
                                KeyboardButton(text="2"),
                                KeyboardButton(text="3"),
                                KeyboardButton(text="4")
                            ],
                            [
                                KeyboardButton(text="5"),
                                KeyboardButton(text="6"),
                                KeyboardButton(text="7"),
                                KeyboardButton(text="8")
                            ],
                            [
                                KeyboardButton(text="9"),
                                KeyboardButton(text="10"),
                                KeyboardButton(text="11"),
                                KeyboardButton(text="12")
                            ]
                        ],
                resize_keyboard=True,
                one_time_keyboard=True
                )
                ,)
    




@form_router.message(Form.ascentMonthOnRoad, lambda message : message.text in [ '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12'])
async def process_waranty(message: Message, state: FSMContext) -> None:
    await state.update_data(ascentMonthOnRoad=message.text)
    await state.set_state(Form.warranty)
    await message.answer(
                f"Guarantee on the car?",
                reply_markup=ReplyKeyboardMarkup(
                    keyboard=[
                        [
                            KeyboardButton(text="ללא אחריות"),
                            KeyboardButton(text="מנוע + הילוכים")
                        ],
                        [
                            KeyboardButton(text="מנוע + הילוכים + עד 5 מכלולים"), 
                            KeyboardButton(text="מנוע + הילוכים + עד 10 מכלולים"),
                            KeyboardButton(text="מנוע + הילוכים + עד 15 מכלולים")
                        ]
                    ],
            resize_keyboard=True,
            one_time_keyboard=True
            )
            ,)
@form_router.message(Form.warranty, lambda message : message.text in ["ללא אחריות", "מנוע + הילוכים", "מנוע + הילוכים + עד 5 מכלולים", "מנוע + הילוכים + עד 10 מכלולים", "מנוע + הילוכים + עד 15 מכלולים"])
async def process_warrantyPercent(message: Message, state: FSMContext) -> None:
    await state.update_data(warranty=message.text)
    if (await state.get_data())['warranty'] == "ללא אחריות":
        await state.update_data(warrantyPercent="0")
        await process_hasLPGSystem(message, state)
    else:
        await state.set_state(Form.warrantyPercent)
        await message.answer(
                    f"Validity of warranty",
                    reply_markup=ReplyKeyboardMarkup(
                        keyboard=[
                            [
                                KeyboardButton(text="חצי שנה"),
                                KeyboardButton(text="שנה")
                            ],
                            [
                                KeyboardButton(text="שנתיים"), 
                                KeyboardButton(text="3 שנים")
                            ]
                        ],
                resize_keyboard=True,
                one_time_keyboard=True
                )
                ,)

@form_router.message(Form.warrantyPercent, lambda message : message.text in ["חצי שנה", "שנה", "שנתיים", "3 שנים"])
async def process_hasLPGSystem(message: Message, state: FSMContext) -> None:
    if 'warrantyPercent' not in await state.get_data():
        await state.update_data(warrantyPercent=message.text)
    await state.set_state(Form.hasLPGSystem)
    await message.answer(
                f"Does the car have an LPG system?",
                reply_markup=ReplyKeyboardMarkup(
                    keyboard=[
                        [
                            KeyboardButton(text="לא"),
                            KeyboardButton(text="כן")
                        ]
                    ],
            resize_keyboard=True,
            one_time_keyboard=True
            )
            ,)
        


@form_router.message(Form.hasLPGSystem, lambda message : message.text in ["כן", "לא"])
async def show_summary(message: Message, state: FSMContext) -> None:
    await state.update_data(hasLPGSystem=True if message.text == "כן" else False)
    data = await state.get_data()
    carInfo = collect_data_from_yad2(data["plateNumber"]) 
    try:
        req = requests.get(f"https://gw.yad2.co.il/price-list/sub-model/price-calculation-options?subModelId={carInfo['id']}")
        priceCalculation = req.json()
        currentOwnershipPercent = [item['value'] for item in priceCalculation['data']['ownershipPercent'] if item['text'] == data['currentOwnershipPercent'] ][-1]
        previousOwnershipPercent = [item['value'] for item in priceCalculation['data']['ownershipPercent'] if item['text'] == data['previousOwnershipPercent'] ][-1]
        warrantyType = [item['value'] for item in priceCalculation['data']['warrantyType'] if item['text'] == data['warranty'] ][-1]
        if warrantyType == 0:
            warrawarrantyPercentByType = 0
        else:
            warrawarrantyPercentByType = math.trunc([item['value'] for item in priceCalculation['data']['warrantyPercentByType'][f'{warrantyType}'] if item['text'] == data['warrantyPercent'] ][-1])
        link = f"https://gw.yad2.co.il/pricelist-calculator/calculate-price?subModelId={carInfo['id']}&previousOwnershipPercent={previousOwnershipPercent}&kilometers={data['kilometers']}&ascentYearOnRoad={carInfo['year']}&ascentMonthOnRoad={data['ascentMonthOnRoad']}&price={carInfo['price']}&ownersNumber={data['ownersNumber']}&currentOwnershipPercent={currentOwnershipPercent}&appraiserReducePercent=0&warrantyPercent={warrawarrantyPercentByType}&hasLPGSystem={data['hasLPGSystem']}"
        req = requests.get(link)
        price = req.json()['data']['calculatedPrice']
        await message.answer(f'Pricelist: {hbold(price)} ₪', reply_markup=ReplyKeyboardRemove())
        await message.answer('Thank you for using our service!\nPress /start to check again', reply_markup=ReplyKeyboardRemove())
    except TypeError:
        await message.answer(f"{carInfo['message']}\nPress /start to check again")
    except:
        await message.answer(f"Something went wrong. Please try again later.\n Or press /start to check again")
    finally:
        await state.clear()


async def main():
    await dp.start_polling(bot)



if __name__ == '__main__':
    asyncio.run(main())


