def get_subarray(array:list):
    "Returns a list of subarrays within the defined range"

    subarray_list = []

    for index_1 in range(len(array) + 1):
        for index_2 in range(index_1):
            subarray_list.append(array[index_2:index_1])
    
    return subarray_list


def check_for_subarray_sum_condition(subarray:list):
    "Calculating if the subarray is in-line with the XOR condition"

    resultant_XOR_sum = 0

    # sum up the XOR each time and store it in a variable
    [resultant_XOR_sum := resultant_XOR_sum ^ item for item in subarray]

    return True if resultant_XOR_sum ^ 1 == resultant_XOR_sum + 1 else False


def get_condition_satisfying_subarray_count(subarray_list:list):
    "Count all the subarrays which satisfies the XOR condition"
    condition_satisfiying_subarray_count = 0

    # iterate over all the subarray and count if the XOR condition is met
    for subarray in subarray_list:
        if check_for_subarray_sum_condition(subarray) :
            condition_satisfiying_subarray_count += 1

    return condition_satisfiying_subarray_count


def solve (N, M, A, queries):

    condition_satisfiying_subarray_count_list = []

    # iterate through all the queries
    for query in queries:
        subarray_list = get_subarray( A[query[0]-1 : query[1]] )

        condition_satisfiying_subarray_count_list.append(get_condition_satisfying_subarray_count(subarray_list))

    return condition_satisfiying_subarray_count_list



N = int(input())
M = int(input())
A = list(map(int, input().split()))
queries = [list(map(int, input().split())) for i in range(M)]

out_ = solve(N, M, A, queries)
print (' '.join(map(str, out_)))
