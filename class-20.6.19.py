# ##import math

# for num in range(3,100):
#     for num1 in range(2,num/2):
#         if(num%num1==0):
#             count+=1
#         break;



# print(abs(2.56))
##
'''
def sum(a,b):
    return(a+b)

x=int(input())
y=int(input())
print(sum(x,y))


class Student:
    def __init__(self,num1,num2):
        self.num1 = num1
        self.num2 = num2
    def sum(self):
        print(self.num1+self.num2)

if __name__ == "__main__":
    s1=Student(5,6)
    s2=Student(4,9)

    print(s1.sum,s2.sum)


n=10
d=dict()
for i in range(1,n+1):
    d[i+1]=i*i
print(d)

for i in range(1,11):
    print(i)
'''

'''
num=input()

if(num==(num[::-1])):
    print("Palindrom")
else:
    print("Not Palindrom")
'''

'''
value =[]
for i in range(100,250):
    s=str(i)
    if(int(s[0])%2==0 & int(s[1])%2==0 & int(s[2])%2==0):
        value.append(s)
print(' '.join(value))
'''
#print(value)
'''
name,age,height=[],[],[]
num =int(input("Enter the number of students:"))
for i in range(num):
    name.append(input("Enter the name:"))
    age.append(int(input("Enter the age:")))
    height.append(int(input("Enter the height:")))
name.sort()
age.sort()
height.sort(reverse='TRUE')
print('\n',join(tuple(name),tuple(age),tuple(height)))
'''
'''
string = input()
word =[]
word = string.split(" ")
#print(word)
for i in word:
    # str1= str(i)
    # str1.upper()
    i.append(i)
    print(i)
'''
'''
def factorial(n):
    if(n<=1):
        return(1)
    else:
        return(n*factorial(n-1))

print(factorial(5))
'''
'''
def primeDectect(num):
    for i in range(2,int(num/2)):
        if(num%i==0):
            flag=1
            break
        else:
            flag=0
    if(flag==0):
        print("prime")
    else:
        print("not prime")
primeDectect(13)
'''

