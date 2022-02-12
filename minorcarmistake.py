import time
import json
import emoji_data_python
import threading
f = open("minorcarmistake/save.txt", "r")

car = emoji_data_python.unified_to_char("1F697")
carnum = 1
hits = 15
funamm = 1
points = 0
rep = 0
key = 0

try: 
    read = json.loads(f.read())
    carnum = read["carnum"]
    hits = read["hits"]
    funamm = read["funamm"]
    points = read["points"]
finally:
    pass


def clear():
    print("a" + "\n" * 100)

def save():
    f = open("minorcarmistake/save.txt", "w")
    f.write('{"carnum":' + str(carnum) + ', "hits":' + str(hits) + ', "funamm":' + str(funamm) + ', "points":' +  str(points) + '}')
    print("Game autosaved!")
    savegame = threading.Timer(240, save)
    savegame.start()


def shop():
    global car
    global carnum
    global hits
    global funamm
    global points
    global key
    global savegame
    clear()
    savegame = threading.Timer(5.0, save)
    savegame.start()
    sel = input(f"B to buy microsoft OR buy bill gates' house\nC to buy better car ({str(1000 * carnum)} Funny points)\nM to gain more Funny points per minor car mistake({str(50 * carnum * funamm)} Funny points)\nS to shorten the amount of hits per minor car mistake({str(10 * carnum * abs((hits - 1)-(15*carnum)))} Funny points)\nE to escape\n")
    if sel.lower() == "c":
        if points >= 1000 * carnum:
            if carnum >= 7:
                print("You already have the best car!")
                time.sleep(1)
            else:
                points -= 1000 * carnum
                carnum += 1
                key = rep + 1
        else:
            print("You don't have enough Funny points!")
            time.sleep(1)
    elif sel.lower() == "b":
        sel = input("Press B to buy bill gates' house (63m Funny points)\nPress M to buy Microsoft (2t Funny points)")
        if sel.lower() == "b":
            if points >= 63000000:
                print("You now own bill gates's house! (you get nothing lol)")
                time.sleep(1)
            else:
                print("You don't have enough Funny points!")
                time.sleep(1)
        elif sel.lower() == "m":
            if points >= 2000000000000:
                print("You now own Microsoft")
                time.sleep(1)
            else:
                print("You don't have enough Funny points!")
                time.sleep(1)
    elif sel.lower() == "s":
        if points >= 10 * carnum * abs((hits - 1)-(15*carnum)):
            if hits >= 1:
                hits -= 1 
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


while True:
    clear()
    if carnum == 2 and key == rep:
        emoji_data_python.unified_to_char("1F698")
        if rep != 0:
            hits = 15
            hits *= carnum
            funamm *= carnum
    elif carnum == 3 and key == rep:
        car = emoji_data_python.unified_to_char("1F693")
        if rep != 0:
            hits = 15
            hits *= carnum
            funamm *= carnum
    elif carnum == 4 and key == rep:
        car = emoji_data_python.unified_to_char("1F697")
        if rep != 0:
            hits = 15
            hits *= carnum
            funamm *= carnum
    elif carnum == 5 and key == rep:
        car = emoji_data_python.unified_to_char("1F68B")
        if rep != 0:
            hits = 15
            hits *= carnum
            funamm *= carnum
    elif carnum == 6 and key == rep:
        car = emoji_data_python.unified_to_char("1F683")
        if rep != 0:
            hits = 15
            hits *= carnum
            funamm *= carnum
    elif carnum == 7 and key == rep:
        car = emoji_data_python.unified_to_char("1F3CE")
        if rep != 0:
            hits = 15
            hits *= carnum
            funamm *= carnum    
    sel = input(f"SAVE to save game\nFunny points:{points}\nCar:{car}\ns for shop\nenter for minor car mistake\n")
    if sel.lower() == "s":
        shop()
    if sel == "":
        # lol.play()
        clear()
        for x in range(hits):
            clear()
            EOF_handle = input(f"Hits:{str(x)}/{hits}")
        points += funamm
    elif sel.lower() == "save":
        f = open("minorcarmistake/save.txt", "w")
        f.write('{"carnum":' + str(carnum) + ', "hits":' + str(hits) + ', "funamm":' + str(funamm) + ', "points":' +  str(points) + '}')
    rep += 1
