import streamlit as st

st.title("🎟️ Check Your Ticket Status")

# Ask user to input phone number
phone_check = st.text_input("Enter your phone number to check ticket:")

if st.button("Check Ticket"):
    if phone_check:
        stored_phone = st.session_state.get("phone", None)

        if stored_phone == phone_check:
            st.success("✅ Ticket Found!")
            st.write("📌 Booking ID:", st.session_state.get("booking_id", "N/A"))
            st.write("👤 Name:", st.session_state.get("user_name", "N/A"))
            st.write("📧 Email:", st.session_state.get("email", "N/A"))
            st.write("📅 Date:", st.session_state.get("date", "N/A"))
            st.write("🎟️ Tickets:", st.session_state.get("tickets", "N/A"))
        else:
            st.error("❌ No ticket found for this phone number.")
    else:
        st.warning("Please enter a phone number.")
if st.button("🏠 Back to Home Page"):
    st.switch_page("frontpage.py")  # Change to your actual home page script
