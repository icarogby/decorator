from time import time
from random import randint

def duration(func):
    def wrapper(n):
        start = time()
        func(n)
        end = time()

        execution_time = end - start

        return execution_time
    
    return wrapper

@duration
def bubble_sort(numbers):
    for i in range(len(numbers)):
        for j in range(len(numbers) - 1):
            if numbers[j] > numbers[j + 1]:
                numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]

    return numbers

def main():
    numbers = [randint(1, 100) for i in range(1000)]

    print(bubble_sort(numbers))

if __name__ == "__main__":
    main()
