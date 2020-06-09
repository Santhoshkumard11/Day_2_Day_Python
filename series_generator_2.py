#question 1
#generate the series 
# #3  5  8  13  20  31  44  61  80  103  132  163

#method to generate the prime number
def prime_number_generator(n):
   
    primeList = [0]
    condition,num = 0,2 

    while condition < n:  
    
        for itr in range(2,num):  
            if (num % itr) == 0:  
                break  
        else:  
            primeList.append(num)
            condition += 1
        num += 1
    return primeList

print("Enter the lenght of the series:")
SeriesLength = int(input())


prime_number_series = prime_number_generator(SeriesLength)
result = [3] 

#generating the series
for i in range(1,SeriesLength):
    
    result.append(prime_number_series[i]+result[i-1])

#printing the result
series = (str(result).replace(',',' '))[1:-1]
print(series)
