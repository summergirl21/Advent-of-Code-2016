import sys
import math
def main():
    print("Hello")
    input = readInput()
    distance = calculatePosition(input)
    print(distance)
    print("Bye")

def readInput():
    input = sys.stdin.readline()
    input = input.split(", ")
    #for move in input:
        #print(move)
    return input;

def calculatePosition(input):
    locations = []
    x = 0
    y = 0
    #0: north, 1: east, 2:south, 3:west,
    orientation = 0
    for move in input:
        if move[0] == "R":
            orientation = (orientation + 1) % 4
        elif move[0] == "L":
            orientation = (orientation - 1) % 4
        else:
            print("error, turn not valid, turn: " + str(move(0)))
        #TODO make this a switch statment
        m = 0
        while(m < int(move[1:])):
            if orientation == 0:
                y += 1
            elif orientation == 1:
                x += 1
            elif orientation == 2:
                y -= 1
            elif orientation == 3:
                x -= 1
            else:
                print("error: orentation out of range, orientation: " + str(orientation))
            m += 1
        #print(move)
        #print("[" + str(x) + ", " + str(y) + "]" + " move: " + move)
            if not (x, y) in locations:
                locations.append((x, y))
            else:
                distance = abs(x) + abs(y)
                print("they cross at " + "[" + str(x) + ", " + str(y) + "]" + " distance: " + str(distance))
    print(locations)
    print("x: " + str(x) + " y: " + str(y))
    distance = abs(x) + abs(y)
    return distance

if __name__ == "__main__":
    main()