#comprasion oprAters
#print(13>9)
#print(18==18)
#print(12<3)

"""
a=74
a+=5
print(a)
a-=7
print(a)"""

"""
b=15
b-=10
print(b)
b+=15
print(b)"""


#Short Hand Operators, Assignment Operators
#+=,-=,*=,%=,**=,//=,/=

"""
a=10
a /= 10
print(a)"""

"""
a=10
a //= 10
print(a)"""

"""
a=10
a **= 10
print(a)"""

"""
a=10
a -= 10
print(a)"""







'''
#These are used to compare two values.
# >Greater than a>b
 
#< Less than a < b
  
# >=Greater than or equal to a>=b
#  == Equal to  a == b

# <=Less than or equal to a<=b
# != Not equal to a != b
'''

#print(34<10)
#print(10<34)
#print(37>10)
#print(34==34)
#print(34==10)
#print(32<=10)
#print(34>=10)
#print(34<=34)
#print("ABC>ABD")
#print(ABC<ABD)
#print (0and 2)



#logical opraters 

#or
#Return False only if both the values are False.
# If both the values are true then it will pick the left value.

"""
left  | rihgt  | output  |
 false | true   | true    |
 true  | false  | true    |
 true  | true   | true    |
 false | false  | false   | 
"""

#print(60 or 0)
#print (""or -13)
#print (1 or True)

#and 
#Return False only if both the values are False.
# If both the values are true then it will pick the right value.
'''left  | rihgt  | output   |
 false | true   | false    |
 true  | false  | false    |
 false | false  | false    | 
 true  | true   | true     |'''

#print (0and 2)
#print  (2and 0)
#print  (13and 20) 

#print(45 and 67 or 13 and 45 and 12)
#print (not False) 
#print (not True )

"""
#membership operators
a= " i live in india"
print("india"  in a) """

#identity operators
"""
user=input("enter your username ")
if user =="admin" or user=="Admin" or user=="ADMIN":
    print("welcome admin")
else:
    print("Invalid username")

    """

"""
ch=input("enter your word  ")
if ch in "aeiouAEIOU":
    print("It is a vowel")
else: print("it is not a vowel") 

"""
"""
#match case  operators
a=input("enter your digits")
match a:
   case "1234":
     print("open")
   case "4321":
     print("ok open")
   case "1111":
     print("than okay")
   case _:
     print("default")
  """

"""
char=input("enter your word ")
match char in "aeiouAEIOU" :
    case True:
        print("it is a vowel")
    case False:
        print("it is not a vowel")

"""

#task solve by  if else:====>>

"""a=int(input("enter a first value"))
b=int(input("enter a second value"))
c=input("enter a opraters")

if c=="+":
    print(a+b)
elif c=="-":
    print(a-b)
elif c=="*":
    print(a*b)
elif c=="/":
    print(a/b)
elif c=="%":
    print(a%b)
elif c=="**":
    print(a**b)
elif c=="//":
    print(a//b)

else:
    print("Invalid operator") 
    """
# task solve by  match case:===>
"""
a=int(input("enter a first value"))
b=int(input("enter a second value"))
c=input("enter a opraters")
match c:
    case "+":
        print(a+b)
    case "-":
        print(a-b)
    case "*":
        print(a*b)
    case "/":
        print(a/b)
    case "%":
        print(a%b)
    case "**":
        print(a**b)
    case "//":
        print(a//b)
    case _:
        print("wrong  operator")  

        """