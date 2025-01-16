# Ascender-Path

PHASE 1: Core Building Blocks (Focus: Python & Basic Flet UI)

    Project 1: "Basic Task Tracker" - Python & Simple Flet UI (Focus: Input, Output, and Lists)

        Goal: Create a simple Flet application to manage a list of tasks.

    Features:

        Text input for adding new tasks.

        Button to add tasks to a list.

        Display the task list in a scrollable format.

        Simple styling and layout in Flet (basics).

    Learning Points:

        Basic Flet UI elements (text fields, buttons, containers, scrollable columns).

        Working with lists in Python.

        Handling user input.

        Updating UI elements dynamically.

        Simple state management in Flet.

        Initial exposure to basic Flet structure.

    Why this is important: Establishes basic UI principles, fundamental interactions, and dynamic display, necessary for bigger applications.

    Project 2: "Enhanced Task Tracker with Persistent Storage" - Python, Flet, and SQLite3 (Focus: Database and Data Handling)

        Goal: Extend the Task Tracker to store tasks in a SQLite database.

    Features:

        All features of "Basic Task Tracker".

        Tasks are stored in a SQLite database.

        Tasks are loaded from the database when the app starts.

        Tasks are saved to the database when new tasks are added.

        (Optional) Basic delete option.

    Learning Points:

        Setting up and using SQLite3 databases in Python.

        Writing SQL queries (INSERT, SELECT, maybe DELETE).

        Data persistence concepts.

        Connecting your Flet application to a database.

        Improved state management with database backing.

    Why this is important: Introduces databases and persitent data, necessary for character stats, quests and any data that you want to save.

PHASE 2: Building the Foundation of "Ascender Path" (Focus: Core System Concepts)

    Project 3: "Simple Character Builder" - Python, Flet, and SQLite3 (Focus: Data Modeling)

        Goal: Create a Flet app to create and manage character data.

    Features:

        Text input for character name, class, and basic stats (e.g., strength, agility, intelligence).

        Button to save the character data to a SQLite3 table.

        Simple display of the saved character data.

    Learning Points:

        Designing database schemas to represent game data.

        Basic form input with Flet.

        More complex database operations.

        Basic data validation in the application.

        Further building on database design.

    Why this is important: Establish a character creation process, core to your app

    Project 4: "Basic Quest System" - Python, Flet, and SQLite3 (Focus: Relational Data)

        Goal: Create a basic quest system with simple quest descriptions.

    Features:

        Ability to add quests with a name and description (input).

        Ability to see quests in a list format.

        Each quest has an ID and is stored in a SQLite database.

        (Optional) a simple "completed" flag.

    Learning Points:

        Using another table in the database

        Creating relationships between database table.

        Understanding relationships concepts.

        Working with different data types.

        Further building on state management.

    Why this is important: Establish a quest system, the core of the system.

PHASE 3: Integration and Extension (Focus: Combined Concepts)

    Project 5: "Character Progression Viewer" - Python, Flet, and SQLite3 (Focus: Combining Systems)

        Goal: Display character information and progress.

    Features:

        Load character data from the database.

        Display character name, class, and stats.

        (Optionally) Visual representation of stats.

        Display completed quests related to the character.

    Learning Points:

        Querying the database with joins.

        More complex data processing.

        Displaying data in a presentable way in Flet.

        Further building on data modeling.

    Why this is important: Show the user progression, and start to combine different systems.

PHASE 4: "Ascender Path" (Focus: Full System)

    Project 6: "Ascender Path" Full System - Combining all the concepts

        Goal: Combine all the previous projects and add the core functionalities needed.

    Features:

        Character Creation

        Leveling System

        Quest/Mission System

        Character Progression/Stats Viewer

        User defined quests

        And more that we discover during the development

    Learning Points:

        Combining all the concepts and systems.

        Improve code performance.

        Debugging complex systems.

        Architecting the app in a structured way.

        Creating a full application

    Why this is important: Combine everything and achieve the initial idea.