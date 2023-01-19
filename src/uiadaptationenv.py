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


        self.observation_space = spaces.Dict(
            dict(
                desired_goal=spaces.Box(-np.inf, np.inf, shape=(2,)),
                achieved_goal=spaces.Box(-np.inf, np.inf, shape=(2,))
                )
            )

        size = 4
        self.observation_space = spaces.Dict(
            {
                "agent": spaces.Box(0, size - 1, shape=(2,), dtype=int),
                "target": spaces.Box(0, size - 1, shape=(2,), dtype=int),
            }
        )


        # assert render_mode is None or render_mode in self.metadata["render_modes"]
        self.render_mode = render_mode

    def render(self):
        pass
        # return super().render()

    def step(self, action):
        pass
        #return super().step(action)
