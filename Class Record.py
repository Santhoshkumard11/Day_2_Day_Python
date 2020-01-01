def main():


    noOfStudents=int(input())

    studentsMark = {}
    avgMark = []
    for _ in range(noOfStudents):
        name, *line = input().split()
        mark = list(map(int,line))
        studentsMark[name] = mark

    studentMarkList=[]
    studentMarkList = list(studentsMark.values())

    total =0;average=0
    totalmark = []
    for index in range(5):
        for index2 in range(noOfStudents):
            
            total += studentMarkList[index2][index]

        average = total/noOfStudents
        total = 0   
        totalmark.append(average)
    
    for index in range(5):
        if(index==4):
            print("%.2f"%totalmark[index],end="")
        else:
            print("%.2f"%totalmark[index],end=" ")
            
main()

"""
Input
2
arpit 100 75 40 56 53
anushka 100 100 76 100 100

Output
100.00 87.50 58.00 78.00 76.50



Solved by santhosh_goku
techgig challenge
"""
