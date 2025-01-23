import flet as ft
from math import floor, sqrt

def build_item(character, item_delete, add_xp):
    stat_texts = []
    character_level = 0
    for stat in character["stats"]:
        character_level = character_level + stat["level"]

        stat_texts.append(
            ft.Row([
               ft.Text(f"{stat['stat_name']}: Level {stat['level']}, XP: {stat['xp']}"),
                ft.ElevatedButton("+XP", on_click=lambda e, stat_name=stat['stat_name']: add_xp(character["id"], stat_name, 5))
            ])
          )

    return ft.Row([
        ft.Text(f"Name: {character['name']}, Level: {character_level}"),
        ft.Column(stat_texts),
        ft.ElevatedButton("Delete", on_click=lambda e: item_delete(character["id"]))
    ])