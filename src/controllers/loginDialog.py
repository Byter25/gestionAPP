import flet as ft

class LoginDialog(ft.UserControl):
  def __ini__(self,page):
    super().__init__()  
    self.page = page
    
  def build(self):
    self.entryName = ft.TextField(label="usuario")
    self.entryContra = ft.TextField(label="contraseña")
    self.iniciarSesion = ft.ElevatedButton("Iniciar Sesion")
    self.registrarSesion = ft.TextButton("Registrarte")
    self.dlg = ft.AlertDialog(
      title=ft.Text("Login"),
      content=(
        ft.Column(
          [
            self.entryName,
            self.entryContra,
            self.iniciarSesion,
            ft.Row([
              ft.Text("No tienes cuenta?"),
              self.registrarSesion
            ])
          ],
          height=200,
          horizontal_alignment = ft.CrossAxisAlignment.CENTER
        )
      ),
      on_dismiss=lambda e: print(f"{ self.entryName.value} - {self.entryContra.value}"),
    )
    return ft.ElevatedButton("Login", on_click=lambda _:self.open_dlg())
  
  def open_dlg(self):
    self.page.dialog = self.dlg
    self.dlg.open = True
    self.page.update()
