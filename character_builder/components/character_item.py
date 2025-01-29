import flet as ft
from database import update_character_stats
from math import floor, sqrt

def build_item(page: ft.Page, character, item_delete, add_xp, show_character_quests, complete_quest_from_character): # Add 'page: ft.Page' as the first parameter
    stat_texts = []
    character_level = 0
    stats_ordered = sorted(character["stats"], key=lambda stat : stat["stat_name"])
    for stat in stats_ordered:
        character_level = character_level + stat["level"]
        xp_to_level_up =  5 + stat['level'] * (1.25 + stat['level']/10)

        progress = stat["xp"] / xp_to_level_up if stat["xp"] < xp_to_level_up else 1

        stat_texts.append(
            ft.Row([
               ft.Text(f"{stat['stat_name']}: Level {stat['level']}"),
               ft.ProgressBar(value=progress, width=200),
                ft.ElevatedButton("+XP", on_click=lambda e, stat_name=stat['stat_name']: add_xp(character["id"], stat_name, 5))
            ])
          )
    rank = calculate_rank(character_level)

    return ft.Row([
        ft.Text(f"Name: {character['name']}, Level: {character_level}, Rank: {rank}"),
        ft.Column(stat_texts),
        ft.ElevatedButton("Quests", on_click=lambda e, current_page=page: show_character_quests(current_page, character["id"])), # Capture and pass 'page' here
        ft.ElevatedButton("Complete", on_click=lambda e: complete_quest_from_character(character["id"], 1)),
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
    