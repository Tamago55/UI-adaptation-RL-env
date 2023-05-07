from enum import Enum

class LOCATION(Enum):
    indoor = 0
    outdoor = 1

class LIGHT(Enum):
    dark = 0
    ambient = 1
    bright = 2


class Environment:
    '''
        * location = [indoor, outdoor]
    '''
    def __init__(self, location):
        self.location = location

    def get_state(self):
        return {
            'environment': {
                'location': LOCATION[self.location].value
            }
        }
    
    def info(self):
        print("\tlocation: {}".format(
            self.location
        ))
