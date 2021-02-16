# Rules syntax will be (FROM_RULE, TO_RULE)
memo = []
history = []

def substitute(ipt, endV, steps, rules):
    def __substitute(ipt, endV, steps, rules):
        

    def __find_subs(ipt, rules):
        substitutions = []

        for i in range(3):
            rule = rules[i]

            if rule[0] in ipt:
                for j in range(len(ipt)):
                    if ipt[j:j+len(rule[0])] == rule[0]:
                        sub = ipt[:j] + rule[1] + ipt[j+len(rule[0]):]
                        substitutions.append((i, j, sub))

        return substitutions

    history = __substitute(ipt, endV, steps, rules)

def main():
    R = []

    for i in range(3):
        inp = input()
        rule = tuple(inp.split())
        R.append(rule)

    sif = tuple(input().split())
    S = sif[0]; I = sif[1]; F = sif[2]

    output = substitute(I, F, int(S), R)

    for line in output:
        print(line)
    
if __name__ == "__main__": main()