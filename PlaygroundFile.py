my_string = "Hello, world"
print(my_string)


def string_bits(str):
    temp = ""
    for i in range(0, len(str), 2):
        temp = temp + str[i]
    return temp

def string_splosion(str):
  temp = ""
  for i in range(0, len(str)):
    temp = temp + str[0:i+1]
  return temp

def last2(str):
    count = 0
    test_string = str[-2:]
    for i in range(0, len(str)-2):
        if str[i:i+2] == test_string:
            count += 1
    return count


def array_count9(nums):
    count = 0
    for i in nums:
        if i == 9:
            count += 1
    return count


def array_front9(nums):
    test_arr = nums[:5]
    for i in test_arr:
        if i == 9:
            return True
    return False


def array123(nums):
    for i in range(0, len(nums)-2):
        if nums[i] == 1 and nums[i+1] == 2 and nums[i+2] == 3:
            return True
    return False


print(last2('axxxaaxx'))