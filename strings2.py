parrot = "Norwegian Blue"

print(parrot)

print(parrot[3])
print(parrot[4])
print(parrot[9])
print(parrot[3])
print(parrot[6])
print(parrot[8])

print()

print(parrot[-1])  #last char
print(parrot[-14]) #First char

print()

print(parrot[-11])
print(parrot[-10])
print(parrot[-5])
print(parrot[-11])
print(parrot[-8])
print(parrot[-6])

print()

print(parrot[3 - 14])
print(parrot[4 - 14])
print(parrot[9 - 14])
print(parrot[3 - 14])
print(parrot[6 - 14])
print(parrot[8 - 14])

print()

#parrot = "Norwegian Blue"
print(parrot[0:6]) # Norweg upto but not including index 6

print(parrot[3:5])
print(parrot[0:9])
print(parrot[:9])

print()

print(parrot[10:14])
print(parrot[10:]) #same

print()

print(parrot[:6])
print(parrot[6:])

print(parrot[:6] + parrot[6:])

print(parrot[:])

print(parrot[-4:2]) #prints nothing, cannot go backwards
print(parrot[-4:-2]) #Bl
print(parrot[-4:12]) #Bl

print(parrot[-14:-8]) #Norweg
#string slicing steps
print()
print(parrot[0:6:2]) #Nre
print(parrot[0:6:3]) #Nw

number = "9,223;372:036 854,775;807"
print(number[1::4])
seperators = number[1::4]
print(seperators)

values = "".join(char if char not in seperators else " " for char in number).split()
print([int(val) for val in values])

number = "9,223,372,036,854,775,807"
print(number[1::4]) #,,,,,,

print()

test = "10:T,20:B,15:F,34:S"
print(test[::5])
print(test[::-1])