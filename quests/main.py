import flet as ft
import sys
import os

# Get the root directory of the project (where database.py is located)
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
# Add the root directory to sys.path so Python can find modules there
sys.path.insert(0, project_root)
import database
from quests.components.quest_item import build_item

def main(page: ft.Page, character_id):
    page.title = "Character Quests"
    # character_id = page.route.split("?")[1].split("=")[1] if len(page.route.split("?")) > 1 else ""

    def update_quest_list_view():
       quests = database.get_all_character_quests(int(character_id))
       quest_list_column.controls.clear()
       for quest in quests:
          quest_list_column.controls.append(build_item(quest, item_delete, complete_quest))
       page.update()


    def item_delete(id):
       database.remove_quest_from_db(id)
       update_quest_list_view()
       page.update()
    
    def complete_quest(id):
      database.complete_quest(character_id, id)
      update_quest_list_view()
      page.update()


    quest_list_column = ft.Column([])
    
    update_quest_list_view()
   

    # User interface
    page.add(
        ft.Column([
          ft.Text(f"Character Quests: {character_id}"),
        ft.Container(
            content=quest_list_column,
            border=ft.border.all(1),
            padding=10
        )
        ])
    )

ft.app(target=main)