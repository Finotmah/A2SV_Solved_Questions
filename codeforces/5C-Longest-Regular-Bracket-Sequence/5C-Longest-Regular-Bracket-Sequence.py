s = input()

stack = [-1]
max_l = 0
n_valid  = 0


for i in range(len(s)):
    if s[i] == '(':
        stack.append(i)
    else:
        if stack:
            stack.pop()

        if not stack:
            stack.append(i)
        else:
            leng = i - stack[-1]
            if leng > max_l:
                max_l = leng
                n_valid = 1
            elif leng == max_l:
                n_valid += 1
if max_l == 0:
    print('0 1')
else:
    print(max_l,n_valid)