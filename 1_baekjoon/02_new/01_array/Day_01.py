# %%
# 문제 1
# 총 N개의 정수가 주어졌을 때, 정수 v가 몇 개인지 구하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 정수의 개수 N(1 ≤ N ≤ 100)이 주어진다.
# 둘째 줄에는 정수가 공백으로 구분되어져있다.
# 셋째 줄에는 찾으려고 하는 정수 v가 주어진다. 입력으로 주어지는 정수와 v는 -100보다 크거나 같으며, 100보다 작거나 같다.

# 출력
# 첫째 줄에 입력으로 주어진 N개의 정수 중에 v가 몇 개인지 출력한다.

# 입력
# 11
# 1 4 1 2 4 2 4 2 3 4 4
# 2

# 출력
# 3

n = int(input())
n_list = list(map(int, input().split()))
v = int(input())

n_list = [1, 4, 1, 2, 4, 2, 4, 2, 3, 4, 4]
v = 2

print(n_list.count(v))

# %%

# 문제 2
# 정수 N개로 이루어진 수열 A와 정수 X가 주어진다. 이때, A에서 X보다 작은 수를 모두 출력하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 N과 X가 주어진다. (1 ≤ N, X ≤ 10,000)
# 둘째 줄에 수열 A를 이루는 정수 N개가 주어진다. 주어지는 정수는 모두 1보다 크거나 같고, 10,000보다 작거나 같은 정수이다.

# 출력
# X보다 작은 수를 입력받은 순서대로 공백으로 구분해 출력한다. X보다 작은 수는 적어도 하나 존재한다.

# 예제 입력 1
# 10 5
# 1 10 4 9 2 3 8 5 7 6

# 예제 출력 1
# 1 4 2 3

n, x = 10, 5
n_list = [1, 10, 4, 9, 2, 3, 8, 5, 7, 6]

# n, x = map(int, input().split())
# n_list = list(map(int, input().split()))

# for i in range(len(n_list)):
#     if n_list[i] < x:
#         print(n_list[i], end=" ")

# 리스트 컴프리헨션을 사용하여 한 줄로 처리
result = [num for num in n_list if num < x]

# join을 사용하여 출력
print(" ".join(map(str, result)))

# %%

# 문제 3
# N개의 정수가 주어진다. 이때, 최솟값과 최댓값을 구하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 정수의 개수 N (1 ≤ N ≤ 1,000,000)이 주어진다.
# 둘째 줄에는 N개의 정수를 공백으로 구분해서 주어진다. 모든 정수는 -1,000,000보다 크거나 같고, 1,000,000보다 작거나 같은 정수이다.

# 출력
# 첫째 줄에 주어진 정수 N개의 최솟값과 최댓값을 공백으로 구분해 출력한다.

# 예제 입력 1
# 5
# 20 10 35 30 7

# 예제 출력 1
# 7 35

n = int(input())
n_list = list(map(int, input().split()))

# n = 5
# n_list = [20, 10, 35, 30, 7]

min, max = min(n_list), max(n_list)

print(min, max)