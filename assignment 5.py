# -*- coding: utf-8 -*-
"""
Madeline Zaiontz 1837445
COSC 1306
Assignment #5
"""

def num(avg):
    if x>= 90 :
        grade = "A"
    elif 90 > x >= 86:
        grade = "A-"
    elif 86 > x >= 82:
        grade = "B+"
    elif 82 > x >= 78:
        grade = "B"
    elif 78 > x >= 74:
        grade = "B-"
    elif 74 > x >= 70:
        grade = "C+"
    elif 70 > x >= 66:
        grade = "C"
    elif 66 > x >= 62:
        grade = "C-"
    elif 62 > x >= 58:
        grade = "D+"
    elif 58 > x >= 54:
        grade = "D"
    elif 54 > x >= 50:
        grade = "D-"
    else:
        grade = "F"
        
    return grade

 
def almost():
    if grade == "A" :
        print("no higher grade")
    elif grade == "A-" :
        print("You are" , 90 - x , "points away from an A")
    elif grade == "B+":
        print("You are" , 86 - x , "points away from an A-")
    elif grade == "B":
        print("You are" , 82 - x , "points away from a B+")
    elif grade == "B-":
        print("You are" , 78 - x , "points away from a B")
    elif grade == "C+":
        print("You are" , 74 - x , "points away from a B-")
    elif grade == "C":
        print("You are" , 70 - x , "points away from a C+")
    elif grade == "C-":
        print("You are" , 66 - x , "points away from a C")
    elif grade == "D+":
        print("You are" , 62 - x , "points away from a C-")
    elif grade == "D":
        print("You are" , 58 - x , "points away from a D+")
    elif grade == "D-":
        print("You are" , 54 - x , "points away from a D")
    else:
        print("You are" , 50 - x , "points away from a D-")
  
    
     

x = float(input("Please enter a final average: "))

grade = num(x)

print("Congratulations, you earned a/an", grade)


almost()
print(40*"=")


