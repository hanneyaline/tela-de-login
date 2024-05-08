from kivy.config import Config

Config.set('graphics', 'width', '360')
Config.set('graphics', 'height', '640')
Config.set('graphics', 'resizable', False)

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.core.window import Window
from kivy.uix.image import Image
from kivy.graphics import Color, RoundedRectangle


class LoginScreen(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'vertical'

        
        with self.canvas.before:
            Color(0.2, 0.6, 0.8, 1)  
            self.rect = RoundedRectangle(pos=self.pos, size=self.size, radius=[(0, 0), (0, 0), (25, 25), (25, 25)])
        self.bind(pos=self.update_rect, size=self.update_rect)

        
        self.add_widget(Image(source='1ba925dd3f7f997d184e37bc3990c985.jpg', allow_stretch=True, keep_ratio=False))

        
        input_layout = BoxLayout(orientation='vertical', padding=8, spacing=10)

        self.add_widget(input_layout)

        input_layout.add_widget(Label(text='Digite seu nome de usuário:', color=(1, 1, 1, 1)))

        
        self.username = TextInput(hint_text='Nome de usuário', multiline=False, size_hint=(None, None), height=50,
                                  width=300)
        input_layout.add_widget(self.username)

        input_layout.add_widget(Label(text='Digite sua senha:', color=(1, 1, 1, 1)))

        
        self.password = TextInput(hint_text='Senha', multiline=False, password=True, size_hint=(None, None),
                                  height=50, width=300)
        input_layout.add_widget(self.password)

        
        button_layout = BoxLayout(padding=8, spacing=10)
        self.add_widget(button_layout)

        
        self.login_button = Button(text='Login', size_hint=(None, None), height=50, width=150)
        self.login_button.bind(on_press=self.login)
        button_layout.add_widget(self.login_button)

        
        self.signup_button = Button(text='Cadastrar', size_hint=(None, None), height=50, width=150)
        self.signup_button.bind(on_press=self.signup)
        button_layout.add_widget(self.signup_button)

    def update_rect(self, instance, value):
        self.rect.pos = instance.pos
        self.rect.size = instance.size

    def login(self, instance):
        
        username = self.username.text
        password = self.password.text
        print(f'Tentativa de login com nome de usuário: {username} e senha: {password}')

    def signup(self, instance):
       
        print('Abrir tela de cadastro')


class LoginApp(App):
    def build(self):
        return LoginScreen()


if __name__ == '__main__':
    LoginApp().run()
