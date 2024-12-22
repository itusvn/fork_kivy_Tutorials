from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import StringProperty, ListProperty

Builder.load_string('''
<BackgroundBox>:
    padding: '10dp', '5dp', '10dp', '5dp',
    canvas.before:
        Color:
            rgba: self.color
        RoundedRectangle:
            pos: self.pos
            size: self.size
            radius: self.radius
        Ellipse:
            pos: self.pos
            size: self.size
            source: self.ellipse
                    
################################################
''')

class BackgroundBox(BoxLayout):
    color = ListProperty([1,1,1,0])
    radius = ListProperty([0.5])
    ellipse = StringProperty()
    def __init__(self, **kw) -> None:
        super().__init__(**kw)
 
