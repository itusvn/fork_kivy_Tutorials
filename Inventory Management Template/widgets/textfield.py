from kivy.lang import Builder
from kivy.uix.textinput import TextInput

Builder.load_string('''
<TextField>:
    cursor_color: [0,0,0,1]
    foreground_color: [0,0,0,1]
    background_color: 0, 0, 0, 0
    background_normal: ''
    background_active: ''
    write_tab: False
    font_size: "11sp"
    font_name: app.body
''')
class TextField(TextInput):
    def __init__(self, **kw) -> None:
        super().__init__(**kw)
 

