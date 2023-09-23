from kivy.app import App
from kivy.lang import Builder

# GUI = Builder.load_file("gameTrabalho.kv")

KV = '''
Label:
    text: 'Test'
    font_size: 20
    text_size: self.size

'''

class AppGame(App):
    def build(self):
        return Builder.load_string(KV)

AppGame().run()
