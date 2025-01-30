import flet as ft

def view_1(page: ft.Page):
    return ft.View(
        "/view_1",
        [
            ft.Text("View 1", style=ft.TextStyle(size=30)),
            ft.ElevatedButton("Go to View 2", on_click=lambda _: page.go("/view_2")),
        ],
    )

def view_2(page: ft.Page):
    return ft.View(
        "/view_2",
        [
            ft.Text("View 2", style=ft.TextStyle(size=30, color=ft.colors.BLUE)),
            ft.ElevatedButton("Go to View 1", on_click=lambda _: page.go("/view_1")),
        ],
    )

def route_change(e):
    page = e.page
    page.views.clear()
    if page.route == "/view_2":
        page.views.append(view_2(page))
    else:
        page.views.append(view_1(page))
    page.update()

def main(page: ft.Page):
    page.title = "Minimal Routing Test"
    page.on_route_change = route_change
    page.go(page.route)

ft.app(target=main)