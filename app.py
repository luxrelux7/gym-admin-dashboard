import streamlit as st
import json
import os
from datetime import datetime

prices = {"Gold": 125, "Silver": 100, "Bronze": 75}
data_file = "gym_data.json"

#Helper Functions
def save_gym_data(data):
    with open(data_file, "w") as f:
        json.dump(data, f, indent=4)
        
def load_gym_data():
    if os.path.exists(data_file):
        with open(data_file, "r") as f:
            return json.load(f)
    return {}

#App title
st.title("Gym Membership App")
st.write("Welcome to the Registration Page.")

#Load Data
data = load_gym_data()

#Sidebar Navigation
choice = st.sidebar.selectbox("Menu", ["Register", "View Members"])
        
#Registration Section

if choice == "Register":

    new_name = st.text_input("Enter your name: ").strip().title()
    plan_choice = st.selectbox("Choose a plan: ", list(prices.keys()))
    
    current_price = prices[plan_choice]
    st.info(f"The price for the {plan_choice} plan is ${current_price}")
    
if st.button("Register Now"):
    if not new_name:
        st.error("Please enter your name.")
    elif new_name in data:
        st.error(f"{new_name} is already in the system")
    else:
        data[new_name] = {
        "plan": plan_choice,
        "amount_paid": current_price,
        "join_data": datetime.now().strftime("%Y-%m-%d")
    }
    
    save_gym_data(data)
    st.success(f"Successfully Registered {new_name}!")
    st.rerun()
    
#View Members Section
elif choice == "View Members":

    col1, col2 = st.columns(2)
    
    total_revenue = sum(m.get("amount_paid", 0) for m in data.values())
    total_members = len(data)
    
    st.divider()
    
    #Search
    search_term = st.text_input("Search")
    
    if not data:
        st.info("No members found.")
    else:
        if search_term:
            results = {
                name: info
                for name, info in data.items()
                if search_term.lower() in name.lower()
            }
            st.table(results)
        else:
            st.table(data)
            
    st.divider()
    
    #Upgrade Section
    
    st.subheader("Admin: Upgrade/Change Plan")
    
    if data:
        upgrade_name = st.selectbox(
            "Select member to upgrade:",
            list(data.keys()),
            key="upgrade_select"
        )
        
        current_plan = data[upgrade_name]["plan"]
        st.write(f"**{upgrade_name}** is currently on the **{current_plan}** plan.")
        
        new_plan = st.selectbox(
            "Choose new plan:",
            list(prices.keys()),
            key = "new_plane_select"
        )
        
        if st.button("Upgrade Plan"):
            data[upgrade_name]["plan"] = new_plan
            data[upgrade_name]["amount_paid"] = prices[new_plan]
            
            save_gym_data(data)
            st.success(f"{upgrade_name} is now on the {new_plan} plan.")
        else:
            st.info("No members available to upgrade")
            
        st.divider()
        
        #Delete Section
        st.subheader("Admin: Remove Member")

        if data:
            delete_name = st.selectbox(
                "Select a member to delete",
                list(data.keys()),
                key = "delete_select"
            )
                
            if st.button("Delete Member", type="primary"):
                    del data[delete_name]
                    save_gym_data(data)
                    st.success(f"{delete_name} has been remove")
                    st.rerun()
            else:
                st.info("No members to delete")
        
        