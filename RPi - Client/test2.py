from kivy.uix.floatlayout import FloatLayout
from kivy.app import App
from kivy.uix.button import Button
import random
from kivy.clock import Clock
from functools import partial







class AI():


    layout_ref = None



    def remove(self,widget,dt):
        self.layout_ref.remove_widget(widget)


    def add(self,widget,dt):
        self.layout_ref.add_widget(widget)


    def draw_stuff(self):




        widget_storage = []


        for i in range(10):
            x = random.randint(0,10)
            y = random.randint(0,10)
            widget = Button( pos=(x*40,y*40), size=(40,40) )
            widget_storage.append(widget)




        delay_time = 2
        add_delay = 0
        remove_delay = 0




        for w in widget_storage:


            remove_delay += delay_time
            Clock.schedule_once( partial(self.add,w), add_delay )
            Clock.schedule_once( partial(self.remove,w), remove_delay)
            add_delay += delay_time




class Layout(FloatLayout):


    def __init__(self):
        super(FloatLayout,self).__init__()




        self.ai = AI()
        self.ai.layout_ref = self


    def on_touch_down(self, touch):
        self.ai.draw_stuff()




class TestApp(App):
    def build(self):
        return  Layout()


TestApp().run()
