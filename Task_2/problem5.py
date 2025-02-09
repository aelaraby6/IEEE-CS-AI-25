try:
    with open("simple_text.txt", "r") as file:
        content = file.read()

    words = content.lower().split()

    wordCounter = {}

    for word in words:
        if word in wordCounter:
            wordCounter[word] += 1
        else:
            wordCounter[word] = 1

    for word, count in wordCounter.items():
        print(f"{word} : {count}")

except Exception as e:
    print(f"Error Found: {e}")