#THE INVALID INPUT TEST

try:
   age = input("age? ")
   age = int(age)
   if age>=18:
      print("access granted")
   else:
      print("access denied")
except:
   print("invalid age")