def cyclic_shifts(string):
    str_list = []
    str_list.append(string)

    c_shift = string[1:] + string[0]

    while c_shift not in str_list:
        str_list.append(c_shift)
        c_shift = c_shift[1:] + c_shift[0]

    return str_list

def main():
    text = input()
    string = input()

    state = "no"

    for s in cyclic_shifts(string):
        if s in text:
            state = "yes"
            break

    print(state)

if __name__ == "__main__": main()