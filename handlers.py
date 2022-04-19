import sqlite3
import requests
from aiogram import types
from aiogram.types import ParseMode

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
    await bot.send_message(message.from_user.id,
                           text="Good evening, Europe and good morning, Australia!\n"
                                "This is 'Douze points' calling!\n"
                                "/odds - to peek at bookmakers' predictions\n"
                                "/semifinal1 - to listen to any song from the first semi-final\n"
                                "/semifinal2 - to listen to any song from the second semi-final\n"
                                "/final - to listen to any song from the Grand final\n"
                                "/12points - to give your douze points to your favourite"
                                " (<b>you can vote more than once - scoreboard will be refreshed automatically</b>)\n"
                                "/scoreboard - see public top of songs (is available after your voting)",
                           parse_mode=ParseMode.HTML)
    if database.user_exists(message.from_user.id):
        await bot.send_message(message.from_user.id, text="You are good to go!")
    else:
        database.register(message.from_user.id)
        await bot.send_message(message.from_user.id, text="Take it away!")


@dp.message_handler(commands="odds", state="*")
async def bookmakers(message: types.Message):
    await bot.send_message(message.from_user.id,
                           text="<a href='https://eurovisionworld.com/odds/eurovision'>Bookmakers' predictions</a>")


@dp.message_handler(commands="semifinal1", state="*")
async def first_semi(message: types.Message):
    await bot.send_message(message.from_user.id, text='Songs of the first semi-final', reply_markup=inline_kb)

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
    await bot.send_message(message.from_user.id, text='Songs of the second semi-final', reply_markup=inline_kb_2)

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
    await bot.send_message(message.from_user.id, text='Songs of the Grand Final', reply_markup=inline_kb_3)

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
        if database.voter_exists(callback_query.from_user.id):
            database.remove_vote(callback_query.from_user.id)
            print('remove')
        database.insert_voter(callback_query.from_user.id)
        print('insert')
        database.give_norway_12_points(callback_query.from_user.id)
        await bot.send_message(callback_query.from_user.id, text="Twelve points to Norway! Thank you!")

    @dp.callback_query_handler(lambda c: c.data == 'Ukraine')
    async def twelve_points_ukraine(callback_query: types.CallbackQuery):
        if database.voter_exists(callback_query.from_user.id):
            database.remove_vote(callback_query.from_user.id)
        database.insert_voter(callback_query.from_user.id)
        database.give_ukraine_12_points(callback_query.from_user.id)
        await bot.send_message(callback_query.from_user.id, text="Twelve points to Ukraine! Thank you!")

    @dp.callback_query_handler(lambda c: c.data == 'Netherlands')
    async def twelve_points_netherlands(callback_query: types.CallbackQuery):
        if database.voter_exists(callback_query.from_user.id):
            database.remove_vote(callback_query.from_user.id)
        database.insert_voter(callback_query.from_user.id)
        database.give_netherlands_12_points(callback_query.from_user.id)
        await bot.send_message(callback_query.from_user.id, text="Twelve points to the Netherlands! Thank you!")

    @dp.callback_query_handler(lambda c: c.data == 'Greece')
    async def twelve_points_greece(callback_query: types.CallbackQuery):
        if database.voter_exists(callback_query.from_user.id):
            database.remove_vote(callback_query.from_user.id)
        database.insert_voter(callback_query.from_user.id)
        database.give_greece_12_points(callback_query.from_user.id)
        await bot.send_message(callback_query.from_user.id, text="Twelve points to Greece! Thank you!")

    @dp.callback_query_handler(lambda c: c.data == 'Albania')
    async def twelve_points_albania(callback_query: types.CallbackQuery):
        if database.voter_exists(callback_query.from_user.id):
            database.remove_vote(callback_query.from_user.id)
        database.insert_voter(callback_query.from_user.id)
        database.give_albania_12_points(callback_query.from_user.id)
        await bot.send_message(callback_query.from_user.id, text="Twelve points to Albania! Thank you!")

    @dp.callback_query_handler(lambda c: c.data == 'Armenia')
    async def twelve_points_armenia(callback_query: types.CallbackQuery):
        if database.voter_exists(callback_query.from_user.id):
            database.remove_vote(callback_query.from_user.id)
        database.insert_voter(callback_query.from_user.id)
        database.give_armenia_12_points(callback_query.from_user.id)
        await bot.send_message(callback_query.from_user.id, text="Twelve points to Armenia! Thank you!")

    @dp.callback_query_handler(lambda c: c.data == 'Moldova')
    async def twelve_points_moldova(callback_query: types.CallbackQuery):
        if database.voter_exists(callback_query.from_user.id):
            database.remove_vote(callback_query.from_user.id)
        database.insert_voter(callback_query.from_user.id)
        database.give_moldova_12_points(callback_query.from_user.id)
        await bot.send_message(callback_query.from_user.id, text="Twelve points to Moldova! Thank you!")

    @dp.callback_query_handler(lambda c: c.data == 'Portugal')
    async def twelve_points_portugal(callback_query: types.CallbackQuery):
        if database.voter_exists(callback_query.from_user.id):
            database.remove_vote(callback_query.from_user.id)
        database.insert_voter(callback_query.from_user.id)
        database.give_portugal_12_points(callback_query.from_user.id)
        await bot.send_message(callback_query.from_user.id, text="Twelve points to Portugal! Thank you!")

    @dp.callback_query_handler(lambda c: c.data == 'Swiss')
    async def twelve_points_swiss(callback_query: types.CallbackQuery):
        if database.voter_exists(callback_query.from_user.id):
            database.remove_vote(callback_query.from_user.id)
        database.insert_voter(callback_query.from_user.id)
        database.give_swiss_12_points(callback_query.from_user.id)
        await bot.send_message(callback_query.from_user.id, text="Twelve points to Switzerland! Thank you!")

    @dp.callback_query_handler(lambda c: c.data == 'Austria')
    async def twelve_points_austria(callback_query: types.CallbackQuery):
        if database.voter_exists(callback_query.from_user.id):
            database.remove_vote(callback_query.from_user.id)
        database.insert_voter(callback_query.from_user.id)
        database.give_austria_12_points(callback_query.from_user.id)
        await bot.send_message(callback_query.from_user.id, text="Twelve points to Austria! Thank you!")

    @dp.callback_query_handler(lambda c: c.data == 'Lithuania')
    async def twelve_points_lithuania(callback_query: types.CallbackQuery):
        if database.voter_exists(callback_query.from_user.id):
            database.remove_vote(callback_query.from_user.id)
        database.insert_voter(callback_query.from_user.id)
        database.give_lithuania_12_points(callback_query.from_user.id)
        await bot.send_message(callback_query.from_user.id, text="Twelve points to Lithuania! Thank you!")

    @dp.callback_query_handler(lambda c: c.data == 'Latvia')
    async def twelve_points_latvia(callback_query: types.CallbackQuery):
        if database.voter_exists(callback_query.from_user.id):
            database.remove_vote(callback_query.from_user.id)
        database.insert_voter(callback_query.from_user.id)
        database.give_latvia_12_points(callback_query.from_user.id)
        await bot.send_message(callback_query.from_user.id, text="Twelve points to Latvia! Thank you!")

    @dp.callback_query_handler(lambda c: c.data == 'Croatia')
    async def twelve_points_croatia(callback_query: types.CallbackQuery):
        if database.voter_exists(callback_query.from_user.id):
            database.remove_vote(callback_query.from_user.id)
        database.insert_voter(callback_query.from_user.id)
        database.give_croatia_12_points(callback_query.from_user.id)
        await bot.send_message(callback_query.from_user.id, text="Twelve points to Croatia! Thank you!")

    @dp.callback_query_handler(lambda c: c.data == 'Iceland')
    async def twelve_points_iceland(callback_query: types.CallbackQuery):
        if database.voter_exists(callback_query.from_user.id):
            database.remove_vote(callback_query.from_user.id)
        database.insert_voter(callback_query.from_user.id)
        database.give_iceland_12_points(callback_query.from_user.id)
        await bot.send_message(callback_query.from_user.id, text="Twelve points to Iceland! Thank you!")

    @dp.callback_query_handler(lambda c: c.data == 'Slovenia')
    async def twelve_points_slovenia(callback_query: types.CallbackQuery):
        if database.voter_exists(callback_query.from_user.id):
            database.remove_vote(callback_query.from_user.id)
        database.insert_voter(callback_query.from_user.id)
        database.give_slovenia_12_points(callback_query.from_user.id)
        await bot.send_message(callback_query.from_user.id, text="Twelve points to Slovenia! Thank you!")

    @dp.callback_query_handler(lambda c: c.data == 'Denmark')
    async def twelve_points_denmark(callback_query: types.CallbackQuery):
        if database.voter_exists(callback_query.from_user.id):
            database.remove_vote(callback_query.from_user.id)
        database.insert_voter(callback_query.from_user.id)
        database.give_denmark_12_points(callback_query.from_user.id)
        await bot.send_message(callback_query.from_user.id, text="Twelve points to Denmark! Thank you!")

    @dp.callback_query_handler(lambda c: c.data == 'Bulgaria')
    async def twelve_points_bulgaria(callback_query: types.CallbackQuery):
        if database.voter_exists(callback_query.from_user.id):
            database.remove_vote(callback_query.from_user.id)
        database.insert_voter(callback_query.from_user.id)
        database.give_bulgaria_12_points(callback_query.from_user.id)
        await bot.send_message(callback_query.from_user.id, text="Twelve points to Bulgaria! Thank you!")

    @dp.callback_query_handler(lambda c: c.data == 'Sweden')
    async def twelve_points_sweden(callback_query: types.CallbackQuery):
        if database.voter_exists(callback_query.from_user.id):
            database.remove_vote(callback_query.from_user.id)
        database.insert_voter(callback_query.from_user.id)
        database.give_sweden_12_points(callback_query.from_user.id)
        await bot.send_message(callback_query.from_user.id, text="Twelve points to Sweden! Thank you!")

    @dp.callback_query_handler(lambda c: c.data == 'Poland')
    async def twelve_points_poland(callback_query: types.CallbackQuery):
        if database.voter_exists(callback_query.from_user.id):
            database.remove_vote(callback_query.from_user.id)
        database.insert_voter(callback_query.from_user.id)
        database.give_poland_12_points(callback_query.from_user.id)
        await bot.send_message(callback_query.from_user.id, text="Twelve points to Poland! Thank you!")

    @dp.callback_query_handler(lambda c: c.data == 'Estonia')
    async def twelve_points_estonia(callback_query: types.CallbackQuery):
        if database.voter_exists(callback_query.from_user.id):
            database.remove_vote(callback_query.from_user.id)
        database.insert_voter(callback_query.from_user.id)
        database.give_estonia_12_points(callback_query.from_user.id)
        await bot.send_message(callback_query.from_user.id, text="Twelve points to Estonia! Thank you!")

    @dp.callback_query_handler(lambda c: c.data == 'Finland')
    async def twelve_points_finland(callback_query: types.CallbackQuery):
        if database.voter_exists(callback_query.from_user.id):
            database.remove_vote(callback_query.from_user.id)
        database.insert_voter(callback_query.from_user.id)
        database.give_finland_12_points(callback_query.from_user.id)
        await bot.send_message(callback_query.from_user.id, text="Twelve points to Finland! Thank you!")

    @dp.callback_query_handler(lambda c: c.data == 'Azerbaijan')
    async def twelve_points_azerbaijan(callback_query: types.CallbackQuery):
        if database.voter_exists(callback_query.from_user.id):
            database.remove_vote(callback_query.from_user.id)
        database.insert_voter(callback_query.from_user.id)
        database.give_azerbaijan_12_points(callback_query.from_user.id)
        await bot.send_message(callback_query.from_user.id, text="Twelve points to Azerbaijan! Thank you!")

    @dp.callback_query_handler(lambda c: c.data == 'Australia')
    async def twelve_points_australia(callback_query: types.CallbackQuery):
        if database.voter_exists(callback_query.from_user.id):
            database.remove_vote(callback_query.from_user.id)
        database.insert_voter(callback_query.from_user.id)
        database.give_australia_12_points(callback_query.from_user.id)
        await bot.send_message(callback_query.from_user.id, text="Twelve points to Australia! Thank you!")

    @dp.callback_query_handler(lambda c: c.data == 'Serbia')
    async def twelve_points_serbia(callback_query: types.CallbackQuery):
        if database.voter_exists(callback_query.from_user.id):
            database.remove_vote(callback_query.from_user.id)
        database.insert_voter(callback_query.from_user.id)
        database.give_serbia_12_points(callback_query.from_user.id)
        await bot.send_message(callback_query.from_user.id, text="Twelve points to Serbia! Thank you!")

    @dp.callback_query_handler(lambda c: c.data == 'Belgium')
    async def twelve_points_belgium(callback_query: types.CallbackQuery):
        if database.voter_exists(callback_query.from_user.id):
            database.remove_vote(callback_query.from_user.id)
        database.insert_voter(callback_query.from_user.id)
        database.give_belgium_12_points(callback_query.from_user.id)
        await bot.send_message(callback_query.from_user.id, text="Twelve points to Belgium! Thank you!")

    @dp.callback_query_handler(lambda c: c.data == 'Czech')
    async def twelve_points_czech(callback_query: types.CallbackQuery):
        if database.voter_exists(callback_query.from_user.id):
            database.remove_vote(callback_query.from_user.id)
        database.insert_voter(callback_query.from_user.id)
        database.give_czech_12_points(callback_query.from_user.id)
        await bot.send_message(callback_query.from_user.id, text="Twelve points to Czech Republic! Thank you!")

    @dp.callback_query_handler(lambda c: c.data == 'Cyprus')
    async def twelve_points_cyprus(callback_query: types.CallbackQuery):
        if database.voter_exists(callback_query.from_user.id):
            database.remove_vote(callback_query.from_user.id)
        database.insert_voter(callback_query.from_user.id)
        database.give_cyprus_12_points(callback_query.from_user.id)
        await bot.send_message(callback_query.from_user.id, text="Twelve points to Cyprus! Thank you!")

    @dp.callback_query_handler(lambda c: c.data == 'Malta')
    async def twelve_points_malta(callback_query: types.CallbackQuery):
        if database.voter_exists(callback_query.from_user.id):
            database.remove_vote(callback_query.from_user.id)
        database.insert_voter(callback_query.from_user.id)
        database.give_malta_12_points(callback_query.from_user.id)
        await bot.send_message(callback_query.from_user.id, text="Twelve points to Malta! Thank you!")

    @dp.callback_query_handler(lambda c: c.data == 'Romania')
    async def twelve_points_romania(callback_query: types.CallbackQuery):
        if database.voter_exists(callback_query.from_user.id):
            database.remove_vote(callback_query.from_user.id)
        database.insert_voter(callback_query.from_user.id)
        database.give_romania_12_points(callback_query.from_user.id)
        await bot.send_message(callback_query.from_user.id, text="Twelve points to Romania! Thank you!")

    @dp.callback_query_handler(lambda c: c.data == 'Marino')
    async def twelve_points_marino(callback_query: types.CallbackQuery):
        if database.voter_exists(callback_query.from_user.id):
            database.remove_vote(callback_query.from_user.id)
        database.insert_voter(callback_query.from_user.id)
        database.give_marino_12_points(callback_query.from_user.id)
        await bot.send_message(callback_query.from_user.id, text="Twelve points to San Marino! Thank you!")

    @dp.callback_query_handler(lambda c: c.data == 'Montenegro')
    async def twelve_points_montenegro(callback_query: types.CallbackQuery):
        if database.voter_exists(callback_query.from_user.id):
            database.remove_vote(callback_query.from_user.id)
        database.insert_voter(callback_query.from_user.id)
        database.give_montenegro_12_points(callback_query.from_user.id)
        await bot.send_message(callback_query.from_user.id, text="Twelve points to Montenegro! Thank you!")

    @dp.callback_query_handler(lambda c: c.data == 'Israel')
    async def twelve_points_israel(callback_query: types.CallbackQuery):
        if database.voter_exists(callback_query.from_user.id):
            database.remove_vote(callback_query.from_user.id)
        database.insert_voter(callback_query.from_user.id)
        database.give_israel_12_points(callback_query.from_user.id)
        await bot.send_message(callback_query.from_user.id, text="Twelve points to Israel! Thank you!")

    @dp.callback_query_handler(lambda c: c.data == 'Macedonia')
    async def twelve_points_macedonia(callback_query: types.CallbackQuery):
        if database.voter_exists(callback_query.from_user.id):
            database.remove_vote(callback_query.from_user.id)
        database.insert_voter(callback_query.from_user.id)
        database.give_macedonia_12_points(callback_query.from_user.id)
        await bot.send_message(callback_query.from_user.id, text="Twelve points to North Macedonia! Thank you!")

    @dp.callback_query_handler(lambda c: c.data == 'Ireland')
    async def twelve_points_ireland(callback_query: types.CallbackQuery):
        if database.voter_exists(callback_query.from_user.id):
            database.remove_vote(callback_query.from_user.id)
        database.insert_voter(callback_query.from_user.id)
        database.give_ireland_12_points(callback_query.from_user.id)
        await bot.send_message(callback_query.from_user.id, text="Twelve points to Ireland! Thank you!")

    @dp.callback_query_handler(lambda c: c.data == 'Georgia')
    async def twelve_points_georgia(callback_query: types.CallbackQuery):
        if database.voter_exists(callback_query.from_user.id):
            database.remove_vote(callback_query.from_user.id)
        database.insert_voter(callback_query.from_user.id)
        database.give_georgia_12_points(callback_query.from_user.id)
        await bot.send_message(callback_query.from_user.id, text="Twelve points to Georgia! Thank you!")

    @dp.callback_query_handler(lambda c: c.data == 'Italy')
    async def twelve_points_italy(callback_query: types.CallbackQuery):
        if database.voter_exists(callback_query.from_user.id):
            database.remove_vote(callback_query.from_user.id)
        database.insert_voter(callback_query.from_user.id)
        database.give_italy_12_points(callback_query.from_user.id)
        await bot.send_message(callback_query.from_user.id, text="Twelve points to Italy! Thank you!")

    @dp.callback_query_handler(lambda c: c.data == 'UK')
    async def twelve_points_uk(callback_query: types.CallbackQuery):
        if database.voter_exists(callback_query.from_user.id):
            database.remove_vote(callback_query.from_user.id)
        database.insert_voter(callback_query.from_user.id)
        database.give_uk_12_points(callback_query.from_user.id)
        await bot.send_message(callback_query.from_user.id, text="Twelve points to the UK! Thank you!")

    @dp.callback_query_handler(lambda c: c.data == 'Spain')
    async def twelve_points_spain(callback_query: types.CallbackQuery):
        if database.voter_exists(callback_query.from_user.id):
            database.remove_vote(callback_query.from_user.id)
        database.insert_voter(callback_query.from_user.id)
        database.give_spain_12_points(callback_query.from_user.id)
        await bot.send_message(callback_query.from_user.id, text="Twelve points to Spain! Thank you!")

    @dp.callback_query_handler(lambda c: c.data == 'France')
    async def twelve_points_france(callback_query: types.CallbackQuery):
        if database.voter_exists(callback_query.from_user.id):
            database.remove_vote(callback_query.from_user.id)
        database.insert_voter(callback_query.from_user.id)
        database.give_france_12_points(callback_query.from_user.id)
        await bot.send_message(callback_query.from_user.id, text="Twelve points to France! Thank you!")

    @dp.callback_query_handler(lambda c: c.data == 'Germany')
    async def twelve_points_germany(callback_query: types.CallbackQuery):
        if database.voter_exists(callback_query.from_user.id):
            database.remove_vote(callback_query.from_user.id)
        database.insert_voter(callback_query.from_user.id)
        database.give_germany_12_points(callback_query.from_user.id)
        await bot.send_message(callback_query.from_user.id, text="Twelve points to Germany! Thank you!")


@dp.message_handler(commands='scoreboard', state="*")
async def show_scoreboard(message: types.Message):
    scoreboard = {'Norway': database.count_norway()[0][0],
                  'Ukraine': database.count_ukraine()[0][0],
                  'The Netherlands': database.count_netherlands()[0][0],
                  'Greece': database.count_greece()[0][0],
                  'Albania': database.count_albania()[0][0],
                  'Armenia': database.count_armenia()[0][0],
                  'Moldova': database.count_moldova()[0][0],
                  'Portugal': database.count_portugal()[0][0],
                  'Switzerland': database.count_swiss()[0][0],
                  'Austria': database.count_austria()[0][0],
                  'Lithuania': database.count_lithuania()[0][0],
                  'Latvia': database.count_latvia()[0][0],
                  'Croatia': database.count_croatia()[0][0],
                  'Iceland': database.count_iceland()[0][0],
                  'Slovenia': database.count_slovenia()[0][0],
                  'Denmark': database.count_denmark()[0][0],
                  'Bulgaria': database.count_bulgaria()[0][0],
                  'Sweden': database.count_sweden()[0][0],
                  'Poland': database.count_poland()[0][0],
                  'Estonia': database.count_estonia()[0][0],
                  'Finland': database.count_finland()[0][0],
                  'Azerbaijan': database.count_azerbaijan()[0][0],
                  'Australia': database.count_australia()[0][0],
                  'Serbia': database.count_serbia()[0][0],
                  'Belgium': database.count_belgium()[0][0],
                  'Czech Republic': database.count_czech()[0][0],
                  'Cyprus': database.count_cyprus()[0][0],
                  'Malta': database.count_malta()[0][0],
                  'Romania': database.count_romania()[0][0],
                  'San Marino': database.count_marino()[0][0],
                  'Montenegro': database.count_montenegro()[0][0],
                  'Israel': database.count_israel()[0][0],
                  'North Macedonia': database.count_macedonia()[0][0],
                  'Ireland': database.count_ireland()[0][0],
                  'Georgia': database.count_georgia()[0][0],
                  'Italy': database.count_italy()[0][0],
                  'The UK': database.count_uk()[0][0],
                  'Spain': database.count_spain()[0][0],
                  'France': database.count_france()[0][0],
                  'Germany': database.count_germany()[0][0]}
    points_scoreboard = sorted(scoreboard.items(), reverse=True, key=lambda x: x[1])
    results = ""
    for result in points_scoreboard:
        results += result[0] + ': ' + str(result[1]) + '\n'
    await bot.send_message(message.from_user.id, text=results)


