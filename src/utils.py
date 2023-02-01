import numpy as np

from user import User
from environment import Environment
from platform_ import Platform

from uidesign import UIDesign


def get_random_user():
    '''
    DocString
    '''
    age = np.random.choice(["teen", "young", "adult", "elder"])
    gender = np.random.choice(["male", "female", "notObt"])
    # education = np.random.choice(["high school", "college", "graduate"])
    experience = np.random.choice(["basic", "advanced"])
    emotion = np.random.choice(["frustrated", "happy", "neutral"])
    random_ui = get_random_ui()
    preferences = {'layout': random_ui.layout,
                   'font_size': random_ui.font_size,
                   'color_scheme': random_ui.color_scheme}

    print("created this user: age {}, experience {}, emotion{}, preferences {}".format(
        age, experience, emotion, preferences
    ))
    return User(age, gender, emotion, experience, preferences)

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
    platform_os = np.random.choice(["windows", "android", "ios", "linux"])
    screen_size = np.random.uniform(low=[0, 0], high=[1920, 1080])
    return Platform(device,platform_os,screen_size)

def get_random_ui():
    layout = np.random.choice(["grid", "list"])
    color_scheme = np.random.choice(["light", "dark"])
    font_size = np.random.choice(["default", "small", "big"])
    print("\tcreated this UI: {} layout, {} color_scheme, {} font_size".format(
        layout,
        color_scheme,
        font_size
    ))
    return UIDesign(layout,color_scheme,font_size)

