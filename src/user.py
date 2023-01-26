import numpy as np
class User:  
    '''
        * age = [teen, young, adult, elder]
        ###* gender = [male, female, noOb]
        * emotion = [frustrated, happy, neutral]
        * experience = [basic, advanced]
        * preferences = {dictionary with UIDesign Preferences}
    '''
    
    def __init__(self, age, emotion, experience, preferences):
        self.age = age
        self.emotion = emotion
        self.experience = experience
        self.preferences = preferences

    def update_emotion(self, initial_ui_design, current_ui_design):
        if (np.abs(current_ui_design.font_size - initial_ui_design.font_size) <= 2):
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
        

