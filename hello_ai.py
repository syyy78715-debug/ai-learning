try:
    num1 = float(input("请输入第一个数字："))
    num2 = float(input("请输入第二个数字："))

    print("加法结果：", num1 + num2)
    print("减法结果：", num1 - num2)
    print("乘法结果：", num1 * num2)
    print("除法结果：", num1 / num2)

except ValueError:
    print("输入错误：请输入数字。")

except ZeroDivisionError:
    print("计算错误：第二个数字不能是 0。")