import requests
import time
import asyncio
import random
import emoji
from telethon import TelegramClient, events, Button
from bs4 import BeautifulSoup
from telethon.tl.functions.users import GetFullUserRequest
from telethon.tl.functions.account import UpdateProfileRequest, UpdateUsernameRequest
from telethon.tl.functions.photos import UploadProfilePhotoRequest
from telethon.tl.functions.messages import SendReactionRequest
import logging
logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)

api_id = 22834783
api_hash = '8a4a156d4946e55cbda7e43decf4f362'
client = TelegramClient(
    'denizzzka2125',
    api_id,
    api_hash,
    proxy=('http', '104.144.26.91', 8621, 'itrlisag', 'zgbasg5sr9e7')
    )

# Auto reply messages
# headers = {
#     'sec-ch-ua': '"Chromium";v="106", "Yandex";v="22", "Not;A=Brand";v="99"',
#     'Referer': 'https://www.infoniac.ru/news/100-krasivyh-kommentariev-kotorye-mozhno-napisat-devushke-pod-foto-v-socsetyah.html',
#     'sec-ch-ua-mobile': '?0',
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 YaBrowser/22.11.5.715 Yowser/2.5 Safari/537.36',
#     'sec-ch-ua-platform': '"Windows"',
# }

# r = requests.get(
#     'https://www.infoniac.ru/news/100-krasivyh-kommentariev-kotorye-mozhno-napisat-devushke-pod-foto-v-socsetyah.html',
#     headers=headers
# )
# soup = BeautifulSoup(r.content, 'lxml')

# # ожидание определенного сообщения
# # message_wait = ''
# # @client.on(events.NewMessage(outgoing=False, pattern=f'.+(?i){message_wait}')) # ждёт какое либо слово

# @client.on(events.NewMessage(outgoing=False))
# async def my_event_handler(event):
#     #if 'hello' in event.raw_text:
#     number = random.randint(1,123)
#     a = soup.find('div', class_='entry').find_all("p")[number].text.strip()
#     a = a[a.find('.')+2:]
#     await event.reply(a)
#     # await event.respond(a) # не в качестве ответа пишет
# client.start()
# client.run_until_disconnected()

# Choice the action
async def choice_action():
    action = input('What do you want to do? Choose something:\n'
                   'Change profile info - 1\n'
                   'Reactions to post - 2\n')
    if action == '1':
        await change_question()
    elif action == '2':
        await send_reaction()

# Full info
async def change_question():
    me = await client.get_me()
    bio = await client(GetFullUserRequest(me.username))
    bio = bio.full_user.about
    print(f'акк | {me.phone} | {me.username} | {me.first_name} | {me.last_name} | {bio} | {me.photo.photo_id}')
    question = input('Do you want to change something in profile? y/n ')
    if question == 'y':
        question = input('What do you want to change?\nname\nbio\nusername\nphoto\n')
        if question == 'name':
            await change_name()
        elif question == 'bio':
            await change_bio()
        elif question == 'username':
            await change_username()
        elif question == 'photo':
            await change_photo()

# Change name
async def change_name():
    new_fname = input('Enter new first name: ')
    new_lname = input('Enter new last name: ')
    await client(UpdateProfileRequest(last_name=new_lname, first_name=new_fname))

# Change bio
async def change_bio():
    new_bio = input('Enter new bio: ')
    await client(UpdateProfileRequest(about=new_bio))
    
# Change username
async def change_username():
    new_username = input('Enter new username: ')
    await client(UpdateUsernameRequest(new_username))

# Change photo
async def change_photo():
    new_photo = input(r'Enter the address of the photo, for example: "C:\Users\me\photo.png" ')
    await client(UploadProfilePhotoRequest(await client.upload_file(new_photo)))

# Send reaction
async def send_reaction():
    reaction = emoji.emojize(f":{input('Enter emoji like -> red_heart : ')}:")
    result = await client(SendReactionRequest(
             peer='piratecryptoblog',
             msg_id=967,
             reaction=reaction
             ))
    print(result.stringify())


async def main():
    await choice_action()
    # Send message + edit + delete
    # message = await client.send_message(
    #     'me',
    #     'This message has **bold**, `code`, __italics__ and '
    #     'a [nice website](https://example.com)!',
    #     link_preview=False
    # )
    # await asyncio.sleep(5)
    # await client.delete_messages(message.chat_id, message.id) # delete
    # await client.edit_message(message.chat_id, message.id, '') # edit

    # Returns message
    # print(message.raw_text)


    # Reply to message
    # await message.reply('Cool!')


    # Write with username
    # await client.send_message('username', 'hi')


    # History of messages
    # async for message in client.iter_messages('me'):
    #     print(message.id, message.text)


    # Save id
    # async def (event):
    # chat = await event.get_chat()
    # sender = await event.get_sender()
    # chat_id = event.chat_id
    # sender_id = event.sender_id

# with client:
#     client.run_until_disconnected()

if __name__ == '__main__':
    try:
        with client:
            client.loop.run_until_complete(main())
    except Exception as ex:
        print(ex)

