def first_unique_char(s: str) -> int:
    counts = {}
    # {"l":1, "e":3 ...}

    for i in s:
        if i not in counts:
            counts[i] = 0
        counts[i] += 1

    # 0 l
    # 1 e
    for k, v in enumerate(s):
        if counts[v] == 1:
            return k
    return -1


print(first_unique_char("leetcode"))  # 0
print(first_unique_char("loveleetcode"))  # 2
print(first_unique_char("aabb"))  # - 1


def two_sum(nums: list[int], target: int) -> list[int]:
    for i, j in enumerate(nums):
        for y, u in enumerate(nums):
            if i == y:
                continue
            if j + u == target:
                return [i, y]
    return -1


print(two_sum([2, 7, 11, 15], 9))     # [0, 1]


def is_valid_parentheses(s: str) -> bool:
    pairs = {
        ")": "(",
        "}": "{",
        "]": "["
    }
    stack = []
    for ch in s:
        if ch in "({[":
            stack.append(ch)
        else:
            if not stack:
                return False
            top = stack.pop()
            if pairs.get(ch) != top:
                return False
    return len(stack) == 0


print(is_valid_parentheses("()"))      # True
print(is_valid_parentheses("()[]{}"))   # True
print(is_valid_parentheses("(]"))      # False
print(is_valid_parentheses("([)]"))    # False
print(is_valid_parentheses("{[]}"))   # True


def length_of_longest_substring(s: str):
    length_s = ""
    for i in s:
        if i in length_s:
            continue
        length_s += i
    return length_s


print(length_of_longest_substring("abcabcbb"))
