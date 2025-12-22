import streamlit as st
from datetime import datetime

# Page configuration
st.set_page_config(
    page_title="Travel Planner & Hotel Finder",
    page_icon="✈️",
    layout="wide"
)

# Initialize booking in session state
if "booking" not in st.session_state:
    st.session_state.booking = None

# Sample hotel data (dummy data)
HOTELS = [
    {
        "name": "Grand Plaza Hotel",
        "city": "Mumbai",
        "price": 5000,
        "rating": 4.5,
        "description": "Luxury hotel in the heart of Mumbai with stunning sea views and world-class amenities."
    },
    {
        "name": "Budget Inn Mumbai",
        "city": "Mumbai",
        "price": 1500,
        "rating": 3.5,
        "description": "Affordable accommodation with clean rooms and basic facilities near the airport."
    },
    {
        "name": "Royal Residency",
        "city": "Mumbai",
        "price": 3500,
        "rating": 4.0,
        "description": "Mid-range hotel offering comfortable stays with excellent service and dining options."
    },
    {
        "name": "Taj Heritage",
        "city": "Delhi",
        "price": 6000,
        "rating": 5.0,
        "description": "Premium heritage hotel with traditional architecture and modern luxury amenities."
    },
    {
        "name": "Delhi Comfort Stay",
        "city": "Delhi",
        "price": 2000,
        "rating": 3.8,
        "description": "Comfortable budget hotel located near major tourist attractions and metro stations."
    },
    {
        "name": "Capital Grand",
        "city": "Delhi",
        "price": 4500,
        "rating": 4.3,
        "description": "Elegant hotel in central Delhi with spacious rooms and conference facilities."
    },
    {
        "name": "Bangalore Tech Suites",
        "city": "Bangalore",
        "price": 3000,
        "rating": 4.2,
        "description": "Modern hotel near IT parks with high-speed internet and business center."
    },
    {
        "name": "Garden View Hotel",
        "city": "Bangalore",
        "price": 2500,
        "rating": 3.9,
        "description": "Peaceful hotel surrounded by gardens, perfect for a relaxing stay."
    },
    {
        "name": "Silicon Valley Inn",
        "city": "Bangalore",
        "price": 1800,
        "rating": 3.6,
        "description": "Budget-friendly option with clean rooms and friendly staff."
    },
    {
        "name": "Goa Beach Resort",
        "city": "Goa",
        "price": 4000,
        "rating": 4.7,
        "description": "Beachfront resort with private beach access, pool, and water sports facilities."
    },
    {
        "name": "Coastal Paradise",
        "city": "Goa",
        "price": 2800,
        "rating": 4.1,
        "description": "Charming hotel near popular beaches with authentic Goan cuisine."
    },
    {
        "name": "Backpacker's Haven",
        "city": "Goa",
        "price": 1200,
        "rating": 3.7,
        "description": "Budget hostel-style accommodation perfect for solo travelers and backpackers."
    },
    {
        "name": "Jaipur Palace Hotel",
        "city": "Jaipur",
        "price": 5500,
        "rating": 4.8,
        "description": "Royal palace converted into a luxury hotel with traditional Rajasthani hospitality."
    },
    {
        "name": "Pink City Lodge",
        "city": "Jaipur",
        "price": 2200,
        "rating": 3.9,
        "description": "Centrally located hotel near major attractions like Hawa Mahal and City Palace."
    },
    {
        "name": "Heritage Haveli",
        "city": "Jaipur",
        "price": 3800,
        "rating": 4.4,
        "description": "Traditional haveli-style hotel with authentic Rajasthani decor and cuisine."
    }
]

# List of cities (extracted from hotel data)
CITIES = sorted(list(set([hotel["city"] for hotel in HOTELS])))

# Main title
st.title("✈️ Travel Planner & Hotel Finder")
st.markdown("---")

# Sidebar for user inputs
st.sidebar.header("📋 Plan Your Trip")

# Source city input
source_city = st.sidebar.text_input(
    "Source City",
    placeholder="e.g., Kolkata",
    help="Enter the city you're traveling from"
)

# Destination city selection
destination_city = st.sidebar.selectbox(
    "Destination City",
    options=[""] + CITIES,
    help="Select your destination city"
)

# Travel date
travel_date = st.sidebar.date_input(
    "Travel Date",
    value=datetime.now(),
    help="Select your travel date"
)

# Number of days
num_days = st.sidebar.number_input(
    "Number of Days",
    min_value=1,
    max_value=30,
    value=3,
    help="How many days will you stay?"
)

# 👉 NEW: Number of members
num_members = st.sidebar.number_input(
    "Number of Members",
    min_value=1,
    max_value=10,
    value=2,
    help="How many people are traveling?"
)

st.sidebar.markdown("---")
st.sidebar.subheader("🔍 Filter Hotels")

# Budget range filter
min_budget, max_budget = st.sidebar.slider(
    "Budget Range (₹ per night)",
    min_value=0,
    max_value=10000,
    value=(0, 10000),
    step=500,
    help="Set your budget range for hotel accommodation"
)

# Rating filter
min_rating = st.sidebar.slider(
    "Minimum Hotel Rating",
    min_value=1.0,
    max_value=5.0,
    value=1.0,
    step=0.5,
    help="Filter hotels by minimum rating"
)

# Sorting option
sort_by = st.sidebar.radio(
    "Sort Hotels By",
    options=["Price (Low to High)", "Price (High to Low)", "Rating (High to Low)"],
    help="Choose how to sort the hotel results"
)

# Main content area
if not destination_city:
    # Show welcome message if no destination selected
    st.info("👈 Please select a destination city from the sidebar to view available hotels.")
    
    # Display some helpful information
    st.subheader("🌟 Welcome to Travel Planner!")
    st.write("""
    This app helps you plan your travel and find the perfect hotel for your stay.
    
    **How to use:**
    1. Enter your source city in the sidebar  
    2. Select your destination city  
    3. Choose your travel date, number of days, and members  
    4. Set your budget and rating preferences  
    5. Browse and book a hotel
    """)
    
    # Display available cities in columns
    st.subheader("📌 Available Destinations")
    cols = st.columns(3)
    for idx, city in enumerate(CITIES):
        with cols[idx % 3]:
            st.write(f"• {city}")

else:
    # Display travel summary
    st.subheader("📍 Your Travel Plan")
    
    col1, col2, col3, col4, col5 = st.columns(5)
    
    with col1:
        st.metric("From", source_city if source_city else "Not specified")
    
    with col2:
        st.metric("To", destination_city)
    
    with col3:
        st.metric("Date", travel_date.strftime("%d %b, %Y"))
    
    with col4:
        st.metric("Duration", f"{num_days} day{'s' if num_days > 1 else ''}")
    
    with col5:
        st.metric("Members", f"{num_members}")
    
    st.markdown("---")
    
    # Filter hotels based on destination and user preferences
    filtered_hotels = [
        hotel for hotel in HOTELS
        if hotel["city"] == destination_city
        and min_budget <= hotel["price"] <= max_budget
        and hotel["rating"] >= min_rating
    ]
    
    # Sort hotels based on user preference
    if sort_by == "Price (Low to High)":
        filtered_hotels.sort(key=lambda x: x["price"])
    elif sort_by == "Price (High to Low)":
        filtered_hotels.sort(key=lambda x: x["price"], reverse=True)
    else:  # Rating (High to Low)
        filtered_hotels.sort(key=lambda x: x["rating"], reverse=True)
    
    # Display hotels
    st.subheader(f"🏨 Available Hotels in {destination_city}")
    
    if not filtered_hotels:
        st.warning(f"No hotels found matching your criteria in {destination_city}. Try adjusting your filters.")
    else:
        st.success(f"Found {len(filtered_hotels)} hotel{'s' if len(filtered_hotels) > 1 else ''} matching your preferences!")
        
        # Display each hotel in a card-like format
        for hotel in filtered_hotels:
            with st.container():
                col1, col2 = st.columns([3, 1])
                
                with col1:
                    st.markdown(f"### {hotel['name']}")
                    st.write(hotel['description'])
                    st.caption(f"📍 Location: {hotel['city']}")
                
                with col2:
                    st.markdown(f"**₹{hotel['price']:,}**")
                    st.caption("per night (per room)")
                    st.markdown(f"⭐ **{hotel['rating']}/5.0**")
                    
                    # Total cost considering days and members
                    total_cost = hotel['price'] * num_days * num_members
                    st.info(
                        f"Total: ₹{total_cost:,}\n"
                        f"{num_days} night(s) × {num_members} member(s)"
                    )

                    # 👉 NEW: Booking button
                    if st.button("Book Now", key=f"book_{hotel['name']}"):
                        st.session_state.booking = {
                            "hotel_name": hotel["name"],
                            "city": hotel["city"],
                            "price_per_night": hotel["price"],
                            "rating": hotel["rating"],
                            "source_city": source_city,
                            "destination_city": destination_city,
                            "travel_date": travel_date,
                            "num_days": num_days,
                            "num_members": num_members,
                            "total_cost": total_cost,
                        }
                        st.success(f"✅ Booking selected for {hotel['name']}!")

                st.markdown("---")

    # 👉 NEW: Show booking summary if any hotel is booked
    if st.session_state.booking:
        st.subheader("🧾 Your Booking Summary")
        booking = st.session_state.booking

        col_a, col_b = st.columns(2)
        with col_a:
            st.write(f"**Traveler Route:** {booking['source_city'] or 'Not specified'} → {booking['destination_city']}")
            st.write(f"**Travel Date:** {booking['travel_date'].strftime('%d %b, %Y')}")
            st.write(f"**Duration:** {booking['num_days']} day(s)")
            st.write(f"**Members:** {booking['num_members']}")

        with col_b:
            st.write(f"**Hotel:** {booking['hotel_name']}")
            st.write(f"**City:** {booking['city']}")
            st.write(f"**Price per Night:** ₹{booking['price_per_night']:,}")
            st.write(f"**Hotel Rating:** ⭐ {booking['rating']}/5.0")
            st.write(f"**Total Cost:** 💰 ₹{booking['total_cost']:,}")

        st.info("This is a demo booking. In a real app, payment and confirmation steps would follow.")

# Footer
st.sidebar.markdown("---")
st.sidebar.markdown("### 💡 Tips")
st.sidebar.info("""
- Book in advance for better rates  
- Check hotel reviews before booking  
- Compare prices across different dates  
- Consider location proximity to attractions  
""")
