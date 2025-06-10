def snake(num):
    max = num * num
    size = 1
    count = 0
    while size*2 < max:
        size *= 2
        count += 1
    return count

def arithmetic_operation(statement):
    parts = statement.split()
    a = int(parts[0])
    op = parts[1]
    b = int(parts[2])
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    elif op == '*':
        return a * b
    elif op == '//':
        return -1 if b == 0 else a // b
print(arithmetic_operation("15 // 2"))
