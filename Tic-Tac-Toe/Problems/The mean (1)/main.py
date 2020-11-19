count = 0
ans = 0
c = True
while c:
    val = input()
    if val == '.':
        c = False
    else:
        count += 1
        ans = ans + int(val)
print(ans / count)
