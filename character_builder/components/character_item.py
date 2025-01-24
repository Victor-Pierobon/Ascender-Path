import flet as ft
from math import floor, sqrt

def build_item(character, item_delete, add_xp):
    stat_texts = []
    character_level = 0
    stats_ordered = sorted(character["stats"], key=lambda stat : stat["stat_name"])
    for stat in character["stats"]:
        character_level = character_level + stat["level"]

        stat_texts.append(
            ft.Row([
               ft.Text(f"{stat['stat_name']}: Level {stat['level']}, XP: {stat['xp']}"),
                ft.ElevatedButton("+XP", on_click=lambda e, stat_name=stat['stat_name']: add_xp(character["id"], stat_name, 5))
            ])
          )
    rank = calculate_rank(character_level)

    return ft.Row([
        ft.Text(f"Name: {character['name']}, Level: {character_level}, Rank: {rank}"),
        ft.Column(stat_texts),
        ft.ElevatedButton("Delete", on_click=lambda e: item_delete(character["id"]))
    ])

def calculate_rank(level):
    if level < 20:
        return "E"
    elif level < 40:
        return "D"
    elif level < 60:
        return "C"
    elif level < 80:
        return "B"
    elif level < 100:
        return "A"
    elif level < 150:
        return "S"
    else:
        return "SS"
    