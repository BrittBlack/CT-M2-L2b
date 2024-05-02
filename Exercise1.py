#1. Nested Decisions:The Adventure Game
#
#
#
#Task 1: Code Correction

# place = input("Choose a place: forest or cave? ")

# if place = "forest":
#     action = input("climb a tree or cross a river?")
#     if action = "climb a tree":
#         print("You found a bird's nest!")
#     else action = "cross a river":
#         print("You found a boat!")
# elif place = "cave":
#     print("You find a hidden treasure!")



place = input("Choose a place: forest or cave? ")

if place == "forest":
    action = input("climb a tree or cross a river?")
    if action == "climb a tree":
        print("You found a bird's nest!")
        if action == "cross a river":
            print("You found a boat!")
elif place == "cave":
    action2 = input("light a torch or proceed in the dark?")
    pass    
    if action2 == "light a torch":
        print("You can see.")
        pass
        if action2 == "proceed in the dark":
            print("You cannot see.")
else:
     print("You find a hidden treasure!")      


