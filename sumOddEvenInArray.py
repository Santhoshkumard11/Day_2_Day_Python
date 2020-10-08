
num=list(input())

sumOdd,sumEven=0,0
j=1

for i in range(4):
    if(j%2!=0):
        sumOdd = sumOdd + int(num[i])-48
    else:
        sumEven =sumEven + int(num[i])-48
    j +=1
print(abs(sumOdd-sumEven))