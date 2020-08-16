print("\nWelcome to tools\n")
pyttsx3.speak("Welcome to tools")

print("Press 1 to open Slack")
print("Press 2 to open Whatsapp")
print("Press 3 to open Atom")
print("Press 4 to open Pycharm")
print("Press 5 to open VLC\n")

app = int(input("Your Choice -> "))
command = ''

if app == 1:
    command = 'open /Applications/Slack.app'
    print('Opening...')
    
elif app == 2:
    command = 'open /Applications/Whatsapp.app'
    print('Opening...')
    
elif app == 3:
    command = 'open /Applications/Atom.app'
    print('Opening...')
    
elif app == 4:
    command = 'open /Applications/Pycharm\ CE.app'
    print('Opening...')
    
elif app == 5:
    command = 'open /Applications/VLC.app'
    print('Opening...')
    
else:
    print('Invalid Input')
    
os.system(command)    