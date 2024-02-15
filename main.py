from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.widget import Widget
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.checkbox import CheckBox
from kivy.uix.textinput import TextInput
from kivy.core.window import Window
from kivy.uix.scrollview import ScrollView
import random, requests

stories = []

url = "https://4cee-95-24-231-234.ngrok-free.app/"


class Application(App):

    # Метод инициализации, который создает и выводит экран, который потом изменяется добавлением или удалением виджетов
    def build(self):
        self.master = False
        self.root = ScrollView(size_hint=(1, 1), size=(Window.width, Window.height))
        self.background = "#faebd7"
        self.buttons = "#222222"
        Window.size = (400, 895)
        Window.clearcolor = self.background
        self.screen = BoxLayout(padding=[50, 150, 50, 150], orientation="vertical", spacing=50)
        self.but = Button(text="Начать!", font_size=30, background_color=self.buttons,
                          on_press=self.GameMode, color=self.background, size_hint=[1, .2])
        self.label = Label(text="Здравствуйте!\n Готовы начать игру?", color=self.buttons, valign="top",
                           halign="center", size_hint=[1, .6])
        self.label.bind(size=self.label.setter('text_size'))
        self.label.font_size = max(Window.size) / 30
        self.screen.add_widget(self.label)
        self.rulesBtn = Button(text="Правила игры", font_size=30, background_color=self.buttons,
                               on_press=self.rules, color=self.background, size_hint=[1, .2])
        self.screen.add_widget(self.rulesBtn)
        self.screen.add_widget(self.but)
        self.root.add_widget(self.screen)
        return self.root

    # Метод, который выводит на экран правила игры

    def rules(self, obj):
        self.root.clear_widgets()
        self.root.size_hint = (1, None)
        self.root.size = (Window.width, Window.height)
        Window.size = (400, 895)
        self.background = "#faebd7"
        self.buttons = "#222222"
        Window.clearcolor = self.background
        self.layout = GridLayout(cols=1, spacing=75, size_hint_y=None, padding=[50, 200, 50, 100])
        self.layout.bind(minimum_height=self.layout.setter('height'))
        self.label = Label(text="Добро пожаловать в\nStory Time!\n\n\n\n\n\n\n", font_size=30, color=self.buttons,
                           halign="center", valign="top", font_name="Comic")
        self.layout.add_widget(self.label)

        self.label = Label(
            text="Суть игры заключается в том,\nчто вы со своими друзьями\nпишете истории, связанные с вами.\nДалее истории выводятся на экран\nведущему в случайном порядке\nи каждый игрок должен угадать,\nчья это история!\n\n\n\n\n",
            font_size=20, color=self.buttons, halign="left", valign="top", font_name="Roboto")

        self.layout.add_widget(self.label)
        self.layout.add_widget(
            Label(text="Как играть?\n", font_size=25, color=self.buttons, halign="center", valign="top",
                  font_name="Comic"))
        self.layout.add_widget(
            Label(
                text="Для начала выберите режим игры:\n\n- Онлайн для игры с разных устройств\n- Оффлайн для игры на одном устройстве\n",
                font_size=18, color=self.buttons, halign="left", valign="top", font_name="Roboto"))
        self.layout.add_widget(
            Label(
                text='Игра онлайн:\n',
                font_size=25, color=self.buttons, halign="left", font_name="Comic"))
        self.layout.add_widget(
            Label(text="1) Выберите ведущего                               \n\n", font_size=18, color=self.buttons,
                  halign="left", font_name="Roboto"))
        self.layout.add_widget(
            Label(
                text="2) Ведущий должен создать комнату,\nиспользуя кнопку “Создать”\nМожно как задать пароль,\nтак и оставить поле пустым\n\n",
                font_size=18, color=self.buttons, halign="left", valign="top", font_name="Roboto"))
        self.layout.add_widget(
            Label(text='3) Подключитесь к комнате\nна других устройствах,\nиспользуя кнопку “Подключиться"     ',
                  font_size=18,
                  color=self.buttons, halign="left", valign="top", font_name="Roboto"))
        self.layout.add_widget(
            Label(text='4) Когда все устройства подключены,\nведущий может начать игру\nиспользуя кнопку “Начать"',
                  font_size=18,
                  color=self.buttons, halign="left", valign="top", font_name="Roboto"))
        self.layout.add_widget(
            Label(text='5) После этого остальные игроки\nтакже нажимают на кнопку “Начать” ', font_size=18,
                  color=self.buttons, halign="left", valign="top", font_name="Roboto"))
        self.layout.add_widget(
            Label(text='6) Игроки пишут свои истории                 ', font_size=18,
                  color=self.buttons, halign="left", valign="top", font_name="Roboto"))
        self.layout.add_widget(
            Label(
                text='7) Когда истории закончены -\nоставьте поле пустым и подождите,    \nпока все игроки будут готовы\nприступить к игре',
                font_size=18,
                color=self.buttons, halign="left", valign="top", font_name="Roboto"))
        self.layout.add_widget(
            Label(text='8) Ведущий начинает игру                         ', font_size=18,
                  color=self.buttons, halign="left", valign="top", font_name="Roboto"))
        self.layout.add_widget(
            Label(text='9) Игроки также нажимают "Начать"   ', font_size=18,
                  color=self.buttons, halign="left", valign="top", font_name="Roboto"))
        self.layout.add_widget(
            Label(
                text='Игра оффлайн:\n',
                font_size=25, color=self.buttons, halign="left", font_name="Comic"))
        self.layout.add_widget(
            Label(text='1) Введите свои истории                              ',
                  font_size=18, color=self.buttons, halign="left", valign="top", font_name="Roboto"))
        self.layout.add_widget(
            Label(text='2) Когда ваши истории закончились – \nпередайте устройство\nследующему игроку                 ',
                  font_size=18, color=self.buttons, halign="left", valign="top", font_name="Roboto"))
        self.layout.add_widget(
            Label(
                text='3) Когда последний игрок\nзакончит вводить истории,\nему необходимо оставить поле ввода \nпустым и нажать кнопку “Ввод”',
                font_size=18,
                color=self.buttons, halign="left", valign="top", font_name="Roboto"))
        self.layout.add_widget(
            Label(
                text='4) Выберете ведущего и\n отдайте ему устройство                             ',
                font_size=18,
                color=self.buttons, halign="left", valign="top", font_name="Roboto"))
        self.layout.add_widget(
            Label(
                text='Приятной игры!\n',
                font_size=30, color=self.buttons, halign="left", font_name="Comic"))
        self.but = Button(text="Играть!", font_size=20, background_color=self.buttons, on_press=self.afterRules,
                          color=self.background, size_hint=(1, None))
        self.layout.add_widget(self.but)
        self.root.add_widget(self.layout)

    # Метод, который возвращает начальный экран после просмотра правил

    def afterRules(self, obj):
        self.root.clear_widgets()
        self.screen = BoxLayout(padding=[50, 150, 50, 150], orientation="vertical", spacing=50)
        self.but = Button(text="Начать!", font_size=30, background_color=self.buttons,
                          on_press=self.GameMode, color=self.background, size_hint=[1, .2])

        self.label = Label(text="Здравствуйте!\n Готовы начать игру?", color=self.buttons, valign="top",
                           halign="center", size_hint=[1, .6])
        self.label.bind(size=self.label.setter('text_size'))
        self.but.border_radius = [80, 80, 80, 80]
        self.label.font_size = max(Window.size) / 30
        self.screen.add_widget(self.label)
        self.screen.add_widget(Button(text="Правила игры", font_size=30, background_color=self.buttons,
                                      on_press=self.rules, color=self.background, size_hint=[1, .2]))
        self.screen.add_widget(self.but)
        self.root.add_widget(self.screen)

    # Метод, отображающий экран выбора режима игры

    def GameMode(self, obj):
        self.screen.clear_widgets()
        self.label = Label(text="Здравствуйте!\n Готовы начать игру?", color=self.buttons, valign="top",
                           halign="center", size_hint=[1, .6])
        self.label.bind(size=self.label.setter('text_size'))
        self.screen.add_widget(self.label)
        self.label.text = "Выберете режим игры"
        self.label.font_size = max(Window.size) / 30
        self.but.text = "Онлайн!"
        self.label.size_hint = [1, .6]
        self.but = Button(text="Онлайн", font_size=30, background_color=self.buttons,
                          on_press=self.online, color=self.background, size_hint=[1, .2])
        self.subm = Button(text="Оффлайн", font_size=30, background_color=self.buttons,
                           on_press=self.storiesOffline, color=self.background, size_hint=[1, .2])
        self.screen.add_widget(self.but)
        self.screen.add_widget(self.subm)

    # Метод, вызываемый при нажатии на кнопку онлайн

    def online(self, obj):
        self.screen.remove_widget(self.subm)
        self.screen.remove_widget(self.but)
        self.label.text = "Создайте или подключитесь к существующей комнате"
        self.but = Button(text="Создать", font_size=30, background_color=self.buttons,
                          on_press=self.createRoom, color=self.background, size_hint=[1, .2])
        self.subm = Button(text="Подключиться", font_size=30, background_color=self.buttons,
                           on_press=self.connectRoom, color=self.background, size_hint=[1, .2])
        self.screen.add_widget(self.but)
        self.screen.add_widget(self.subm)

    # Метод, отображающий экран создания комнаты

    def createRoom(self, obj):
        self.screen.remove_widget(self.but)
        self.screen.remove_widget(self.subm)
        self.subm = Button(text="Установить", font_size=30, background_color=self.buttons, on_press=self.addLobby,
                           color=self.background, size_hint=[1, .2])
        responce = requests.get(url + "rooms/")
        rooms = responce.json()
        self.room = None
        for i in range(len(rooms)):
            if rooms[i]["inUse"] == "False":
                self.room = rooms[i]
                break
        if self.room != None:
            self.label.text = f"id вашей комнаты: {self.room['id']}\n\nУстановите пароль:"
            self.label.size_hint = [1, .3]

            self.password = TextInput(password=True, size_hint=[0.75, 1])
            self.checkbox = CheckBox(color=self.buttons)
            self.checkbox.bind(active=self.on_checkbox_active)
            self.inputLayout = GridLayout(cols=1, size_hint=[1, 0.35], spacing=50)
            self.inputLayout.add_widget(self.password)
            self.checkboxLayout = BoxLayout(orientation="vertical", spacing=10, size_hint=[0.25, 1])
            self.checkboxLayout.add_widget(self.checkbox)
            self.checkboxLayout.add_widget(Label(text="Показать", color=self.buttons, valign="top", halign="right"))
            self.inputLayout.add_widget(self.checkboxLayout)
            self.screen.add_widget(self.inputLayout)
            self.screen.add_widget(Widget(size_hint=[1, 0.1]))
            self.screen.add_widget(self.subm)
            self.screen.add_widget(Widget(size_hint=[1, 0.05]))


    # Метод, отвечающий за показ пароля при создании комнаты

    def on_checkbox_active(self, obj, value):
        if value:
            self.password.password = False
        else:
            self.password.password = True

    # Метод, отвечающий за создание комнаты и вывода экрана ожидания

    def addLobby(self, obj):

        requests.patch(url + f"rooms/{self.room['id']}",
                       data={'inUse': "True",
                             'password': self.password.text})
        self.master = True

        self.screen.clear_widgets()
        self.label = Label(text="Дождитесь подключения всех игроков...", color=self.buttons, valign="top",
                           halign="center",
                           size_hint=[1, .7])
        self.but = Button(text="Начать игру", font_size=30, background_color=self.buttons,
                          on_press=self.startGameOnline,
                          color=self.background, size_hint=[1, .2])
        self.label.font_size = max(Window.size) / 30
        self.label.bind(size=self.label.setter('text_size'))
        self.screen.add_widget(self.label)
        self.screen.add_widget(self.but)

    # Метод, отвечающий за начало игры в режиме онлайн

    def startGameOnline(self, obj):
        if self.master:
            requests.patch(url + f"rooms/{self.room['id']}",
                           data={'gameStarted': "True"})
            self.StoriesOnline()
        else:
            self.room = requests.get(url + f"rooms/{self.room['id']}").json()
            if self.room['gameStarted'] == True:
                self.StoriesOnline()
            else:
                self.label.text = "Пожалуйста дождитесь, пока ведущий запустит игру!"

    # Метод, отображающий экран ввода историй в режиме онлайн
    def StoriesOnline(self):
        self.screen.clear_widgets()
        self.label = Label(text="Введите историю!\n Если истории закончились - оставьте поле пустым",
                           color=self.buttons, valign="top", halign="center",
                           size_hint=[1, .7])
        self.screen.padding = [50, 100, 50, 125]
        self.label.bind(size=self.label.setter('text_size'))
        self.label.font_size = max(Window.size) / 30
        self.label.size_hint = [1, .3]
        self.but = Button(text="Отправить", font_size=30, background_color=self.buttons,
                          on_press=self.addStoryOnline, color=self.background, size_hint=[1, .2])
        self.storyInput = TextInput(size_hint=[1, .5])
        self.screen.add_widget(self.label)
        self.screen.add_widget(self.storyInput)
        self.screen.add_widget(self.but)

    # Метод, отправляющий истории на сервер

    def addStoryOnline(self, obj):
        if self.storyInput.text != "":
            requests.post(url + "stories/",
                          data={"room": self.room['id'],
                                "story": self.storyInput.text})
            self.storyInput.text = ""
        else:
            self.viewStoryes()

    # Метод, отображающий истории для ведущего и финальный экран для игрока

    def viewStoryes(self):
        if self.master:

            self.randomStorieOnline()
        else:
            self.screen.clear_widgets()
            self.label = Label(text="Приятной игры!", color=self.buttons,
                               valign="top", halign="center",
                               size_hint=[1, .7])
            self.screen.padding = [50, 100, 50, 125]
            self.label.bind(size=self.label.setter('text_size'))
            self.label.font_size = max(Window.size) / 30
            self.but = Button(text="Готово", font_size=30, background_color=self.buttons,
                              on_press=self.rerun, color=self.background, size_hint=[1, .3])
            self.screen.add_widget(self.label)
            self.screen.add_widget(self.but)

    # Метод отвечающий за вывод следующей истории и удаления предыдущей с сервера

    def randomStorieOnline(self):
        self.screen.remove_widget(self.storyInput)
        self.stories = requests.get(url + f"stories?room={self.room['id']}").json()
        if len(self.stories) > 0:
            self.but.text = "Следующая история"
            ind = random.randint(0, len(self.stories) - 1)
            self.label.text = str(self.stories[ind]['story'])
            requests.delete(url + f"stories/{self.stories[ind]['id']}")
        else:
            self.screen.remove_widget(self.but)
            self.label.text = "Истории закончились!"
            self.label.size_hint = [1, .7]
            self.but = Button(text="Сыграть еще раз!", font_size=30,
                              background_color=self.buttons,
                              on_press=self.rerun, color=self.background,
                              size_hint=[1, .3])
            self.screen.add_widget(self.but)

    # Метод, отображающий экран подключения к лобби

    def connectRoom(self, obj):

        self.screen.remove_widget(self.but)
        self.screen.remove_widget(self.subm)
        self.label.text = f"Подключиться к комнате:"
        self.label.size_hint = [1, .2]
        self.screen.padding[1] = 100
        self.id = TextInput(size_hint=[1, 0.1])
        self.password = TextInput(password=True, size_hint=[1, 0.1])

        self.but = Button(text="Подключиться", font_size=30, background_color=self.buttons, on_press=self.connectLobby,
                          color=self.background, size_hint=[1, .2])

        self.idLabel = Label(text="id:", size_hint=[1, .1], color=self.buttons, valign="top", halign="center")
        self.idLabel.font_size = max(Window.size) / 30
        self.idLabel.bind(size=self.label.setter('text_size'))

        self.passLabel = Label(text="Пароль:", size_hint=[1, .1], color=self.buttons, valign="top", halign="center")
        self.passLabel.font_size = max(Window.size) / 30
        self.passLabel.bind(size=self.label.setter('text_size'))

        self.screen.add_widget(self.idLabel)
        self.screen.add_widget(self.id)
        self.screen.add_widget(self.passLabel)
        self.screen.add_widget(self.password)
        self.screen.add_widget(Widget(size_hint=[1, 0.1]))
        self.screen.add_widget(self.but)

    # Метод, подключающий игрока к лобби

    def connectLobby(self, obj):
        try:
            self.master = False
            self.room = requests.get(url + f"rooms/{self.id.text}").json()
            if self.password.text == self.room["password"]:
                self.lobbyConnected()
            else:
                self.label.text = f"Пароль не верен"
                self.master = False
        except:
            self.label.text = f"Комнаты {self.id.text} не существует"

    # Метод, отвечающий за начало игры в режиме офлайн
    def lobbyConnected(self,obj):
        self.screen.clear_widgets()
        self.label = Label(text="Подключено!", color=self.buttons, valign="top",
                           halign="center",
                           size_hint=[1, .7])
        self.but = Button(text="Начать игру", font_size=30, background_color=self.buttons,
                          on_press=self.startGameOnline,
                          color=self.background, size_hint=[1, .2])
        self.label.font_size = max(Window.size) / 30
        self.label.bind(size=self.label.setter('text_size'))
        self.screen.add_widget(self.label)
        self.screen.add_widget(self.but)
    def storiesOffline(self, obj):
        self.screen.remove_widget(self.subm)
        self.screen.remove_widget(self.but)
        self.screen.padding = [50, 100, 50, 125]
        self.label.text = f"Введите историю и нажмите кнопку если истории закончились - оставьте поле пустым"
        self.label.size_hint = [1, .3]
        self.but = Button(text="Ввод", font_size=30, background_color=self.buttons,
                          on_press=self.addStoryOffline, color=self.background, size_hint=[1, .2])
        self.inp = TextInput(size_hint=[1, .5])
        self.screen.add_widget(self.inp)
        self.screen.add_widget(self.but)
        self.stories = []

    # Метод, записывающий истории

    def addStoryOffline(self, i):
        if self.inp.text == "":
            self.startGameOffline()
        else:
            self.stories.append(self.inp.text)
            self.inp.text = ''

    # Метод, отображащий экран начала игры в режиме офлайн

    def startGameOffline(self):
        self.screen.padding = [50, 150, 50, 125]
        self.label.size_hint = [1, .7]
        self.screen.remove_widget(self.inp)
        self.screen.remove_widget(self.but)
        self.label.text = "Вы готовы приступить к игре?"
        self.but = Button(text="Начать!", font_size=30, background_color=self.buttons,
                          on_press=self.randomStorieOffline, color=self.background, size_hint=[1, .3])
        self.screen.add_widget(self.but)

    # Метод, отвечающий за отображение историй в режиме офлайн

    def randomStorieOffline(self, obj):
        if len(self.stories) > 0:
            self.but.text = "Следующая история"
            ind = random.randint(0, len(self.stories) - 1)
            self.label.text = self.stories[ind]
            del self.stories[ind]
        else:
            self.screen.remove_widget(self.but)
            self.label.text = "Истории закончились!"
            self.label.size_hint = [1, .7]
            self.but = Button(text="Сыграть еще раз!",
                              font_size=30, background_color=self.buttons,
                              on_press=self.rerun, color=self.background,
                              size_hint=[1, .3])
            self.screen.add_widget(self.but)

    # Метод, выводящий начальный экран приложения

    def rerun(self, obj):
        if self.master:
            requests.patch(url +
                           f"rooms/{self.room['id']}",
                           data={'gameStarted': "False",
                                 'inUse': "False"})
        self.screen.clear_widgets()
        self.but = Button(text="Начать!", font_size=30, background_color=self.buttons,
                          on_press=self.GameMode, color=self.background, size_hint=[1, .3])
        self.label = Label(text="Здравствуйте!\n Готовы начать игру?", color=self.buttons,
                           valign="top", halign="center", size_hint=[1, .7])
        self.label.bind(size=self.label.setter('text_size'))
        self.label.font_size = max(Window.size) / 30
        self.screen.add_widget(self.label)
        self.screen.add_widget(self.but)


if __name__ == "__main__":
    Application().run()
