from functions import *

app, session = initialize_app()
me = None

@ignore
@app.on_message()
async def handle_message(client, message):
    # Получение переменной владельца аккаунта
    global me
    if me == None: me = await app.get_me()

    # Обработка остальных переменных
    text = message.text or ""
    user_id = str(message.from_user.id)
    user_name = f'{message.from_user.first_name+' ' if check_void(message.from_user.first_name) != None else ''}{message.from_user.last_name if check_void(message.from_user.last_name) != None else ''}'
    user_name = user_name if user_name != '' else 'None'
    user_username = message.from_user.username

    chat_id = message.chat.id
    chat_name = message.chat.title or f'{message.chat.first_name+' ' if check_void(message.chat.first_name) != None else ''}{message.chat.last_name if check_void(message.chat.last_name) != None else ''}'
    chat_name = chat_name if chat_name != '' else 'None'
    chat_username = message.chat.username
    # Обработка сообщения
    if message.from_user:
        await general_command(client, message)

    if user_id == str(me.id): await me_command(client, message)
    
    # Логирование сообщений
    log.write(f'\n[{get_time()}] Chat(chat_name={chat_name},chat_username={chat_username},chat_id={chat_id}) User(user_name={user_name},user_username={user_username},user_id={user_id}): {text if text != '' and text != ' ' else 'Пусто'}', rewrite=False)


@ignore
@app.on_edited_message()
async def handle_edited_message(client, message):
    pass

@ignore
@app.on_edited_message()
async def handle_on_deleted_messages(client, message):
    text = message.text or ""
    user_id = str(message.from_user.id)
    user_name = f'{message.from_user.first_name+' ' if check_void(message.from_user.first_name) != None else ''}{message.from_user.last_name if check_void(message.from_user.last_name) != None else ''}'
    user_name = user_name if user_name != '' else 'None'
    user_username = message.from_user.username

    chat_id = message.chat.id
    chat_name = message.chat.title or f'{message.chat.first_name+' ' if check_void(message.chat.first_name) != None else ''}{message.chat.last_name if check_void(message.chat.last_name) != None else ''}'
    chat_name = chat_name if chat_name != '' else 'None'
    chat_username = message.chat.username
    
    # Логирование сообщений
    log.write(f'\n[{get_time()}] [DELETED] Chat(chat_name={chat_name},chat_username={chat_username},chat_id={chat_id}) User(user_name={user_name},user_username={user_username},user_id={user_id}): {text if text != '' and text != ' ' else 'Пусто'}', rewrite=False)

if __name__ == '__main__':
    clear()
    print(app_title)
    app.run()