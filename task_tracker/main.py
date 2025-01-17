import flet as ft
import database
from components.task_item import build_item

def main(page: ft.Page):
    page.title = "Task Tracker"


    # how it should store and displays tasks
    def add_task(e): # e is the event
     task = task_field.value # get the value of the task field
     if task:
        database.add_task_to_db(task)
        task_field.value = ""
        update_task_list_view()
        page.update()

    def clear_list(e):
       database.clear_task_db()
       update_task_list_view()
       page.update()

    def item_delete(id):
       database.remove_task_from_db(id)
       update_task_list_view()
       page.update()

    # components and actions
    task_field = ft.TextField(label = "Add task", on_submit=add_task) # on_submit is an event that triggers when the user presses enter
    add_button = ft.ElevatedButton("Add", on_click=add_task) # on_click is an event that triggers when the user clicks the button
    clear_button = ft.ElevatedButton("Clear", on_click=clear_list)
    task_list_column = ft.Column([])

    def update_task_list_view():
       tasks = database.get_all_tasks()
       task_list_column.controls.clear()
       for task in tasks:
          task_list_column.controls.append(build_item(task, item_delete))

    page.update()

    database.create_table()
    database.create_characters_table()
    update_task_list_view()

    # User interface
    page.add(
       ft.Row(
          [task_field, add_button, clear_button],
          alignment=ft.MainAxisAlignment.CENTER
       ),
       ft.Container(
          content=task_list_column,
          border=ft.border.all(1),
          padding=10
       )
    )
    

ft.app(target=main)