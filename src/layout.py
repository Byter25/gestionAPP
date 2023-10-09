from flet import *
from src.views.settings import Settings
from src.controllers.slidebar import Slidebar
from src.views.home import Home

class AppLayout(Row):
  def __init__(self,page: Page, *args, **kwargs):
    super().__init__(*args, **kwargs)
    self.app = app
    self.page = page
    self.sidebar = Slidebar(self, page)
    
    self.toggle_nav_rail_button = IconButton(
      icon=icons.ARROW_CIRCLE_LEFT, icon_color=colors.BLUE_GREY_400, selected=False,
      selected_icon=icons.ARROW_CIRCLE_RIGHT, on_click=self.toggle_nav_rail
      )
    
    self._active_view: Control = Home(page)
    
    self.controls = [
      self.sidebar,
      self.toggle_nav_rail_button, 
      self.active_view
      ]
      
  @property
  def active_view(self):
    return self._active_view
 
  @active_view.setter
  def active_view(self, view):
    self._active_view = view
    self.update()
 
  def toggle_nav_rail(self, e):
    self.sidebar.visible = not self.sidebar.visible
    self.toggle_nav_rail_button.selected = not self.toggle_nav_rail_button.selected
    self.page.update()

    

# class Router:
#   def __init__(self,page) 
#     self.Page = page
#     self.routes = {
#       "/":Home(page),
#       "/login":Login(page),
#       "/settings":Settings(page),
#     }
    
#     self.body = Container(content=self.routes["/"])
    
#   def router_change(self,route):
#     self.body.content = self.routes[route.route]
#     self.body.update()

#   def views_handler(page):
#     return {
#       '/':View(
#         route='/',
#         controls=[
#           Row(
#             [
#               Home(page)
#             ]
#           ),
#         ],
#       ),
#       '/login':View(
#         route='/login',
#         controls=[Login(page)],
#       ),
#       '/settings':View(
#         route='/settings',
#         controls=[
#           Row(
#             [
#               VerticalDivider(width=1),
#               Settings(page)
#             ],
#             expand=True,
#           ),
#         ],
#       )
#     }