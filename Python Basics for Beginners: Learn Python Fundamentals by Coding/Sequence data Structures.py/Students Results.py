n = int(input())
passed = []
failed = []
for i in range(n):
    marks = int(input())
    if marks < 40:
        failed.append(i + 1)
    else:
        passed.append(i + 1)
if len(failed) == n:
    print("All are failed")
elif len(passed) == n:
    print("All are passed")
else:
    print("Students who failed in Final Exam")
    for i in range(len(failed)):
        print("Roll No: " + str(failed[i]))
    print("Students who passed in Final Exam")
    for i in range(len(passed)):
        print("Roll No: " + str(passed[i]))