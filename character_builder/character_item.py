import flet as ft

def build_item(character, item_delete):
    return ft.row([
            ft.Text(f"Name: {character[1]}, Level:{character[2]}"),
            ft.ElevatedButton("Delete", on_click=lambda e: item_delete(character[0]))
        ])