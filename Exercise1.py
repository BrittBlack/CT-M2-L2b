#1. Nested Decisions:The Adventure Game
#
#
#
#Task 1: Code Correction

place = input("Choose a place: forest or cave? ")
action = input("climb a tree or cross a river? ")
action2 = input("light a torch or proceed in the dark? ")

if place == "forest":
    if action == "climb a tree":
        print("You found a bird's nest!")
    else:
        print("You found a boat!")
    
    if action2 == "light a torch": #Task 2: Setting the Scene
            print("You found a bug!")
    else:
        print("You can't see a thing in the dark.")
 
elif place == "cave":
     print("You find a hidden treasure!")


 
