# 괄호로 된 입력값이 올바른지 판별
# input : ()[]{}
# output : true


class StackValid:
    def isValid(self, s: str) -> bool:
        stack = []
        table = {
            ')': '(',
            '}': '{',
            ']': '[',
        }
        for char in s:
            if char not in table:
                print(char)
                stack.append(char)
            elif not stack or table[char] != stack.pop():
                return False
        return len(stack) == 0


if __name__ == '__main__':
    a = "()[]{}"
    stack = StackValid()
    print(stack.isValid(a))
