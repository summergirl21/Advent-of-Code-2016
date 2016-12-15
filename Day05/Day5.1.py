import hashlib

def main():
    print("Hello")
    input = open("Day5_input.txt", "r").read()
    #print(input)
    index = 0
    password = ""

    while len(password) < 8:
        hash_input = input + str(index)
        #print(hash_input)
        hash = hashlib.md5()
        hash.update(hash_input.encode())
        hash_out = hash.hexdigest()
        #print(hash_out)
        if hash_out[:5] == "00000":
            print("found one: " + hash_out[5] + " index: " + str(index) + " input: " + str(hash_input) + " hash: " + str(hash_out))
            password += hash_out[5]
        if index%100000 == 0:
            print("index: " + str(index) + " input: " + str(hash_input) + " hash: " + str(hash_out))
        index += 1
    print(password)


if __name__ == "__main__":
    main()