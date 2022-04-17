import sqlite3
import requests
from aiogram import types

from main import dp, bot
from config import USER_ID, DB_NAME
from aiogram.dispatcher import FSMContext
from keyboards import *
from sql import *

database = SQL(f'{DB_NAME}')

@dp.message_handler(commands="start", state="*")
async def greet_function(message: types.Message):
    await bot.send_message(USER_ID,
                           text="<a href='tg://user?id={1}'>{0}</a>"
                                         " launched the bot!".format(message.from_user.first_name,
                                                                    message.from_user.id))
    if database.user_exists(message.from_user.id):
        await bot.send_message(message.from_user.id, text="You are good to go!")
    else:
        database.register(message.from_user.id)
        await bot.send_message(message.from_user.id, text="Take it away!")


@dp.message_handler(commands="odds", state="*")
async def bookmakers(message: types.Message):
    await bot.send_message(USER_ID,
                           text="<a href='https://eurovisionworld.com/odds/eurovision'>Bookmakers' predictions</a>")

@dp.message_handler(commands="semifinal1", state="*")
async def first_semi(message: types.Message):
    await bot.send_message(message.from_user.id, text='Songs of the first semi-final:', reply_markup=inline_kb)
    @dp.callback_query_handler(lambda c: c.data == 'norway')
    async def norway(callback_query: types.CallbackQuery):
        await bot.send_message(callback_query.from_user.id, text="<a href='https://www.youtube.com/watch?v=O_AvUlCQ_Cc&list=PLmWYEDTNOGULG6eg0zgzvRercwqRP6mII&index=27'>Norway</a>")

    @dp.callback_query_handler(lambda c: c.data == 'moldova')
    async def moldova(callback_query: types.CallbackQuery):
        await bot.send_message(callback_query.from_user.id,
                               text="<a href='https://www.youtube.com/watch?v=C9RJQPZsj8E&list=PLmWYEDTNOGULG6eg0zgzvRercwqRP6mII&index=28'>Moldova</a>")

    @dp.callback_query_handler(lambda c: c.data == 'ukraine')
    async def ukraine(callback_query: types.CallbackQuery):
        await bot.send_message(callback_query.from_user.id,
                               text="<a href='https://www.youtube.com/watch?v=UiEGVYOruLk&list=PLmWYEDTNOGULG6eg0zgzvRercwqRP6mII&index=1'>Ukraine</a>")

    @dp.callback_query_handler(lambda c: c.data == 'austria')
    async def austria(callback_query: types.CallbackQuery):
        await bot.send_message(callback_query.from_user.id,
                               text="<a href='https://www.youtube.com/watch?v=tF6LY7lnVFU&list=PLmWYEDTNOGULG6eg0zgzvRercwqRP6mII&index=2'>Austria</a>")

    @dp.callback_query_handler(lambda c: c.data == 'netherlands')
    async def netherlands(callback_query: types.CallbackQuery):
        await bot.send_message(callback_query.from_user.id,
                               text="<a href='https://www.youtube.com/watch?v=v2m-MGSys0k&list=PLmWYEDTNOGULG6eg0zgzvRercwqRP6mII&index=3'>The Netherlands</a>")

    @dp.callback_query_handler(lambda c: c.data == 'albania')
    async def albania(callback_query: types.CallbackQuery):
        await bot.send_message(callback_query.from_user.id,
                               text="<a href='https://www.youtube.com/watch?v=iMu47raqbcc&list=PLmWYEDTNOGULG6eg0zgzvRercwqRP6mII&index=4'>Albania</a>")

    @dp.callback_query_handler(lambda c: c.data == 'armenia')
    async def armenia(callback_query: types.CallbackQuery):
        await bot.send_message(callback_query.from_user.id,
                               text="<a href='https://www.youtube.com/watch?v=gVqGKkm7xBE&list=PLmWYEDTNOGULG6eg0zgzvRercwqRP6mII&index=9'>Armenia</a>")

    @dp.callback_query_handler(lambda c: c.data == 'lithuania')
    async def lithuania(callback_query: types.CallbackQuery):
        await bot.send_message(callback_query.from_user.id,
                               text="<a href='https://www.youtube.com/watch?v=acya6UcJP1k&list=PLmWYEDTNOGULG6eg0zgzvRercwqRP6mII&index=14'>Lithuania</a>")

    @dp.callback_query_handler(lambda c: c.data == 'greece')
    async def greece(callback_query: types.CallbackQuery):
        await bot.send_message(callback_query.from_user.id,
                               text="<a href='https://www.youtube.com/watch?v=Uv7PcRKXZDg&list=PLmWYEDTNOGULG6eg0zgzvRercwqRP6mII&index=15'>Greece</a>")

    @dp.callback_query_handler(lambda c: c.data == 'bulgaria')
    async def bulgaria(callback_query: types.CallbackQuery):
        await bot.send_message(callback_query.from_user.id,
                               text="<a href='https://www.youtube.com/watch?v=HySI2igCcx4&list=PLmWYEDTNOGULG6eg0zgzvRercwqRP6mII&index=22'>Bulgaria</a>")

    @dp.callback_query_handler(lambda c: c.data == 'portugal')
    async def portugal(callback_query: types.CallbackQuery):
        await bot.send_message(callback_query.from_user.id,
                               text="<a href='https://www.youtube.com/watch?v=eQul-rkcGPQ&list=PLmWYEDTNOGULG6eg0zgzvRercwqRP6mII&index=23'>Portugal</a>")

    @dp.callback_query_handler(lambda c: c.data == 'iceland')
    async def iceland(callback_query: types.CallbackQuery):
        await bot.send_message(callback_query.from_user.id,
                               text="<a href='https://www.youtube.com/watch?v=vk9D10EyxHA&list=PLmWYEDTNOGULG6eg0zgzvRercwqRP6mII&index=32'>Iceland</a>")

    @dp.callback_query_handler(lambda c: c.data == 'swiss')
    async def swiss(callback_query: types.CallbackQuery):
        await bot.send_message(callback_query.from_user.id,
                               text="<a href='https://www.youtube.com/watch?v=EnsqrM40uaY&list=PLmWYEDTNOGULG6eg0zgzvRercwqRP6mII&index=25'>Swiss</a>")

    @dp.callback_query_handler(lambda c: c.data == 'denmark')
    async def denmark(callback_query: types.CallbackQuery):
        await bot.send_message(callback_query.from_user.id,
                               text="<a href='https://www.youtube.com/watch?v=xqakAZP4D24&list=PLmWYEDTNOGULG6eg0zgzvRercwqRP6mII&index=36'>Denmark</a>")

    @dp.callback_query_handler(lambda c: c.data == 'latvia')
    async def latvia(callback_query: types.CallbackQuery):
        await bot.send_message(callback_query.from_user.id,
                               text="<a href='https://www.youtube.com/watch?v=DbDj9mBI4g0&list=PLmWYEDTNOGULG6eg0zgzvRercwqRP6mII&index=37'>Latvia</a>")

    @dp.callback_query_handler(lambda c: c.data == 'croatia')
    async def croatia(callback_query: types.CallbackQuery):
        await bot.send_message(callback_query.from_user.id,
                               text="<a href='https://www.youtube.com/watch?v=4mTLfWMSNtw&list=PLmWYEDTNOGULG6eg0zgzvRercwqRP6mII&index=40'>Croatia</a>")

    @dp.callback_query_handler(lambda c: c.data == 'slovenia')
    async def slovenia(callback_query: types.CallbackQuery):
        await bot.send_message(callback_query.from_user.id,
                               text="<a href='https://www.youtube.com/watch?v=g8Ezl7xucCU&list=PLmWYEDTNOGULG6eg0zgzvRercwqRP6mII&index=39'>Slovenia</a>")



@dp.message_handler(commands="semifinal2", state="*")
async def second_semi(message: types.Message):
    await bot.send_message(message.from_user.id, text='Songs of the second semi-final:', reply_markup=inline_kb_2)
    @dp.callback_query_handler(lambda c: c.data == 'serbia')
    async def serbia(callback_query: types.CallbackQuery):
        await bot.send_message(callback_query.from_user.id, text="<a href='https://www.youtube.com/watch?v=3S1jrYq87Zw&list=PLmWYEDTNOGULG6eg0zgzvRercwqRP6mII&index=6'>Serbia</a>")

    @dp.callback_query_handler(lambda c: c.data == 'sweden')
    async def sweden(callback_query: types.CallbackQuery):
        await bot.send_message(callback_query.from_user.id,
                               text="<a href='https://www.youtube.com/watch?v=wWDThAfryW4&list=PLmWYEDTNOGULG6eg0zgzvRercwqRP6mII&index=7'>Sweden</a>")

    @dp.callback_query_handler(lambda c: c.data == 'romania')
    async def romania(callback_query: types.CallbackQuery):
        await bot.send_message(callback_query.from_user.id,
                               text="<a href='https://www.youtube.com/watch?v=Ru3y4ivY3lQ&list=PLmWYEDTNOGULG6eg0zgzvRercwqRP6mII&index=12'>Romania</a>")

    @dp.callback_query_handler(lambda c: c.data == 'belgium')
    async def belgium(callback_query: types.CallbackQuery):
        await bot.send_message(callback_query.from_user.id,
                               text="<a href='https://www.youtube.com/watch?v=GZ3mLO4uFjY&list=PLmWYEDTNOGULG6eg0zgzvRercwqRP6mII&index=13'>Belgium</a>")

    @dp.callback_query_handler(lambda c: c.data == 'azerbaijan')
    async def azerbaijan(callback_query: types.CallbackQuery):
        await bot.send_message(callback_query.from_user.id,
                               text="<a href='https://www.youtube.com/watch?v=TGd1AFKR_-E&list=PLmWYEDTNOGULG6eg0zgzvRercwqRP6mII&index=16'>Azerbaijan</a>")

    @dp.callback_query_handler(lambda c: c.data == 'montenegro')
    async def montenegro(callback_query: types.CallbackQuery):
        await bot.send_message(callback_query.from_user.id,
                               text="<a href='https://www.youtube.com/watch?v=7e3GiXy7SLc&list=PLmWYEDTNOGULG6eg0zgzvRercwqRP6mII&index=17'>Montenegro</a>")

    @dp.callback_query_handler(lambda c: c.data == 'cyprus')
    async def cyprus(callback_query: types.CallbackQuery):
        await bot.send_message(callback_query.from_user.id,
                               text="<a href='https://www.youtube.com/watch?v=GM8CY08UT6I&list=PLmWYEDTNOGULG6eg0zgzvRercwqRP6mII&index=18'>Cyprus</a>")

    @dp.callback_query_handler(lambda c: c.data == 'israel')
    async def israel(callback_query: types.CallbackQuery):
        await bot.send_message(callback_query.from_user.id,
                               text="<a href='https://www.youtube.com/watch?v=WNFeohWlA20&list=PLmWYEDTNOGULG6eg0zgzvRercwqRP6mII&index=19'>Israel</a>")

    @dp.callback_query_handler(lambda c: c.data == 'marino')
    async def san_marino(callback_query: types.CallbackQuery):
        await bot.send_message(callback_query.from_user.id,
                               text="<a href='https://www.youtube.com/watch?v=P-RloZ-Fv38&list=PLmWYEDTNOGULG6eg0zgzvRercwqRP6mII&index=20'>San Marino</a>")

    @dp.callback_query_handler(lambda c: c.data == 'australia')
    async def australia(callback_query: types.CallbackQuery):
        await bot.send_message(callback_query.from_user.id,
                               text="<a href='https://www.youtube.com/watch?v=ByUD4d89_is&list=PLmWYEDTNOGULG6eg0zgzvRercwqRP6mII&index=21'>Australia</a>")

    @dp.callback_query_handler(lambda c: c.data == 'poland')
    async def poland(callback_query: types.CallbackQuery):
        await bot.send_message(callback_query.from_user.id,
                               text="<a href='https://www.youtube.com/watch?v=wh47vgUwInU&list=PLmWYEDTNOGULG6eg0zgzvRercwqRP6mII&index=24'>Poland</a>")

    @dp.callback_query_handler(lambda c: c.data == 'macedonia')
    async def north_macedonia(callback_query: types.CallbackQuery):
        await bot.send_message(callback_query.from_user.id,
                               text="<a href='https://www.youtube.com/watch?v=EzOpAduUlmo&list=PLmWYEDTNOGULG6eg0zgzvRercwqRP6mII&index=26'>North Macedonia</a>")

    @dp.callback_query_handler(lambda c: c.data == 'malta')
    async def malta(callback_query: types.CallbackQuery):
        await bot.send_message(callback_query.from_user.id,
                               text="<a href='https://www.youtube.com/watch?v=df-fks-Pj-8&list=PLmWYEDTNOGULG6eg0zgzvRercwqRP6mII&index=29'>Malta</a>")

    @dp.callback_query_handler(lambda c: c.data == 'ireland')
    async def ireland(callback_query: types.CallbackQuery):
        await bot.send_message(callback_query.from_user.id,
                               text="<a href='https://www.youtube.com/watch?v=pkHzvy-Pscw&list=PLmWYEDTNOGULG6eg0zgzvRercwqRP6mII&index=30'>Ireland</a>")

    @dp.callback_query_handler(lambda c: c.data == 'finland')
    async def finland(callback_query: types.CallbackQuery):
        await bot.send_message(callback_query.from_user.id,
                               text="<a href='https://www.youtube.com/watch?v=IwHijzdNN2A&list=PLmWYEDTNOGULG6eg0zgzvRercwqRP6mII&index=31'>Finland</a>")

    @dp.callback_query_handler(lambda c: c.data == 'czech')
    async def czech_republic(callback_query: types.CallbackQuery):
        await bot.send_message(callback_query.from_user.id,
                               text="<a href='https://www.youtube.com/watch?v=QRgj3enaAhI&list=PLmWYEDTNOGULG6eg0zgzvRercwqRP6mII&index=33'>Czech Republic</a>")
    @dp.callback_query_handler(lambda c: c.data == 'estonia')
    async def estonia(callback_query: types.CallbackQuery):
        await bot.send_message(callback_query.from_user.id,
                               text="<a href='https://www.youtube.com/watch?v=bKhSlSx00-I&list=PLmWYEDTNOGULG6eg0zgzvRercwqRP6mII&index=34'>Estonia</a>")

    @dp.callback_query_handler(lambda c: c.data == 'georgia')
    async def georgia(callback_query: types.CallbackQuery):
        await bot.send_message(callback_query.from_user.id,
                               text="<a href='https://www.youtube.com/watch?v=qgukml7zDAA&list=PLmWYEDTNOGULG6eg0zgzvRercwqRP6mII&index=38'>Georgia</a>")

@dp.message_handler(commands="final", state="*")
async def final(message: types.Message):
    await bot.send_message(message.from_user.id, text='Songs of the Grand Final:', reply_markup=inline_kb_3)

    @dp.callback_query_handler(lambda c: c.data == 'spain')
    async def spain(callback_query: types.CallbackQuery):
        await bot.send_message(callback_query.from_user.id,
                               text="<a href='https://www.youtube.com/watch?v=N3eiW6E0ldc&list=PLmWYEDTNOGULG6eg0zgzvRercwqRP6mII&index=10'>Spain</a>")

    @dp.callback_query_handler(lambda c: c.data == 'uk')
    async def uk(callback_query: types.CallbackQuery):
        await bot.send_message(callback_query.from_user.id,
                               text="<a href='https://www.youtube.com/watch?v=udsMTb2NIak&list=PLmWYEDTNOGULG6eg0zgzvRercwqRP6mII&index=5'>The UK</a>")

    @dp.callback_query_handler(lambda c: c.data == 'italy')
    async def italy(callback_query: types.CallbackQuery):
        await bot.send_message(callback_query.from_user.id,
                               text="<a href='https://www.youtube.com/watch?v=Beqe14HYY5o&list=PLmWYEDTNOGULG6eg0zgzvRercwqRP6mII&index=11'>Italy</a>")

    @dp.callback_query_handler(lambda c: c.data == 'france')
    async def france(callback_query: types.CallbackQuery):
        await bot.send_message(callback_query.from_user.id,
                               text="<a href='https://www.youtube.com/watch?v=CO07xLUlK2g&list=PLmWYEDTNOGULG6eg0zgzvRercwqRP6mII&index=8'>France</a>")

    @dp.callback_query_handler(lambda c: c.data == 'germany')
    async def germany(callback_query: types.CallbackQuery):
        await bot.send_message(callback_query.from_user.id,
                               text="<a href='https://www.youtube.com/watch?v=Oy-s-IZIHkI&list=PLmWYEDTNOGULG6eg0zgzvRercwqRP6mII&index=35'>Germany</a>")

@dp.message_handler(commands='12points', state="*")
async def scoreboard(message: types.Message):
    await bot.send_message(message.from_user.id, text='May we have your 12 points please?', reply_markup=inline_voting)

    @dp.callback_query_handler(lambda c: c.data == 'Norway')
    async def twelve_points_norway(callback_query: types.CallbackQuery):
        if database.voter_exists(message.from_user.id):
            database.remove_vote(message.from_user.id)
            database.insert_voter(message.from_user.id)
        database.give_norway_12_points(message.from_user.id)
        await bot.send_message(message.from_user.id, text="Twelve points to Norway! Thank you!")


