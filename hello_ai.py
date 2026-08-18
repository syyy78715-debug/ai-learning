password = ""

while password != "123456":
    password = input("请输入密码：")

    if password != "123456":
        print("密码错误，请重新输入。")

print("密码正确，登录成功！")