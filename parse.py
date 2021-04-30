# IMPORTS
import subprocess, sys, sched, time, os, argparse

try:
    from telethon import TelegramClient, events, sync
except:
    subprocess.check_call([sys.executable, "-m", "pip", "install", "telethon"])
    from telethon import TelegramClient, events, sync

# VARIABLES
channels = []
keywords = {}
s = sched.scheduler(time.time, time.sleep)


# FUNCTIONS
def InitParams():
    parser = argparse.ArgumentParser()
    parser.add_argument('--keys', nargs='+',type=str)
    parser.add_argument('--wait', nargs='+',type=int)
    args = parser.parse_args()

    keysList = args.keys
    for key in keysList:
        keywords['#' + key] = 0

    global waitTime
    waitTime = args.wait[0]

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
    InitConnection()
    GetData()
    CheckKey()
    ShowScanResult() #TODO: replace print to email send function

    s.enter(waitTime, 1, StartScriptLogic, (sc,))

def main():
    InitParams()

    s.enter(waitTime, 1, StartScriptLogic, (s,))
    s.run()

main()