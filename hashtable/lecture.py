def my_hash(s):
    sb = s.encode()
    total = 0
    for b in sb:
        total +=　
    return total

my_array = [None] * 8
print(f"my_array {my_array}")

#storing a value
hash_index = my_hash("hello world") % 8
print(f"hash_index {hash_index}")

my_array[hash_index] = 'my value'
print(f"my_array {my_array}")

#get a value
hash_index = my_hash("hello world") % 8
print(my_array[hash_index])
