from flet import *

class Settings(UserControl):
  def __init__(self, layout, page):
    super().__init__()
    self.layout = layout
    self.page = page
    
    
  def build(self):

    entryNom = TextField(label='Ingresa usuario',width=250)
    entryContra = TextField(label='contraseña',width=250)
    
    return Column(
      controls=[
        Text('Ajustes'),
        Text('Ajustes'),
        Text('Ajustes'),
        Text('Ajustes'),
        Text('Ajustes'),
      ]
    )