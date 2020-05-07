"""
Authors:
Logan Kilfoy,
Seth

INTRODUCTION TO LOOPS

The goal of this program is to print the following using a for loop

*
**
***
****
*****
******
*******

"""
# for loop example

# for i in range(1,6):
#     print(i)

# fruits = ["apple", "banana", "cherry"]
# for x in fruits:
#   print(x)
#   print(x[0])

# print(fruits[0][0])

# stars = ["*", "**", "***", "****"]

# for i in range(0,4):
#     print(i)
#     print(stars[i])

# for star in stars:
#     print(star)

# for i in range(1,6):
#     print(i)
    # print(i * "*")
# appstr = "Apple"
# x = appstr[0]

# temp = ""

# for char in "logAn":
#     if(char != "A"):
#         temp += char

# print(temp)
# print("outside the for loop")

star_amount = input("Enter: ")
star_amount_number = int(star_amount)

ascending = input("Ascending?(y/n): ")
if (ascending == 'y'):
    justification = input("Enter justification(r/l): ")
    if (justification == "r"):
        for i in range(1, star_amount_number + 1):
            print(((star_amount_number - i) * " ") +  (i * "*"))
    else:
        for i in range(1, int(star_amount) + 1):
            print(i * "*")
    
else: 
    justification = input("Enter(r/l): ")
    if (justification == "r"):
        for i in range(star_amount_number, 0, -1):
            print(((star_amount_number - i) * " ") +  (i * "*"))
    else:
        for i in range(star_amount_number, 0, -1):
            print(i * "*")