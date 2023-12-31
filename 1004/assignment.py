class stack:
    def __init__(self):  # 스택 객체 생성
        self.items = []
    def push(self, item):  # 스택 요소 추가 push(.append())
        self.items.append(item)
    def pop(self):   # 스택 요소 삭제 pop()
        return self.items.pop()

acc = stack()
str = input().split()
x = 0

for c in str:
    x = 0
    if c == '+':
        n1 = acc.pop()
        n2 = acc.pop()
        x = n2 + n1 
    elif c == '*':
        n1 = acc.pop()
        n2 = acc.pop()
        x = n2 * n1
    elif c == '-':
        n1 = acc.pop()
        n2 = acc.pop()
        x = n2 - n1 
    elif c == '/':
        n1 = acc.pop()
        n2 = acc.pop()
        x = n2 / n1
    elif c >= '0' and c <= '9':
        x = int(c)
    acc.push(x)

x = acc.pop()
print(x)