# Elementi
from random import randint
answer=input('Spreman za igru? (da/ne):')

# pomeranje igraca 
moves=["vatra", "voda", "zemlja", "list", "vazduh"]
if answer.lower()=='da':
    while True:
        computer = moves[randint(0,3)]
        igrac =input("vatra, voda, zemlja,list or vazduh (or zavrsi igru) ")
        if igrac == "zavrsi igru":
            print("Vidimo se drugi put.")
            break
        elif igrac == computer:
            print("Izjednaceno")
            break
        elif igrac == "voda":
            if computer == "vatra":
                print("Pobedio si!", igrac, "pobedjuje", computer)
                break
        elif igrac == "voda":
            if computer == "vazduh":
                print("Pobedio si!", igrac, "pobedjuje", computer)
                break
        elif igrac == "voda":
            if computer == "list":
                print("Izgubio si!",computer, "pobedjuje", igrac)
                break
        elif igrac == "vatra":
            if computer == "list":
                print("Pobedio si!",igrac, "pobedjuje", computer)
                break
        elif igrac == "vatra":
            if computer == "vazduh":
                print("Pobedio si!",igrac, "pobedjuje", computer)
                break
        elif igrac == "vatra":
            if computer == "voda":
                print("Izgubio si", computer, "pobedjuje", igrac)
                break
        elif igrac == "vatra":
            if computer == "zemlja":
                print("Izgubio si", computer, "pobedjuje", igrac)
                break
        elif igrac == "zemlja":
            if computer == "vatra":
                print("Pobedio si!",igrac, "pobedjuje", computer)
                break
        elif igrac == "zemlja":
            if computer == "list":
                print("Pobedio si!",igrac, "pobedjuje", computer)
                break
        elif igrac == "zemlja":
            if computer == "vazduh":
                print("Izgubio si", computer, "pobedjuje", igrac)
                break
        elif igrac == "list":
            if computer == "voda":
                print("Pobedio si!",igrac, "pobedjuje", computer)
                break
        elif igrac == "list":
            if computer == "vatra":
                print("Izgubio si", computer, "pobedjuje", igrac)
                break
        elif igrac == "list":
            if computer == "zemlja":
                print("Izgubio si", computer, "pobedjuje", igrac)
                break
        elif igrac == "vazduh":
            if computer == "zemlja":
                print("Pobedio si!",igrac, "pobedjuje", computer)
                break
        elif igrac == "vazduh":
            if computer == "list":
                print("Pobedio si!",igrac, "pobedjuje", computer)
                break
        elif igrac == "vazduh":
            if computer == "voda":
                print("Izgubio si", computer, "pobedjuje", igrac)
                break
        elif igrac == "vazduh":
            if computer == "vatra":
                print("Izgubio si", computer, "pobedjuje", igrac)
                break