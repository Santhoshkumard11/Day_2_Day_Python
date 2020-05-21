#find the uniqure words in a string

#method to convert the list to dict type
def List_To_Dict(lst): 
    res_dct = {lst[i] : i for i in range(0, len(lst))} 
    return res_dct

#get the input string
input_string = list(input().split())



dict_string = List_To_Dict(input_string)

res_key = list(dict_string.keys())

#print the unique words
print(res_key)

# input
# santhosh kumar santhosh kumar sam joe

# output
# ['santhosh', 'kumar', 'sam', 'joe']