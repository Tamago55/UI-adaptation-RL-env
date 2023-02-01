from enum import Enum

class DEVICE(Enum):
    desktop = 0
    tablet = 1
    mobile = 2

class OS(Enum):
    windows = 0
    android = 1
    ios = 2
    linux = 3


class Platform:
    def __init__(self, device, os, screen_size):
        self.device = device
        self.os = os
        self.screen_size = screen_size

    def get_state(self):
        return {
            'platform': {
                'device': DEVICE[self.device].value,
                'os': OS[self.os].value
                # 'screen_size': self.np_random.uniform(low=[0, 0], high=[1920, 1080]),

            }
        }
        
        