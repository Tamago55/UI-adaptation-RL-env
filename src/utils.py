import numpy as np

from user import User
from environment import Environment
from platform_ import Platform



def get_random_user():
    '''
    DocString
    '''
    age = np.random.normal(35, 20)
    gender = np.random.choice(["male", "female"])
    education = np.random.choice(["high school", "college", "graduate"])
    experience = np.random.normal(5, 2)
    preferences = {}
    return User(gender, age, education, experience, preferences)

def get_random_environment():
    '''
    DocString
    '''
    location = np.random.choice(["indoor", "outdoor"])
    return Environment(location)

def get_random_platform():
    '''
    DocString
    '''
    device = np.random.choice(["desktop", "tablet", "mobile"])
    platform_os = np.random.choice(["Windows", "Android", "iOS", "Linux"])
    screen_size = np.random.normal(500,220) ## This should be checked.
    return Platform(device,platform_os,screen_size)

