from PyQt5 import QtWidgets, QtCore, QtGui

import numpy as np

class App():
    def __init__(self):
        
        self.app = QtWidgets.QApplication([])

        self.nav_column = QtWidgets.QToolBar()
        self.nav_column.setOrientation(QtCore.Qt.Vertical)
        self.nav_column.addAction("App", self.on_app_clicked)
        self.nav_column.addAction("Preferences", self.on_preferences_clicked)

        self.nav_column.addAction("Change layout", self.on_c_layout_clicked)
        self.nav_column.addAction("Change color", self.on_c_color_clicked)
        self.nav_column.addAction("Change font", self.on_c_font_clicked)

        self.nav_column.addAction("Grid view", self.on_grid_view_clicked)
        self.nav_column.addAction("List view", self.on_list_view_clicked)

        self.nav_column.addAction("Quit", self.on_quit_clicked)


        self.grid_widget = QtWidgets.QWidget()
        self.grid_layout = QtWidgets.QGridLayout()
        self.total_products = 6
        self.products = create_products(self.total_products)
        self.init_grid()
        self.grid_widget.setLayout(self.grid_layout)


        self.preferences_widget = QtWidgets.QWidget()
        self.preferences_layout = QtWidgets.QVBoxLayout()
        self.preferences_widget.setLayout(self.preferences_layout)

        self.init_preferences()

        self.home_widget = QtWidgets.QWidget()
        self.home_layout = QtWidgets.QVBoxLayout()
        self.home_widget.setLayout(self.home_layout)

        self.current_widget = QtWidgets.QWidget()
        self.current_widget.setLayout(self.home_layout)
        # self.current_widget.setLayout(self.grid_layout)
        
        self.list_widget = QtWidgets.QListWidget()
        self.init_list()


        self.layout = QtWidgets.QHBoxLayout()
        self.layout.addWidget(self.nav_column)
        self.layout.addWidget(self.current_widget)
        self.window = QtWidgets.QWidget()
        self.window.setLayout(self.layout)
        self.window.show()
        self.app.exec_()


    def on_grid_view_clicked(self):
        if self.current_widget == self.grid_widget:
            return
        self.layout.replaceWidget(self.current_widget, self.grid_widget)
        self.current_widget.hide()
        self.current_widget = self.grid_widget
        self.grid_widget.show()

    def on_list_view_clicked(self):
        if self.current_widget == self.list_widget:
            return
        self.layout.replaceWidget(self.current_widget, self.list_widget)
        self.current_widget.hide()
        self.current_widget = self.list_widget
        self.list_widget.show()

    def showUI(self):
        self.window.show()
        self.app.exec_()

    def on_app_clicked(self):
        if self.current_widget == self.grid_widget:
            print("NOCHANGES")
            return
        self.layout.replaceWidget(self.current_widget, self.grid_widget)
        self.current_widget.hide()
        self.current_widget = self.grid_widget
        self.grid_widget.show()

    def on_preferences_clicked(self):
        if self.current_widget == self.preferences_widget:
            print("NOCHANGES")
            return
        self.layout.replaceWidget(self.current_widget, self.preferences_widget)
        self.current_widget.hide()
        self.current_widget = self.preferences_widget
        self.preferences_widget.show()

    def init_list(self):
        for i, product in enumerate(self.products):
            name, price, image_path = product
            item = QtWidgets.QListWidgetItem()
            item_widget = QtWidgets.QWidget()
            item_layout = QtWidgets.QHBoxLayout()
            item_widget.setLayout(item_layout)
            
            # Add image
            image = QtGui.QPixmap(image_path)
            image = image.scaled(100,100,QtCore.Qt.KeepAspectRatio)
            image_label = QtWidgets.QLabel()
            image_label.setPixmap(image)
            item_layout.addWidget(image_label)
            
            # Add label
            label = QtWidgets.QLabel(name)
            item_layout.addWidget(label)
            
            # Add price
            price_label = QtWidgets.QLabel(str(price))
            item_layout.addWidget(price_label)
            
            # Set widget as the item's widget
            self.list_widget.setItemWidget(item, item_widget)
            self.list_widget.addItem(item)

            

    def init_grid(self):
        for i, product in enumerate(self.products):
            name, price, image_path = product
            product_widget = ProductWidget(name, price, image_path)
            row, col = i // 2, i % 2
            self.grid_layout.addWidget(product_widget, row, col)

    def init_preferences(self):
        # UI layout group
        self.ui_layout_group = QtWidgets.QGroupBox("UI Layout")
        self.ui_layout_group.setLayout(QtWidgets.QVBoxLayout())
        self.ui_layout_grid = QtWidgets.QRadioButton("Grid")
        self.ui_layout_list = QtWidgets.QRadioButton("List")
        self.ui_layout_grid.setChecked(True)
        self.ui_layout_group.layout().addWidget(self.ui_layout_grid)
        self.ui_layout_group.layout().addWidget(self.ui_layout_list)
        self.preferences_layout.addWidget(self.ui_layout_group)
        
        # UI color group
        self.ui_color_group = QtWidgets.QGroupBox("UI Color")
        self.ui_color_group.setLayout(QtWidgets.QVBoxLayout())
        self.ui_color_light = QtWidgets.QRadioButton("Light")
        self.ui_color_dark = QtWidgets.QRadioButton("Dark")
        self.ui_color_light.setChecked(True)
        self.ui_color_group.layout().addWidget(self.ui_color_light)
        self.ui_color_group.layout().addWidget(self.ui_color_dark)
        self.preferences_layout.addWidget(self.ui_color_group)

        # UI font size group
        self.ui_font_size_group = QtWidgets.QGroupBox("UI Font Size")
        self.ui_font_size_group.setLayout(QtWidgets.QVBoxLayout())
        self.ui_font_size_small = QtWidgets.QRadioButton("Small")
        self.ui_font_size_default = QtWidgets.QRadioButton("Default")
        self.ui_font_size_big = QtWidgets.QRadioButton("Big")
        self.ui_font_size_default.setChecked(True)
        self.ui_font_size_group.layout().addWidget(self.ui_font_size_small)
        self.ui_font_size_group.layout().addWidget(self.ui_font_size_default)
        self.ui_font_size_group.layout().addWidget(self.ui_font_size_big)
        self.preferences_layout.addWidget(self.ui_font_size_group)
        
        # Save and cancel buttons
        self.save_button = QtWidgets.QPushButton("Save")
        self.cancel_button = QtWidgets.QPushButton("Cancel")
        self.save_button.clicked.connect(self.save_preferences)
        self.cancel_button.clicked.connect(self.cancel_preferences)
        self.preferences_layout.addWidget(self.save_button)
        self.preferences_layout.addWidget(self.cancel_button)
    

    def save_preferences(self):
        print("SAVED!")        
    
    def cancel_preferences(self):
        print("Canceled!")        

    def on_c_layout_clicked(self):
        print("Change layout!")        

    def on_c_color_clicked(self):
        print("Change Color!")        

    def on_c_font_clicked(self):
        print("Change font!")        

    def on_quit_clicked(self):
        self.window.close()


    def on_tab_changed(self, index):
        if index == 0:
            self.current_widget.setText("App contents")
        elif index == 1:
            self.current_widget.setText("Preferences contents")

    def render(self, ui_design):
        
        pass


def create_products(num, type=1):

    products = []
    for i in range(num):
        name = 'Product'+str(i+1)
        price = np.random.normal(10,50)
        price = int(np.abs(price) * 100) / 100
        img_path = "img.png"
        if type == 0:
            products.append(ProductWidget(name, str(price), img_path))
        else:
            products.append([name, price, img_path])
    return products


class ProductWidget(QtWidgets.QWidget):
    def __init__(self, name:str, price:float, image_path:str):
        super().__init__()
        self.layout = QtWidgets.QVBoxLayout()
        self.image = QtWidgets.QLabel()
        self.image.setMaximumSize(200,120)
        self.image.setPixmap(QtGui.QPixmap(image_path).scaled(150, 150))

        self.layout.addWidget(self.image)
        self.label = QtWidgets.QLabel(name)
        self.layout.addWidget(self.label)
        self.price = QtWidgets.QLabel(str(price) + "€")
        self.layout.addWidget(self.price)
        self.setLayout(self.layout)





if __name__ == "__main__":
    App()