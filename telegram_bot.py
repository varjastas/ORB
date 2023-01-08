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

api_id = #your_api_id_int
api_hash = 'your_api_hash'
client = TelegramClient(
    'your_nick',
    api_id,
    api_hash,
    #proxy=('type', 'ip', port_int, 'login', 'pass')
    )


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

if __name__ == '__main__':
    try:
        with client:
            client.loop.run_until_complete(main())
    except Exception as ex:
        print(ex)

