import flet as ft

def build_item(task, item_delete):
    return ft.Row(
        [
            ft.Text(task[1]),
            ft.ElevatedButton("Delete", on_click=lambda e: item_delete(task[0]))
        ]
    )