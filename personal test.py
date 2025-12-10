'''
a=float(input("Enter 1st number: "))
b=float(input("Enter 2nd number: "))
c=float(input("Enter 3rd number: "))
d=float(input("Enter 4th number: "))
e=float(input("Enter 5th number: "))
f=float(input("Enter 6th number: "))
g=float(input("Enter 7th number: "))
h=float(input("Enter 8th number: "))
i=float(input("Enter 9th number: "))
j=float(input("Enter 10th number: "))
k=float(input("Enter 11th number: "))
l=float(input("Enter 12th number: "))
q=float(input("Enter 13th number: "))
r=float(input("Enter 14th number: "))

Continue = input("Do you want to continue? (yes/y to continue): ")

while Continue.lower() == 'yes' or Continue.lower() == 'y':
    choose = input("Choose an operation (+, -, *, /, %, **, //): ")

    if choose == '+':
        print("Result:", a + b)
    elif choose == '-':
        print("Result:", c - d)
    elif choose == '*':
        print("Result:", e * f)
    elif choose == '/':
        print("Result:", g / h)
    elif choose == '%':
        print("Result:", i % j)
    elif choose == '**':
        print("Result:", k ** l)
    elif choose == '//':
        print("Result:", q // r)
    else:
        print("Invalid operation selected.")

    Continue = input("Do you want to continue? (yes/y to continue): ")
    if Continue.lower() != 'no' and Continue.lower() != 'n':
        print("Thank you for using the calculator. Goodbye!")
    break
'''


'''
a=["apple", "banana", "cherry"]
a=a +["orange"]
print(a)

a.pop(2)
print(a)

a="HI"
b="HI"
print(id(a))
print(id(b))
print(a is not b)

a=['A', 'B', 'C', 'D','B']
while "B" in a:
    a.remove("B")
print(a)
del a[1]
print(a)


a=("apple", "banana", "cherry", "banana",34,56.7,True)
print(len(a))
a+=("orange",)
print(a[-4:-1])
print(a)
print(a[1])
print(a.index("cherry"))
print(a.count("banana"))
for x in a:
    print(x)
print(id(a))

b=tuple(("apple",))
print(b)


x=("HI",23,"32",24)
y=("HELLO",34,"56",45)
(*a,y,z)=x
print(a)
(a,*y,z)=x
print(y)
(a,y,*z)=x
print(z)
y=list(x)
y.append("34")
x=tuple(y)
print(x)
print(type(y))
print(type(x))


x=frozenset({"hello",1,True,0,"ORANGE","HI"})
y=frozenset({34,23,45,"hello"})
print(type(x))
print(x)
print(False in x)
print(x)
print(x)
print(y)
print(x)
z={"a","b"}
z.clear()
print(z)
g=x|z
print(x)
print(x.isdisjoint(y))
print(x|y)
print(x^y)
print(x&y)
print(x-y)


x={"KEY":"BREAD","KEY":"NEWBREAD"}
print(type(x))
print(x)
print(x["KEY"])
x["NEWKEY"]="BUTTER"
print(x)
print(x["KEY"],x["NEWKEY"])
for i in x:
    print(i)
for i in x.values():
    print(i)
for i,j in x.items():
    print(i,j)
print(x.keys())

a=20
ID=True
if a>=18:
    if ID:
        print("You can enter the club")
    else:
        print("You cannot enter the club without ID")
else:
    print("You are not old enough to enter the club")


for i in range(1,6,2):
    print(i,end=" ")

print("\nNEW LINE")
a=0
while a<5:
    print(a,end=" ")
    a+=1
'''
