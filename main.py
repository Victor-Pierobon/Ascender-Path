import flet as ft
import sys
import os
project_root = os.path.abspath(os.path.dirname(__file__))
sys.path.insert(0, project_root)
import database
import character_builder.main as character_builder_main
import quests.main as quests_main


def main(page: ft.Page):
    page.title = "Main Page"

    def route_change(route):
        page.views.clear()
        if page.route.startswith("/quests"):
            character_id = page.route.split("?")[1].split("=") if len(page.route.split("?")) > 1 else ""
            page.views.append(
                quests_main.main(page, character_id)
            )
        else: # Default route - now explicitly Characters
            page.views.append(
                character_builder_main.main(page)
            )
        page.update()

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