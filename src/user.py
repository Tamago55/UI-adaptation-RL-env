import numpy as np
from enum import Enum

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
        current_f_size = current_ui_design.font_sizes[current_ui_design.font_size]
        initial_f_size = initial_ui_design.font_sizes[initial_ui_design.font_size]
        if (np.abs(current_f_size - initial_f_size) <= 2):
            self.emotion = np.random.choice(["happy","neutral"])
        else:
            self.emotion = 'frustrated'

    def get_satisfaction(self, ui_design):
        '''
        Based on the user preference, and given a UIDesign;
        What is the satisfaction for this user using this uiDesign?

        '''
        score = 0
        if 'font_size' in self.preferences and self.preferences['font_size'] == ui_design.font_size:
            score = score + 1
        if 'layout' in self.preferences and self.preferences['layout'] == ui_design.layout:
            score = score + 1
        if 'color_scheme' in self.preferences and self.preferences['color_scheme'] == ui_design.color_scheme:
            score = score + 1
        
        if self.emotion == 'frustrated':
            score = score - 1
        if self.emotion == 'happy':
            score = score + 1
        if self.emotion == 'neutral':
            pass
        return score

    def get_state(self):
        return {
            'user': {
                'age': AGE[self.age].value,
                'gender': GENDER[self.gender].value,
                'emotion': EMOTION[self.emotion].value,
                'experience': EXPERIENCE[self.experience].value 
            }
        }
    
    def info(self):
        print("\tage: {}\n\tgender: {}\n\temotion: {}\n\tpreferences: {}".format(
            self.age,
            self.gender,
            self.emotion,
            self.preferences
        ))

