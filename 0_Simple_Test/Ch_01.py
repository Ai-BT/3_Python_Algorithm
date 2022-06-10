# %%

# 1. 리스트에서 400,500 을 삭제

nums = [100,200,300,400,500]
nums.pop()
nums.pop()
print(nums)

# %%

# 2. 출력 [200,100,1000,300]

l = [200,100,300]
l.insert(2,1000)
print(l)

# %%

# 3. 결과값은?

a = 10
b = 2
for i in range(1,5,2):
    a += i

print(a+b)

# %%

# 4. sep, end 사용하여 출력(2019/04/26 11:34:27)

year = '2019'
month = '04'
day = '26'
hour = '11'
minute = '34'
second = '27'

print(year, month, day, sep='/', end=' ')
print(hour, minute, second, sep=':')

# %%

# 5. 별찍기 입력 (5)
#     *
#    ***
#   *****
#  *******
# *********

def star(n):
    for i in range(1,n+1):
        print( 
            " "*(n-i) + ("*"*(2*i-1)) 
            )
star(5)



