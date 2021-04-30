# IMPORTS
from telethon import TelegramClient, events, sync

# VARIABLES
channels = []
api_id = 5220734
api_hash = 'c66c23afec32a8cfc9919ff9152434e6'

# CONNECTION
client = TelegramClient('session_name', api_id, api_hash)
client.start()

# GET ALL DIALOGS AND CHATS
allChannels = client.iter_dialogs()
print("--- DIALOGS ---")
for channel in allChannels:
    channels.append(channel.name)

#CHECK KEYWORD IN CHATS
print("--- MESSAGES ---")
for channel in channels:
    for message in client.get_messages(channel, limit=20):
        if " " in message.message: 
            if "art" in message.message:
                print(message.message)
                print("Contains")
            else:
                print(message.message)
                print("Don`t contains")
        else:
            continue
