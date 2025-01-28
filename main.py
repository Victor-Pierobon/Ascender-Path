import flet as ft
import sys
import os
project_root = os.path.abspath(os.path.dirname(__file__))
sys.path.insert(0, project_root)
import database


def main(page: ft.Page):
    page.title = "Main Page"

    def route_change(route):
        page.views.clear()
        if page.route =="/quests":
            page.views.append(
                database.quests.main.main(page)
            )
        else:
            page.views.append(
                database.character_builder.main.main(page)
            )

    page.on_route_change = route_change

    page.add(
        ft.ElevatedButton("Characters", on_click=lambda _: page.go("/characters"))
    )
    if page.route =="/quests":
        page.views.append(
            database.quests.main.main(page)
        )
    else:
        page.views.append(
            database.character_builder.main.main(page)
        )
    page.update()
ft.app(target=main)