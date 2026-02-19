Gym Membership System

A simple web application built with Streamlit to manage gym members, track subscriptions, and monitor revenue.

This project allows you to register members, assign membership plans, update plans, search for members, and remove members when needed. Data is stored locally using a JSON file.

Features

Register new gym members

Choose between Gold, Silver, and Bronze plans

Automatically calculate total revenue

View total number of members

Search for members by name

Upgrade or change a member’s plan

Remove members from the system

Persistent storage using a local JSON file

Customizable Streamlit theme

Tech Stack

Python

Streamlit

JSON (for local data storage)

Project Structure
gym-membership-system/
│
├── app.py
├── gym_data.json (auto-created)
└── .streamlit/
    └── config.toml

Installation

Clone the repository or download the project folder.

Install Streamlit if you haven’t already:

pip install streamlit


Navigate to the project directory:

cd gym-membership-system


Run the app:

streamlit run app.py


The app will open in your browser.

Theme Configuration

The app uses a custom Streamlit theme defined in:

.streamlit/config.toml


You can modify the colors inside that file to change the look and feel of the app.

Example:

[theme]
primaryColor = "#39FF14"
backgroundColor = "#0E1117"
secondaryBackgroundColor = "#1C1F26"
textColor = "#FAFAFA"
font = "sans serif"


After changing the theme, restart the app.

Data Storage

All member data is stored locally in:

gym_data.json


The file is automatically created when the first member is registered.

Each member record includes:

Name

Plan

Amount paid

Join date

Future Improvements

Some possible enhancements:

Use SQLite instead of JSON

Add authentication (admin login)

Add revenue charts and analytics

Implement recurring monthly billing

Deploy to Streamlit Cloud

License

This project is for educational and personal use.