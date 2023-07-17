from kivy.uix.boxlayout import BoxLayout
from kivy.uix.carousel import Carousel
from kivy.uix.image import AsyncImage
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.popup import Popup

class CardWindow(Popup):
    def __init__(self, card, **kwargs):
        super(CardWindow, self).__init__(**kwargs)
        self.title = card['name']
        self.auto_dismiss = False

        # Create the layout for the card window
        layout = BoxLayout(orientation='horizontal')

        # Create and add the carousel
        carousel = Carousel(direction='right')
        layout.add_widget(carousel)

        # Retrieve the image URLs from the card
        image_uris = card.get('image_uris', {})

        for key, url in image_uris.items():
            img = AsyncImage(source=url)
            carousel.add_widget(img)

        # Create and add the label layout
        label_layout = BoxLayout(orientation='vertical', padding=10)
        layout.add_widget(label_layout)

        # Create and add the label
        label_text = f"Card: {card['name']}\nArtist: {card['artist']}\n\n"

        # Iterate over the desired keys and include them in the label text
        desired_keys = ['color_identity', 'keywords', 'loyalty', 'power', 'mana_cost', 'produced_mana', 'toughness', 'type_line', 'flavor_text', 'printed_text', 'rarity', 'oracle_text']
        for key in desired_keys:
            if key in card:
                value = card[key]
                print(f"Key: {key}, Value: {value}")
                print(label_text)
                if value is None:
                    value = "N/A"  # Replace None with "N/A"
                label_text += f"{key.capitalize()}: {value}\n"

        label = Label(text=label_text, halign='left', valign='top')
        label_layout.add_widget(label)

        # Create and add the close button
        close_button = Button(text='Close', size_hint=(None, None), size=(100, 50), pos_hint={'center_x': 0.5})
        close_button.bind(on_release=self.dismiss)
        label_layout.add_widget(close_button)

        self.content = layout

        def set_label_text_size(*args):
            label.text_size = label.size

        self.bind(on_open=set_label_text_size)
