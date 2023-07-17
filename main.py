from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.screenmanager import ScreenManager, Screen
from build_deck import BuildDeckScreen

class MenuScreen(Screen):
    def __init__(self, **kwargs):
        super(MenuScreen, self).__init__(**kwargs)
        layout = BoxLayout(orientation='vertical')
        button = Button(text='Build Deck', on_release=self.switch_to_build_deck)
        layout.add_widget(button)
        self.add_widget(layout)

    def switch_to_build_deck(self, *args):
        self.manager.current = 'build_deck'


class MainApp(App):
    def build(self):
        # Create the screen manager
        screen_manager = ScreenManager()

        # Create the screens
        menu_screen = MenuScreen(name='menu')
        build_deck_screen = BuildDeckScreen(name='build_deck')

        # Add the screens to the screen manager
        screen_manager.add_widget(menu_screen)
        screen_manager.add_widget(build_deck_screen)

        return screen_manager


if __name__ == '__main__':
    MainApp().run()
