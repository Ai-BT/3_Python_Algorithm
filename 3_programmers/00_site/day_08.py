# Day 8

# %%

# 1 **

# 문자열 s가 주어졌을 때, s의 각 위치마다 자신보다 앞에 나왔으면서,
# 자신과 가장 가까운 곳에 있는 같은 글자가 어디 있는지 알고 싶습니다.
# 예를 들어, s="banana"라고 할 때,
# 각 글자들을 왼쪽부터 오른쪽으로 읽어 나가면서 다음과 같이 진행할 수 있습니다.

# b는 처음 나왔기 때문에 자신의 앞에 같은 글자가 없습니다. 는 -이1로 표현합니다.
# a는 처음 나왔기 때문에 자신의 앞에 같은 글자가 없습니다. 이는 -1로 표현합니다.
# n은 처음 나왔기 때문에 자신의 앞에 같은 글자가 없습니다. 이는 -1로 표현합니다.
# a는 자신보다 두 칸 앞에 a가 있습니다. 이는 2로 표현합니다.
# n도 자신보다 두 칸 앞에 n이 있습니다. 이는 2로 표현합니다.
# a는 자신보다 두 칸, 네 칸 앞에 a가 있습니다. 이 중 가까운 것은 두 칸 앞이고, 이는 2로 표현합니다.
# 따라서 최종 결과물은 [-1, -1, -1, 2, 2, 2]가 됩니다.

# 문자열 s이 주어질 때, 위와 같이 정의된 연산을 수행하는 함수 solution을 완성해주세요.

# 제한사항
# 1 ≤ s의 길이 ≤ 10,000
# s은 영어 소문자로만 이루어져 있습니다.

# 입출력    예
# s	        result
# "banana"	[-1, -1, -1, 2, 2, 2]
# "foobar"	[-1, -1, 1, -1, -1, -1]


def solution(s):
    answer = []
    visited = {}

    for i, c in enumerate(s):
        if c in visited:
            diff = i - visited[c] + 1
            answer.append(diff)
            visited[c] = i + 1
        else:
            answer.append(-1)
            visited[c] = i + 1

    return answer
# %%

# 2 **
# 네오와 프로도가 숫자놀이를 하고 있습니다.
# 네오가 프로도에게 숫자를 건넬 때 일부 자릿수를 영단어로 바꾼 카드를 건네주면 프로도는 원래 숫자를 찾는 게임입니다.

# 다음은 숫자의 일부 자릿수를 영단어로 바꾸는 예시입니다.

# 1478 → "one4seveneight"
# 234567 → "23four5six7"
# 10203 → "1zerotwozero3"
# 이렇게 숫자의 일부 자릿수가 영단어로 바뀌어졌거나, 혹은 바뀌지 않고 그대로인 문자열 s가 매개변수로 주어집니다.
# s가 의미하는 원래 숫자를 return 하도록 solution 함수를 완성해주세요.

# 참고로 각 숫자에 대응되는 영단어는 다음 표와 같습니다.

# 숫자	영단어
# 0	zero
# 1	one
# 2	two
# 3	three
# 4	four
# 5	five
# 6	six
# 7	seven
# 8	eight
# 9	nine

# 제한사항
# 1 ≤ s의 길이 ≤ 50
# s가 "zero" 또는 "0"으로 시작하는 경우는 주어지지 않습니다.
# return 값이 1 이상 2,000,000,000 이하의 정수가 되는 올바른 입력만 s로 주어집니다.

# 입출력 예
# s	                    result
# "one4seveneight"	    1478
# "23four5six7"	        234567
# "2three45sixseven"	234567
# "123"	                123


s = "one4"


def solution(s):
    dict_s = {'zero': '0', 'one': '1', 'two': '2', 'three': '3', 'four': '4',
              'five': '5', 'six': '6', 'seven': '7', 'eight': '8', 'nine': '9'}
    for key in dict_s:
        s = s.replace(key, dict_s[key])
    return int(s)


# %%

# 3 **
# 문제 설명
# 정수 배열 numbers가 주어집니다.
# numbers에서 서로 다른 인덱스에 있는 두 개의 수를 뽑아 더해서 만들 수 있는 모든 수를 배열에 오름차순으로 담아
# return 하도록 solution 함수를 완성해주세요.

# 제한사항
# numbers의 길이는 2 이상 100 이하입니다.
# numbers의 모든 수는 0 이상 100 이하입니다.

# 입출력 예
# numbers	    result
# [2,1,3,4,1]	[2,3,4,5,6,7]
# [5,0,2,7]	    [2,5,7,9,12]


def solution(numbers):
    answer = set()
    for i in range(len(numbers)):
        for j in range(i+1, len(numbers)):
            answer.add(numbers[i]+numbers[j])
    answer = list(answer)
    answer.sort()
    return answer


# %%

# 4 **
# 배열 array의 i번째 숫자부터 j번째 숫자까지 자르고 정렬했을 때, k번째에 있는 수를 구하려 합니다.

# 예를 들어 array가 [1, 5, 2, 6, 3, 7, 4], i = 2, j = 5, k = 3이라면

# array의 2번째부터 5번째까지 자르면 [5, 2, 6, 3]입니다.
# 1에서 나온 배열을 정렬하면 [2, 3, 5, 6]입니다.
# 2에서 나온 배열의 3번째 숫자는 5입니다.
# 배열 array, [i, j, k]를 원소로 가진 2차원 배열 commands가 매개변수로 주어질 때,
# commands의 모든 원소에 대해 앞서 설명한 연산을 적용했을 때 나온 결과를 배열에 담아 return 하도록 solution 함수를 작성해주세요.

# 제한사항
# array의 길이는 1 이상 100 이하입니다.
# array의 각 원소는 1 이상 100 이하입니다.
# commands의 길이는 1 이상 50 이하입니다.
# commands의 각 원소는 길이가 3입니다.

# 입출력 예
# array	                    commands	                            return
# [1, 5, 2, 6, 3, 7, 4]	    [[2, 5, 3], [4, 4, 1], [1, 7, 3]]	    [5, 6, 3]

array = [1, 5, 2, 6, 3, 7, 4]
commands = [[2, 5, 3], [4, 4, 1], [1, 7, 3]]


def solution(array, commands):
    answer = []
    for i in range(len(commands)):
        arr = array[commands[i][0]-1:commands[i][1]]
        arr.sort()  # 정렬
        answer.append(arr[commands[i][2]-1])  # 0부터 시작이니 -1
    return answer


arr1 = array[commands[0][0]-1:commands[0][1]]
arr2 = array[commands[1][0]-1:commands[1][1]]
arr3 = array[commands[2][0]-1:commands[2][1]]

print(arr1, arr2, arr3)


# %%
