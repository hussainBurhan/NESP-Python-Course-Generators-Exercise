# Import the sys module to access system-related functionality
import sys

# Define a generator function named 'my_gen' that yields numbers up to 'n'
def my_gen(n: int):
    start = 0
    while start < n:
        print(f'My_range is returning: {start}')
        yield start
        start += 1

# Create a generator object 'gen_list' using the 'my_gen' function with n=10
gen_list = my_gen(10)

# Print the first three values yielded by the generator
print(next(gen_list))
print(next(gen_list))
print(next(gen_list))

# Print the size (in bytes) of the generator object
print(f'This generator takes {sys.getsizeof(gen_list)} bytes')

# Separator for output clarity
print('x'*20)

# Create a list 'itr_list' by iterating through the generator
itr_list = []
for val in gen_list:
    itr_list.append(val)

# Print the size (in bytes) of the list
print(f'This normal list takes {sys.getsizeof(itr_list)} bytes')
