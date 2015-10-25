__version__ = '1.0'

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import NumericProperty, ObjectProperty, ReferenceListProperty


class DragGame(Widget):
	block = ObjectProperty(None)
	movement = False

	#variabelen die bij moeten gaan houden welke positie de x inneemt t.o.v. de drag
	xdif = 0
	ydif = 0

	def on_touch_down(self, touch):
		self.xdif = touch.x-self.block.xposition
		self.ydif = touch.y-self.block.yposition

	def on_touch_move(self, touch):
		self.block.xposition = touch.x-self.xdif
		self.block.yposition = touch.y-self.ydif

	def on_touch_up(self, touch):
		pass

class DragBlock(Widget):
	xposition = NumericProperty(0)
	yposition = NumericProperty(0)

class DragApp(App):
	def build(self):
		game = DragGame()
		#Clock.schedule_interval(game.update(), 1.0/60.0)
		return game

if __name__ == '__main__':
	DragApp().run()