# Day_04

# %%

# 1
# 정수 n을 입력받아 n의 약수를 모두 더한 값을 리턴하는 함수, solution을 완성해주세요.

# 제한 사항
# n은 0 이상 3000이하인 정수입니다.

# 입출력 예
# n	return
# 12	28
# 5	    6

def solution(n):
    answer = 0
    for i in range(1, n + 1):
        if n % i == 0:
            answer += i
    return answer


# %%

# 2
# 자연수 N이 주어지면,
# N의 각 자릿수의 합을 구해서 return 하는 solution 함수를 만들어 주세요.
# 예를들어 N = 123이면 1 + 2 + 3 = 6을 return 하면 됩니다.

# 제한사항
# N의 범위 : 100,000,000 이하의 자연수

# 입출력 예
# N	    answer
# 123	6
# 987	24

n = 987


def solution(n):
    answer = 0
    answer = sum(map(int, str(n)))

    return answer


solution(n)

# result = list(map(int, str(n)))
# print(result)


# %%

# 3
# 자연수 n을 뒤집어 각 자리 숫자를 원소로 가지는 배열 형태로 리턴해주세요.
# 예를들어 n이 12345이면 [5,4,3,2,1]을 리턴합니다.

# 제한 조건
# n은 10,000,000,000이하인 자연수입니다.
# 입출력 예
# n	    return
# 12345	[5,4,3,2,1]

n = 12345


def solution(n):

    answer = list(map(int, str(n)))
    answer.reverse()

    return answer


solution(n)

# %%

# 4

# 함수 solution은 정수 n을 매개변수로 입력받습니다.
# n의 각 자릿수를 큰것부터 작은 순으로 정렬한 새로운 정수를 리턴해주세요.
# 예를들어 n이 118372면 873211을 리턴하면 됩니다.

# 제한 조건
# n은 1이상 8000000000 이하인 자연수입니다.

# 입출력   예
# n	    return
# 118372	873211


def solution(n):
    answer = list(str(n))
    answer.sort(reverse=True)

    answer = ''.join(answer)

    return int(answer)


n = 118372

solution(118372)


# %%

# 5
# 문제 설명
# 임의의 양의 정수 n에 대해,
# n이 어떤 양의 정수 x의 제곱인지 아닌지 판단하려 합니다.
# n이 양의 정수 x의 제곱이라면 x+1의 제곱을 리턴하고, n이 양의 정수 x의 제곱이 아니라면 -1을 리턴하는 함수를 완성하세요.

# 제한 사항
# n은 1이상, 50000000000000 이하인 양의 정수입니다.

# 입출력 예
# n 	return
# 121	144
# 3	    -1


def solution(n):
    if int(n**0.5) == n**0.5:  # 제곱수 판별
        return ((n**0.5)+1)**2  # 제곱근+1의 제곱수 반환
    else:
        return -1  # 제곱수 아니면 -1반환


# %%

# 6
# 정수 num이 짝수일 경우 "Even"을 반환하고 홀수인 경우 "Odd"를 반환하는 함수, solution을 완성해주세요.

# 제한 조건
# num은 int 범위의 정수입니다.
# 0은 짝수입니다.

# 입출력 예
# num	return
# 3	"Odd"
# 4	"Even"

def solution(num):
    if num % 2 == 0:
        answer = "Even"
    else:
        answer = "Odd"
    return answer

# %%

# 7
# 정수를 담고 있는 배열 arr의 평균값을 return하는 함수, solution을 완성해보세요.

# 제한사항
# arr은 길이 1 이상, 100 이하인 배열입니다.
# arr의 원소는 -10,000 이상 10,000 이하인 정수입니다.

# 입출력 예
# arr	    return
# [1,2,3,4]	    2.5
# [5,5]	    5


arr = [5, 5]


def solution(arr):

    arr_sum = sum(arr)
    arr_avg = arr_sum/len(arr)

    return arr_avg


solution(arr)

# %%

# 8
# 양의 정수 x가 하샤드 수이려면 x의 자릿수의 합으로 x가 나누어져야 합니다.
# 예를 들어 18의 자릿수 합은 1+8=9이고, 18은 9로 나누어 떨어지므로 18은 하샤드 수입니다.
# 자연수 x를 입력받아 x가 하샤드 수인지 아닌지 검사하는 함수, solution을 완성해주세요.

# 제한 조건
# x는 1 이상, 10000 이하인 정수입니다.

# 입출력 예
# x	    return
# 10	true
# 12	true
# 11	false
# 13	false


def solution(x):
    answer = True

    x_list = list(map(int, str(x)))
    x_sum = sum(x_list)

    if x % x_sum == 0:
        answer = True
    else:
        answer = False
    return answer


solution(18)


# %%

# 9
# 함수 solution은 정수 x와 자연수 n을 입력 받아, x부터 시작해 x씩 증가하는 숫자를 n개 지니는 리스트를 리턴해야 합니다.
# 다음 제한 조건을 보고, 조건을 만족하는 함수, solution을 완성해주세요.

# 제한 조건
# x는 -10000000 이상, 10000000 이하인 정수입니다.
# n은 1000 이하인 자연수입니다.

# 입출력 예
# x	    n	answer
# 2	    5	[2,4,6,8,10]
# 4	    3	[4,8,12]
# -4	2	[-4, -8]

x = -4
n = 2


def solution(x, n):
    answer = []

    for i in range(n):
        answer.append(x * (i + 1))

    return answer


solution(x, n)


# %%

# 10

# 문제 설명
# 자연수 n이 매개변수로 주어집니다.
# n을 x로 나눈 나머지가 1이 되도록 하는 가장 작은 자연수 x를 return 하도록 solution 함수를 완성해주세요.
# 답이 항상 존재함은 증명될 수 있습니다.

# 제한사항
# 3 ≤ n ≤ 1,000,000
# 입출력 예

# n	    result
# 10	3
# 12	11

n = 12


def solution(n):
    answer = 0
    num_list = []

    for i in range(n):
        if n % (i + 1) == 1:
            num_list.append(i+1)

    answer = min(num_list)

    return answer


solution(n)

# %%

# 11 **
# 문제 설명
# 두 정수 a, b가 주어졌을 때 a와 b 사이에 속한 모든 정수의 합을 리턴하는 함수, solution을 완성하세요.
# 예를 들어 a = 3, b = 5인 경우, 3 + 4 + 5 = 12이므로 12를 리턴합니다.

# 제한 조건
# a와 b가 같은 경우는 둘 중 아무 수나 리턴하세요.
# a와 b는 -10,000,000 이상 10,000,000 이하인 정수입니다.
# a와 b의 대소관계는 정해져있지 않습니다.
# 입출력 예
# a	b	return
# 3	5	12
# 3	3	3
# 5	3	12

a = 5
b = 3


def solution(a, b):
    answer = 0

    list_num = []
    list_num.append(a)
    list_num.append(b)

    max_num = max(list_num)
    min_num = min(list_num)

    list_sum = []

    for i in range(min_num, max_num+1):
        list_sum.append(i)

    answer = sum(list_sum)

    return answer


solution(5, 3)


# 다른 사람 풀이
def adder(a, b):
    if a > b:
        a, b = b, a
    return sum(range(a, b + 1))


# %%

# 12
# String형 배열 seoul의 element중 "Kim"의 위치 x를 찾아,
# "김서방은 x에 있다"는 String을 반환하는 함수,
# solution을 완성하세요.
# seoul에 "Kim"은 오직 한 번만 나타나며 잘못된 값이 입력되는 경우는 없습니다.

# 제한 사항
# seoul은 길이 1 이상, 1000 이하인 배열입니다.
# seoul의 원소는 길이 1 이상, 20 이하인 문자열입니다.
# "Kim"은 반드시 seoul 안에 포함되어 있습니다.

# 입출력 예
# seoul 	        return
# ["Jane", "Kim"]	"김서방은 1에 있다"

seoul = ["Jane", "Kim"]


def solution(seoul):
    answer = ''
    for i in range(len(seoul)):
        if seoul[i] == "Kim":
            answer = "김서방은 {}에 있다".format(i)
    return answer


solution(seoul)


def findKim(seoul):
    return "김서방은 {}에 있다".format(seoul.index('Kim'))

# %%

# 13
# 어떤 정수들이 있습니다.
# 이 정수들의 절댓값을 차례대로 담은 정수 배열 absolutes와 이 정수들의 부호를 차례대로 담은 불리언 배열 signs가 매개변수로 주어집니다.
# 실제 정수들의 합을 구하여 return 하도록 solution 함수를 완성해주세요.

# 제한사항
# absolutes의 길이는 1 이상 1,000 이하입니다.
# absolutes의 모든 수는 각각 1 이상 1,000 이하입니다.
# signs의 길이는 absolutes의 길이와 같습니다.
# signs[i] 가 참이면 absolutes[i] 의 실제 정수가 양수임을, 그렇지 않으면 음수임을 의미합니다.

# 입출력 예
# absolutes	signs	            result
# [4,7,12]	[true,false,true]	9
# [1,2,3]	[false,false,true]	0


# true +
# false -

def solution(absolutes, signs):
    answer = 0
    arr_num = []

    for i in range(len(absolutes)):
        if signs[i] == False:
            arr_num.append(-absolutes[i])
        else:
            arr_num.append(absolutes[i])

    answer = sum(arr_num)

    return answer


# %%

# 14 **

# 문제 설명
# 0부터 9까지의 숫자 중 일부가 들어있는 정수 배열 numbers가 매개변수로 주어집니다.
# numbers에서 찾을 수 없는 0부터 9까지의 숫자를 모두 찾아 더한 수를 return 하도록 solution 함수를 완성해주세요.

# 제한사항
# 1 ≤ numbers의 길이 ≤ 9
# 0 ≤ numbers의 모든 원소 ≤ 9
# numbers의 모든 원소는 서로 다릅니다.

# 입출력 예
# numbers	result
# [1,2,3,4,6,7,8,0]	14
# [5,8,4,0,6,7,9]	6

numbers = [1, 2, 3, 4, 6, 7, 8, 0]


def solution(numbers):
    answer = 0
    for i in range(10):
        if i not in numbers:
            answer += i

    return answer


def solution_2(numbers):
    return 45 - sum(numbers)

# %%

# 15 **
# 문제 설명
# 1937년 Collatz란 사람에 의해 제기된 이 추측은, 주어진 수가 1이 될 때까지 다음 작업을 반복하면,
# 모든 수를 1로 만들 수 있다는 추측입니다. 작업은 다음과 같습니다.

# 1-1. 입력된 수가 짝수라면 2로 나눕니다.
# 1-2. 입력된 수가 홀수라면 3을 곱하고 1을 더합니다.
# 2. 결과로 나온 수에 같은 작업을 1이 될 때까지 반복합니다.
# 예를 들어, 주어진 수가 6이라면 6 → 3 → 10 → 5 → 16 → 8 → 4 → 2 → 1 이 되어 총 8번 만에 1이 됩니다.
# 위 작업을 몇 번이나 반복해야 하는지 반환하는 함수, solution을 완성해 주세요.
# 단, 주어진 수가 1인 경우에는 0을, 작업을 500번 반복할 때까지 1이 되지 않는다면 –1을 반환해 주세요.

# 제한 사항
# 입력된 수, num은 1 이상 8,000,000 미만인 정수입니다.

# 입출력 예
# n	        result
# 6	        8
# 16	    4
# 626331	-1


n = 626331


def solution(n):
    answer = 0
    while True:
        if n == 1:
            break
        elif answer == 500:
            answer = -1
            break
        elif n % 2 == 0:
            n = n / 2
            answer += 1
        else:
            n = n * 3 + 1
            answer += 1
    return answer


# %%

# 16
# 문제 설명
# array의 각 element 중 divisor로 나누어 떨어지는 값을 오름차순으로 정렬한 배열을 반환하는 함수, solution을 작성해주세요.
# divisor로 나누어 떨어지는 element가 하나도 없다면 배열에 -1을 담아 반환하세요.

# 제한사항
# arr은 자연수를 담은 배열입니다.
# 정수 i, j에 대해 i ≠ j 이면 arr[i] ≠ arr[j] 입니다.
# divisor는 자연수입니다.
# array는 길이 1 이상인 배열입니다.

# 입출력 예
# arr	            divisor	    return
# [5, 9, 7, 10]	    5	        [5, 10]
# [2, 36, 1, 3]	    1	        [1, 2, 3, 36]
# [3,2,6]	        10	        [-1]


arr = [2, 36, 1, 3]
divisor = 1


def solution(arr, divisor):
    answer = []
    count = 0

    for i in range(len(arr)):
        # print(arr[i])

        if arr[i] % divisor == 0:
            answer.append(arr[i])
            answer.sort()
            count += 1

    if count == 0:
        answer.append(-1)
    return answer


solution(arr, divisor)
# %%

# 17 **
# 프로그래머스 모바일은 개인정보 보호를 위해 고지서를 보낼 때 고객들의 전화번호의 일부를 가립니다.
# 전화번호가 문자열 phone_number로 주어졌을 때,
# 전화번호의 뒷 4자리를 제외한 나머지 숫자를 전부 *으로 가린 문자열을 리턴하는 함수, solution을 완성해주세요.

# 제한 조건
# phone_number는 길이 4 이상, 20이하인 문자열입니다.

# 입출력 예
# phone_number	return
# "01033334444"	"*******4444"
# "027778888"	"*****8888"


def solution(phone_number):
    answer = ''

    phone_number_len = len(phone_number)

    answer = '*' * (phone_number_len - 4)

    answer += phone_number[-4:]

    return answer

# %%

# 18 **
# 정수를 저장한 배열, arr 에서 가장 작은 수를 제거한 배열을 리턴하는 함수, solution을 완성해주세요.
# 단, 리턴하려는 배열이 빈 배열인 경우엔 배열에 -1을 채워 리턴하세요.
# 예를들어 arr이 [4,3,2,1]인 경우는 [4,3,2]를 리턴 하고, [10]면 [-1]을 리턴 합니다.

# 제한 조건
# arr은 길이 1 이상인 배열입니다.
# 인덱스 i, j에 대해 i ≠ j이면 arr[i] ≠ arr[j] 입니다.

# 입출력 예
# arr	    return
# [4,3,2,1]	[4,3,2]
# [10]	    [-1]


arr = [10]


def solution(arr):
    if len(arr) > 1:
        arr.remove(min(arr))

        return arr
    else:
        return [-1]


solution(arr)

# %%

# 19 **
# 단어 s의 가운데 글자를 반환하는 함수,
# solution을 만들어 보세요. 단어의 길이가 짝수라면 가운데 두글자를 반환하면 됩니다.

# 재한사항
# s는 길이가 1 이상, 100이하인 스트링입니다.
# 입출력 예
# s	return
# "abcde"	"c"
# "qwer"	"we"


s = "qwer"


def solution(s):
    center = int(len(s)/2)
    if len(s) % 2 != 0:
        return s[center]
    else:
        return s[center-1:center+1]


# %%

# 20
# 길이가 n이고, "수박수박수박수...."와 같은 패턴을 유지하는 문자열을 리턴하는 함수, solution을 완성하세요.
# 예를들어 n이 4이면 "수박수박"을 리턴하고 3이라면 "수박수"를 리턴하면 됩니다.

# 제한 조건
# n은 길이 10,000이하인 자연수입니다.

# 입출력 예
# n	    return
# 3	    "수박수"
# 4	    "수박수박"


n = 6


def solution(n):
    answer = ''
    for i in range(n):
        if i % 2 == 0:
            answer += "수"
        else:
            answer += "박"

    return answer

# %%
