# %%

a, b = input().split()


print(int(a) / int(b))

# %%

a, b = input().split()


def operation(x, y):
    add = int(x) + int(y)
    minus = int(x) - int(y)
    multi = int(x) * int(y)
    divide = int(x) / int(y)
    rest = int(x) % int(y)

    return add, minus, multi, int(divide), rest


print(operation(a, b)[0])
print(operation(a, b)[1])
print(operation(a, b)[2])
print(operation(a, b)[3])
print(operation(a, b)[4])


# %%

# 10430
# (A+B)%C는 ((A%C) + (B%C))%C 와 같을까?
# (A×B)%C는 ((A%C) × (B%C))%C 와 같을까?
# 세 수 A, B, C가 주어졌을 때, 위의 네 가지 값을 구하는 프로그램을 작성하시오.

a, b, c = map(int, input().split())

print((a + b) % c)
print(((a % c) + (b % c)) % c)
print((a * b) % c)
print(((a % c) * (b % c)) % c)

# %%
