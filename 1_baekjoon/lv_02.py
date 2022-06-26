# %%
# 1330

a, b = map(int, input().split())

if a > b:
    print('>')
elif a < b:
    print('<')
elif a == b:
    print('==')

# %%
# 14681

x= int(input())
y= int(input())

if x > 0 and y > 0:
    print('1')
elif x < 0 and y > 0:
    print('2')
elif x < 0 and y < 0:
    print('3')
elif x > 0 and y < 0:
    print('4')

# %%

h = range(1,24)

print(h)
