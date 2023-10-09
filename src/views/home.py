from flet import *

class Home(UserControl):
  def __init__(self,page):
    super().__init__()
    self.page = page
    
  def build(self):
    return Column(
      controls=[
        Text('Entraste a la app'),
        ElevatedButton('Salir',
                       on_click= lambda _:self.page.go('/login'))
      ]
    )