def swap_case(s):
    x =''
    for c in s:
        if c.isupper():
            x += c.lower()
        else:
            x += c.upper()
    return x 

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
