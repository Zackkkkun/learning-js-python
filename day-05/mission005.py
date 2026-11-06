#Specific Exception Handling

try:
   age = input("age? ")
   age = int(age)
   if age>=18:
      print("access granted")
   else:
      print("access denied")
except:
   print("invalid age")
except ValueError:
    print("wrong data type entered")