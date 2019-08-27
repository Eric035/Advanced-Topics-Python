# Generators

# Normal function


def square(nums):
    results = []
    for num in nums:
        results.append(num**2)
    return results


my_nums1 = square([1, 2, 3, 4, 5])
print(my_nums1)

# Generator version


def squareGen(nums):
    for i in nums:
        yield (i**2)


my_nums2 = squareGen([1, 2, 3, 4, 5])
print(next(my_nums2))
print(next(my_nums2))
print(next(my_nums2))
print(next(my_nums2))
print(next(my_nums2))
# print(next(my_nums2)) (StopIteration: Generator has been exhausted)

# List comprehension
nums = [1, 2, 3, 4, 5]
my_nums = [x**2 for x in nums]
print(my_nums)


# Generator list comprehension: use round brackets
my_nums_gen = (x**2 for n in nums)
print(my_nums_gen)
