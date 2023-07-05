
#First day

'''
a='efg'
b='abc'
print("a>b",a>b)
print("a<b",a<b)
'''

#11-05-2023

'''
s='mohan is good boy'
print(s[1:5])
print(s[1:5:1])
print(len(s))
'''
'''
l=[10,20,30, 40, 'aman']
print(l)
l.append(5)
print(l)
'''

#error
'''
s={10,20,30}
print(s[0])
'''

'''
s={10,20,30}
print(s.remove(20))
print(s)
'''

'''
d={1:'abc', 2:'def'}
print(d[1])
'''

'''
name=input('enter your name: ')
age=input('enter your age: ')
print(name)
print(age)
print('hello', name, 'your age is', age, 'old')
'''

'''
if x:
    action-1
elif:
    action-2
elif:
    action-3
else:
    action-4
'''   

'''
n1=int(input('enter the number: '))
n2=int(input('enter the number: '))
if n1>n2:
    print('the bigger number is', n1)
else:
    print('the bigger number is', n2)
'''

'''
n=int(input('enter the number: '))
if n>=1 and n<=100:
    print('the number', n, 'is in between 1 and 100')
else:
    print('the number', n, 'is not in between 1 and 100')
'''

'''
l=[10,20,[30,40],50]
print(l)
print(l[0:3])
print(0)
print(l[0:3][2][0])
'''

'''
a=10
b=20
print(a>b)
'''

'''
s='my name is vikram'
print(s)
print(s[0:5])
print(s[2:5])
print(s[0:5])
print(s[3:10:3])
print(s[::2])
'''

'''
s='vicky'
print(s*3)
print(len(s))
'''

'''
n=12.55
print(int(n))
print(int(True))
print(int(False))
'''

'''
n=12
print(float(n))
print(float(True))
print(float(False))
'''

'''
s="this is 'done vikram'"
print(s)
'''

'''
x=[10,20,30,40,50,60,70,80]
print(type(x))
print(len(x))
print(x[2])
print(x[1:2])
print(x[2:2])
print(x[1:-2])
'''

'''
x={10,20,30,40,50}
b=bytes(x)
print(x)
print(b)
print(type(b))
print(b[0])
'''

'''
x={10,20,30,40,50}
b=bytes(x)
print(x)
print(b)
for y in b:
    print(y)
'''

'''
x=[10,20,30,40]
b=bytearray(x)
b[0]=0
for y in b:
    print(y)
print(b)
'''

'''
x=10
y=x
print(id(x))
print(id(y))
'''

'''
s1=[10,20,30,'vicky','hero']
s2=[10,20,30,'vicky','hero']
s2=s2*2
print(s1)
print(s2)
'''

'''
list=[10,20,30] Mutabule
tuple=(10,20,30) In-Mutabule
set={10,20,30} Mutabule
'''

'''
t=(10,20,30,'vikram', 'vicky',40,[50,60])
print(type(t))
print(t)
'''

'''
s={10,20,30,}
print(s.remove(20))
print(s)
'''

'''
d={1:'abc', 2:'def'}
print(d[1])
'''

'''
l=[10,'vikram',True,20,30]
#l1=l[1]
print(l[1])
print(l)
'''

'''
t=(10,20,30,40,50)
print(t[2])
'''

'''
a=range(0,20,2)
for x in a:
    print(x)
'''

'''
for x in range(0,10):
    print(x)
'''

'''
a=10
b=10
print(id(a))
print(id(b))
'''

'''
x=[1,2,3,4]
a=bytes(x)
print(a)
'''

'''
n=range(0,10)
for x in n:
    print(-x)


n=range(-10,0)
for x in n:
    print(x)
'''

'''
n=range(0,20,2)
for x in n:
    if x>10 and x<15:
        print(-x)
'''

'''
l=[10,20,30]
l.append(40)
l.append(50)
l.append(60)
print(l)
''' 

'''
a=[0,1,2,3,4,5,6,7,8,9,10]
print(a[::2])
print(a[::3])
'''

'''
for x in range(0,10):
    if x%2==0:
        print(x)
'''

'''
for x in range(10):
    if x%2==0:
        print(x)
'''


'''
d={}
d[1]='vicky1'
d[2]='vicky2'
d[2]='vicky3'
d['name']='vikram'
print(d)
'''

'''
t=10,20,30,40
print(t)
print(type(t))


t=10
print(t)
print(type(t))
'''

'''
a=10
b=20
print('a+b', a+b)
print('a-b', a-b)
print('a/b', a/b)
print('a*b', a*b)
print('a%b', a%b)
'''

'''
a=10
b=2
print('a value is',a,'b value is', b)
print('a>b', a>b)
print('a<b', a<b)
print('a>=b', a>=b)
print('a<=b', a<=b)
print('a==b', a==b)
'''

'''
a='amon'
b='boy'
print(a>b)
print(a<b)
'''

'''
a=10
b=10.0
print(a==b)
print(a!=b)
'''

'''
a=input('enter value: ')
b=input('enter value: ')
if(a>b):
    print(a,'a value greater then b', b)
elif(a<b):
    print(a,'a value not greater then b', b)
else:
    print('bouth values are equal')
'''

'''
n=int(input('enter number: '))
sum=0
i=1
while i<=n:
    sum=sum+1
    i+=1
    print('the sum of first', n, 'number is:', sum)
'''
 

'''
name=''
while name!='vikram':
    name=input('enter your name: ')
print('Hello vikram thank you for utontication')
'''

'''
name=''
password=''
while name!='vikram':
    name=input('enter your name: ')
print('Hello', name, 'enter the password')
while password!='1234':
    password=input('enter your password: ')
print('congraulation, wellcome to the login page')
'''    
    
'''
for i in range(1,5):
    for j in range(1,5):
        print('*', end='')
    print()
'''

'''    
for i in range(1,5):
    for j in range(1,5):
        print(i, end='')
    print()
'''

'''
n=int(input('Enter the number: '))
for i in range(n):
    for j in range(n):
        print('*',end='')
    print()
'''


'''
n=int(input('Enter the number: '))
for i in range(1,n+1):
    for j in range(1,n+1):
        print(j,end='')
    print()
'''

'''
#n=int(input('Enter the number: '))
for i in range(1,6):
    for j in range(i):
        print('*',end='')
    print()
'''

'''
for i in range(0,5):
    for j in range(0,i+1):
        print('*', end='')
    print('')
'''

'''
n=int(input('Enter th value: '))
for i in range(n):
    for j in range(n-i-1):
        print(' ', end='')
    for j in range(2*i+1):
        print('*', end='')
    print()
'''


'''
n=int(input('Enter th value: '))
for i in range(n):
    for j in range(n-i-1):
        print('', end='')
    for j in range(i+1):
        print('*', end='')
    print()


n=int(input('Enter th value: '))
for i in range(n):
    for j in range(n-i-1):
        print(' ', end='')
    for j in range(i+1):
        print('*', end=' ')
    print()


n=int(input('Enter th value: '))
for i in range(n):
    for j in range(n-i-1):
        print(' ', end='')
    for j in range(i+1):
        print('*', end='')
    print()
'''

'''
for i in range(10):
    if i==11:
        print('Good')
    print(i)
'''
'''
cart=[10,20,30, 400, 800, 50]
for iteam in cart:
    if iteam>500:
        print('the value is more then 500')
        break
    print(iteam)
'''

'''
cart=[10,20,30, 400, 800, 50,60]
for iteam in cart:
    if iteam>500:
        print('the value is more then 500')
        continue
    print(iteam)
'''


'''
for i in range (11):
    if i%2==0:
        pass
        print(i)
'''

'''
numbers=[10,20,0,5,0,30]
for n in numbers:
    if n==0:
        print('connot divided by zero')
        continue
    print('100/{}={}'. format(n,100/n))
'''

'''
numbers=[10,20,0,5,0,30]
for n in numbers:
    if n==0:
        print('connot divided by zero')
        break
    print('100/{}={}'. format(n,100/n))
'''

'''
for i in range(100):
    if i%10==0:
        print(i)
    else:
        pass
'''

'''
num = int(input("Enter a number: "))
if num < 0:  
   print("Enter a positive number")  
else:  
   sum = 0 
   while(num > 0):  
       sum += num  #(1+=num)(1+=2)
       num -= 1    #(num-=1)(2-=1)
   print("The sum is",sum)  
'''

'''
num=int(input('enter the number: '))
for i in range(1,11):
    print(num,'*', i, '=', num*i)
'''

'''
a = [1, 2, 3, 4, 5]
# printing the list using * operator separated
# by comma
print(a)
# printing the list using * and sep operator
print("printing lists separated by commas")
print(a, sep = ", ")
# print in new line
print("printing lists in new line")
print(*a, sep = "\n")
'''

'''
n=int(input("Enter number: "))
count=0
while(n>0):
    count=count+1
    n=n//10
print("The number of digits in the number are:",count)
'''

'''
list = [1,2,3,4,5]
print("List before reverse : ",list)
list.reverse()
print("List after reverse : ",list)
'''

'''
list = [1, 2, 3, 4, 5]
print("List before reverse : ", list)
reversed_list = []
for value in list:
  reversed_list = [value] + reversed_list
print("List after reverse : ", reversed_list)
'''

'''
numbers=list(range(1,11))
print(numbers)
#for n in range(1, -10):
   # print(n, end='1')
'''

'''
num=0
while num >=-10:
    print(num)
    num-= 1
'''

'''
name=''
password=''
while name!='vikram' or password!='1234':
    name=input('Enter your name: ')
    password=input('Enter your password: ')
print('Hello', name, 'sucessfully login the page')
'''

