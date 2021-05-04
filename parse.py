# IMPORTS
import subprocess, sys, sched, time, os, argparse

try:
    from telethon import TelegramClient, events, sync
except:
    subprocess.check_call([sys.executable, "-m", "pip", "install", "telethon"])
    from telethon import TelegramClient, events, sync

# VARIABLES
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

channels = {}
keywords = {}
waitTime = 10
s = sched.scheduler(time.time, time.sleep)

# FUNCTIONS
def CheckKey():
    for channel in channels:
        print(bcolors.OKGREEN + "CHANNEL - " + channel + bcolors.ENDC)
        for message in client.get_messages(channel, limit=20):
            try:
                for key in keywords:
                    if key in message.message:
                        keywords[key] += 1
                    else:
                        continue
            except:
                continue

def ShowScanResult():
    print(keywords)

def ResetKeysCounter():
    keywords.update((key, 0) for key in keywords)

def InitConnection():
    global client
    api_id = 5220734
    api_hash = 'c66c23afec32a8cfc9919ff9152434e6'
    
    client = TelegramClient('session_name', api_id, api_hash)
    client.start()

def SetParam(paramForInit, destDictionary):
    paramFile = open(paramForInit, 'r')
    lines = paramFile.readlines()
    for item in lines:
        item = item.replace('\n','')
        destDictionary[item] = 0

def InitParams():
    parser = argparse.ArgumentParser()
    parser.add_argument('--keys',type=str, help="List of keywords")
    parser.add_argument('--channels', type=str, help="List of channels")
    args = parser.parse_args()

    SetParam(paramForInit = args.keys, destDictionary = keywords)
    SetParam(paramForInit = args.channels, destDictionary = channels)

def ClearConsole():
    clear = lambda: os.system('cls')
    clear()
#
# LET`S MAKE SOME MAGIC
#

def StartScriptLogic(sc):
    CheckKey()
    ShowScanResult()
    ResetKeysCounter()

    s.enter(waitTime, 1, StartScriptLogic, (sc,))

def main():
    ClearConsole()
    InitParams()
    InitConnection()

    s.enter(waitTime, 1, StartScriptLogic, (s,))
    s.run()

main()