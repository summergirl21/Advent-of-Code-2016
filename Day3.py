def main():
    print("Hello")
    input = open("Day3_input.txt", "r")
    #input = open("Day3_input_test.txt", "r")
    newinput = {0:[], 1:[], 2:[]}
    for line in input:
        line = [int(x) for x in line.split()]
        for i in range(0, 3):
            newinput[i].append(line[i])
    print(newinput[0])
    print(newinput[1])
    print(newinput[2])

    count = 0
    for i in range(0, 3):
        input = newinput[i]
        index = 0
        while index < len(input):
            sides = [input[index], input[index+1], input[index+2]]
            sides.sort()
            if sides[0] + sides[1] > sides[2]:
                print ("is valid triangle " + str(sides[0]) + " " + str(sides[1]) + " " + str(sides[2]))
                count += 1
            else:
                print("is not valid triangle " + str(sides[0]) + " " + str(sides[1]) + " " + str(sides[2]))
            index += 3
    print(count)



    # count = 0
    # for line in input:
    #     sides = [0, 0, 0]
    #     #line = [int(x) for x in line.split()]
    #     line.sort()
    #     #print(line)
    #     if line[0] + line[1] > line[2]:
    #         count += 1
    # print(count)



if __name__ == "__main__":
    main()