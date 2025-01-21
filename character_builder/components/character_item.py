import flet as ft

def build_item(character, item_delete):
    stat_texts = []
    for stat in character["stats"]:
        stat_texts.append(ft.Text(f"Level:{stat['stat_name']}, XP:{stat['xp']}"))

    return ft.Row([
        ft.Text(f"Name: {character['name']}"),
        ft.Column(stat_texts),
        ft.ElevatedButton("Delete", on_click=lambda e: item_delete(character["id"]))
    ])