# Ascender-Path (Tkinter Version)

This document outlines the development plan for "Ascender Path" using Python and Tkinter, following a phased approach similar to the original project plan.

**Why Tkinter?**

After encountering challenges with Kivy setup, we are transitioning to Tkinter for this project. Tkinter is Python's built-in GUI library, known for its simplicity and cross-platform compatibility for desktop applications. This change aims to prioritize a smoother development experience and focus on core application logic.

**Project Phases (Tkinter Adaptation)**

We will follow a phased approach, building upon core concepts and gradually integrating features, mirroring the original project plan but adapted for Tkinter's capabilities and paradigms.

**PHASE 1: Core Building Blocks (Focus: Python & Basic Tkinter UI)**

    ✓ Project 1: "Basic Task Tracker" - Python & Simple Tkinter UI (Focus: Input, Output, and Lists)

        Goal: Create a simple Tkinter application to manage a list of tasks.

    Features:

        Entry widget for adding new tasks.
        Button to add tasks to a list.
        Listbox widget to display the task list in a scrollable format.
        Simple styling and layout in Tkinter (basics).

    Learning Points:

        Basic Tkinter UI elements (Entry, Button, Listbox, Frame, Label).
        Working with lists in Python.
        Handling user input (getting text from Entry, button clicks).
        Updating UI elements dynamically (updating Listbox).
        Simple state management in Tkinter variables.
        Initial exposure to basic Tkinter structure (root window, widgets, layout managers).

    Why this is important: Establishes basic UI principles, fundamental interactions, and dynamic display, necessary for bigger applications in Tkinter.

    ✓ Project 2: "Enhanced Task Tracker with Persistent Storage" - Python, Tkinter, and SQLite3 (Focus: Database and Data Handling)

        Goal: Extend the Task Tracker to store tasks in a SQLite database.

    Features:

        All features of "Basic Task Tracker".
        Tasks are stored in a SQLite database.
        Tasks are loaded from the database when the app starts.
        Tasks are saved to the database when new tasks are added.
        (Optional) Basic delete option (button to remove selected task from Listbox and database).

    Learning Points:

        Setting up and using SQLite3 databases in Python (same as before).
        Writing SQL queries (INSERT, SELECT, maybe DELETE) (same as before).
        Data persistence concepts (same as before).
        Connecting your Tkinter application to a database.
        Improved state management with database backing.

    Why this is important: Introduces databases and persistent data, necessary for character stats, quests and any data that you want to save (remains the same importance).

**PHASE 2: Building the Foundation of "Ascender Path" (Focus: Core System Concepts)**

    ✓ Project 3: "Simple Character Builder" - Python, Tkinter, and SQLite3 (Focus: Data Modeling)

        Goal: Create a Tkinter app to create and manage character data.

    Features:

        Entry widgets for character name, class, and basic stats (e.g., strength, agility, intelligence).
        Button to save the character data to a SQLite3 table.
        Simple display of the saved character data (using Labels or Text widget).

    Learning Points:

        Designing database schemas to represent game data (same as before).
        Basic form input with Tkinter (Entry widgets, Labels).
        More complex database operations (same as before).
        Basic data validation in the application (same as before).
        Further building on database design (same as before).

    Why this is important: Establish a character creation process, core to your app (remains the same importance).

    - Project 4: "Basic Quest System" - Python, Tkinter, and SQLite3 (Focus: Relational Data)

        Goal: Create a basic quest system with simple quest descriptions.

    Features:

        Ability to add quests with a name and description (using Entry widgets and Button).
        Ability to see quests in a Listbox format.
        Each quest has an ID and is stored in a SQLite database (same as before).
        (Optional) a simple "completed" flag (Checkbox or similar in Tkinter).

    Learning Points:

        Using another table in the database (same as before).
        Creating relationships between database tables (same as before).
        Understanding relationships concepts (same as before).
        Working with different data types (same as before).
        Further building on state management (same as before).

    Why this is important: Establish a quest system, the core of the system (remains the same importance).

**PHASE 3: Integration and Extension (Focus: Combined Concepts)**

    Project 5: "Character Progression Viewer" - Python, Tkinter, and SQLite3 (Focus: Combining Systems)

        Goal: Display character information and progress in Tkinter.

    Features:

        Load character data from the database (same as before).
        Display character name, class, and stats (using Labels and potentially Progress bars - Tkinter `Progressbar` widget).
        (Optionally) Visual representation of stats (Tkinter `Progressbar` or simple text-based bars).
        Display completed quests related to the character (using Listbox or Text widget).

    Learning Points:

        Querying the database with joins (same as before).
        More complex data processing (same as before).
        Displaying data in a presentable way in Tkinter (using Labels, Listbox, Text, Progressbar).
        Further building on data modeling (same as before).

    Why this is important: Show the user progression, and start to combine different systems (remains the same importance).

**PHASE 4: "Ascender Path" (Focus: Full System)**

    Project 6: "Ascender Path" Full System - Combining all the concepts

        Goal: Combine all the previous projects and add the core functionalities needed in Tkinter.

    Features:

        Character Creation (Tkinter forms)
        Leveling System (backend logic, display in Tkinter)
        Quest/Mission System (Tkinter UI for quests)
        Character Progression/Stats Viewer (Tkinter UI)
        User defined quests (Tkinter UI for quest creation)
        And more that we discover during the development

    Learning Points:

        Combining all the concepts and systems (same as before).
        Improve code performance (same focus).
        Debugging complex systems (same focus).
        Architecting the app in a structured way (same focus, but now in Tkinter context).
        Creating a full application using Tkinter.

    Why this is important: Combine everything and achieve the initial idea (remains the same importance).

