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


    def get_satisfaction(self, ui_design):
        '''
        Based on the user preference, and given a UIDesign;
        What is the satisfaction for this user using this uiDesign?
        '''
