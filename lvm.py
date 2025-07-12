n = int(input())
stack = []
arr= []
reg = 0

for i in range(n):
    a = list(input().split())
    
    arr.append(a)

i = 0
while i < n:
    line = arr[i]
    op = line[0]

    if op == "PUSH":
        stack.append(int(line[1]))
        i += 1
    elif op == "STORE":
        reg = stack.pop()
        i += 1
    elif op == "LOAD":
        stack.append(reg)
        i += 1
    elif op == "PLUS":
        a = stack.pop()
        b = stack.pop()
        stack.append(a + b)
        i += 1
    elif op == "TIMES":
        a = stack.pop()
        b = stack.pop()
        stack.append(a * b)
        i += 1
    elif op == "IFZERO":
        a = stack.pop()
        if a == 0:
            i = int(line[1])
        else:
            i += 1
    elif op == "DONE":
        print(stack[-1])
        break
