import flet as ft

def build_item(character, item_delete, add_xp):
    stat_texts = []
    for stat in character["stats"]:
        stat_texts.append(
            ft.Row([
                ft.text(f"Level: {stat['stat_name']}, XP:{stat['xp']}"),
                ft.ElevatedButton("+XP", on_click=lambda e: add_xp(character["id"], stat["stat_name"], 5))
            ])
        )

    return ft.Row([
        ft.Text(f"Name: {character['name']}"),
        ft.Column(stat_texts),
        ft.ElevatedButton("Delete", on_click=lambda e: item_delete(character["id"]))
    ])