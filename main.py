import streamlit as st

SOCIAL_MEDIA_FACTORS = {
 "Facebook": 0.0474,
   "Instagram": 0.0066,
    "X": 0.036,
    "WhatsApp": 0.00072,
    "YouTube": 0.0276,
    "Gmail": 0.0006,
    "Google Chrome": 0.00084,
    "GitHub": 0.0006,
    "Snapchat": 0.0522,
    "LinkedIn": 0.0426,
    "Reddit": 0.00042,
    "Pinterest":0.078,
}

ICON_PATHS = {
    "Facebook": "https://img.icons8.com/color/96/000000/facebook.png",
    "Instagram": "https://img.icons8.com/color/96/000000/instagram-new.png",
    "X": "https://img.icons8.com/ios/50/000000/x.png",
    "YouTube": "https://img.icons8.com/color/96/000000/youtube-play.png",
    "Snapchat": "https://img.icons8.com/color/96/000000/snapchat.png",
    "LinkedIn": "https://img.icons8.com/color/96/000000/linkedin.png",
    "Reddit": "https://img.icons8.com/color/96/000000/reddit.png",
    "Pinterest": "https://img.icons8.com/color/96/000000/pinterest.png",
    "Gmail": "https://img.icons8.com/color/96/000000/gmail.png",
    "Google Chrome": "https://img.icons8.com/color/96/000000/google.png",
    "GitHub": "https://img.icons8.com/ios/50/000000/github.png",
    "WhatsApp": "https://img.icons8.com/color/96/000000/whatsapp.png"
}

st.set_page_config(layout="wide", page_title="Social Media Carbon Footprint Calculator")

st.title("📱 Social Media Carbon Footprint Calculator")

st.markdown(
    """
   <style>
body {
    background-color: #f5f5f5; /* Light background color for better contrast */
    color: #333;
    font-family: Arial, sans-serif;
}

.app-container {
    text-align: center;
    margin: 20px;
    border: 2px solid #b0bec5; /* Soft gray-blue border for subtlety */
    border-radius: 12px;
    padding: 20px;
    background-color: #ffffff; /* White background for the container */
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
    display: flex;
    flex-direction: column;
    align-items: center;
    border-image: linear-gradient(45deg, #b0bec5, #eceff1) 1; /* Soft gradient border */
}

.app-icon {
    width: 100px;
    height: 100px;
    margin-bottom: 10px;
    display: flex;
    justify-content: center;
    align-items: center;
    overflow: hidden;
    border-radius: 10px;
    transition: transform 0.3s ease, box-shadow 0.3s ease;
}

.app-icon img {
    max-width: 100%;
    max-height: 100%;
    object-fit: contain;
    transition: transform 0.3s ease, box-shadow 0.3s ease;
}

.app-icon:hover {
    transform: scale(1.05);
    box-shadow: 0 6px 12px rgba(0, 0, 0, 0.3);
}

.app-icon:hover img {
    transform: scale(1.05);
}

.app-title {
    font-size: 18px;
    font-weight: 600;
    margin: 10px 0;
    color: #37474f; /* Dark slate gray color for the title */
}

.result-highlight {
    font-size: 18px;
    font-weight: bold;
    color: #ffffff;
    padding: 10px;
    background-color: #009688; /* Teal color for the result background */
    border: 1px solid #00796b; /* Darker shade of teal for the border */
    border-radius: 8px;
    margin-top: 10px;
    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
    text-align: center;
}

.footer {
    font-size: 14px;
    color: #666;
    margin-top: 20px;
}
</style>

    """,
    unsafe_allow_html=True
)

row_count = 3
col_count = len(SOCIAL_MEDIA_FACTORS) // row_count + (len(SOCIAL_MEDIA_FACTORS) % row_count > 0)
for row in range(row_count):
    cols = st.columns(col_count)
    for col in range(col_count):
        app_index = row * col_count + col
        if app_index >= len(SOCIAL_MEDIA_FACTORS):
            break
        app = list(SOCIAL_MEDIA_FACTORS.keys())[app_index]
        with cols[col]:
            st.markdown(f'<div class="app-container"><div class="app-icon"><img src="{ICON_PATHS[app]}" width="80" height="80" alt="{app}"></div>', unsafe_allow_html=True)
            st.markdown(f'<div class="app-title">{app}</div>', unsafe_allow_html=True)
            daily_usage_hours = st.slider(f"{app} Daily Usage (in hours)", 0.0, 24.0, 0.0)
            emission_factor = SOCIAL_MEDIA_FACTORS[app]
            yearly_usage_hours = daily_usage_hours * 365
            carbon_emissions = round(emission_factor * yearly_usage_hours, 2)  # kg of CO2 per year
            st.markdown(f'<div class="result-highlight">{carbon_emissions} kg CO2/year</div>', unsafe_allow_html=True)
            st.markdown('</div>', unsafe_allow_html=True)

st.markdown("---")
st.markdown("### Strategies for Reducing Your Carbon Footprint")
st.write(
    """
    - **Limit Usage:** Reduce the time spent on social media to lower emissions.
    - **Optimize Data Usage:** Use lower resolution settings and avoid auto-play features.
    - **Switch to Green Energy:** Ensure that your devices and networks are powered by renewable energy sources.
    """
)
st.markdown('<div class="footer">Note: The carbon footprint data provided is based on estimations and may vary over time. It should be considered as a general guideline rather than an exact measurement.</div>', unsafe_allow_html=True)