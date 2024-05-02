#2 Quick Decisions: The Event Planner
#Task 1: Code Correction
#
#
#
attendees = int(input("Enter number of attendees: "))
food_preference = input("Type of food for event: (vegetarian/other) ")
print("large hall") if attendees > 100 else print("conference room")
print("projector") if attendees > 100 else print("audio system")
if food_preference == "vegetarian":
    print("Try Veggie Delight Caterers.")
else:
    print("Try Gourmet Meals Caterers.")

