from flet import *
from src.views.home import Home
from src.views.login import Login
from src.views.settings import Settings

class Router:
  def __init__(self,page):
    self.Page = page
    self.routes = {
      "/":Home(page),
      "/login":Login(page),
      "/settings":Settings(page),
    }
  
    self.body = Container(content=self.routes["/"])
  
  def initialize(self):
    self.page.views.append(
      View(
        "/",
        [
          self.appbar,
          self.layout
        ],
        padding=padding.all(0),
        bgcolor=colors.BLUE_GREY_200
      )
    )
    self.page.update()
    # create an initial board for demonstration
    self.create_new_board("My First Board")
    self.page.go("/")
 
  def route_change(self, e):
        troute = TemplateRoute(self.page.route)
        if troute.match("/"):
            self.page.go("/boards")
        elif troute.match("/board/:id"):
            if int(troute.id) > len(self.store.get_boards()):
                self.page.go("/")
                return
            self.layout.set_board_view(int(troute.id))
        elif troute.match("/boards"):
            self.layout.set_all_boards_view()
        elif troute.match("/members"):
            self.layout.set_members_view()
        self.page.update()