
class UIDesign:
    
    def __init__(self, layout, color, font_size):
        self.layout = layout
        self.color_scheme = color
        self.font_size = font_size

        self.font_sizes = {
            'big': 16,
            'default': 14,
            'small': 12 
        }

    def change_layout(self, layout):
        #layout may be one of these: ["grid", "list"]
        self.layout = layout

    def change_color_scheme(self, color_scheme):
        # Color scheme might be one of these: ["light", "dark"]
        self.color_scheme = color_scheme

    def change_font_size(self, font_size):
        # Color scheme might be one of these: ["default", "small", "big"]
        self.font_size = self.font_sizes[font_size]


    def get_state(self):
        return {
            'layout': self.layout,
            'color_scheme': self.color_scheme,
            'font_size': self.font_size
        }
