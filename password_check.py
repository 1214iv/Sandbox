# password_check.py
# 密码检查：以星号打印、简单校验
def check_password(pwd):
    # 简单规则：长度至少6位
    if len(pwd) >= 6:
        return True
    else:
        return False

if __name__ == "__main__":
    password = input("请输入密码：")
    if check_password(password):
        # 全部用*打印
        print("密码：" + "*" * len(password))
        print("密码校验通过")
    else:
        print("密码：" + "*" * len(password))
        print("密码太短，校验失败")