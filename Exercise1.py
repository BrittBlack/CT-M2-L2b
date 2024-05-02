#1. Nested Decisions:The Adventure Game
#
#
#
#Task 1: Code Correction
#1st Attempt
# place = input("Choose a place: forest or cave? ")
# action = input("climb a tree or cross a river? ")
# action2 = input("light a torch or proceed in the dark? ")

# if place == "forest":
#     if action == "climb a tree":
#         if action2 == "light a torch":
#     print("You found a bird's nest!")
#           print("You found a bug!")
    
#     else:
#         print("You found a boat!")
    
#     if action2 == "light a torch": #Task 2: Setting the Scene
          
#     else:
#         print("You can't see a thing in the dark.")
 
# elif place == "cave":
#      print("You find a hidden treasure!")
#
#
#
#2nd attempt


place = input("Choose a place: forest or cave? ")

if place == "forest":
    action = input("climb a tree or cross a river?")
    if action == "climb a tree":
        print("You found a bird's nest!")
    if action == "cross a river":
        print("You found a boat!")
elif place == "cave":
    print("You find a hidden treasure!")


 
