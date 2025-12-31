def addition (a, b):
    c = a+b
    print (c)

addition(2, 4)


def table (x, y):
    z = x*y
    print(z)

table(9, 9)


def students (Name, Roll_no, Class):
    print(f"I'm {Name}. My roll number is {Roll_no} and I studies in {Class}." ) 

students("Salman", "1045", "10th")




def Percentage (math, physics, chemistry, urdu, english):
    c = (math+physics+chemistry+urdu+english)/500*100
    d = c
    print (f"Your total marks percentage is {d}.")

Percentage(23, 55, 66, 34, 99)



def Traffic(color):
    if color.lower() == "green":
        print("Go")
    elif color.lower() == "yellow":
        print("Slow")
    elif color.lower() == "red":
        print ("Stop")
    else:
        print("invalid")

user_color = input ("Enter your color: ")
result = Traffic(user_color)
