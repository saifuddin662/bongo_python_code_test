def print_depth(data, depth):
  for k, v in data.items():
    # check value as dictionary and print its depth depth
    if isinstance(v, dict):
        print(k, depth)
        depth += 1
        print_depth(v, depth)
        depth -= 1
    else:
        print("{0} {1}".format(k, depth))

# call print_depth() from main
if __name__ == "__main__":
    sample_dictionary = {'key1': 1,'key2': {'key3': 1,'key4': {'key5': 4}}}
    initial_depth = 1
    print_depth(sample_dictionary, initial_depth)