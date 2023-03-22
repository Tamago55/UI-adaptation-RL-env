import numpy as np

from user import User
from environment import Environment
from platform_ import Platform

from uidesign import UIDesign


def get_random_user(verbose=False):
    '''
    DocString
    '''
    # age = np.random.choice(["teen", "young", "adult", "elder"])
    age = np.random.choice(["adult", "elder"])
    gender = np.random.choice(["male", "female", "notObt"])
    # education = np.random.choice(["high school", "college", "graduate"])
    experience = np.random.choice(["basic", "advanced"])
    emotion = np.random.choice(["frustrated", "happy", "neutral"])
    random_ui = get_random_ui()
    preferences = {'layout': random_ui.layout,
                   'font_size': random_ui.font_size,
                   'color_scheme': random_ui.color_scheme}
    if verbose:
        print("created this user: age {}, experience {}, emotion{}, preferences {}".format(
            age, experience, emotion, preferences
        ))
    return User(age, gender, emotion, experience, preferences)

def get_random_environment():
    '''
    DocString
    '''
    location = np.random.choice(["indoor", "outdoor"])
    # location = "indoor"
    return Environment(location)

def get_random_platform():
    '''
    DocString
    '''
    device = np.random.choice(["desktop", "tablet", "mobile"])
    platform_os = np.random.choice(["windows", "android", "ios", "linux"])

    # device = np.random.choice(["desktop", "mobile"])
    # device = "desktop"
    ''' if device == "desktop":
        platform_os = np.random.choice(["windows", "ios", "linux"])
        # platform_os = "windows"
    else:
        platform_os = np.random.choice(["android", "ios"])
        # platform_os = "android"
    '''
    
    #platform_os = np.random.choice(["windows", "android", "ios", "linux"])

    screen_size = np.random.choice(["small", "big","default"])
    #screen_size = np.random.uniform(low=[0, 0], high=[1920, 1080])
    return Platform(device,platform_os,screen_size)

def get_random_ui(verbose=False):
    layout = np.random.choice(["grid", "list"])
    color_scheme = np.random.choice(["light", "dark"])
    font_size = np.random.choice(["default", "small", "big"])
    if verbose:
        print("\tcreated this UI: {} layout, {} color_scheme, {} font_size".format(
            layout,
            color_scheme,
            font_size
        ))
    return UIDesign(layout,color_scheme,font_size)

