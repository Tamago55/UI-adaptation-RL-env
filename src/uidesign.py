import numpy as np

class UIDesign:

    def __init__(self, layout, functionality, color, font_size):
        self.layout = layout
        self.functionality = functionality
        self.color_scheme = color
        self.font_size = font_size

        self.MAX_font_size = 16
        self.MIN_font_size = 12
        

    def changeLayout(self, layout):
        #layout may be one of these: ["default", "compact", "extended"]
        self.layout = layout

    def changeFunctionality(self, functionality):
        # functionality may be one of these: ["basic", "advanced", "expert"]
        self.functionality = functionality

    def changeColor_scheme(self, color_scheme):
        # Color scheme might be one of these: ["light", "dark"]
        self.color_scheme = color_scheme

    def get_state(self):
        return {
            'layout': self.layout,
            'functionality': self.functionality,
            'color_scheme': self.color_scheme,
            'font_size': self.font_size
        }
