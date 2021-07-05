def reverse(txt):
    stack = []
    i = 0
    print(txt)
    for c in txt:
        if c == '(':
            stack.append(i)
        elif c == ')':
            if len(stack) == 0:
                print("Hay un ) de más.")
                return
            l = stack.pop()
            txt = txt[0:l] + (txt[l+1:i])[::-1] + txt[i+1:]
            i -= 2
            print(txt)
        i += 1


reverse(input())
