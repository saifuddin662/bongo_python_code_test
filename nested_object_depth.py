# create person class following question
class Person(object):
    def __init__(self, first_name, last_name, father):
        self.first_name = first_name
        self.last_name = last_name
        self.father = father

# printing depth of objects and dictionary
def print_depth(data, depth):
  for key, value in data.items():
    # checking person object and convert to dictionary
    if isinstance(value, Person):
        value = vars(value)

    # check value as dictionary and print its depth depth
    if isinstance(value, dict):
        print(key, depth)
        depth += 1
        print_depth(value, depth)
        depth -= 1
    else:
        print("{0} {1}".format(key, depth))

# call print_depth() from main
if __name__ == "__main__":
    person_a = Person('User', '1', None)
    person_b = Person('User', '2', person_a)
    sample_dictionary = {'key1': 1,'key2': {'key3': 1,'key4': {'key5': 4, 'user': person_b,}},}
    initial_depth = 1
    print_depth(sample_dictionary, initial_depth)