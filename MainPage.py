from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.image import Image
from kivy.uix.screenmanager import Screen
import qrcode
from io import BytesIO
from kivy.core.image import Image as CoreImage

class MainPage(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        layout = BoxLayout(orientation='vertical', spacing=10, padding=10)

        # Beispiel-Daten
        entries = [
            {"name": "Fahrrad A", "fahrgestellnummer": "12345", "seriennummer": "A1"},
            {"name": "Fahrrad B", "fahrgestellnummer": "67890", "seriennummer": "B2"},
            {"name": "Fahrrad C", "fahrgestellnummer": "11223", "seriennummer": "C3"},
            {"name": "Fahrrad D", "fahrgestellnummer": "44556", "seriennummer": "D4"},
        ]

        for entry in entries:
            row_layout = BoxLayout(orientation='horizontal', spacing=5, size_hint=(1, None), height=80)

            # Name Label hinzufügen
            name_label = Label(
                text=f"Name:\n{entry['name']}",
                size_hint=(0.3, 1),
                halign="center",
                valign="middle",
            )
            name_label.bind(size=name_label.setter("text_size"))
            row_layout.add_widget(name_label)

            # Bild
            img = Image(source='dein_bild.png', size_hint=(None, None), size=(50, 50))
            row_layout.add_widget(img)

            # Fahrgestellnummer
            label_fahrgestellnummer = Label(
                text=f"Fahrgestellnummer:\n{entry['fahrgestellnummer']}",
                size_hint=(0.4, 1),
                halign="center",
                valign="middle",
            )
            label_fahrgestellnummer.bind(size=label_fahrgestellnummer.setter("text_size"))
            row_layout.add_widget(label_fahrgestellnummer)

            # Seriennummer
            label_seriennummer = Label(
                text=f"Seriennummer:\n{entry['seriennummer']}",
                size_hint=(0.4, 1),
                halign="center",
                valign="middle",
            )
            label_seriennummer.bind(size=label_seriennummer.setter("text_size"))
            row_layout.add_widget(label_seriennummer)

            # Details-Button
            details_button = Button(
                text="Details", size_hint=(0.2, 1),
                on_press=lambda instance, e=entry: self.open_details_page(e)
            )
            row_layout.add_widget(details_button)

            layout.add_widget(row_layout)

        self.add_widget(layout)

    def open_details_page(self, entry):
        self.manager.current = "details"
        self.manager.get_screen("details").populate_form(entry)