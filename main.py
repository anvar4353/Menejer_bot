
import logging

from aiogram import Bot, Dispatcher, executor, types
from config import *
from buttons import *
from aiogram.types import Message,CallbackQuery


logging.basicConfig(level=logging.INFO)


bot = Bot(token=TOKEN)
dp = Dispatcher(bot)




'''start knopka'''
@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    info = "Tilni tanlang / Choose language"
    await message.reply(info, parse_mode='markdown', reply_markup=til)



'''ozbekcha knopkadan yonalishi'''
@dp.callback_query_handler(text="uz")
async def echo(call: CallbackQuery):
    info = """*👋Assalomu alaykum!

Sizni kuzatuvchilarimiz safida ko'rganimizdan mamnunmiz!
    
Yosh menejerlar dasturi Besh tashabbus loyihasi hamda MBM IT kompaniyasi vakillari hamkorligida tashkil etilgan maxsus dastur hisoblanadi!
    
Ushbu loyiha orqali xalqaro doirada boshqaruv qobiliyatiga ega kadrlar tizimi shakllantiriladi.*"""
    await call.message.answer(info, parse_mode='markdown', reply_markup=salom)
    await call.message.delete()


'''englishcha knopkadan yonalishi'''
@dp.callback_query_handler(text="en")
async def echo(call: CallbackQuery):
    info = """*👋Assalomu alaykum!

 We are glad to see you among our observers! 
    
 The Young Managers Program is a special project organized in collaboration with the Five Initiative Project and representatives of MBM IT Company! 
    
 Through this program personnel management skills system will be formed in the international arena.*"""
    await call.message.answer(info, parse_mode='markdown', reply_markup=salom_en)
    await call.message.delete()








"""loyiha haqida yonalishi"""
@dp.callback_query_handler(text="loyiha_menu")
async def echo(call: CallbackQuery):
    info = """Loyiha haqida"""   
    await call.message.answer(info, parse_mode='markdown', reply_markup=loyiha_haqida_menu)
    await call.message.delete()

"""About the project yonalishi"""
@dp.callback_query_handler(text="abo")
async def echo(call: CallbackQuery):
    info = """About the project"""   
    await call.message.answer(info, parse_mode='markdown', reply_markup=loyiha_haqida_menu_en)
    await call.message.delete()




"""loyiha haqida yonalishi"""
@dp.callback_query_handler(text="ortka")
async def echo(call: CallbackQuery):
    info = """👋Assalomu alaykum!

Sizni kuzatuvchilarimiz safida ko'rganimizdan mamnunmiz!
    
Yosh menejerlar dasturi Besh tashabbus loyihasi hamda MBM IT kompaniyasi vakillari hamkorligida tashkil etilgan maxsus dastur hisoblanadi!
    
Ushbu loyiha orqali xalqaro doirada boshqaruv qobiliyatiga ega kadrlar tizimi shakllantiriladi."""   
    await call.message.answer(info, parse_mode='markdown', reply_markup=salom)
    await call.message.delete()


"""loyiha haqida yonalishi"""
@dp.callback_query_handler(text="back")
async def echo(call: CallbackQuery):
    info = """👋Assalomu alaykum!

 We are glad to see you among our observers! 
    
 The Young Managers Program is a special project organized in collaboration with the Five Initiative Project and representatives of MBM IT Company! 
    
 Through this program personnel management skills system will be formed in the international arena."""   
    await call.message.answer(info, parse_mode='markdown', reply_markup=salom_en)
    await call.message.delete()
# 



@dp.callback_query_handler(text="maqsad")
async def echo(call: CallbackQuery):
    info = """🔰 Yosh Menejerlar dasturi nima maqsadda tashkil etilmoqda?

Mazkur loyiha 17 yoshdan 25 yoshgacha bo'lgan yoshlar qatlamini loyihalar boshqaruvi bo'yicha nazariy jihatdan o'qitish, amaliy jihatdan yoshlarga ish tajribasini ulashish, turli fikr va dunyoqarashga ega shaxslar orasida muloqot almashinuvini yo'lga qo'yish maqsadida tashkil etilgan."""   
    await call.message.answer(info, parse_mode='markdown', reply_markup=loyiha_maqsad)
    await call.message.delete()

@dp.callback_query_handler(text="aim")
async def echo(call: CallbackQuery):
    info = """🔰 What is the main purpose of the Young Managers Program?

 Project is designed to provide theoretical training in project management to young people from aged 17 to 25, to share practical work experience with young people, and to establish a community between people with different ideas and worldviews."""   
    await call.message.answer(info, parse_mode='markdown', reply_markup=loyiha_maqsad_en)
    await call.message.delete()





@dp.callback_query_handler(text="vazifa")
async def echo(call: CallbackQuery):
    info = """🔰 Loyihaning vazifalari nimalardan iborat?

 • Boshqaruv sohasida malakaga ega, xalqaro doirada faoliyat yurita oladigan mutaxassislar tayyorlab, davlat va nodavlat sektoridagi subyekt/obyektlar uchun salohiyatli kadrlar tizimini yaratib berish;

 • Yoshlarning bilim va ko'nikmasini oshirib, yuqori daromad keltiradigan ish bilan ta'minlash;

 • Kattalar va yoshlar orasida kommunikatsiya jarayonini shakllantirib, o'rtadagi "jarlik"ka ma'lum ma'noda chek qo'yish, ularning o'zaro hamkorligini ta'minlashga ko'maklashish."""   
    await call.message.answer(info, parse_mode='markdown', reply_markup=loyiha_vazifasi)
    await call.message.delete()


@dp.callback_query_handler(text="pro")
async def echo(call: CallbackQuery):
    info = """🔰 What are the objectives of project? 

 • Training of specialists with international qualifications in the field of management and creation of a potential human resources system for entities and objects in the public and private sectors;

 • Providing high-paid jobs to increase the knowledge and skills of youth; 

 • To form a process of communication between the older and younger generations, to put an end to the "cliff" between them, to help them to ensure their interaction."""   
    await call.message.answer(info, parse_mode='markdown', reply_markup=loyiha_vazifasi_en)
    await call.message.delete()






@dp.callback_query_handler(text="tartibi")
async def echo(call: CallbackQuery):
    info = """🔰 Loyiha qancha vaqt davom etadi va o'tkazilish tartibi qanday?

📝Yosh menejerlar dasturining o’tkazilish tartibi:

Loyiha 10 hafta davomida bo'lib o'tadi: amaliy va nazariy darslar olib boriladi.

📋 Avgust oyining 25-sanasidan boshlab 10-Sentabr kuniga qadar loyihada ishtirok etishga nomzod shaxslarni ro'yxatdan o'tkazish va saralash jarayoni tashkil etiladi:

• 1-bosqichi saralashdan o’tganlar: 13 Sentabr e’lon qilinadi. (100 ta ishtirokchi);
• 2-saralash bosqichi: 15-16 Sentabr kuni bo’lib o’tadi;
• Javoblar: 18 Sentabr kuni e’lon qilinadi (50 ta ishtirokchi).

 💡 Nomzodlar ichidan 50 nafar kuchga to'la, ingliz tilini yaxshi biluvchi, o'z ambitsiyalariga ega va kelajakda katta maqsadlari bor yoshlar tanlab olinadi."""   
    await call.message.answer(info, parse_mode='markdown', reply_markup=loyiha_tartibi)
    await call.message.delete()


@dp.callback_query_handler(text="the")
async def echo(call: CallbackQuery):
    info = """🔰 How long will the project last and what is the procedure?

  📝 Procedure for the Young Managers Program:

  The project will last for 10 weeks: practical and theoretical lessons will be conducted.

  📋 From August 25 to September 10, the process of registration and selection of candidates for participation in the project will be organized:

• Round 1 qualifiers: September 13 will be announced. (100 participants);
• Qualifying Round 2: September 15-16;
• Answers: to be announced on September 18 (50 participants).

  💡 Out of the candidates, 50 young people who are strong, fluent in English, have their own ambitions and have big goals for the future will be selected."""   
    await call.message.answer(info, parse_mode='markdown', reply_markup=loyiha_tartibi_en)
    await call.message.delete()







@dp.callback_query_handler(text="talab")
async def echo(call: CallbackQuery):
    info = """🔰 Loyihada qatnashish uchun nomzodlarga qanday talablar qo'yiladi?

 — ingliz, rus, o'zbek tilida ish yuritish: erkin so'zlashish va yoza olish;
 — IT texnologiyalari hamda mediasavodxonlik bo'yicha bilimga egalik;
 — 17-25 yosh orasida bo'lish;
 — Toshkent shahri va viloyati hududida istiqomat qilish."""   
    await call.message.answer(info, parse_mode='markdown', reply_markup=loyiha_talablari)
    await call.message.delete()


@dp.callback_query_handler(text="req")
async def echo(call: CallbackQuery):
    info = """🔰 What are the requirements for candidates to participate?

 — Office work in English, Russian, Uzbek: fluent speaking and writing skills;
 — Knowledge of IT and media; 
 — 17-25 years old;
 — Resident of Tashkent city and region."""   
    await call.message.answer(info, parse_mode='markdown', reply_markup=loyiha_talablari_en)
    await call.message.delete()






@dp.callback_query_handler(text="savol")
async def echo(call: CallbackQuery):
    info = """Assalomu alaykum!

Savollaringizni @anvar4353 ga yo'llashingiz mumkin. Sizga tez orada javob beramiz!

E'tiboringiz uchun rahmat."""   
    await call.message.answer(info, parse_mode='markdown', reply_markup=savollar_yollash)
    await call.message.delete()
# 

@dp.callback_query_handler(text="send")
async def echo(call: CallbackQuery):
    info = """Assalamu alaikum!

You can send your questions to @anvar4353 We will reply you soon.

Thank you for your attention."""   
    await call.message.answer(info, parse_mode='markdown', reply_markup=savollar_yollash_en)
    await call.message.delete()





@dp.callback_query_handler(text="royxat")
async def echo(call: CallbackQuery):
    await call.answer("Siz royxatdan otingiz!",show_alert=True)

@dp.callback_query_handler(text="reg")
async def echo(call: CallbackQuery):
    await call.answer("You are registered!",show_alert=True)





if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
