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

print(string_splosion(my_string))