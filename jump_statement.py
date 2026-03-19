# break -> break statement help us to break the flow of a loop when it's executed
# continue -> continue statement is a jump statement that can help us to skip a certain part of the code
# exit() -> Exit function in python help us to terminate the program based on any condition and it also sends a signal back to the computer for analytics.


# task
# Sum of Even Numbers: Write a program that asks the user to enter a positive integer N. 
# Use a while loop to iterate from 1 up to N.
# Inside the loop, use an if statement to check if the current number is odd. 
# If it is, add it to a running total. Finally, print the sum of all odd numbers up to N.











# 
# sum=0

# while True:
#     price=int(input("enter a number "))
#     sum+=price
#     print(sum)




# #break
# sum=0
# while True:
#     price=int(input("enter a number "))
#     if price < 0:
#         break
#     sum +=price
#     print(sum)




counter=1
while counter <= 3:
    username=input("enter your username ")
    password=input("enter your password ")
    if username=="admin" and password== "1234":
     print("password accepect")
    break
else:
    print("inccrect password:try again")

    counter += 1

if  counter == 4 :
    print("account locked")
























































