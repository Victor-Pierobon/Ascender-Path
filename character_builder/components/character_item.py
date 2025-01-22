import flet as ft
from math import floor, sqrt

def build_item(character, item_delete, add_xp):
    stat_texts = []
    character_level = 0
    for stat in character["stats"]:
        stat_level = floor(sqrt(stat["xp"]) / 3)
        character_level = character_level + stat_level

        stat_texts.append(
            ft.Row([
               ft.Text(f"{stat['stat_name']}: Level {stat_level}, XP: {stat['xp']}"),
                ft.ElevatedButton("+XP", on_click=lambda e: add_xp(character["id"], stat['stat_name'], 5))
            ])
          )

    return ft.Row([
        ft.Text(f"Name: {character['name']}, Level: {character_level}"),
        ft.Column(stat_texts),
        ft.ElevatedButton("Delete", on_click=lambda e: item_delete(character["id"]))
    ])