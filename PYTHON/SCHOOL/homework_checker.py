
## This is the homework checker script to verify the math homework

a    = int( input("     Enter first number: "))
b    = int( input("    Enter second number: "))
ans2 = int( input("      Enter your answer: "))

ans1 = a - b

##ans2 = 2122948830

if (ans1 - ans2) == 0:
    print ("Gaby, you rock!")
else:
     print ("Gaby, keep working on it!     ")
     print ("You entered : ",ans2)
     print ("The answer  : ",ans1)
     
     
