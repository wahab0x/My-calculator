a = int(input("pehla number likho:"))

operation = input("operation likho(+,-,*,/):")

b = int(input("doosra number likho:"))

if operation =="+":
    print("Answer:",a+b)
elif operation =="-":
    print("Answer:",a-b)
elif operation =="/":
    print("Answer:",a/b)
elif operation =="*":
    print("Answer:",a*b)
else:
    print("Answer Ghalat!")