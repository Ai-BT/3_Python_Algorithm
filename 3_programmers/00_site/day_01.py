# 기초 트레이닝

# %%

# 문자열 my_string과 정수 n이 매개변수로 주어질 때,
# my_string의 앞의 n글자로 이루어진 문자열을 return 하는 solution 함수를 작성해 주세요.

# 입출력 예
# my_string	n	result
# "ProgrammerS123"	11	"ProgrammerS"
# "He110W0r1d"	5	"He110"

def solution(my_string, n):
    answer = my_string[:n]
    return answer


solution("He110W0r1d", 5)

# %%

# 어떤 문자열에 대해서 접미사는 특정 인덱스부터 시작하는 문자열을 의미합니다.
# 예를 들어, "banana"의 모든 접미사는 "banana", "anana", "nana", "ana", "na", "a"입니다.
# 문자열 my_string과 is_suffix가 주어질 때,
# is_suffix가 my_string의 접미사라면 1을,
# 아니면 0을 return 하는 solution 함수를 작성해 주세요.

# 입출력 예
# my_string	is_suffix	result
# "banana"	"ana"	1
# "banana"	"nan"	0
# "banana"	"wxyz"	0
# "banana"	"abanana"	0


def solution(my_string, is_suffix):
    answer = 0
    if my_string.endswith(is_suffix):
        answer = 1

    return answer


solution("banana", "ana")

# %%
