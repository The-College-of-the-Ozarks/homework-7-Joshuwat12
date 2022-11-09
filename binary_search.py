# binary_search.py


# Function definition
def binary_search(list, value, offset=0):
  # Bonus
  if list != sorted(list):
    print("The list is not sorted")
    return None

  # Base case
  if len(list) == 0:
    return None

  middle = len(list) // 2
  midVal = list[middle]
  if midVal == value:
    return middle + offset
  if midVal < value:
    # The right half
    return binary_search(list[(middle + 1):], value, offset + middle + 1)

  # The left half
  return binary_search(list[:middle], value, offset)


# Input
nums = input("Enter a sorted list of integers separated by commas: ")
search = int(input("Enter the value to search for in the list: "))

# Computation
nums = nums.split(",")
for n in range(len(nums)):
  nums[n] = int(nums[n])
# The parameter "offset" is optional with a default value, so I don't have to pass an argument for it.
result = binary_search(nums, search)

# Output
if result is None:
  print(search, "was not found")
else:
  print(search, "was found at index", result)