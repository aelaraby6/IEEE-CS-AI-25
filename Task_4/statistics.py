import math

arr = []


def get_numbers():
    global arr
    n = int(input("Enter the number of elements: "))

    for i in range(n):
        element = int(input(f"Enter element {i+1}: "))  
        arr.append(element)


def find_min(sample):
    if len(sample) == 0:
        print("arr is empty !")
        return

    minElement = sample[0]
    for x in sample:
        if x < minElement:
            minElement = x
    
    return minElement


def find_max(sample):
    if len(sample) == 0:
        print("arr is empty !")
        return

    maxElement = sample[0]
    for x in sample:
        if x > maxElement:
            maxElement = x
    
    return maxElement


def find_mean(sample):
    if len(sample) == 0:
        print("arr is empty !")
        return

    return sum(sample) / len(sample)

def find_mode(sample):
    if len(sample) == 0:
        print("arr is empty!")
        return None

    frequency = {}  
    for num in sample:
        if num in frequency:
            frequency[num] += 1
        else:
            frequency[num] = 1

    max_count = max(frequency.values())  
    modes = [key for key, value in frequency.items() if value == max_count]  

    return modes  

def find_median(sample):
    if len(sample) == 0:
        print("arr is empty !")
        return
    
    sample.sort()
    mid  = len(sample) // 2

    if len(sample) & 1 :
        return sample[mid]
    else:
        return ((sample[mid - 1] + sample[mid]) / 2)


def find_range(sample):
    if len(sample) == 0:
        print("arr is empty !")
        return
    
    return max(sample) - min(sample)


def find_variance(sample):
    if len(sample) == 0:
        print("arr is empty !")
        return
    
    n = len(sample)
    mean = find_mean(sample)
    squaredDiffs = [(x - mean) ** 2 for x in sample]
        
    return sum(squaredDiffs) / (n - 1)  


def find_STD(sample):
    if len(sample) == 0:
        print("arr is empty !")
        return 0 

    return math.sqrt(find_variance(sample))

def find_Quariles(sample):
    if len(sample) == 0:
        print("arr is empty !")
        return

    sample.sort()

    Q2 = find_median(sample)

    mid = len(sample) // 2

    if len(sample) % 2 == 0:
        lower_half = sample[:mid]  
        upper_half = sample[mid:]  
    else:
        lower_half = sample[:mid]  
        upper_half = sample[mid+1:]  

    Q1 = find_median(lower_half)  
    Q3 = find_median(upper_half) 

    return Q1,Q2,Q3

def find_IQR(sample):
    Q1, _, Q3 = find_Quariles(sample)
    return Q3 - Q1  

get_numbers()

print("Min:", find_min(arr))
print("Max:", find_max(arr))
print("Mean:", round(find_mean(arr), 2))
print("Mode:", find_mode(arr))
print("Median:", find_median(arr))
print("Range:", find_range(arr))
print("Variance:", round(find_variance(arr), 2))
print("Standard Deviation:", round(find_STD(arr), 5))
print("Quartiles:", find_Quariles(arr))
print("Interquartile Range (IQR):", find_IQR(arr))
12











