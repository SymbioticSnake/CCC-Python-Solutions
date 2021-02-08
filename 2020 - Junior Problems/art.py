def smallest_frame(list_of_coordinates):
    x_list = [tup[0] for tup in list_of_coordinates]
    y_list = [tup[1] for tup in list_of_coordinates]

    largest_x = None; largest_y = None; smallest_x = None; smallest_y = None

    for x in x_list:
        if largest_x == None or x > largest_x: largest_x = x
        if smallest_x == None or x < smallest_x: smallest_x = x
    
    for y in y_list:
        if largest_y == None or y > largest_y: largest_y = y
        if smallest_y == None or y < smallest_y: smallest_y = y

    maximum = (smallest_x-1, smallest_y-1)
    minimum = (largest_x+1, largest_y+1)

    return maximum, minimum

def main():
    coordinates_list = []
    num_pd = int(input())

    if 2 <= num_pd <= 100:

        for _ in range(num_pd):
            str_coors = input()
            
            if str_coors[2] == ",":
                coordinates_list.append((int(str_coors[:2]), int(str_coors[3:])))
            else:
                coordinates_list.append((int(str_coors[:1]), int(str_coors[2:])))

        for i in smallest_frame(coordinates_list):
            print(str(i[0]) + ", " + str(i[1]))

    else: print("Beyond specified inclusive limit of between 2 to 100")

if __name__ == "__main__": main()