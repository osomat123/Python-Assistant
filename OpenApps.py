import os
import pyttsx3
import json

def getApps():
    
    try:
        with open("apps.json","r") as read_file:
            strApps = read_file.read()
            apps = eval(json.loads(strApps))
     
    except FileNotFoundError:
        
        apps = {}

        for (path,app,file) in os.walk('/Applications'):
            if path.endswith('.app') and path.count('.app') == 1:
                app = path[1:].split('/')[-1].replace('.app','')  # Get app name
                path = path.replace(' ','\ ') # Set app path
                apps[app] = path

        for (path,app,file) in os.walk('/System/Applications'):
            if path.endswith('.app') and path.count('.app') == 1:
                app = path[1:].split('/')[-1].replace('.app','') # Get app name
                path = path.replace(' ','\ ') # Set app path
                apps[app] = path
                
        with open("apps.json",'w') as file:
            file.write(json.dumps(str(apps)))
    
    return apps


def addNick(nick,longApp):
    
    flag = 0
    
    with open("apps.json","r") as read_file:
        strApps = read_file.read()
        apps = eval(json.loads(strApps))
        
    newApps = apps
    
    for app in apps.keys():
        if app.upper() == longApp:
            newApps[nick] = apps[app]
            flag = 1
            break
    
    if flag ==0:
        return False
    
    with open("apps.json",'w') as file:
        file.write(json.dumps(str(newApps)))
    
    return True


print("Initializing...\n")
valid = ['RUN','OPEN','EXECUTE','BYE','EXIT','QUIT','ADD NICKNAME','HELP','STOP','CIAO']
apps = getApps()

print("Welcome to Py Assistant")
print("How can I help?\n")
pyttsx3.speak("Welcome to Py Assistant....How can I help?")

print("Type 'help' if you're confused\n")
pyttsx3.speak("Type help if you're confused")

while True:
    
    query = input("Type here -> ").upper()
    appFound = 0
    commandValid = 0
    
    for command in valid:
        if command in query:
            commandValid = 1
            break
    
    if commandValid == 0:
        print('Sorry, operation not supported\n')
        pyttsx3.speak('Sorry, operation not supported.')
        continue

    if "HELP" in query:
        f = open("help.txt",'r')
        print(f.read())
        f.close()
        continue
        
    if ("BYE" == query) or ("EXIT" == query) or ("QUIT" == query) or ('STOP' == query) or ('CIAO' == query):
        print("Bye!\n")
        pyttsx3.speak("Bye.")
        break
        
    if 'ADD NICKNAME'in query:
        names = [i.strip() for i in query.split('FOR')]
        nick = names[0][13:]
        longApp = names[1]
        
        if nick in apps:
            print("Nickname already exists. Give another nickname.\n")
            pyttsx3.speak("Nickname already exists. Give another nickname")
            continue
        
        ret = addNick(nick,longApp)
        
        if ret == True:
            with open("apps.json","r") as read_file:
                strApps = read_file.read()
                apps = eval(json.loads(strApps))
                
            print("Nickname added.\n")
            pyttsx3.speak("Nickname added.")
            appFound = 1
            continue
            
    if ('RUN' in query) or ('OPEN' in query) or ('EXECUTE' in query):
        for app in apps.keys():
            if app.upper() in query:
                command = 'open '+apps[app]
                print("Sure!\nOpening "+app+" ...\n")
                pyttsx3.speak("Sure.....Opening "+app)
                os.system(command)
                appFound = 1
                break        

    if appFound == 0:
        print('Application not found. Try Again!\n')
        pyttsx3.speak("Application not found. Try Again!")
