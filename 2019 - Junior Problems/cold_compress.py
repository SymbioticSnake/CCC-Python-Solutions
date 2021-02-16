def cc_func(inp):
    opt = []

    c_ch = inp[0]
    ch_count = 0

    for ch in inp:
        if ch == c_ch: ch_count += 1
        else:
            opt.append(ch_count); opt.append(c_ch)
            ch_count = 1; c_ch = ch
    
    opt.append(ch_count); opt.append(c_ch)

    return opt

def main():
    output = []

    lines = int(input())

    for i in range(lines):
        inp = input()
        oLine = cc_func(inp)
        output.append(oLine)

    for i in output:
        for j in i:
            if j == i[-1]: print(j)
            else: print(j, end=" ")
            # print(j, end=" ")
        # print()

if __name__ == "__main__": main()