from kivy.app import App
from kivy.uix.widget import Widget
from kivy.lang import Builder
from kivy.properties import ObjectProperty
from kivy.animation import Animation

# Fire with animation
Builder.load_file('main.kv')


class MyLayout(Widget):

    def animate_it(self, widget, *args):
        # Define The animation
        animate = Animation(
            background_color=(0, 0, 1, 0), duration=.5
        )

        # Do Second animation
        animate += Animation(size_hint=(1, 1))

        # Do Third animation
        animate += Animation(size_hint=(.5, 0.5))

        # Do Third animation
        animate += Animation(pos_hint={'center_x': 0.1})
        # Do Third animation
        animate += Animation(pos_hint={'center_y': 0.5})

        # start the animation
        animate.start(widget)

        # create a callback
        animate.bind(on_complete=self.my_callback)

    def my_callback(self, *args):
        self.ids.my_lable.text = "Wow! Look at that!"


class MyApp(App):
    def build(self):
        return MyLayout()


if __name__ == "__main__":
    MyApp().run()
