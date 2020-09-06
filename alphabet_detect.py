#                                       Program to check the alphabets in the given string
print("Enter the string:")
strin = str(input())
alp= ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
i,j=0,0
# Finding the letters in the given string 
while(i<(len(strin))):
    while(j<(len(alp))):
        if(strin[i]==alp[j]):
            print(strin[i],alp[j]) 
            alp.remove(alp[j])
        j = j+1
    i = i+1
    j=0
# Checking for the condition 
if(len(alp)==0):
    print("String has all the alphabets")
else:
    print("String don't have all the alphabets")

'''
Input :

asnd

Output :

String don't have all the alphabets 


'''
