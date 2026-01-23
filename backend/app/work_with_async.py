import sys

data = [2, 4, 8]

# print(data)
# print(sys.getsizeof(data))

# data_str = [str(e) for e in data]
# data_str = {str(e) for e in data}
# data_str = {str(e): e for e in data}
data_str = (str(e) for e in data)
# print(data_str)
# print(sys.getsizeof(data_str))

# print(list(data_str))
# print(list(data_str))

# print(next(data_str))
# print(next(data_str))
# print(9999999999999)
# print(next(data_str))
# data.append(3333)
# print(next(data_str))


def generator():
    n = 1
    while True:
        print("before yield", n)
        yield n
        n += 1
        print("after yield", n)

        yield 100

        # if n == 10:
        #     return n


gen = generator()
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))