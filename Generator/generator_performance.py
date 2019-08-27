import os
import psutil


def memory_usage_psutil():
    pid = os.getpid()
    py = psutil.Process(pid)
    return py.memory_info()[0] / 2.**30  # memory use in GB


import random
import time


names = ['John', 'Eric', 'Henry', 'Minna', 'Tony', 'Kanye']
majors = ['Math', 'CS', 'Food', 'Civil', 'CS', 'Music']

print(
    f'Memory (Before): {memory_usage_psutil()*1000}Mb')


def people_list(num_people):
    result = []
    for i in range(num_people):
        person = {
            'id': i,
            'name': random.choice(names),
            'major': random.choice(majors)
        }
        result.append(person)
    return result


def people_generator(num_people):
    for i in range(num_people):
        person = {
            'id': i,
            'name': random.choice(names),
            'major': random.choice(majors)
        }
        yield person


# t1 = time.time()
# print('Running people_list(1000000)')
# people = people_list(1000000)
# t2 = time.time()

# print(
#     f'Memory (After): {memory_usage_psutil()*1000}Mb')
# print(f'Ran in {t2 - t1}s')

print('#------------------------------------------------------------------------#')

t1 = time.time()
print('Running people_generator(1000000)')
people = people_generator(1000000)
t2 = time.time()

print(
    f'Memory (After): {memory_usage_psutil()*1000}Mb')
print(f'Ran in {t2 - t1}s')
