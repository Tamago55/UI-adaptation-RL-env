import gym
from gym import spaces
import numpy as np
from user import User
from platform_ import Platform
from environment import Environment 
from uidesign import UIDesign
import utils

import copy


class UIAdaptationEnv (gym.Env):
    '''
    DocString
    '''

    metadata = {"render_modes": ["human", "rgb_array"], "render_fps": 4}

    def __init__(self,render_mode=None):
        self.user = utils.get_random_user()
        self.platform = utils.get_random_platform()
        self.environment = utils.get_random_environment()
        self.uidesign = utils.get_random_ui()
        self.state = self.get_observation()

        # We have 4 actions, corresponding to "NoOperate", "DefaultLayout", "left", "down", "right"
        self.action_space = spaces.Discrete(8)

        self.observation_space = gym.spaces.Dict({
            'layout': gym.spaces.Discrete(2),
            'color': gym.spaces.Discrete(2),
            'size': gym.spaces.Discrete(3),
            'user': gym.spaces.Dict({
                'age': gym.spaces.Discrete(4),
                'gender': gym.spaces.Discrete(2),
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

        self.reward_collected = 0

        assert render_mode is None or render_mode in self.metadata["render_modes"]
        self.render_mode = render_mode

    def render(self):
        '''
        Returns: None
        Show the current environment state e.g., the graphical window
        This method must be implemented, but it's ok to have an empty implementation if
        rendering is not important
        '''
        self.uidesign.render()
        print("\t-----")
        self.user.info()
    
    def close (self):
        '''
        Return: None
        This method is optional. Used to cleanup all resources (threads, GUI, etc)
        '''
        pass

    def step(self, action):
        done = False
        info = {}
        reward = 0
        initial_design = copy.deepcopy(self.uidesign)
        penalize_flag = False
        if action == 0:
            # noop
            pass
        elif action == 1:
            # Change to Grid
            if self.uidesign.layout == 'grid':
                penalize_flag = True
            else:
                self.uidesign.change_layout('grid')
        elif action == 2:
            # Change to List
            if self.uidesign.layout == 'list':
                penalize_flag = True
            else:
                self.uidesign.change_layout('list')
        elif action == 3:
            # Change to Light color
            if self.uidesign.color_scheme == 'light':
                penalize_flag = True
            else:
                self.uidesign.change_color_scheme('light')
        elif action == 4:
            # Change to Dark color
            if self.uidesign.color_scheme == 'dark':
                penalize_flag = True
            else:
                self.uidesign.change_color_scheme('dark')
        elif action == 5:
            # Change to default font size.
            if self.uidesign.font_size == 'default':
                penalize_flag = True
            else:
                self.uidesign.change_font_size('default')
        elif action == 6:
            # Change to small font size
            if self.uidesign.font_size == 'small':
                penalize_flag = True
            else:
                self.uidesign.change_font_size('small')
        elif action == 7:
            # Change to big font size
            if self.uidesign.font_size == 'big':
                penalize_flag = True
            else:        
                self.uidesign.change_font_size('big')

        ## if the action had no effect (repeated action), we penalize the agent.
        if penalize_flag:
            reward = -5
        else:
            reward = self.user.get_satisfaction(self.uidesign)    
            ## After an action, only if UI was updated, user emotions are updated.
            self.user.update_emotion(initial_design, self.uidesign)

        self.state = self.get_observation()
        
        self.reward_collected += reward

        # If we obtain the maxium reward (5), then the agent has adapted the UI to
        # the user preferences and achieved the `happy` emotion
        if reward == 4:
            done = True
        print("ONE STEP! action {}. REWARD: {} - Collected_reward: {}".format(
            action,
            reward,
            self.reward_collected))
        self.render()
        return self.state, self.reward_collected, done, info

        #return super().step(action)


    def reset(self):
        print("RESET! CREATING A NEW UI AND CONTEXT")
        self.user = utils.get_random_user()
        self.platform = utils.get_random_platform()
        self.environment = utils.get_random_environment()
        self.uidesign = utils.get_random_ui()
        self.state = self.get_observation()


    def get_observation(self):
        uidesign_state = self.uidesign.get_state()
        user_state = self.user.get_state()
        environment_state = self.environment.get_state()
        platform_state = self.platform.get_state()

        self.state = {
            **uidesign_state,
            **user_state, 
            **platform_state,
            **environment_state
            }
        return self.state