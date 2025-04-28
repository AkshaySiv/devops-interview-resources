"""
Write a Python function checkinventorylist(inventorylist) 
that checks whether the given list of strings is sorted alphabetically (case-insensitive).
The function should return True if the list is sorted in ascending order and False if it is not.
"""

def checkinventorylist(inventorylist):
    # print (sorted (inventorylist))
    # return sorted (inventorylist) == inventorylist
    flag=False
    for i in range(0,len(inventorylist)-1):
         if inventorylist[i].lower() < inventorylist[i+1].lower():
            flag=True
         else:
            flag=False
            break
    return flag

inventorylist = ["canDy","corn","piece"]

print (checkinventorylist(inventorylist))