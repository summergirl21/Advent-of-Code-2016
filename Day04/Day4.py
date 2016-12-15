def main():
    print("hello")
    input = open("Day4_input.txt", 'r')
    letters = "abcdefghijklmnopqrstuvwxyz"
    nums = "0123456789"
    counts = {}
    sum = 0


    for line in input:
        for char in letters:
            counts[char] = 0
        #print(line)
        room = ""
        checksum = ""
        bcount = 0
        room_name = ""
        new_name = ""
        for char in line:
            #print(char)
            if char in letters:
                if bcount == 1:
                    checksum += char
                else:
                    #print("adding to " + char)
                    counts[char] += 1
                    room_name += char
            elif char in nums:
                room += char
            elif char == "[":
                bcount += 1
        #print(room)
        #print(checksum)
        #print(counts)
        for char in room_name:
            i = letters.index(char)
            l = letters[(i+int(room))%len(letters)]
            new_name += l
        #print(new_name)
        if new_name == "northpoleobjectstorage":
            print("found it")
            print(new_name)
            print(room)

        sorted_counts = sort_dict(counts)
        #print(sorted_counts)
        sorted_counts = sorted_counts[:5]
        check = ""
        for (k, v) in sorted_counts:
            check += k
        #print(check)
        if check == checksum:
            sum += int(room)
        #print("\n")
    print(sum)

def sort_dict(d):
    l = [(k, v) for k,v in d.items()]
    #print(l)
    l.sort(key=lambda x:x[0])
    #print(l)
    l.sort(key=lambda x:x[1], reverse=True)
    #print(l)
    return l

if __name__ == "__main__":
    main()