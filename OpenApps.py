import os
import pyttsx3

def getApps():
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
    
    return apps


print("Initializing...\n")
apps = getApps()

print("Welcome to tools")
pyttsx3.speak("Welcome to tools")

print("How can I help?\n")
pyttsx3.speak("How can I help?")

query = input("Type here -> ").upper()
command = ''

for app in apps.keys():
    if app.upper() in query:
        command = 'open '+apps[app]
        
        print("Opening "+app+" ...")
        pyttsx3.speak("Opening "+app)
        
        os.system(command)
        break
        
if command == '':
    print('Application not found. Try Again!')
    pyttsx3.speak("Application not found. Try Again!")