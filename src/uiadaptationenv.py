import gym
from gym import spaces
import numpy as np
from user import User
from platform_ import Platform
from environment import Environment
from uidesign import UIDesign
import utils

import copy

class UIAdaptationEnv(gym.Env):
    
    metadata = {"render_modes": ["human", "rgb_array"], "render_fps": 4}
    actions = {
        0: 'noOperate',
        1: 'Layout to grid',
        2: 'Layout to list',
        3: 'Color to light',
        4: 'Color to dark',
        5: 'Default size',
        6: 'Small size',
        7: 'Big size'
    }

    def __init__(self,render_mode=None):
        self.user = utils.get_random_user()
        self.platform = utils.get_random_platform()
        self.environment = utils.get_random_environment()
        self.uidesign = utils.get_random_ui()
        
        self.state = self.get_observation()

        # We have 8 actions, corresponding to:
        # NoOperate,
        # GridLayout, List Layout,
        # Dark theme, Light theme
        # Default font_size, Small font_size, Big font_size
        
        # self.action_space = spaces.Discrete(8)
        self.action_space = spaces.Discrete(7)

        '''
        Layout (2), Colour (2), FSize (3) = 12 combinations
        user = 3 emotions
        platform = 2 posibilities (Windows-desktop OR mobile android)
        environment = 2 posibilities (in/out door)
        Total possibilities = 12*3*2*2*3 = 144 * 3
        '''
        self.observation_space = gym.spaces.MultiDiscrete([ 2, 2, 3,    # layout
                                                            2, 2, 3, 3, # user pref + emotion
                                                            3, 4, 3,    # platform
                                                            2  ])       # environment

        self.observation_space_size = np.prod(self.observation_space.nvec)

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
        print("\t--Context--")
        print("\t\t-User---")
        self.user.info()
        print("\t\t-Environment---")
        self.environment.info()
        print("\t\t-Platform---")
        self.platform.info()
    
    def close (self):
        '''
        Return: None
        This method is optional. Used to cleanup all resources (threads, GUI, etc)
        '''
        pass

    def step(self, action, verbose=False):
        done = False
        info = {}
        reward = 0

        initial_design = copy.deepcopy(self.uidesign)

        penalize_flag = False

        action_num = action + 1
        #action_num = action

        if action_num == 0:
            # noop
            pass
        elif action_num == 1:
            # Change to Grid
            if self.uidesign.layout == 'grid':
                penalize_flag = True
            else:
                self.uidesign.change_layout('grid')
        elif action_num == 2:
            # Change to List
            if self.uidesign.layout == 'list':
                penalize_flag = True
            else:
                self.uidesign.change_layout('list')
        elif action_num == 3:
            # Change to Light color
            if self.uidesign.color_scheme == 'light':
                penalize_flag = True
            else:
                self.uidesign.change_color_scheme('light')
        elif action_num == 4:
            # Change to Dark color
            if self.uidesign.color_scheme == 'dark':
                penalize_flag = True
            else:
                self.uidesign.change_color_scheme('dark')
        elif action_num == 5:
            # Change to default font size.
            if self.uidesign.font_size == 'default':
                penalize_flag = True
            else:
                self.uidesign.change_font_size('default')
        elif action_num == 6:
            # Change to small font size
            if self.uidesign.font_size == 'small':
                penalize_flag = True
            else:
                self.uidesign.change_font_size('small')
        elif action_num == 7:
            # Change to big font size
            if self.uidesign.font_size == 'big':
                penalize_flag = True
            else:
                self.uidesign.change_font_size('big')

        ## if the action had no effect (repeated action), we penalize the agent.
        if penalize_flag:
            reward = -5
        else:
            # self.user.update_emotion(initial_design, self.uidesign)
            reward = self.user.get_satisfaction(self.uidesign)
            ## After an action, only if UI was updated, user emotions are updated.

        self.state = self.get_observation()
        
        self.reward_collected += reward

        # If we obtain the maxium reward (50), then the agent has adapted the UI to
        # the user preferences and achieved the `happy` emotion
        if reward >= 10 :
            done = True
        
        if verbose:
            print("ONE STEP! action {} - {} . REWARD: {} - Collected_reward: {}, DONE? {}".format(
                action,
                self.actions[action_num],
                reward,
                self.reward_collected,
                done))
            
        print("TESTING PULL REQUESTS")

        return self.state, reward, done, info


    def reset(self, *, seed = None, options = None):
        # print("RESET! CREATING A NEW UI AND CONTEXT")
        self.user = utils.get_random_user()
        self.platform = utils.get_random_platform()
        self.environment = utils.get_random_environment()
        self.uidesign = utils.get_random_ui()
        self.state = self.get_observation()
        self.reward_collected = 0
        return self.state

    def state_as_array(self, state, npArray=False):
        state_array = []
        for a in state:
            if type(state[a]) is dict:
                for b in state[a]:
                    if type(state[a][b]) is dict:
                        for c in state[a][b]:
                            state_array.append(state[a][b][c])
                    else:
                        state_array.append(state[a][b])
            else:
                state_array.append(state[a])
        if npArray:
            return np.array(state_array)
        return state_array


    def get_observation(self):
        """
            This method traduces the representation of the state into an observation
            that the gym can work with.
        """
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
        return self.state_as_array(self.state, npArray=True)