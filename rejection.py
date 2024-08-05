import random

def random_choice():
    items = ['apple', 'banana', 'cherry', 'date']
    return random.choice(items)

def random_integer():
    return random.randint(1, 100)

def shuffle_list():
    my_list = [1, 2, 3, 4, 5]
    random.shuffle(my_list)
    return my_list

if __name__ == "__main__":
    print("Random choice from list:", random_choice())
    print("Random integer between 1 and 100:", random_integer())
    print("Shuffled list:", shuffle_list())
