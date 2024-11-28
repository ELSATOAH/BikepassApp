from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.image import Image
from kivy.uix.screenmanager import Screen
import qrcode
from io import BytesIO
from kivy.core.image import Image as CoreImage

class DetailsPage(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.layout = BoxLayout(orientation="vertical", spacing=10, padding=10)

        self.fahrgestellnummer = TextInput(hint_text="Fahrgestellnummer", multiline=False, disabled=True)
        self.seriennummer = TextInput(hint_text="Seriennummer", multiline=False, disabled=True)

        self.layout.add_widget(self.fahrgestellnummer)
        self.layout.add_widget(self.seriennummer)

        button_layout = BoxLayout(size_hint=(1, None), height=50)

        # Edit-Button
        edit_button = Button(text="Edit", on_press=self.enable_editing)
        button_layout.add_widget(edit_button)

        # QR-Code-Button
        qr_button = Button(text="QR-Code", on_press=self.generate_qr_code)
        button_layout.add_widget(qr_button)

        # Zurück-Button
        #back_button = Button(text="Zurück", on_press=lambda instance: self.manager.current = "main")
        #button_layout.add_widget(back_button)

        # Speichern-Button
        save_button = Button(text="Save", size_hint=(1, None), height=50)
        button_layout.add_widget(save_button)

        self.layout.add_widget(button_layout)

        # QR-Code-Anzeige
        self.qr_image = Image(size_hint=(1, None), height=200)
        self.layout.add_widget(self.qr_image)

        self.add_widget(self.layout)

    def populate_form(self, entry):
        self.fahrgestellnummer.text = entry["fahrgestellnummer"]
        self.seriennummer.text = entry["seriennummer"]

    def enable_editing(self, instance):
        self.fahrgestellnummer.disabled = False
        self.seriennummer.disabled = False

    def generate_qr_code(self, instance):
        data = f"Fahrgestellnummer: {self.fahrgestellnummer.text}, Seriennummer: {self.seriennummer.text}"
        qr = qrcode.make(data)
        buffer = BytesIO()
        qr.save(buffer, format="PNG")
        buffer.seek(0)
        img = CoreImage(buffer, ext="png").texture
        self.qr_image.texture = img