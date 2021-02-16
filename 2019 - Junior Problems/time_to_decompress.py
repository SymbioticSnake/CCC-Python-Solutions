def expand_ch(num, ch=None):
    return int(num) * ch

code_list = []

lines = int(input())
for _ in range(lines):
    inp = input()
    li = inp.split()

    code_list.append(expand_ch(li[0], li[1]))

for i in code_list: print(i)