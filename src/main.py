import flet as ft
from app_file.pages.login import login
from app_file.pages.home_page import home

# main.py
def main_location(page: ft.Page):
    # Set global page properties
    page.title = "Archemede School"
    page.theme_mode = ft.ThemeMode.DARK
    
    def route_change(e):
        page.clean()
        
        # Check login status from client storage
        is_logged_in = page.client_storage.get("logged_in") == "yes"

        if page.route == "/":
            if is_logged_in:
                page.go("/home")
            else:
                login(page)

        elif page.route == "/home":
            if not is_logged_in:
                page.go("/")
            else:
                # home(page) handles its own layout and background threads
                home(page) 

        else:
            page.add(ft.Text("404: Not Found", size=30, color="red"))
        
        page.update()

    def view_pop(e):
        page.views.pop()
        top_view = page.views[-1]
        page.go(top_view.route)

    page.on_route_change = route_change
    page.on_view_pop = view_pop
    
    # Start the app at the current route
    page.go(page.route)

# Note: assets_dir is relative to the "src" folder defined in pyproject.toml
ft.app(target=main_location, assets_dir="assets")