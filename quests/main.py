import flet as ft
import sys
import os
# Get the root directory of the project (where database.py is located)
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
# Add the root directory to sys.path so Python can find modules there
sys.path.insert(0, project_root)
import database
from quests.components.quest_item import build_item

def main(page: ft.Page):
    page.title = "Quests"

    # UI elements fo quest creation
    quest_name_field = ft.TextField(label="Quest name")
    quest_description_field = ft.TextField(label="Quest Description")
    quest_rank_dropdown = ft.Dropdown(
       label="Quest Rank",
       options=[
          ft.dropdown.Option("E"),
          ft.dropdown.Option("D"),
          ft.dropdown.Option("C"),
          ft.dropdown.Option("B"),
          ft.dropdown.Option("A"),
          ft.dropdown.Option("S"),
       ]
    )
   
    def add_a_quest(e):
     quest_name = quest_name_field.value
     quest_description =quest_description_field.value
     quest_rank = quest_rank_dropdown.value

     if quest_name and quest_description and quest_rank:
        database.add_quest(quest_name, quest_description, quest_rank)
        quest_name_field.value = ""
        quest_description_field.value = ""
        update_quest_list_view()
        page.update()


    def item_delete(id):
       database.remove_quest_from_db(id)
       update_quest_list_view()
       page.update()

    def add_quest_to_character(character_id, quest_id):
       database.add_character_quest(character_id, quest_id)
       update_quest_list_view()
       page.update()

    def complete_quest(quest_id):
       database.complete_quest(quest_id)
       update_quest_list_view()
       page.update()

    def update_quest_list_view():
       quests = database.get_all_quests()
       character_quests = database.get_all_character_quests(1)
       quest_list_column.controls.clear()
       for quest in quests:
          quest_list_column.controls.append(build_item(quest, item_delete, add_quest_to_character, complete_quest))
    page.update()


    create_button = ft.ElevatedButton("Create Quest", on_click=add_a_quest)
    quest_list_column = ft.Column([])

    database.create_quests_table()
    database.create_characters_table()
    database.create_character_stat_table()
    database.create_character_quests_table()
    update_quest_list_view()
    page.update()

    # User interface
    page.add(
        ft.Column([
           ft.Row(
                [quest_name_field, quest_description_field, quest_rank_dropdown],
                 alignment=ft.MainAxisAlignment.CENTER
             ),
            ft.Row(
                [create_button],
                 alignment=ft.MainAxisAlignment.CENTER
             ),
        ft.Container(
            content=quest_list_column,
            border=ft.border.all(1),
            padding=10
        )
        ])
    )

ft.app(target=main)