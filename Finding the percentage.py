if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()

    # print(student_marks)

    final_score =[]
    final_score = student_marks[query_name]
    total = sum(final_score)

    total /= len(final_score)   
    
    print("%.2f"%total)
    
    //sample input
    
    3
    Krishna 67 68 69
    Arjun 70 98 63
    Malika 52 56 60
    Malika
    
    //sample output
    
    56.00
    
    
    
    //Solved by Santhosh_Goku
    //HackerRank Problem
