import time

car = "🚗"
carnum = 1
hits = 15
funamm = 1
points = 0
rep = 0
income = 0
#mp3 = mutagen.mp3.MP3("olo.mp3")

def clear():
    print("a" + "\n" * 100)

def shop():
    global car
    global carnum
    global hits
    global funamm
    global points
    global key
    global income
    clear()
    sel = input(f"B to buy microsoft OR buy bill gates' house\nC to buy better car ({str(1000 * carnum)} Funny points)\nM to gain more Funny points per minor car mistake({str(50 * carnum * funamm)} Funny points)\nS to shorten the amount of hits per minor car mistake({str(10 * carnum * abs((hits - 1)-(15*carnum)))} Funny points)\nE to escape\n")
    if sel.lower() == "c":
        if points >= 1000 * carnum:
            if carnum >= 7:
                print("You already have the best car!")
                time.sleep(1)
            else:
                carnum += 1
                points -= 1000 * carnum
                key = rep + 1
        else:
            print("You don't have enough Funny points!")
            time.sleep(1)
    elif sel.lower() == "b":
        sel = input("Press B to buy bill gates' house (63m Funny points)\nPress M to buy Microsoft (2t Funny points)")
        if sel.lower() == "b":
            if points >= 63000000:
                print("You now own bill gates's house! (you get nothing lol)")
            else:
                print("You don't have enough Funny points!")
        elif sel.lower() == "m":
            if points >= 2000000000000:
                print("You now own Microsoft")
    elif sel.lower() == "s":
        if points >= 10 * carnum * abs((hits - 1)-(15*carnum)):
            if hits >= 1:
                hits -= 1 
                #pg.mixer.init(frequency=lol.info.sample_rate + soundlen)
                points -= 10 * carnum * abs((hits + 1)-(15*carnum))
            else:
                print("You are at the minimum amount of hits!")
                time.sleep(1)
        else:
            print("You don't have enough Funny points!")
            time.sleep(1)
    elif sel.lower() == "m":
        if points >= 50 * carnum * funamm:
            funamm += 1
            points -= 50 * carnum * funamm
        else:
            print("You don't have enough Funny points!")
            time.sleep(1)
    elif sel.lower() == "e":
        return
    else:
        print("That is not a valid selection!")
        time.sleep(1)

#pygame.mixer.init(frequency=mp3.info.sample_rate)
#pygame.mixer.music.load("olo.mp3") 

def passive_income():
    global points
    global income
    time.sleep(1)
    points += income


while True:
    clear()
    if carnum == 2 and key == rep:
        car = "🚘"
        hits = 15
        hits *= carnum
        funamm *= carnum
    elif carnum == 3 and key == rep:
        car = "🚓"
        hits = 15
        hits *= carnum
    elif carnum == 4 and key == rep:
        car = "🚔"
        hits = 15
        hits *= carnum
    elif carnum == 5 and key == rep:
        car = "🚋"
        hits = 15
        hits *= carnum
    elif carnum == 6 and key == rep:
        car = "🚃"
        hits = 15
        hits *= carnum
    elif carnum == 7 and key == rep:
        car = "🏎"
        hits = 15
        hits *= carnum
    sel = input(f"Funny points:{points}\nCar:{car}\ns for shop\nenter for minor car mistake\n")
    if sel.lower() == "s":
        shop()
    if sel == "":
        # lol.play()
        clear()
        for x in range(hits):
            clear()
            EOF_handle = input(f"Hits:{str(x)}/{hits}")
        points += funamm
    rep += 1