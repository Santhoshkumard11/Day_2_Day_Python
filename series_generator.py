#question 2
#generate the series
#3  8  14  22  34  53  83  129  197  294


print("Enter the lenght of the series:")
seriesLength =int(input())
s1,s2,s3 = 1,5,3

gen_series = []

for itr in range(1,seriesLength):

    gen_series.append(s3)
    s3 += s2
    s2 += s1
    s1 += itr

result = (str(gen_series).replace(',',' '))[1:-1]

#print the series
print(result)


