class User:

    def __init__(self, gender, age, education, experience, preferences):
        self.gender = gender
        self.age = age
        self.education = education
        self.experience = experience
        self.preferences = preferences
    
    def get_satisfaction(self, uiDesign):
        '''
        Based on the user preference, and given a UIDesign;
        What is the satisfaction for this user using this uiDesign?
        '''
