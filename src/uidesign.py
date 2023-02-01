
from enum import Enum

class LAYOUT(Enum):
    grid = 0
    list = 1

class COLOR_SCHEME(Enum):
    light = 0
    dark = 1

class FONT_SIZE(Enum):
    default = 0
    small = 1
    big = 2

class UIDesign:
    def __init__(self, layout, color, font_size):
        self.font_sizes = {
            'big': 16,
            'default': 14,
            'small': 12 
        }
        self.layout = layout
        self.color_scheme = color
        self.font_size = font_size

        ### CREATE THE APP TO DISPLAY THE UI
        #self.ui = App()
        #self.ui_thread = Thread(target=self.ui.showUI())
        # self.ui_thread.start()

    def change_layout(self, layout):
        #layout may be one of these: ["grid", "list"]
        self.layout = layout

    def change_color_scheme(self, color_scheme):
        # Color scheme might be one of these: ["light", "dark"]
        self.color_scheme = color_scheme

    def change_font_size(self, font_size):
        # Color scheme might be one of these: ["default", "small", "big"]
        # self.font_size = self.font_sizes[font_size]
        self.font_size = font_size

    def render(self):
        print("\tlayout: {}\n\tcolor_scheme: {}\n\tfont_size: {}".format(
            self.layout,
            self.color_scheme,
            self.font_size
        ))
        # self.ui.render(self)

    def get_state(self):
        return {
            'layout': LAYOUT[self.layout].value,
            'color_scheme': COLOR_SCHEME[self.color_scheme].value,
            'font_size': FONT_SIZE[self.font_size].value
        }
