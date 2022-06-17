# Методы
* переслать сообщение с текстом


    bot.reply_to(message, "text")

* написать сообщение


    bot.send_message(message.chat.id, "text")

* удалить сообщение


    bot.delete_message(chat_id, message_id)

* редактировать сообщение


    bot.edit_message_text(chat_id, message_id, text='new text')