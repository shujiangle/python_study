# _*_ coding: utf8 _*_

# author:shujiangle

for i in range(1, 10):
    for j in range(1, i+1):
        print("{}x{}={}\t".format(j, i, j*i), end='')
    print()

print("="*100)

inp1 = input("please input your name: ")
inp1_return = list(inp1)
inp1_return.reverse()
inp1_return = ''.join(inp1_return)
print(inp1_return)
print("="*100)

num=0
for i in range(1, 101):
    num += i
print("1+2+3+......4+100=%s"%num)


















