if __name__ == '__main__':
    arr = []
    N = int(input())
    while N > 0:
        input_data = input().split()
        x = input_data[0]
        
        if x == "insert":
            a = int(input_data[1])
            b = int(input_data[2])
            arr.insert(a, b)
        elif x == "print":
            print(arr)
        elif x == "remove":
            a = int(input_data[1])
            if a in arr:
                arr.remove(a)
        elif x == "append":
            a = int(input_data[1])
            arr.append(a)
        elif x == "sort":
            arr.sort()
        elif x == "pop":
            arr.pop()
        elif x == "reverse":
            arr.reverse()

        N -= 1
