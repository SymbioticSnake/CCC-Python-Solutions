def infect_check(people_compare, num_initial_people, rate_infect):
    exp = 0
    day_count = 0
    infected = int(num_initial_people)

    while infected <= int(people_compare):
        day_count += 1
        exp += 1

        infected += int(num_initial_people)*int(rate_infect)**exp

    return day_count

def main():
    p = input()
    n = input()
    r = input()

    print(infect_check(p, n, r))

if __name__ == "__main__": main()