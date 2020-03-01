import winsound
import sys
MasterK = 0
import random
l = 'loading...'
zipline = 0
pistol = 0
missions = 0
money = 0

print('You are agent 87 An Agent for the NIK Its Time for your training mission')
print("you have to get info from the top of a building")
answer = input("do you accept the Mission? ")
if answer.lower().strip() == 'yes':
    print(l)
elif answer.lower().strip() == 'no':
    print("go you baby")
winsound.PlaySound("Nes", winsound.SND_FILENAME)
print("you arrive through the window with a glass cutter ")
answer = input('you see a guard do you go past the guard or do you attack (Past or attack) ')
if answer.lower().strip() == 'past':
    print('you go past')
elif answer.lower().strip() == 'attack':
    print('you sneakily take him down')

answer = input(
    'you find the room but another guard is there.but there seems to be another way through the vent(Vent or Attack?) ')
if answer.lower().strip() == 'vent':
    print('you steal the data')
    print(l)
    winsound.PlaySound("Nes", winsound.SND_FILENAME)
elif answer.lower().strip() == 'attack':
    if print((random.sample(range(1, 2), 1))) == 1:
        print('You take out the guard')
    elif print((random.sample(range(1, 2), 1))) == 2:
        exit('game over')

answer = input('You have the data! How do you escape Roof or Front door ')
if answer.lower().strip() == 'roof':
    missions = 1
    money = 20000
    print('money:', money)
    print('You Escaped!')
elif answer.lower().strip() == 'front door':
    if print((random.sample(range(0, 3), 0))) == 1:
        missions = 1
        print('You Escaped!')
    elif print((random.sample(range(0, 3), 0))) == 2:
        print("A guard realizes that your're not supposed to be there ")
        exit('Game Over')

if missions == 1:
    answer = input('Do you go to the next mission ')
    if answer.lower().strip() == 'yes':
        print(l)
        winsound.PlaySound("Nes", winsound.SND_FILENAME)
    elif answer.lower().strip() == 'no':
        exit('goodbye')
else:
    exit('Try again')
    # Mission2 #

print('The NIK Gives you another mission')
print('they want you to Setup an backdoor So they can get in to bank & Trust ')
answer = input('Do You Accept ')
if answer.lower().strip() == 'yes':
    print(l)
    winsound.PlaySound("Nes", winsound.SND_FILENAME)
elif answer.lower().strip() == 'no':
    print("your're FIRED")
    exit('Game over')

answer = input('You arrive in a taxi in a worker outfit where do you go?(offices or bathroom) ')
if answer.lower().strip() == 'bathroom':
    print('you change outfits! and you go to the next floor')
    print(l)
    winsound.PlaySound("Nes", winsound.SND_FILENAME)
elif answer.lower().strip() == 'office':
    print('you arrive')
    print('and Change into a new outfit')

answer = input('Do you Steal the data Or do you steal some items? ')
if answer.lower().strip() == 'items':
    money = 120000
    print('you steal some valuable items')
    print('Cash:', money)
elif answer.lower().strip() == 'data':
    print('You take the data')

answer = input("The worker's realize that your're not supposed to be there.do you attack a guard and steal the outfit, or do you escape through the vents? (attack or vent) ")
if answer.lower().strip() == 'attack':
    print('you take out a guard and escape')
    missions = 2
elif answer.lower().strip() == 'vent':
    exit(print('You fell trough the vent and got caught'))
                #Mission 3#
if money == 100000:
    print('The Nik Send you on another mission')
    print(l)
    winsound.PlaySound("Nes", winsound.SND_FILENAME)

elif money <= 100000:
    exit(print('you need more money'))

print('the NIK lets you buy some new equipment')
answer = input('do you buy a pistol or a zipline? ')
if answer.lower().strip() == 'pistol':
    pistol = 1
    money = 20000
    print(l)
    winsound.PlaySound("Nes", winsound.SND_FILENAME)
elif answer.lower().strip() == 'Zipline':
    Zipline = 1
    print(l)
    winsound.PlaySound("Nes", winsound.SND_FILENAME)
    money = 20000

answer = input('You have to save a Hostage!Do you Run or do you sneak around ')
if answer.lower().strip() == 'run':
    print(l)
    winsound.PlaySound("Nes", winsound.SND_FILENAME)
elif answer.lower().strip() == 'sneak':
    print('WE DONT HAVE TIME')

answer = input('you find the hostage and some items ')
if answer.lower().strip() == 'items':
    money = 200000
    print('your items will be calculated at the end of mission.NOW GO')
    print('you get the hostage!')
elif answer.lower().strip() == 'hostage':
    print('You Get the hostage!')

if zipline == 1:
    print('you escape through the zipline')

elif pistol == 1:
    print('You go down the stairs and shoot everyone')

missions = 2
print('Mission accomplished')
print('Cash:', money)

            #Mission 4#

print('Its time for a new mission')
print('The NIK wants you to Spend 100000$ towards gadgets for your final mission')
answer = input('What Do you want (A New Rifle or a new sneaking suit) ')
if answer.lower().strip() == 'sneaking suit':
    ss = 1
    money = 000000
    print('You Have No money left')
    print(l)
    winsound.PlaySound("Nes", winsound.SND_FILENAME)
elif answer.lower().strip() == 'rifle':
    rifle = 1
    money = 0
    print('You have no cash left')
    print(l)
    winsound.PlaySound("Nes", winsound.SND_FILENAME)

           #Mission 5#
print('you are send to rob bank and trust')
answer = input('You arrive in a Limo with a gun and a sneaking suit Do you enter through the front door or a window ')
if answer.lower().strip() == 'window':
    print('you make it in!')
elif answer.lower().strip() == 'front door':
    exit(print('A Guard Finds out who you are'))

answer = input('Where do you get a keycard? a guard or the owner ')
if answer.lower().strip() == 'owner':
    MasterK == 1
    print('you got the master keycard')
elif answer.lower().strip() == 'guard':
    print('You got a keycard')

answer = input('Do you open the vault? ')
if answer.lower().strip() == 'no':
    print('you realize that there is lazer guard')
    print('but then you get through ')
elif answer.lower().strip() == 'yes':
    exit(print('the alarm is tripped'))

answer = input('Do you take all of it? ')
if answer.lower().strip() == 'yes':
    money = 1000000
    print('you ESCAPE!')
elif answer.lower().strip() == 'no':
    money = 500000
    exit(print('THE NIK FIRE YOU'))



print('Credits')
print('Desgner:', 'Lpokimo')
print('Programer:', 'Lpokimo')
print('©L  M')
#Bonus Level#
if money == 1000000:
    if MasterK == 1:
        if ss == 1:
            if zipline == 1:
                print(l)
else:
    exit(print('goodbye'))

print('The CEO of the NIK fires you And with everything YOU did They are taking over the world')
answer = input('Are you ready for your final Mission Agent 87 ')
if answer.lower().strip() == 'yes':
    print(l)
    winsound.PlaySound("Nes", winsound.SND_FILENAME)
elif answer.lower().strip() == 'no':
    exit(print('WOW!!'))

answer = input('You Get in with your Zipline Do you go to the server room or the Head Office ')
if answer.lower().strip() == 'sever room':
    print('you Emplant A Virus in the severs')
    print(l)
    winsound.PlaySound("Nes", winsound.SND_FILENAME)
elif answer.lower().strip() == 'head office':
    print('You Find CEO but he doesnt reconize you')

answer = input('Do you Kill the CEO? ')
if answer.lower().strip() == 'yes':
    exit('CONGRATS YOU GOT THE TRUE ENDING!!!!!')
elif answer.lower().strip() == 'no':
    print('You Saved the world without Murder ')

    print("True Credits")
    print("programmer:", "Lpokimo")
    print('Music:' "Konami")
