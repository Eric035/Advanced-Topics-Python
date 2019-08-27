# Iterable: Needs to have __iter__()

nums = [1, 2, 3]
print(dir(nums))

i_nums = iter(nums)  # List Iterator

# What a for loop does in the background
while True:
    try:
        item = next(i_nums)
        print(item)
    except StopIteration:
        break

print(i_nums)
print(dir(i_nums))

print(nums.__str__())

x = nums.copy()
x.append(4)
print(x)
print(nums)


class MyRange():
    def __init__(self, start, end):
        self.value = start
        self.end = end

    def __iter__(self):
        return self

    def __next__(self):     # Iterators have state
        if self.value >= self.end:
            raise StopIteration
        current_val = self.value
        self.value += 1
        return current_val


nums = MyRange(1, 10)
# for num in nums:
#     print(num)

print(next(nums))

# Generator function


def my_range(start, end):
    current_val = start
    while current_val < end:
        yield current_val
        current_val += 1


nums = my_range(1, 10)
print(next(nums))
print(next(nums))
