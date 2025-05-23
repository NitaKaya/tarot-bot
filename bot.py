import random
import json
import os
import asyncio
import nest_asyncio
from telegram import Update
from telegram.ext import Application, CommandHandler

# Применяем патч для работы с уже запущенным Event Loop
nest_asyncio.apply()

import os
print("Environment variables:", os.environ)

from telegram.ext import ApplicationBuilder

TOKEN = os.getenv("TOKEN")

if not TOKEN:
    raise ValueError("TOKEN is not set in environment variables")

app = ApplicationBuilder().token(TOKEN).build()
# (Твой токен правильный)

CHAT_ID = "7548864954" 

folder_path = "unzipped/ezyZip"

for filename in os.listdir(folder_path):
    if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.webp')):
        full_path = os.path.join(folder_path, filename)
        with open(full_path, "rb") as image:
            sent_message = bot.send_photo(chat_id=CHAT_ID, photo=image, caption=filename)
            print(f"{filename} → {sent_message.photo[-1].file_id}")

# Список карт Таро
cards = [
    {
        "name": "Шут",
        "image": "https://disk.yandex.ru/i/rC2A0sWncndPeg?force_download=true",
        "quote": "Тропой не топтаной, как ветер по полю...(с) Девица",
        "description": "Шут символизирует начало пути, наивность, спонтанность и готовность к новым приключениям. Эта карта говорит о свободе, доверии к миру и смелости сделать первый шаг в неизвестность.",
        "message": "Забудь обо всех заботах и планах. Пробуй что-то новое. Путь открыт."
    },
    {
        "name": "Маг",
        "image": "https://disk.yandex.ru/i/_6b2ueUXCilX6g?force_download=true",
        "quote": "Ты же чувствуешь силу во мне и опасности больше, чем в огне... (с) Северный Ветер",
        "description": "Маг — это проявление воли и возможностей. У него есть всё необходимое, чтобы творить свою реальность. Это карта действия, ясности и внутренней силы.",
        "message": "Ты обладаешь всем, чтобы воплотить задуманное. Начинай!"
    },
    {
        "name": "Верховная Жрица",
        "image": "https://disk.yandex.ru/i/cnkvQCCwDuZdkw?force_download=true",
        "quote": "Старыми преданиями разбредалась по земле, волнами разливалась и во снах являлась... (с.) Девица",
        "description": "Жрица символизирует интуицию, тайны, глубокое знание и связь с потаённым. Она хранит то, что сокрыто от глаз, и открывает истину лишь готовым к ней.",
        "message": "Доверься внутреннему знанию и интуиции. Ответ уже живёт внутри тебя"
    },
    {
        "name": "Императрица",
        "image":"https://disk.yandex.ru/i/8roLghLszz4TNg?force_download=true",
        "quote": "И взойдут с рассветом дикие сады... (с.) вОда",
        "description": "Императрица- архетип плодородия, заботы, творчества и природной силы. Она говорит о росте, любви и процветании.",
        "message": "Создавай и взращивай. Заложенные вами семена наконец прорастут. "
    },
    {
        "name": "Император",
        "image": "https://disk.yandex.ru/i/-wTK2L1P38AYLA?force_download=true",
        "quote": "Я не хочу с тобой соревноваться... (с.) Северный Ветер",
        "description": "Император- это структура, ответственность и опора. Он символизирует порядок, уверенность, защиту и силу воли.",
        "message": "Стой прочно на земле. Иди вперёд настойчиво, не теряя реализма."
    },
    {
        "name": "Иерофант",
        "image": "https://disk.yandex.ru/i/2tXf17UagHXbKg?force_download=true",
        "quote": "А чтобы выйти не хватает роста, но лишь как посмотреть... (с.) Тёмная сторона луны",
        "description": "Иерофант олицетворяет традиции, наставничество, духовную опору и обучение. Он говорит о поиске смысла в знаниях и передаче мудрости.",
        "message": "Положись на свой опыт и делай то, что не противоречит совести. Есть шанс на успех."
    },
    {
        "name": "Влюблённые",
        "image": "https://disk.yandex.ru/i/eMidii7Ko6O_cw?force_download=true",
        "quote": "... к милому манило, душу доверила... (с.) Кая",
        "description": "Карта Влюблённые говорит о выборе сердцем, соединении, доверии и слиянии. Это союз сердец, но и точка, где нужно решить, чему следовать- голосу ума и голосу сердца.",
        "message": "Прими важное решение, находясь в согласии с собой и своим сердцем"
    },
    {
        "name": "Колесница",
        "image": "https://disk.yandex.ru/i/tksQhctfT52uYg?force_download=true",
        "quote": "... догнать меня смогу птицы, стая белых птиц надо мной... (с.) вОда",
        "description": "Колесница- это движение, победа, концентрация и прорыв. Это сила воли, направленная в нужную сторону, и внутренний контроль над противоречиями.",
        "message": "Не медли и не сомневайся. Твоя решимость тебя ведём к победе."
    },
    {
        "name": "Сила",
        "image": "https://disk.yandex.ru/i/xCHrNXuXHAJoFQ?force_download=true",
        "quote": "Ты же чувствуешь силу во мне и опасности больше, чем в огне... (с.) Северный Ветер",
        "description": "Сила олицетворяет укрощение и овладение инстинктами, но не за счёт грубой силы и давления. Эта карта о том, как смирение может быть сильнее насилия.",
        "message": "Истинная сила- в принятии и любви к себе. Лишь в крайнем случае показывай свои когти."
    },
    {
        "name": "Отшельник",
        "image": "https://disk.yandex.ru/i/Ue0gRa-qEaS6Vg?force_download=true",
        "quote": "Спелые плоды, да в заснеженной пустыне не собрать (с.) Не молитвами",
        "description": "Отшельник- символ внутреннего поиска, одиночества и мудрости. Он уединяется, чтобы найти свой путь и истину.",
        "message": "Остановись и прислушайся. В тишине твой ответ."
    },
    {
        "name": "Колесо Фортуны",
        "image": "https://disk.yandex.ru/i/BEhDPjzKyOL9Tw?force_download=true",
        "quote": "Камни на дороге я обойду, я обточу... (с.) вОда",
        "description": "Колесо Фортуны указывает на перемены, цикличность и судьбоносные события. Это напоминание о непредсказуемости жизни и важности гибкости",
        "message": "Прими поворот. Всё меняется- и это к лучшему."
    },
    {
        "name": "Справедливость",
        "image": "https://disk.yandex.ru/i/UIud92aUbVrjpw?force_download=true",
        "quote": "Светлые головы с тёмными мыслями. А кто же узнает? (с.) Не молитвами",
        "description": "Справедливость говорит о правде, равновесии и честности. Это карта выбора по совести и ответственности за действия.",
        "message": "Прими на себя ответственность. Правда откроет тебе путь."
    },
    {
        "name": "Повешенный",
        "image": "https://disk.yandex.ru/i/xRUomV_Fx0RfqQ?force_download=true",
        "quote": "А ты поверил, что это всё реально, но всё не так... (с.) Тёмная сторона луны",
        "description": "Повешенный символизирует жертву, переосмысление и взгляд с другой стороны. Он предлагает взять паузу, чтобы увидеть суть происходящего.",
        "message": "Поменяй угол зрения. Возможно придётся чем-то повертвовать, чтобы получить новое начало."
    },
    {
        "name": "Смерть",
        "image": "https://disk.yandex.ru/i/JcacX3hHUMf6fA?force_download=true",
        "quote": "И во мне родится новый смысл слов- быть живой (с.) вОда",
        "description": "Смерть- не конец, а трансформация. Это карта завершений, которые дают начало новой жизни. Оставь прошлое, чтобы войти в новое.",
        "message": "Прими, что пришло время проститься с прежними жизненными обстоятельствами, образом действий или ситуацией."
    },
    {
        "name": "Умеренность",
        "image": "https://disk.yandex.ru/i/cJZ7IisfaSsN2Q?force_download=true",
        "quote": "Я хотела просто поймать ветер..., а теперь он во мне звучит... (с.) вОда",
        "description": "Умеренность- это гармония, равновесие и внутренний поток. Она учит выбирать нужную меру и следовать ритму жизни.",
        "message": "Верь в своего ангела- хранителя и позволь ему повести тебя. Ты обретёшь мир и гармонию."
    },
    {
        "name": "Дьявол",
        "image": "https://disk.yandex.ru/i/uyx6Wz8tGHGgVA?force_download=true",
        "quote": "Это чёрные перья на моих белых крыльях... и запачканы нефтью мои белые пальцы... (с.) Не молитвами",
        "description": "Дьявол говорит о привязанностях, соблазнах и теневых сторонах. Он проявляет то, что требует освобождения и честного взгляда.",
        "message": "Особождайся. Это иллюзия, а не реальность."
    },
    {
        "name": "Башня",
        "image": "https://disk.yandex.ru/i/HH_5C2tKk36LGw?force_download=true",
        "quote": "В месте, где не бывало веры быстро твои разрушат стены... (с.) Тёмная сторона луны",
        "description": "Башня- разрушение иллюзий, неожиданный перелом и очищение. Она обрушивает старое, чтобы построить новое на правде.",
        "message": "Пусть рушится. Это начало настоящего."
    },
    {
        "name": "Звезда",
        "image": "https://disk.yandex.ru/i/pE_Or_b50ox7ag?force_download=true",
        "quote": "Талая вода к горной реке найдёт дорогу... (с.) Кая",
        "description": "Звезда- надежда, вдохновение, ясность после шторма. Она указывает на светлый путь и связь с высшим.",
        "message": "Не ставь перед собой незначительные цели. Верь в своё будущее, на это есть основания."
    },
    {
        "name": "Луна",
        "image": "https://disk.yandex.ru/i/HIssHEexGhFX8A?force_download=true",
        "quote": "Просто ты на самой тёмной стороне луны... (с.) Тёмная сторона луны",
        "description": "Луна символизирует страхи, иллюзии и подсознание. Она говорит о времени тумана, но и о глубокой интуиции.",
        "message": "Иди дорогой страха, но иди осторожно. Не педалируй ситуацию, а спокойно её контролируй."
    },
    {
        "name": "Солнце",
        "image": "https://disk.yandex.ru/i/-EWBfITzWymtjA?force_download=true",
        "quote": "А меня от горя солнце ведёт... (с.) вОда",
        "description": "Солнце- радость, ясность, тепло и пробуждение. Эта карта говорит об успехе, внутреннем свете и настоящем счастье.",
        "message": "Сияй. Тьма уже позади."
    },
    {
        "name": "Суд",
        "image": "https://disk.yandex.ru/i/WhxU83tEQk_IkA?force_download=true",
        "quote": "Но я с начала начну этот год, без снежного сердца... (с.) Кая",
        "description": "Суд- пробуждение, перерождение, осознание своего пути. Оно говорит о прозрении и новом этапе жизни.",
        "message": "Пришло время избавиться от всего фальшивого и обрести настоящее. Ты готов начать заново."
    },
    {
        "name": "Мир",
        "image": "https://disk.yandex.ru/i/SrsCd2r_Acw9eA?force_download=true",
        "quote": "Запертые ставни отворялись понемногу, стоя у порога... (с.) Кая",
        "description": "Мир- завершение цикла, целостность, гармония. Эта карта говорит о внутреннем и внешнем объединении, победе над собой и возвращении домой.",
        "message": "ТЗдесь ты обретёшь свой дом. Всё завершилось- и всё начинается снова. "
    }
]

file_ids = {}
if os.path.exists("file_ids.json"):
    with open("file_ids.json", "r", encoding="utf-8") as f:
        file_ids = json.load(f)


# Функция для команды /card
async def card(update: Update, context):
    await update.message.reply_text("🔮 Перемешиваю карты...")
    selected_card = random.choice(cards)

    await update.message.reply_photo(
        selected_card["image"],
        caption=f"🔹 <b>{selected_card['name']}</b>\n\n"
                f"🌙 <i>{selected_card['quote']}</i>\n\n"
                f"{selected_card['description']}\n\n"
                f"✨ <b>Послание от карты:</b>\n<b>{selected_card['message']}</b>",
        parse_mode='HTML'
    )



# Главная функция запуска бота
async def main():
    application = Application.builder().token(TOKEN).build()
    application.add_handler(CommandHandler("card", card))
    print("Бот запущен...")
    await main()

# Запуск
if __name__ == "__main__":
    asyncio.run(main())
# Добавим фейковый веб-сервер, чтобы Render не ругался
import threading
from http.server import BaseHTTPRequestHandler, HTTPServer

class DummyHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b'Tarot bot is alive!')

def run_dummy_server():
    port = int(os.environ.get('PORT', 10000))  # Render передаёт свой порт через переменную
    server = HTTPServer(('', port), DummyHandler)
    server.serve_forever()

# Запускаем сервер в отдельном потоке
threading.Thread(target=run_dummy_server, daemon=True).start()
