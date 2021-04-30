# IMPORTS
import subprocess
import sys
import sched, time
import os
try:
    from telethon import TelegramClient, events, sync
except:
    subprocess.check_call([sys.executable, "-m", "pip", "install", "telethon"])
    from telethon import TelegramClient, events, sync

# VARIABLES
waitTime = 10
channels = []
keywords = {}

# FUNCTIONS
def GetKeysFromParams():
    arguments = len(sys.argv) - 1

    if arguments <= 0:
        sys.exit("Your keywords list is empty! Try again!")

    position = 1
    while (arguments >= position):
        keywords[sys.argv[position]] = 0
        position = position + 1

def ClearConsole():
    clear = lambda: os.system('cls')
    clear()

def InitConnection():
    global client
    api_id = 5220734
    api_hash = 'c66c23afec32a8cfc9919ff9152434e6'
    
    client = TelegramClient('session_name', api_id, api_hash)
    client.start()

def GetData():
    allChannels = client.iter_dialogs()
    
    for channel in allChannels:
        channels.append(channel.name)

def CheckKey():
    print("--- MESSAGES ---")
    for channel in channels:
        for message in client.get_messages(channel, limit=20):
            try:
                for key in keywords:
                    if key in message.message:
                        print(message.message)
                        print("Contains")
                        keywords[key] += 1
                    else:
                        continue
            except:
                continue

def ShowScanResult():
    print(keywords)

#
# LET`S MAKE SOME MAGIC
#

def StartScriptLogic(sc):
    ClearConsole()
    print(keywords)
    InitConnection()
    GetData()
    CheckKey()
    ShowScanResult()
    s.enter(waitTime, 1, StartScriptLogic, (sc,))

def main():
    GetKeysFromParams()
    # WAIT TIMER
    s = sched.scheduler(time.time, time.sleep)
    s.enter(waitTime, 1, StartScriptLogic, (s,))
    s.run()

main()