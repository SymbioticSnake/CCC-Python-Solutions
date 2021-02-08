def barley_mood(s, m, l):
    if (int(s) + 2*int(m) + 3*int(l)) >= 10: return "happy"
    else: return "sad"

def main():
    s = input()
    m = input()
    l = input()

    print(barley_mood(s, m, l))

if __name__ == "__main__": main()