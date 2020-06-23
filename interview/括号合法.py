# 题目很简单，输入一个字符串，其中包含 [](){} 六种括号，请你判断这个字符串组成的括号是否合法。

# Input: "()[]{}"
# Output: true

# Input: "([)]"
# Output: false

# Input: "{[]}"
# Output: true


def is_valid(str):
    i = 0  # 分别表示‘()’、'[]'、'{}'
    j = 0
    k = 0
    for c in str:
        if c == '(':
            i += 1
        if c == ')':
            i -= 1
            if i % 2 == j % 2 and i % 2 == k % 2:
                continue
            else:
                return False
        if c == '[':
            i += 1
        if c == ']':
            i -= 1
            if i % 2 == j % 2 and i % 2 == k % 2:
                continue
            else:
                return False
        if c == '{':
            i += 1
        if c == '}':
            i -= 1
            if i % 2 == j % 2 and i % 2 == k % 2:
                continue
            else:
                return False

    if i == j == k == 0:
        return True
    else:
        return False


if __name__ == '__main__':
    str = '()[]][]{}[]()['
    print(is_valid(str))
