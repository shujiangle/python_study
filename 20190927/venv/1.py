# _*_ coding=utf8 _*_

def auth(index):
    def login():
        index()
        print("已经进入登录界面")
    return login


@auth
def f1():
    print("我是f1")

@auth
def f2():
    print("我是f2")

@auth
def f3():
    print("我是f3")

f1()
f2()
f3()



