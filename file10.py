mark=[]
with open("marks.txt","a") as f:
    n=1
    x=int(input("Enter the no. of students: "))
    while n<=x:
        f.write(f"Student {n} \n")
        print("-"*5 + f"Student {n} Details" + "-"*5)
        name=input("Enter Name: ")
        roll_no=int(input("Enter Roll number : "))
        marks=int(input("Enter Marks: "))
        f.write(f"Name: {name} \n")
        f.write(f"Roll number: {str(roll_no)}\n")
        f.write(f"Marks: {str(marks)} \n")
        f.write("\n")
        mark.append(marks)
        n=n+1

    highest_marks=max(mark)
    lowest_marks=min(mark)
    avg_marks=sum(mark)/len(mark)

    f.write(f"Highest Marks {highest_marks}\n")
    f.write(f"Lowest Marks {lowest_marks}\n")
    f.write(f"Average Marks {avg_marks}\n")
