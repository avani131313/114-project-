a = 33
b = "33"
if b > a:
    print("b is greater than a")
elif a == b:
    print("a and be are equal")
    
#output of the above code will be an error since a is an integer while b is a string
#TypeError: '>' not supported between instances of 'str' and 'int'