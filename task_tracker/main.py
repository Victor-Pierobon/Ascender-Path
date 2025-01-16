import flet as ft

def main(page: ft.Page):
    page.title = "Task Tracker"

    task_list = [] 

    # how it should store and displays tasks
    def add_task(e): # e is the event
     task = task_field.value # get the value of the task field
     if task:
        task_list.append({"task": task}) # store each task as a dictionary
        task_field.value = "" 
        update_task_list_view()
        page.update()

    def clear_list(e):
       task_list.clear()
       update_task_list_view()
       page.update()

    def item_delete(index):
       task_list.pop(index)
       update_task_list_view()
       page.update()

    def build_item(task, index):
       return ft.Row([
          ft.Text(task["task"]),
          ft.ElevatedButton("Delete", on_click=lambda e: item_delete(index))
       ])

    # components and actions
    task_field = ft.TextField(label = "Add task", on_submit=add_task) # on_submit is an event that triggers when the user presses enter
    add_button = ft.ElevatedButton("Add", on_click=add_task) # on_click is an event that triggers when the user clicks the button
    clear_button = ft.ElevatedButton("Clear", on_click=clear_list)
    task_list_column = ft.Column([])

    def update_task_list_view():
       task_list_column.controls.clear()
       for index, task in enumerate(task_list):
          task_list_column.controls.append(build_item(task, index))

    page.update()

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