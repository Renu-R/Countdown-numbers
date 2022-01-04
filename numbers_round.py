from random import randint
from random import sample

def generate_target():
    return randint(100, 999)

def generate_little_numbers():
    little = [1,1,2,2,3,3,4,4,5,5,6,6,7,7,8,8,9,9,10,10]
    return sample(little, 4)

def generate_big_numbers():
    big = [25,50,75,100]
    return sample(big,2)