from flet import *

class Login(UserControl):
  def __init__(self,page):
    super().__init__()
    self.page = page
    
    
  def build(self):

    entryNom = TextField(label='Ingresa usuario',width=250)
    entryContra = TextField(label='contraseña',width=250)
    
    return Column(
      controls=[
        Text('Bienvenido a la pagina'),
        entryNom,
        entryContra,
        ElevatedButton(
          'Iniciar Sesion',
            on_click= lambda _:self.page.go('/'))
      ],horizontal_alignment=  CrossAxisAlignment.CENTER
    )