from PyQt5 import QtWidgets, QtCore
from threading import Thread

class UIDesign:
    
    
    def __init__(self, layout, color, font_size):
        self.font_sizes = {
            'big': 16,
            'default': 14,
            'small': 12 
        }
        self.layout = layout
        self.color_scheme = color
        self.font_size = self.font_sizes[font_size]

        ### CREATE THE APP TO DISPLAY THE UI
        self.app = QtWidgets.QApplication([])
        self.label = QtWidgets.QLabel("Hello, World!")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.button = QtWidgets.QPushButton("Click me!")
        self.button.clicked.connect(self.on_button_clicked)
        self.Qtlayout = QtWidgets.QVBoxLayout()
        self.Qtlayout.addWidget(self.label)
        self.Qtlayout.addWidget(self.button)
        self.window = QtWidgets.QWidget()
        self.window.setLayout(self.Qtlayout)
        self.window.show()
        self.ui_thread = Thread(target=self.app.exec_)
        self.ui_thread.start()



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

    def on_button_clicked(self):
        layout = self.layout
        color = self.color_scheme
        font = self.font_size
        self.label.setText("Layout: {}\nColor: {}\nFont: {}".format(layout, color, font))
    
    def render_ui(self):
        pass
