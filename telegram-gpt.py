import telebot
import openai

bot = telebot.TeleBot('6153376308:AAGLdSMLUVpBT80HNQY79eIhS7BXYN55VpM')
openai.api_key = "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"


@bot.message_handler(commands=["start"])
def start(msg):
    bot.send_message(msg.chat.id,
                     f'Привет {msg.from_user.first_name}, я бот GPT. Задавайте свои вопросы.'
                     f'\n\nАвтор: [Firdavs](israilzadeh.t.me)',
                     parse_mode='Markdown')

    @bot.message_handler(content_types=["text"])
    def handle_text(message):
        completion = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "user", "content": f"{message.text}"}
            ]
        )
        # print(completion.choices[0].message.content)
        bot.send_message(message.chat.id, completion.choices[0].message.content, parse_mode='Markdown')


bot.polling(none_stop=True, interval=0)