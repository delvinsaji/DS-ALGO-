def func(s,index = 0):
    if index == len(s):
        b = "".join(s)
        a = int(b)**0.5
        if a == int(a):
            return "".join(s)
        else:
            return False


    if s[index] == "_":
        for i in range(10):
            s[index] = str(i)
            c = func(s,index + 1)
            if c != False:
                return c
        s[index] = "_"
    else:
        c = func(s,index + 1)
        if c != False:
            return c

    return False




s = "1_0_5"
s = list(s)
print(func(s))
