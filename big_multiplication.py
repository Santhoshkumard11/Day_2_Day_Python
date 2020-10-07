'''
Given two integer N and K, find the minimum number of times N must be multiplied by X to make it divisible by (2K).
Where X = Summation (2(4*i)) for 1 <= i <= 25.
Input
The first and the only line of input contains two space separated integers N and K.

Constraints
1 <= N <= 10^18
1 <= K <= 10^18
Output
Print a single integer which is the minimum number of times N must be multiplied by X to make it divisible by (2K).
Example
'''

n = int(input())

k = int(input())


power = 2**k

x = sum([ 2*(4**index) for index in range(25)])
count = 1

while(1):

    multip = x * n

    if (multip % power) ==0 :

        print(count)
        break

    count += 1
    multip *= x


