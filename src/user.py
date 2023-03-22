import numpy as np
from enum import Enum
from uidesign import FONT_SIZE, LAYOUT, COLOR_SCHEME

class AGE(Enum):
    teen = 0
    young = 1
    adult = 2
    elder = 3

class GENDER(Enum):
    notObt = 0
    male = 1
    female = 2

class EMOTION(Enum):
    frustrated = 0
    happy = 1
    neutral = 2

class EXPERIENCE(Enum):
    basic = 0
    advanced = 1


class User:
    '''
        * age = [teen, young, adult, elder]
        * gender = [male, female, noOb]
        * emotion = [frustrated, happy, neutral]
        * experience = [basic, advanced]
        * preferences = {dictionary with UIDesign Preferences}
    '''

    def __init__(self, age, gender, emotion, experience, preferences):
        self.age = age
        self.gender = gender
        self.emotion = emotion
        self.experience = experience
        self.preferences = preferences

    def update_emotion(self, initial_ui_design, current_ui_design):
        '''
        
        '''
        frustrated = 0
        
        '''
        current_f_size = current_ui_design.font_sizes[current_ui_design.font_size]
        initial_f_size = initial_ui_design.font_sizes[initial_ui_design.font_size]
        if (np.abs(current_f_size - initial_f_size) >= 2):
            frustrated += 1
        '''

        if 'font_size' in self.preferences and \
            self.preferences['font_size'] == initial_ui_design.font_size and \
            not (self.preferences['font_size'] == current_ui_design.font_size):
            frustrated += 1
        if 'layout' in self.preferences and \
            self.preferences['layout'] == initial_ui_design.layout and \
            not (self.preferences['layout'] == current_ui_design.layout):
            frustrated += 1
        if 'color_scheme' in self.preferences and \
            self.preferences['color_scheme'] == initial_ui_design.color_scheme and \
            not (self.preferences['color_scheme'] == current_ui_design.color_scheme):
            frustrated += 1

        if frustrated > 1:
            self.emotion = 'frustrated'
        elif frustrated == 1:
            self.emotion = "neutral"
        else:
            self.emotion = 'happy'
        

    def get_satisfaction(self, ui_design):
        '''
        Based on the user preference, and given a UIDesign;
        What is the satisfaction for this user using this uiDesign?
        '''
        score = 0
        if 'font_size' in self.preferences and \
            self.preferences['font_size'] == ui_design.font_size:
            score += 1
        
        if 'layout' in self.preferences and \
            self.preferences['layout'] == ui_design.layout:
            score += 1
        
        if 'color_scheme' in self.preferences and \
            self.preferences['color_scheme'] == ui_design.color_scheme:
            score += 1
        
        
        # Si las preferencias del usuario == interfaz. Recompensamos mucho al agente.
        if score >=3:
            score = 10
        else:
            score = 0
        
        # if self.emotion == 'frustrated':
        #     score -= 1
        # if self.emotion == 'happy':
        #     score += 1
        # if self.emotion == 'neutral':
        #     score += 0
        return score

    def preferences_as_values(self):
        return {
            'layout': LAYOUT[self.preferences['layout']].value,
            'color_scheme': COLOR_SCHEME[self.preferences['color_scheme']].value,
            'font_size': FONT_SIZE[self.preferences['font_size']].value
        }

    def get_state(self):
        return {
            'user': {
                # 'age': AGE[self.age].value,
                # 'gender': GENDER[self.gender].value,
                'preferences': self.preferences_as_values(),
                'emotion': EMOTION[self.emotion].value
                # 'experience': EXPERIENCE[self.experience].value 
            }
        }
    
    def info(self):
        print("\tage: {}\n\tgender: {}\n\temotion: {}\n\tpreferences: {}".format(
            self.age,
            self.gender,
            self.emotion,
            self.preferences
        ))

