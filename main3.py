import streamlit as st

# Estimated carbon emission per prompt for each AI tool in kg CO2
AI_TOOL_FACTORS = {
    "ChatGPT": 0.03,
    "Gemini": 0.02,
    "Copilot": 0.015,
    "Claude": 0.025,
    "Bard": 0.018,
    "AlphaCode": 0.022,
    "LLaMA": 0.02,
    "DALL·E": 0.05,
}

ICON_PATHS_AI = {
    "ChatGPT": "https://res.cloudinary.com/di7wy7ldo/image/upload/v1725677144/chat-gpt_vrvq9q.png",
    "Gemini": "https://res.cloudinary.com/di7wy7ldo/image/upload/v1725677148/Google-Ai_tkewou.png",
    "Copilot": "https://res.cloudinary.com/di7wy7ldo/image/upload/v1725677146/copilot_rv8fsh.png",
    "Claude": "https://res.cloudinary.com/di7wy7ldo/image/upload/v1725677145/claude-2_rmjhpr.png",
    "Bard": "https://res.cloudinary.com/di7wy7ldo/image/upload/v1725677148/Google-Ai_tkewou.png",
    "AlphaCode": "https://res.cloudinary.com/di7wy7ldo/image/upload/v1725677143/alphacode_par7xe.png",
    "LLaMA": "https://res.cloudinary.com/di7wy7ldo/image/upload/v1725680453/Meta-Logo_akxoix.png",
    "DALL·E": "https://res.cloudinary.com/di7wy7ldo/image/upload/v1725677147/dall-e2_zgmpgs.png"
}

st.set_page_config(layout="wide", page_title="AI Tools Carbon Footprint Calculator")

st.title("💻 Generative AI Tools Carbon Footprint Calculator")

st.markdown(
    """
    <style>
    body {
        background-color: #ffffff;
        color: #333;
    }
    .ai-container {
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
    .ai-icon {
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
    .ai-icon img {
        max-width: 100%;
        max-height: 100%;
        object-fit: contain;
        transition: transform 0.3s ease, box-shadow 0.3s ease;
    }
    .ai-icon:hover {
        transform: scale(1.05);
        box-shadow: 0 6px 12px rgba(0, 0, 0, 0.2);
    }
    .ai-icon:hover img {
        transform: scale(1.05);
    }
    .ai-title {
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
    .prompts-label {
        font-size: 12px;
        font-weight: bold;
        color: #555;
    }
    </style>
    """,
    unsafe_allow_html=True
)

row_count_ai = 3
col_count_ai = len(AI_TOOL_FACTORS) // row_count_ai + (len(AI_TOOL_FACTORS) % row_count_ai > 0)

for row in range(row_count_ai):
    cols = st.columns(col_count_ai)
    for col in range(col_count_ai):
        ai_index = row * col_count_ai + col
        if ai_index >= len(AI_TOOL_FACTORS):
            break
        ai_tool = list(AI_TOOL_FACTORS.keys())[ai_index]
        with cols[col]:
            st.markdown(f'<div class="ai-container"><div class="ai-icon"><img src="{ICON_PATHS_AI[ai_tool]}" alt="{ai_tool}"></div>', unsafe_allow_html=True)
            st.markdown(f'<div class="ai-title">{ai_tool}</div>', unsafe_allow_html=True)
            hours_used = st.slider(f"{ai_tool} Hours Used (per day)", 0, 24, 0)
            prompts_per_hour = 10  # Example number of prompts per hour, adjust as needed
            emission_factor_ai = AI_TOOL_FACTORS[ai_tool]
            yearly_prompts = hours_used * prompts_per_hour * 365
            carbon_emissions_ai = round(emission_factor_ai * yearly_prompts, 2)  # Emissions in kg
            st.markdown(f'<div class="result-highlight">{carbon_emissions_ai} kg CO2/year</div>', unsafe_allow_html=True)
            st.markdown('</div>', unsafe_allow_html=True)

st.markdown("---")
st.markdown("### Strategies for Reducing AI Tool Carbon Footprint")
st.write(
    """
    - **Limit Usage:** Reduce the number of hours used per day to minimize emissions.
    - **Use Efficient Models:** Choose AI tools optimized for lower energy consumption.
    - **Support Green Energy:** Encourage AI providers to adopt renewable energy sources.
    """
)
st.markdown('<div class="footer">Note: The carbon footprint data provided is based on estimations and may vary over time. It should be considered as a general guideline rather than an exact measurement.</div>', unsafe_allow_html=True)