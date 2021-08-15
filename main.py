import random


numlist = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]


def num() -> str:
    print("RNG")
    nam = str()
    try:
        numb = int(input("Amount of digits: "))
    except ValueError:
        print("This has to be a number")
        return
    try:
        amn = int(input("Amount of numbers to generate: "))
    except ValueError:
        print("This has to be a number")
        return
    for i in range(amn):
        for n in range(numb):
            nam = nam + nam.join(random.choice(numlist))
        print(nam)
        nam = str()
    return nam


if __name__ == '__main__':
    while True:
        num()
