import flet as ft
import character_builder.main as character_builder_main
import quests.character_quests_view as character_quests_view_main


def route_change(e):
    page = e.page
    page.views.clear()
    if page.route.startswith("/quests?id="):
        try:
            character_id = page.route.split("?")[1].split("=")[1]
            page.views.append(character_quests_view_main.main(page, character_id))
        except IndexError:
            page.views.append(ft.View(page.route, [ft.Text("Invalid Quests route")]))
    else:
        page.views.append(character_builder_main.main(page))
    page.update()


def main(page: ft.Page):
    page.title = "Main Page"
    page.on_route_change = route_change
    page.go("/characters")  # Explicitly set initial route to "/characters"

    page.add(
        ft.Row(
            [
                ft.ElevatedButton("Characters", on_click=lambda _: page.go("/characters")),
                ft.ElevatedButton("Quests", on_click=lambda _: page.go("/quests"))
            ],
            alignment=ft.MainAxisAlignment.CENTER
        )
    )

ft.app(target=main)