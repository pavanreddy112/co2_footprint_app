import streamlit as st

GAME_FACTORS = {
        "BGMI": 0.019,
    "Free Fire": 0.018,
    "Among Us": 0.011,
    "Clash of Clans": 0.012,
    "Call of Duty": 0.050,
    "Minecraft": 0.016,
    "PUBG": 0.048,
    "Fortnite":0.045,

}

ICON_PATHS = {
    "BGMI": "https://res.cloudinary.com/di7wy7ldo/image/upload/v1725677144/bgmi_zm1soq.png",
    "Free Fire": "https://res.cloudinary.com/di7wy7ldo/image/upload/v1725677148/free-fire_y37wkw.png",
    "Among Us": "https://res.cloudinary.com/di7wy7ldo/image/upload/v1725679706/resize-17256796642139617138amoungus_ieldyq.png",
    "Clash of Clans": "https://res.cloudinary.com/di7wy7ldo/image/upload/v1725680227/resize-172567989238515125clash_godc0w.png",
    "Call of Duty": "https://res.cloudinary.com/di7wy7ldo/image/upload/v1725677145/cod_fzpi58.png",
    "Minecraft": "https://res.cloudinary.com/di7wy7ldo/image/upload/v1725680227/wp6548068_jzulup.png",
    "PUBG": "https://res.cloudinary.com/di7wy7ldo/image/upload/v1725680226/pubg-logo-5322826_960_720_ahgeuw.png",
    "Fortnite": "https://res.cloudinary.com/di7wy7ldo/image/upload/v1725680226/fortnite-logo-fortnite-logo-white-background-vector-format-available-ai-246319808_siiq20.png"
}

st.set_page_config(layout="wide", page_title="Gaming Carbon Footprint Calculator")

st.title("🎮 Gaming Carbon Footprint Calculator")

st.markdown(
    """
    <style>
    .game-container {
        text-align: center;
        margin: 20px;
        border: 1px solid #ccc;
        border-radius: 12px;
        padding: 20px;
        background-color: #fff;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
        display: flex;
        flex-direction: column;
        align-items: center;
    }
    .game-icon {
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
    .game-icon img {
        max-width: 100%;
        max-height: 100%;
        object-fit: contain;
        transition: transform 0.3s ease, box-shadow 0.3s ease;
    }
    .game-icon:hover {
        transform: scale(1.05);
        box-shadow: 0 6px 12px rgba(0, 0, 0, 0.2);
    }
    .game-icon:hover img {
        transform: scale(1.05);
    }
    .game-title {
        font-size: 18px;
        font-weight: 600;
        margin: 10px 0;
        color: #333;
    }
    .result-highlight {
          font-size: 18px;
    font-weight: bold;
    color: #ffffff;
    padding: 10px;
    background-color: #009688; 
    border: 1px solid #00796b;
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
col_count = len(GAME_FACTORS) // row_count + (len(GAME_FACTORS) % row_count > 0)
for row in range(row_count):
    cols = st.columns(col_count)
    for col in range(col_count):
        game_index = row * col_count + col
        if game_index >= len(GAME_FACTORS):
            break
        game = list(GAME_FACTORS.keys())[game_index]
        with cols[col]:
            st.markdown(f'<div class="game-container"><div class="game-icon"><img src="{ICON_PATHS[game]}" alt="{game}"></div>', unsafe_allow_html=True)
            st.markdown(f'<div class="game-title">{game}</div>', unsafe_allow_html=True)
            
            daily_usage_hours = st.slider(f"{game} Daily Usage (in hours)", 0.0, 24.0, 0.0, label_visibility="visible")
            
            emission_factor = GAME_FACTORS[game]
            yearly_usage_hours = daily_usage_hours * 365
            carbon_emissions = round(emission_factor * yearly_usage_hours, 2)
            
            st.markdown(f'<div class="result-highlight">{carbon_emissions} kg CO2/year</div>', unsafe_allow_html=True)
            st.markdown('</div>', unsafe_allow_html=True)

st.markdown("---")
st.markdown("### Strategies for Reducing Your Carbon Footprint")
st.write(
    """
    - **Limit Usage:** Reduce the time spent on games to lower emissions.
    - **Optimize Data Usage:** Use lower resolution settings and avoid unnecessary downloads.
    - **Switch to Green Energy:** Ensure that your gaming devices are powered by renewable energy sources.
    """
)
st.markdown('<div class="footer">Note: The carbon footprint data provided is based on estimations and may vary over time. It should be considered as a general guideline rather than an exact measurement.</div>', unsafe_allow_html=True)