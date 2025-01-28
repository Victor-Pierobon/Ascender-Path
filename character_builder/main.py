import flet as ft
import sys
import os
# Get the root directory of the project (where database.py is located)
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
# Add the root directory to sys.path so Python can find modules there
sys.path.insert(0, project_root)
import database
from character_builder.components.character_item import build_item


def main(page: ft.Page):
    page.title = "Character Builder"

    def update_dropdowns():
       characters = database.get_all_characters()
       quests = database.get_all_quests()

       characters_dropdown.options.clear()
       for character in characters:
          characters_dropdown.options.append(ft.dropdown.Option(str(character["id"]), text=character["name"]))
       
       quests_dropdown.options.clear()
       for quest in quests:
        quests_dropdown.options.append(ft.dropdown.Option(str(quest[0]), text=quest[1]))
       page.update()


    def add_character(e):
        name = name_field.value
        
        if name:
            character_data = (name,) # Create a tuple with default values
            database.add_character(character_data) # add character to database
            name_field.value = "" # clear name field
            update_characters_view() # update the list of characters
            update_dropdowns()
            page.update() # update the UI

    def add_xp(character_id, stat_name, xp_amount):
        database.add_xp_to_stat(character_id, stat_name, xp_amount)
        update_characters_view()
        page.update()

    def update_characters_view():
        characters = database.get_all_characters()
        character_list_column.controls.clear()
        for character in characters:
            character_list_column.controls.append(build_item(character, item_delete, add_xp, show_character_quests, complete_quest_from_character))
        page.update()


    def item_delete(id):
       database.remove_character(id)
       update_characters_view()
       page.update()

    def add_quest_to_character_test(e):
        character_id = characters_dropdown.value
        quest_id = quests_dropdown.value
        if character_id and quest_id:
            database.add_quest_to_character(int(character_id), int(quest_id))
            confirmation_text.value = f"Quest {quest_id}, added to character {character_id}!"
            update_characters_view()
            page.update()

    def show_character_quests(id):
        nonlocal character_id
        character_id = id
        page.route = "/quests"
        page.update()

    def complete_quest_from_character(character_id, quest_id):
        database.complete_quest(character_id, quest_id)
        update_characters_view()
        page.update()

    # UI elements for character creation
    name_field = ft.TextField(label="Character Name")
    create_button = ft.ElevatedButton("Create Character", on_click=add_character)
    character_list_column = ft.Column([])

    characters_dropdown = ft.Dropdown(label="Characters")
    quests_dropdown = ft.Dropdown(label="Quests")
    confirmation_text = ft.Text("")
    character_id = ""

    database.create_character_stat_table() # create stat table
    database.create_characters_table() # create characters table
    database.create_quests_table()
    database.create_character_quests_table()
    update_characters_view() # initial render of the characters
    update_dropdowns()

    add_quest_to_char_button = ft.ElevatedButton("Add Quest To Character", on_click= add_quest_to_character_test)

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
             ft.Row(
               [characters_dropdown, quests_dropdown],
               alignment=ft.MainAxisAlignment.CENTER  
             ),
             ft.Row(
                 [add_quest_to_char_button],
                 alignment=ft.MainAxisAlignment.CENTER
             ),
             ft.Row(
                [confirmation_text],
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