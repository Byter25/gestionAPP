from flet import *
from src.controllers.loginDialog import LoginDialog
from src.views.home import Home 
from src.views.settings import Settings
class Slidebar(UserControl):
  def __init__(self, layout, page):
    super().__init__()
    self.layout = layout
    self.page = page
    
    self.rail_items = [
      NavigationRailDestination(
        label_content=Text("Boards"),
        label="Boards",
        icon=icons.BOOK_OUTLINED,
        selected_icon=icons.BOOK_OUTLINED
      ),
      NavigationRailDestination(
        label_content=Text("Members"),
        label="Members",
        icon=icons.PERSON,
        selected_icon=icons.PERSON
      ),
    ]
    self.regresa = []
    self.rail_bar = NavigationRail(
      selected_index=None,
      label_type="all",
      on_change=self.top_nav_change,
      destinations=self.rail_items,
      bgcolor=colors.BLUE_GREY,
      extended=True,
      expand=True
    )
    
  def build(self):
    self.view = Container(
      content=Column([
        Row([Text("Workspace")],alignment="center"),
        # divider
        Container(
          bgcolor=colors.BLACK26,
          border_radius=border_radius.all(30),
          height=1,
          alignment=alignment.center_right,
          width=220
          ),
        self.rail_bar,
        # divider
        Container(
          bgcolor=colors.BLACK26,
          border_radius=border_radius.all(30),
          height=1,
          alignment=alignment.center_right,
          width=220
        ),
        LoginDialog(self.page)
      ],tight=True),
      padding=padding.all(15),
      margin=margin.all(0),
      width=250,
      bgcolor=colors.BLUE_GREY,
    )
    
    return self.view
  
  def top_nav_change(self, e):
    self.rail_bar.selected_index = e.control.selected_index
    self.update()