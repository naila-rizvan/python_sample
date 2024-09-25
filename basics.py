# Accept student scores and find (i) average marks (ii) maximum marks (iii) minimum marks

n = int(input("Enter the number of subjects: "))
marks = []

for i in range(n):
    element = int(input("Enter marks of subject " + str(i+1) + ": "))
    marks.append(element)

sum_marks = 0
max_marks = marks[0]

for mark in marks:
    sum_marks += mark
    if mark > max_marks:
        max_marks = mark

average_marks = sum_marks/n
print("Average marks: " + str(average_marks))
print("Maximum marks: " + str(max_marks))
print("Minimum marks: " + str(min(marks)))

print("Marks: " + str(marks[0::2]))         # Prints every second element starting at index 0
