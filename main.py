import time,os,sys

def typingPrint(text):
  for character in text:
    sys.stdout.write(character)
    sys.stdout.flush()
    time.sleep(0.07)
  print()
  
def typingInput(text):
  for character in text:
    sys.stdout.write(character)
    sys.stdout.flush()
    time.sleep(0.05)
  value = input()  
  return value  
  
def clearScreen():
  typingPrint("Clear screen...")
  os.system("clear")

'''
█▀ █▀▀ █▀▀ █▄░█ █▀▀   ▄█ ▀   █ █▄░█ ▀█▀ █▀█ █▀█ █▀▄ █░█ █▀▀ ▀█▀ █ █▀█ █▄░█
▄█ █▄▄ ██▄ █░▀█ ██▄   ░█ ▄   █ █░▀█ ░█░ █▀▄ █▄█ █▄▀ █▄█ █▄▄ ░█░ █ █▄█ █░▀█
'''
print(" /   |   \  ______  _  __ __  _  _|__|  | |  |    ___.__. ____  __ __ ")
print("/    ~    \/  _ \ \/ \/ / \ \/ \/ /  |  | |  |   <   |  |/  _ \|  |  \ ")
print("\    Y    (  <_> )     /   \     /|  |  |_|  |__  \___  (  <_> )  |  /")
print(" \___|_  / \____/ \/\_/     \/\_/ |__|____/____/  / ____|\____/|____/ ")
print("       \/                                         \/                  ")
print("                     __                   __ _________ ")
print("_____________  _____/  |_  ____   _______/  |\_____   \ ")
print("\____ \_  __ \/  _ \   __\/ __ \ /  ___/\   __\ /   __/")
print("|  |_> >  | \(  <_> )  | \  ___/ \___ \  |  |  |   |   ")
print("|   __/|__|   \____/|__|  \___  >____  > |__|  |___|   ")
print("|__|                          \/     \/        <___> ")

typingPrint("\n\n\nCreated by Ethan Shao")

time.sleep(1)
typingPrint("Welcome to How will you protest?")
time.sleep(1)
print()
egg = typingInput("What's your name?:")

if egg=="":
  for i in range(50):
    print("Oui Oui Baguette")
    time.sleep(0.05)
  typingPrint("Are you still here? Starting...")
else:
  typingPrint("You will be William, William.")
  
print("Clearing...")
time.sleep(1)

clearScreen()

# Waking Up
typingPrint("SCENE 1\n\n")
typingPrint("You wake up.\n")
typingPrint("On the right there is a desk, with an alarm clock and lamp.\nOn the left, you see a window that is too bright \nto look into from afar.\n")
choose1 = typingInput("Look in the window(x) or look into the desk(y) >")
if choose1 == "x":
  typingPrint("You see the scenery outside.\nIt looks like the side of a road,\npeople taking a stroll around town.\n")
  
elif choose1 == "y":
  choose1a = typingInput("You look at the desk, and see a letter on the top of it.\nWould you like to read the letter?(x) or look around the room(y) >")
  if choose1a == "x":
    typingPrint("The letter writes:")
    time.sleep(1)
    print()
    typingPrint("From Uncle Johnson    To William Johnson   1/3/1965\n\n\n")
    typingPrint("You should join the protest :)))) XD")
    typingPrint("\n\nFrom, Uncle Johnson")
    choose1aa = typingInput("Would you like to look around the room(x) or wait(y) >")
    if choose1aa == "x":
      typingPrint("Around the room, you see some old furniture, and a \nbroken closet sitting on the opposite side of the room.")
      choose1c= typingInput("You can:\nLook into the closet(x)\nLook on the desk(y)\nWait(z)\n >")
      if choose1c=="x":
        typingPrint("You look into the closet. It creaks open...")
        typingPrint("There are some work clothes inside. ")
        choose1ca = typingPrint("Would you like to put the clothes on(x) or wait(y)\n > ")
        if choose1ca == "x":
          typingPrint("You rummage around and find a dusty suit that looks nice.")
          time.sleep(2)
          clearScreen()
          time.sleep(1)
          print("RING!")
          time.sleep(0.5)
          print("RING!")  
          time.sleep(0.1)
          typingPrint("The phone is ringing, probably your boss calling to make sure you get to work on time.")
          typingPrint("You pick up the phone against your will, dreading the\ndiscriminating voice of your boss.\n")
          typingPrint("'... Hello?'\n 'It's your boss. You better get here on time today or your pay will be reduced.'\n'... Yes, Sir.'\n\n")
          typingPrint("You are about to leave the room when")
          typingPrint("The phone rings again, and you pick up.")
          typingPrint("'Hello? Who is this?' \n- 'Hey, it's cousin Jim! :D Are you coming to the march!:D :D :D? \n- 'uh, yeah. Coming over right after work.'")
          typingPrint("You quickly dress up and run out of the door, worried you would be late to work again.")
          typingPrint("\n\n\n")
          #end
        
        elif choose1ca=="y":
          typingPrint("You wait, realizing that you slept with your work clothes on.\nLast night you overworked a bit, thanks to your unfair boss.")
          time.sleep(2)
          clearScreen()
          time.sleep(1)
          print("RING!")
          time.sleep(0.5)
          print("RING!")
          time.sleep(0.1)
          typingPrint("The phone is ringing, probably your boss calling to make sure you get to work on time.")
          typingPrint("You pick up the phone against your will, dreading the\ndiscriminating voice of your boss.\n")
          typingPrint("'... Hello?'\n 'It's boss. You better get here on time today or your pay will be reduced.'\n'... Yes, Sir.'\n\n")
          typingPrint("You are about to leave the room when")
          typingPrint("The phone rings again, and you pick up.")
          typingPrint("'Hello? Who is this?' \n- 'Hey, it's cousin Jim! :D Are you coming to the march!:D :D :D? \n- 'uh, yeah. Coming over right after work.'")
          typingPrint("You quickly dress up with a random suit you find in the closet and run out of the door, worried you would be late to work again.")
          typingPrint("\n\n\n")
          time.sleep(2)
          clearScreen()
          #end
    elif choose1aa=="y":
      typingPrint("You wait...")
      time.sleep(1)
      print("RING!")
      time.sleep(0.5)
      print("RING!")  
      time.sleep(0.1)
      typingPrint("The phone is ringing, probably your boss calling to make sure you get to work on time.")
      typingPrint("You pick up the phone against your will, dreading the\ndiscriminating voice of your boss.\n")
      typingPrint("'... Hello?'\n 'It's your boss. You better get here on time today or your pay will be reduced.'\n'... Yes, Sir.'\n\n")
      typingPrint("You are about to leave the room when")
      typingPrint("The phone rings again, and you pick up.")
      typingPrint("'Hello? Who is this?' \n- 'Hey, it's cousin Jim! :D Are you coming to the march!:D :D :D? \n- 'uh, yeah. Coming over right after work.'")
      typingPrint("You quickly dress up and run out of the door, worried you would be late to work again.")
      typingPrint("\n\n\n")
      #end
  elif choose1a=="y":
    typingPrint("Around the room, you see some old furniture, and a \nbroken closet sitting on the opposite side of the room.")
    choose1c= typingInput("You can:\nLook into the closet(x)\nLook on the desk(y)\nWait(z)\n >")
    if choose1c=="x":
      typingPrint("You look into the closet. It creaks open...")
      typingPrint("There are some work clothes inside. ")
      choose1ca = typingInput("Would you like to put the clothes on(x) or wait(y)\n > ")
      if choose1ca == "x":
        typingPrint("You rummage around and find a dusty suit that looks nice.")
        time.sleep(2)
        clearScreen()
        time.sleep(1)
        print("RING!")
        time.sleep(0.5)
        print("RING!")  
        time.sleep(0.1)
        typingPrint("The phone is ringing, probably your boss calling to make sure you get to work on time.")
        typingPrint("You pick up the phone against your will, dreading the\ndiscriminating voice of your boss.\n")
        typingPrint("'... Hello?'\n 'It's your boss. You better get here on time today or your pay will be reduced.'\n'... Yes, Sir.'\n\n")
        typingPrint("You are about to leave the room when")
        typingPrint("The phone rings again, and you pick up.")
        typingPrint("'Hello? Who is this?' \n- 'Hey, it's cousin Jim! :D Are you coming to the march!:D :D :D? \n- 'uh, yeah. Coming over right after work.'")
        typingPrint("You quickly dress up and run out of the door, worried you would be late to work again.")
        typingPrint("\n\n\n")
        #end
        
      elif choose1ca=="y":
        typingPrint("You wait, realizing that you slept with your work clothes on.\nLast night you overworked a bit, thanks to your unfair boss.")
        time.sleep(2)
        clearScreen()
        time.sleep(1)
        print("RING!")
        time.sleep(0.5)
        print("RING!")
        time.sleep(0.1)
        typingPrint("The phone is ringing, probably your boss calling to make sure you get to work on time.")
        typingPrint("You pick up the phone against your will, dreading the\ndiscriminating voice of your boss.\n")
        typingPrint("'... Hello?'\n 'It's boss. You better get here on time today or your pay will be reduced.'\n'... Yes, Sir.'\n\n")
        typingPrint("You are about to leave the room when")
        typingPrint("The phone rings again, and you pick up.")
        typingPrint("'Hello? Who is this?' \n- 'Hey, it's cousin Jim! :D Are you coming to the march!:D :D :D? \n- 'uh, yeah. Coming over right after work.'")
        typingPrint("You quickly dress up with a random suit you find in the closet and run out of the door, worried you would be late to work again.")
        typingPrint("\n\n\n")
        time.sleep(2)
        clearScreen()
        #end
    elif choose1c == "y":
      choose1a = typingInput("You look at the desk, and see a letter on the top of it.\nWould you like to read the letter?(x) or look around the room(y) >")
      if choose1a == "x":
        typingPrint("The letter writes:")
        time.sleep(1)
        print()
        typingPrint("From Uncle Johnson    To William Johnson   1/3/1965\n\n\n")
        typingPrint("You should join the protest :)))) XD")
        typingPrint("\n\nFrom, Uncle Johnson")
        choose1aa = typingInput("Would you like to look around the room(x) or wait(y) >")
        if choose1aa == "x":
          typingPrint("Around the room, you see some old furniture, and a \nbroken closet sitting on the opposite side of the room.")
          choose1c= typingInput("You can:\nLook into the closet(x)\nLook on the desk(y)\nWait(z)\n >")
          if choose1c=="x":
            typingPrint("You look into the closet. It creaks open...")
            typingPrint("There are some work clothes inside. ")
            choose1ca = typingPrint("Would you like to put the clothes on(x) or wait(y)\n > ")
            if choose1ca == "x":
              typingPrint("You rummage around and find a dusty suit that looks nice.")
              time.sleep(2)
              clearScreen()
              time.sleep(1)
              print("RING!")
              time.sleep(0.5)
              print("RING!")  
              time.sleep(0.1)
              typingPrint("The phone is ringing, probably your boss calling to make sure you get to work on time.")
              typingPrint("You pick up the phone against your will, dreading the\ndiscriminating voice of your boss.\n")
              typingPrint("'... Hello?'\n 'It's your boss. You better get here on time today or your pay will be reduced.'\n'... Yes, Sir.'\n\n")
              typingPrint("You are about to leave the room when")
              typingPrint("The phone rings again, and you pick up.")
              typingPrint("'Hello? Who is this?' \n- 'Hey, it's cousin Jim! :D Are you coming to the march!:D :D :D? \n- 'uh, yeah. Coming over right after work.'")
              typingPrint("You quickly dress up and run out of the door, worried you would be late to work again.")
              typingPrint("\n\n\n")
              #end
            
        elif choose1ca=="y":
          typingPrint("You wait, realizing that you slept with your work clothes on.\nLast night you overworked a bit, thanks to your unfair boss.")
          time.sleep(2)
          clearScreen()
          time.sleep(1)
          print("RING!")
          time.sleep(0.5)
          print("RING!")
          time.sleep(0.1)
          typingPrint("The phone is ringing, probably your boss calling to make sure you get to work on time.")
          typingPrint("You pick up the phone against your will, dreading the\ndiscriminating voice of your boss.\n")
          typingPrint("'... Hello?'\n 'It's boss. You better get here on time today or your pay will be reduced.'\n'... Yes, Sir.'\n\n")
          typingPrint("You are about to leave the room when")
          typingPrint("The phone rings again, and you pick up.")
          typingPrint("'Hello? Who is this?' \n- 'Hey, it's cousin Jim! :D Are you coming to the march!:D :D :D? \n- 'uh, yeah. Coming over right after work.'")
          typingPrint("You quickly dress up with a random suit you find in the closet and run out of the door, worried you would be late to work again.")
          typingPrint("\n\n\n")
          time.sleep(2)
          clearScreen()
          #end
    elif choose1aa=="y":
      typingPrint("You wait...")
      time.sleep(1)
      print("RING!")
      time.sleep(0.5)
      print("RING!")  
      time.sleep(0.1)
      typingPrint("The phone is ringing, probably your boss calling to make sure you get to work on time.")
      typingPrint("You pick up the phone against your will, dreading the\ndiscriminating voice of your boss.\n")
      typingPrint("'... Hello?'\n 'It's your boss. You better get here on time today or your pay will be reduced.'\n'... Yes, Sir.'\n\n")
      typingPrint("You are about to leave the room when")
      typingPrint("The phone rings again, and you pick up.")
      typingPrint("'Hello? Who is this?' \n- 'Hey, it's cousin Jim! :D Are you coming to the march!:D :D :D? \n- 'uh, yeah. Coming over right after work.'")
      typingPrint("You quickly dress up and run out of the door, worried you would be late to work again.")
      typingPrint("\n\n\n")
      #end

'''
█▀ █▀▀ █▀▀ █▄░█ █▀▀   ▀█ ▀   █░█░█ █▀█ █▀█ █▄▀
▄█ █▄▄ ██▄ █░▀█ ██▄   █▄ ▄   ▀▄▀▄▀ █▄█ █▀▄ █░█

Mainly just conversation
'''

clearScreen()
typingPrint("SCENE 2: Work\n\n\n")
typingPrint("You make your way to your job, a construction worker working on the minimum wage of $1.15 an hour.")
typingPrint("As you enter the site, you see your friends and co-workers already getting ready, and your work pal, Michael comes up to you.")
typingPrint("M: Yo Johnson, come help me with the new load of concrete!")
typingPrint("J(you): Coming, wait up a second.")
time.sleep(2)
clearScreen()

typingPrint("You hop over to Michael with a wheelbarrow, and he starts loading bags.")
typingPrint("\nM: You going to the march tonight?")
typingPrint("J: Of course, I wouldn't miss a chance to get out of the royal shaft(To be unfairly treated or put-off)")
typingPrint("M: All that everyone's talking about is the march. They're saying it'll be huge.")
typingPrint("\n\nYou wheelbarrow the concrete bags from the truck, and spot your discriminative boss.")
time.sleep(2)
clearScreen()

typingPrint("B(oss): Get to work! If you'r not working, get to it! >:o")
typingPrint("The boss assigns black workers to the harder jobs and white workers to easier jobs.")
typingPrint("Just the thought of social communication with him makes you sick. :(")
time.sleep(2)
clearScreen()


'''
░██████╗░█████╗░███████╗███╗░░██╗███████╗  ██████╗░██╗  ███╗░░░███╗░█████╗░██████╗░░█████╗░██╗░░██╗
██╔════╝██╔══██╗██╔════╝████╗░██║██╔════╝  ╚════██╗╚═╝  ████╗░████║██╔══██╗██╔══██╗██╔══██╗██║░░██║
╚█████╗░██║░░╚═╝█████╗░░██╔██╗██║█████╗░░  ░█████╔╝░░░  ██╔████╔██║███████║██████╔╝██║░░╚═╝███████║
░╚═══██╗██║░░██╗██╔══╝░░██║╚████║██╔══╝░░  ░╚═══██╗░░░  ██║╚██╔╝██║██╔══██║██╔══██╗██║░░██╗██╔══██║
██████╔╝╚█████╔╝███████╗██║░╚███║███████╗  ██████╔╝██╗  ██║░╚═╝░██║██║░░██║██║░░██║╚█████╔╝██║░░██║
╚═════╝░░╚════╝░╚══════╝╚═╝░░╚══╝╚══════╝  ╚═════╝░╚═╝  ╚═╝░░░░░╚═╝╚═╝░░╚═╝╚═╝░░╚═╝░╚════╝░╚═╝░░╚═╝
'''

typingPrint("SCENE 3: The March\n\n")

typingPrint("You arrive to the protest march. There are already many people gathered there.")
typingPrint("Just as you get there, the march begins. People are holding up signs.")
choosec = typingInput("\nYou can go to the front(x) or the back(x) of the march > ")
if choosec=="x":
  typingPrint("You run over to the back, where a couple people are handing out posters.")
  typingPrint("You grab one quickly and start following the people in front of you.")
  typingPrint("Suddenly, one firefighters with a hose\nstarts blasting you and your fellow friends.")
  chooseca = typingInput("Do you want to: Fight them(x) or run away(y)")
  if chooseca == "x":
    typingPrint("NO. YOU DO NOT ATTACK BC THIS IS A PEACEFUL PROTEST")
    typingPrint("Moving on...")
  elif chooseca=="y":
    typingPrint("Good job! :DDDDDD You just run, because this is peaceful.")
elif choosec=="y":
  typingPrint("You run over to the front, where a couple people are handing out posters.")
  typingPrint("You grab one quickly and start following the people in front of you.")
  typingPrint("Suddenly, one firefighters with a hose\nstarts blasting you and your fellow friends.")
  chooseca = typingInput("Do you want to: Fight them(x) or run away(y)")
  if chooseca == "x":
    typingPrint("NO. YOU DO NOT ATTACK BC THIS IS A PEACEFUL PROTEST")
    typingPrint("Moving on...")
  elif chooseca=="y":
    typingPrint("Good job! :DDDDDD You just run, because this is peaceful.")
typingPrint("Good job. You are good.")

typingPrint("After the march, a few of your friends invite you to the diner as a celebration.")
typingPrint("At the diner, you find a few other people talking about\nthe upcoming diner sit-in that is happening.")
geez = typingInput("Would you like to join?(y/n) > ")
if geez == "y":
  typingPrint("You decide to participate, like the patriotic man you are.")
else:
  typingPrint("You go anyway >:)")
time.sleep(2)
clearScreen()

'''
  _________                               _____         _________.__  __    .__        
 /   _____/ ____  ____   ____   ____     /  |  |  /\   /   _____/|__|/  |_  |__| ____  
 \_____  \_/ ___\/ __ \ /    \_/ __ \   /   |  |_ \/   \_____  \ |  \   __\ |  |/    \ 
 /        \  \__\  ___/|   |  \  ___/  /    ^   / /\   /        \|  ||  |   |  |   |  \
/_______  /\___  >___  >___|  /\___  > \____   |  \/  /_______  /|__||__|   |__|___|  /
        \/     \/    \/     \/     \/       |__|              \/                    \/ 
'''

typingPrint("You arrive at the diner, anticipation lingering around.")
typingPrint("You sit down, nervous of who would interrupt.\n")
typingPrint("After a while of sitting around and recieving weird looks,")
typingPrint("a man finally ")
