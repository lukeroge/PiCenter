# generic imports
from time import localtime, strftime

# set config before importing
from kivy.config import Config
Config.set('graphics', 'resizable', 0)

# kivy imports
from kivy.app import App
from kivy.clock import Clock
from kivy.core.window import Window
from kivy.uix.tabbedpanel import TabbedPanelItem
from kivy.uix.floatlayout import FloatLayout


class Frame(FloatLayout):
    def update(self, *args):
        self.ids.status_time.text = strftime("%I:%M %p", localtime())


class StatusTab(TabbedPanelItem):
    pass


class WeatherTab(TabbedPanelItem):
    pass


class PiCenterApp(App):
    title = 'PiCenter'

    def build(self):
        # set window size
        Window.size = (800, 480)

        # initialise main panel and start updates
        frame = Frame()
        Clock.schedule_interval(frame.update, 1)
        return frame

if __name__ == '__main__':
    PiCenterApp().run()
