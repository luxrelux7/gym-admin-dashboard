Gym Membership System

This is a functional admin tool for small gym owners to manage their member database. It allows for quick registration, plan tracking, and revenue oversight using a simple web interface.
Key Features

  *  Member Onboarding: Register new members with automatic formatting (proper name casing) and plan assignment.

  *  Live Dashboard: Instant view of total revenue and membership count.

  *  Searchable Records: A filterable table showing member plans, payments, and their specific join dates.

  *  Plan Management: An admin section to upgrade members to different tiers (Gold, Silver, Bronze) or remove them from the system.

  *  Custom Styling: Integrated theme support to change app colors (like the "Neon Green" primary color) via a configuration file.

How it Works

  *  Logic: Built with Python and Streamlit using a CRUD (Create, Read, Update, Delete) structure.

  *  Storage: Data is saved locally in gym_data.json. The app automatically handles file creation and date stamping for new members.

  *  Theming: Custom colors are managed in .streamlit/config.toml.

Setup Instructions

    Installation
    Ensure you have Streamlit installed:
    Bash

    pip install streamlit

    Configuration
    To use the custom look, ensure the .streamlit/config.toml file is in your project folder.

    Run the App
    Bash

    streamlit run app.py

Future Enhancements

While the app is fully functional for local use, future versions could include:

  *  Moving from JSON to an SQLite database for better scaling.

  *  Adding login credentials for a more secure admin area.

  *  Visualizing revenue trends with charts and graphs.

License

This project is open-source and intended for educational and personal use.