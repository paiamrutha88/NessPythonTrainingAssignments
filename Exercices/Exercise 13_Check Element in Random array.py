import numpy as np

random_array = np.random.randint(0,21,5)
print(random_array)

value = int(input("Enter a number between 0 and 21 : "))

if value in random_array:
    print(f"{value} is present in random array")
else:
    print(f"{value} is not present in random array")