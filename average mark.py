tamil = int(input("tamil  marks: "))
english = int(input("english marks: "))
maths = int(input("maths marks: "))
science = int(input("science marks: "))
social = int(input("social marks: "))
marks =(tamil+english+maths+science+social)/5
if (marks<35):
    print("addition class is required")
else:
    print("you are good")    