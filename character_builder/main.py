import flet as ft
import sys
import os

# Get the root directory of the project (where database.py is located)
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
# Add the root directory to sys.path so Python can find modules there
sys.path.insert(0, project_root)

import database
from character_item import build_item


def main(page: ft.Page):
    page.title = "Character Builder"

    

    def add_character(e):
        name = name_field.value
        
        if name:
            character_data = (name, 1, 1, 1, 1, 1, 1) # Create a tuple with default values
            database.add_character(character_data) # add character to database
            name_field.value = "" # clear name field
            update_characters_view() # update the list of characters
            page.update() # update the UI

    def update_characters_view():
        characters = database.get_all_characters()
        character_list_column.controls.clear()
        for character in characters:
            character_list_column.controls.append(build_item(character, item_delete))
        page.update()


    def item_delete(id):
       database.remove_character(id)
       update_characters_view()
       page.update()

    # UI elements for character creation
    name_field = ft.TextField(label="Character Name")
    create_button = ft.ElevatedButton("Create Character", on_click=add_character)
    character_list_column = ft.Column([])


    database.create_characters_table() # create characters table
    update_characters_view() # initial render of the characters

    # Layout for the UI
    page.add(
      ft.Column(
        [
          ft.Row(
                [name_field],
                 alignment=ft.MainAxisAlignment.CENTER
              ),
            ft.Row(
                [create_button],
                 alignment=ft.MainAxisAlignment.CENTER
             ),
             ft.Container(
                content=character_list_column,
                border=ft.border.all(1),
                padding=10
             ),

         ]
       )
    )

ft.app(target=main)