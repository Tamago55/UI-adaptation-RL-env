import gym
from gym import spaces
import numpy as np

class UIAdaptationEnv (gym.Env):
    '''
    DocString
    '''

    metadata = {"render_modes": ["human", "rgb_array"], "render_fps": 4}

    def __init__(self,render_mode=None):
        self.state = None
        self.user = None
        self.platform = None
        self.environment = None
        self.uidesign = None

        # We have 4 actions, corresponding to "NoOperate", "DefaultLayout", "left", "down", "right"
        self.action_space = spaces.Discrete(2)


        self.observation_space = gym.spaces.Dict({
            'layout': gym.spaces.Discrete(2),
            'color': gym.spaces.Discrete(2),
            'size': gym.spaces.Discrete(3),
            'user': gym.spaces.Dict({
                'age': gym.spaces.Discrete(4),
                # 'gender': gym.spaces.Discrete(2),
                'emotion': gym.spaces.Discrete(3),
                'experience': gym.spaces.Discrete(10)
            }),
            'platform': gym.spaces.Dict({
                'screen_size': gym.spaces.Box(low=np.array([0, 0]), high=np.array([1920, 1080]), dtype=np.float32),
                'device': gym.spaces.Discrete(3),
                'os': gym.spaces.Discrete(3)
            }),
            'environment': gym.spaces.Dict({
                'location': gym.spaces.Discrete(2),
                #'time': gym.spaces.Discrete(24)
            })
        })


        # assert render_mode is None or render_mode in self.metadata["render_modes"]
        self.render_mode = render_mode

    def render(self):
        pass
        # return super().render()

    def step(self, action):
        pass
        #return super().step(action)
