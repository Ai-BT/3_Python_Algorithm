# Day_03

# %%

# 1
# 문제 설명
# 대문자와 소문자가 섞여있는 문자열 s가 주어집니다.
# s에 'p'의 개수와 'y'의 개수를 비교해 같으면 True, 다르면 False를 return 하는 solution를 완성하세요.
# 'p', 'y' 모두 하나도 없는 경우는 항상 True를 리턴합니다. 단, 개수를 비교할 때 대문자와 소문자는 구별하지 않습니다.

# 예를 들어 s가 "pPoooyY"면 true를 return하고 "Pyy"라면 false를 return합니다.

# 제한사항
# 문자열 s의 길이 : 50 이하의 자연수
# 문자열 s는 알파벳으로만 이루어져 있습니다.

# 입출력 예
#   s	    answer
# "pPoooyY"	true
# "Pyy"	    false

s = "pPoooyY"


def solution(s):
    s = s.lower()

    p_count = s.count('p')
    y_count = s.count('y')

    return p_count == y_count


solution(s)

# %%

# 2
# 문제 설명
# 문자열 s를 숫자로 변환한 결과를 반환하는 함수, solution을 완성하세요.

# 제한 조건
# s의 길이는 1 이상 5이하입니다.
# s의 맨앞에는 부호(+, -)가 올 수 있습니다.
# s는 부호와 숫자로만 이루어져있습니다.
# s는 "0"으로 시작하지 않습니다.

# 입출력 예
# 예를들어 str이 "1234"이면 1234를 반환하고, "-1234"이면 -1234를 반환하면 됩니다.
# str은 부호(+,-)와 숫자로만 구성되어 있고, 잘못된 값이 입력되는 경우는 없습니다.


s = "-1234"


def solution(s):
    answer = int(s)

    return answer


solution(s)

# %%
