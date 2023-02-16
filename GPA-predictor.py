def gradetomarks(x):
    if x == "O" or x=="o":
        x = 10
        return x
    elif x == "A+" or x=="a+":
        x = 9
        return x
    elif x == "A" or x=="a":
        x = 8
        return x
    elif x == "B+" or x=="b+":
        x = 7
        return x
    elif x == "B" or x=="b":
        x = 6
        return x
    elif x == "C" or x=="c":
        x = 5
        return x
    elif x == "D" or x=="d":
        x = 4
        return x
    else:
        x=0
        return x
print("*************GPA PREDICTOR****************")
print("Warning - please enter grades without adding space between the plus and alphabet.")
Che = str(input("Please enter your grade in CHE110: "))
Che = gradetomarks(Che)*4
cse111 = str(input("Please enter your grade in CSE111: "))
cse111 = gradetomarks(cse111)*2
Cse326 = str(input("Please enter your grade in CSE326: "))
Cse326 = gradetomarks(Cse326)*2
ece249 = str(input("Please enter your grade in ECE249: "))
ece249 = gradetomarks(ece249)*4
ece279 = str(input("Please enter your grade in ECE279: "))
ece279 = gradetomarks(ece279)*1
int108 = str(input("Please enter your grade in INT108: "))
int108 = gradetomarks(int108)*4
mth174 = str(input("Please enter your grade in MTH174: "))
mth174 = gradetomarks(mth174)*4
pes318= str(input("Please enter your grade in PES318: "))
pes318 = gradetomarks(pes318)*3

gpa = (Che+cse111+Cse326+ece249+ece279+int108+mth174+pes318)/24

print("your calculated gpa is :",gpa)
