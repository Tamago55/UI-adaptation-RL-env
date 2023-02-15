from enum import Enum

class LOCATION(Enum):
    indoor = 0
    outdoor = 1


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
