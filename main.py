
from flet import *
from src.layout import AppLayout

if __name__ == "__main__":
  
  def main(page: Page):
    
    layout = AppLayout(page,
                       tight=True,
                       expand=True,
                       vertical_alignment="start")
    
    page.add(layout)
    # def actualizarRuta(route):

      # page.views.append(
      # 	Router.views_handler(page)[page.route]
      # )


    # page.on_route_change = actualizarRuta
    
    # page.go('/login')
    # page.update()

  app(main)
