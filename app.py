import streamlit as st
import json
import os

def save_gym_data(data):
    with open("gym_data.json", "w") as f:
        json.dump(data, f, indent=4)

def load_gym_data():
    if os.path.exists("gym_data.json"):
        with open("gym_data.json", "r") as f:
            return json.load(f)
    return{}  

st.title("Gym Membership App")
st.write("Welcome to the Registration Page.")     
        
data = load_gym_data()
choice = st.sidebar.selectbox("Menu", ["Register", "View Members"])

if choice == "Register":
    new_name = st.text_input("Enter member name: ").strip().capitalize()
    plan_choice = st.selectbox("Choose a plan:", ["Gold", "Silver", "Bronze"])
    
    prices = {"Gold": 125, "Silver": 100, "Bronze": 75}
    current_price = prices[plan_choice]    
    st.info(f"The price for the {plan_choice} plan is ${current_price}")

    if st.button("Register Now"):
        if new_name == "":
            st.error("Please enter your name: ")
        elif new_name in data:
            st.error(f"{new_name} is already in the system.")
        else:
            data[new_name] = {"plan": plan_choice, "amount_paid": current_price}
            st.success(f"Successfully registered {new_name}!")
            save_gym_data(data)
            st.rerun()       

       
elif choice == "View Members":
    col1, col2 = st.columns(2)
    
    total_revenue = sum(m.get("amount_paid", 0) for m in data.values())
    total_members = len(data)
    
    col1.metric("Total Revenue", f"${total_revenue}")
    col2.metric("Total Members", total_members)
    
    search_term = st.text_input("Search")
    results = [name for name in data if search_term.lower() in name.lower()]
    if not data:
        st.info("No members found")
    elif search_term:
        st.table(results)
    else:
        st.table(data)
        
    st.divider()
    st.subheader("Admin: Upgrade/Change Plan")

    upgrade_name = st.selectbox("Select member to upgrade:", list(data.keys()), key="upgrade_select")

    if upgrade_name:
        current_p = data[upgrade_name]["plan"]
        st.write(f"**{upgrade_name}** is currently on the **{current_p}** plan.")
        new_plan = st.selectbox("Choose new plan:", ["Gold", "Silver", "Bronze"], key="new_plan_select")
        prices = {"Gold": 125, "Silver": 100, "Bronze": 75}

    if st.button("Update Plan"):
        data[upgrade_name]["plan"] = new_plan
        data[upgrade_name]["amount_paid"] = prices[new_plan] 
        save_gym_data(data)
        st.success(f"Success! {upgrade_name} is now on the {new_plan} plan.")
        st.rerun()

        st.divider()
        st.subheader("Admin: Remove Member")
        member_list = list(data.keys())
        
    st.divider()
    st.subheader("Admin: Remove Member")
    member_list = list(data.keys())

    if member_list:
        delete_name = st.selectbox("Select a member to delete:", member_list)
        if st.button("Delete Member", type="primary"):
            del data[delete_name]
            save_gym_data(data)
            st.success(f"Deleted {delete_name}")
            st.rerun()
        else:
            st.write("No members to delete.")