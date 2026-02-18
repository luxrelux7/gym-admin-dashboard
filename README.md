Gym Membership System

This is a local management tool built with Python and Streamlit. It was designed to help small gym owners handle their daily operations without needing complex software or expensive subscriptions.
Key Features

   * Member Registration: A simple interface to add new members and assign them to Gold, Silver, or Bronze plans.

   * Live Dashboard: Real-time tracking of total active members and total revenue based on current plan assignments.

   * Member Database: A searchable table that lists all registered members and their payment status.

   * Plan Management: Admin tools to quickly upgrade or downgrade a member's plan or remove a member from the system entirely.

   * Local Data Storage: Uses a JSON-based system to ensure data persists even after the application is closed.

Technical Stack

   * Frontend: Streamlit

   * Language: Python

   * Database: JSON (Local file storage)

Getting Started

    Prerequisites
    You will need Python and the Streamlit library installed on your machine.
    Bash

    pip install streamlit

    Installation
    Clone this repository or download the files to a local folder.

    Running the App
    Navigate to the project folder in your terminal and run:
    Bash

    streamlit run app.py