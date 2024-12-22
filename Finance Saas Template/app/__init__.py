from kivymd.app import MDApp
from kivy.core.window import Window
from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder

height = 650
width = 1050
Window.size = (width, height)

Builder.load_string("""

#: import Home views.home.Home

#: import BackgroundBox widgets.backgrounds.BackgroundBox
#: import TextField widgets.textfield.TextField
#: import Factory kivy.factory.Factory

<sp@SpinnerOption>:
    font_size: '10sp'
    bold: True
    color:  [0,0,0,1]
    background_color: [0,0,0,0]
    background: ''
    font_style: "Label"
    role: "medium"
    spacing: "1dp"
    canvas.before:
        Color:
            rgba: rgba("#f5f5f5")
        RoundedRectangle:
            size: self.size
            pos: self.pos
            radius: [5,5,5,5]

<MainWindow>:
    orientation: 'vertical'
    canvas.before:
        Color:
            rgba: rgba("#ffffff")
        Rectangle:
            size: self.size
            pos: self.pos

    ScreenManager:
        id: screen_manager

        Home:
            name: 'home_screen'

""")


class MainWindow(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)


class MainApp(MDApp):
    body = "assets/fonts/OpenSans-Regular.ttf"
    bold = "assets/fonts/OpenSans-Bold.ttf"
    semibold = "assets/fonts/OpenSans-Semibold.ttf"

    def build(self):
        return MainWindow()


if __name__ == "__main__":
    MainApp().run()
