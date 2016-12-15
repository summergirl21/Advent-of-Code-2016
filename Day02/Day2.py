def main():
    print("Hello")
    input = open("Day2_input.txt", "r")
    code = ""
    buttons = [['1', '2', '3'],
               ['4', '5', '6'],
               ['7', '8', '9']]
    buttons = [['X', 'X', '1', 'X', 'X'],
               ['X', '2', '3', '4', 'X'],
               ['5', '6', '7', '8', '9'],
               ['X', 'A', 'B', 'C', 'X'],
               ['X', 'X', 'D', 'X', 'X']]

    for line in input:
        #print(line)
        position = [2, 0] # row, column
        for move in line:
            #print(move)
            if move == "D" and position[0] < 4 and buttons[position[0]+1][position[1]] != 'X':
                position[0] += 1
            elif move == "U" and position[0] > 0 and buttons[position[0]-1][position[1]] != 'X':
                position[0] -= 1
            elif move == "L" and position[1] > 0 and buttons[position[0]][position[1]-1] != 'X':
                position[1] -= 1
            elif move == "R" and position[1] < 4 and buttons[position[0]][position[1]+1] != 'X':
                position[1] += 1
        print(position)
        code += buttons[position[0]][position[1]]
    print(code)

if __name__ == "__main__":
    main()