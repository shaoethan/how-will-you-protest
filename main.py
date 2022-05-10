import time,os,sys

def typingPrint(text):
  for character in text:
    sys.stdout.write(character)
    sys.stdout.flush()
    time.sleep(0.05)
  print()
  
def typingInput(text):
  for character in text:
    sys.stdout.write(character)
    sys.stdout.flush()
    time.sleep(0.05)
  value = input()  
  return value  
  
def clearScreen():
  os.system("clear")

'''
█▀ █▀▀ █▀▀ █▄░█ █▀▀   ▄█ ▀   █ █▄░█ ▀█▀ █▀█ █▀█ █▀▄ █░█ █▀▀ ▀█▀ █ █▀█ █▄░█
▄█ █▄▄ ██▄ █░▀█ ██▄   ░█ ▄   █ █░▀█ ░█░ █▀▄ █▄█ █▄▀ █▄█ █▄▄ ░█░ █ █▄█ █░▀█
'''

print("")


print()
typingPrint("Created by Ethan Shao")
print()

time.sleep(1)
typingPrint("Welcome to How will you protest?")
time.sleep(1)
print()
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
      choose1ca = typingPrint("Would you like to put the clothes on(x) or wait(y)\n > ")
      if choose1ca == "x":
        typingPrint("You rummage around and find a dusty suit that looks nice.")
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
'''

clearScreen()
typingPrint("You make your way to your job, a construction worker working on the minimum wage of $1.15 an hour.")
typingPrint("As you enter the site, you see your friends and co-workers already getting ready, and your work pal, Michael comes up to you.")
typingPrint("M: Yo Johnson, come help me with the load,")
