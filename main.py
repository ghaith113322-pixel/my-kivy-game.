
from kivy.app import App
from kivy.uix.button import Button

class GhaithGame(App):
    def build(self):
        return Button(text='Welcome Ghaith! Your game is ready.')

if __name__ == '__main__':
    GhaithGame().run()
