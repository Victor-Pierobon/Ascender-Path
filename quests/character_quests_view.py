import flet as ft
import sys
import os
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, project_root)
import database
from quests.components.quest_item import build_item

def main(page: ft.Page, character_id):
    page.title = f"Character Quests - Character ID: {character_id}"

    def update_quest_list_view():
        print(f"update_quest_list_view called, character_id={character_id}")  # Debug print 1 - before query
        quests = database.get_all_character_quests(int(character_id))
        print(f"quests: {quests}")  # Debug print 2 - after query - what data are we getting?
        quest_list_column.controls.clear()
        for quest in quests:
            quest_list_column.controls.append(build_item(quest, item_delete, complete_quest))
        page.update()
        print("after update") # Debug print 3 - after page.update()


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

    print(f"page at return from character_quests_view {page}") # Debug print 4 - just before return

    return ft.View(
        f"/quests?id={character_id}",  # Keep the route the same as navigation
        [
            ft.Text(f"Character Quests (Character ID: {character_id})", style=ft.TextStyle(size=20)),
            ft.Container(
                content=quest_list_column,
                border=ft.border.all(1),
                padding=10
            )
        ],
    )