nums = [1, 2, 3, 4, 5]

it = iter(nums)

while True:
    try:
        print(next(it))

    except StopIteration:
        break



def fibonacci(n):
    p = pp = 1
    for i in range(n):
        if i in [0, 1]:
            yield 1
        else:
            n = p + pp
            pp, p = p, n
            yield n

fibs = list(fibonacci(10))
print(fibs)