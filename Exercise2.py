#2 Quick Decisions: The Event Planner
#Task 1: Code Correction
#
#
#
# attendees = int(input("Enter number of attendees:  "))

# if attendees > 100:
#     print("large hall")
#     if attendees < 100:
#         print("conference room")
    

attendees = int(input("Enter number of attendees: "))
print("large hall") if attendees > 100 else print("conference room")
