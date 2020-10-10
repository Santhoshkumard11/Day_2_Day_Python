# to implement simple recursion 


# method to calculate the sum of n numbers 
total = 1
def SumOfNNUmbers(number):

    if(number==1):
        return ( 1 )
     
    else:
        return number * SumOfNNUmbers ( number-1 )  
      

print("The sum of {} number is {}".format(2,SumOfNNUmbers(3)))