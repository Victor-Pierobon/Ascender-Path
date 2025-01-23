import flet as ft

def build_item(quest, item_delete, add_quest_to_character, complete_quest):
    return ft.Row(
        [
            ft.Text(f"Name: {quest[1]}, Description: {quest[2]}, Rank: {quest[3]}"),
            ft.ElevatedButton("Add", on_click=lambda e: add_quest_to_character(quest[0])),
            ft.ElevatedButton("Complete", on_click=lambda e: complete_quest(quest[0])),
            ft.ElevatedButton("Delete", on_click=lambda e: item_delete(quest[0]))
        ]
    )