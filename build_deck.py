from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.dropdown import DropDown
from kivy.uix.screenmanager import Screen
from kivy.uix.textinput import TextInput
from scryfall import ScryfallDatabase
from card_window import CardWindow
from kivy.uix.label import Label

class BuildDeckScreen(Screen):
    def __init__(self, **kwargs):
        super(BuildDeckScreen, self).__init__(**kwargs)
        layout = BoxLayout(orientation='vertical')
        input_box = TextInput(multiline=True)
        layout.add_widget(input_box)
        database = ScryfallDatabase()
        deck = []
        label_text = 'no deck'
        dropdown_text = 'no deck built'

        dropdown = DropDown()
        dropdown_button = Button(text='deck list')

        def populate_dropdown(instance):
            dropdown.clear_widgets()
            options = input_box.text.split('\n')
            label_text = options[0] + 'Deck'

            for option in options:
                card = database.search_card_by_name(option)

                if card is not None:
                    deck.append(card)
                    btn = Button(text=card['name'], size_hint_y=None, height=44)
                    btn.bind(on_release=lambda btn, card=card: open_card_window(card))
                    dropdown.add_widget(btn)

            dropdown.deck = deck

        dropdown_button.bind(on_release=dropdown.open)
        dropdown.bind(on_select=lambda instance, x: setattr(dropdown_button, 'text', x))
        layout.add_widget(dropdown_button)

       # label = Label(text=label_text + 'Built')
       # layout.add_widget(label)

        button = Button(text='Update Deck')

        def open_card_window(card):
            card_window = CardWindow(card)
            card_window.open()

        button.bind(on_release=populate_dropdown)
        layout.add_widget(button)

        self.add_widget(layout)
