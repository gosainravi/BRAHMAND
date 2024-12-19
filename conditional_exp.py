#conditional Expression method
#Chapter -6
#if, else, elif
##condition: This is the expression that is evaluated to True or False.
#value_if_true: The value to return if the condition is True.
#value_if_false: The value to return if the condition is False.

# jo input hota ha wo string output karta hai to hamko typecast 
# karna padega integer banae ke liye

age = int(input("Enter your Age"))

if (age>=18) : #: colon means we have entered in to indentation meanse spacing 
    print("You are above the age of concent")
    print("Good for you")
    print("enjoy yourself")
    
else : 
    print("ghal ja mele pyale bache")
    
    
#if ki condition true hogi to else ki condition ignore hogi
#else ki condition true hogi to if ki condition ignore hogi

#Elif condition (multiple condition)

age = int(input("Enter your Age"))

if (age>=18) : #: colon means we have entered in to indentation meanse spacing 
    print("You are above the age of concent")
    print("Good for you")
    print("enjoy yourself")

elif(age<0) :
    print("Ye mat Mat karo negiative value nahi allowed hain")

else : 
    print("ghal ja mele pyale bache")