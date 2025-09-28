import streamlit as st
import random

# Page config
st.set_page_config(page_title="🎶 MelodyMood 💖", page_icon="🎧", layout="centered")

# CSS for cute preppy theme
st.markdown("""
<style>
body {background-color: #F4C2C2; color: #000000; font-family: 'Fredoka One', cursive;}
.main {padding: 20px; border-radius: 15px;}
.stButton>button {
    background-color: #FF69B4; 
    color: #fff; 
    border-radius: 15px; 
    padding: 10px 20px; 
    font-weight: bold;
    font-size: 16px;
}
.stButton>button:hover {background-color: #FF85C1; color: #fff;}
.card {background-color: #fff0f5; padding: 15px; border-radius: 12px; margin-bottom: 10px;}
.quote {background-color: #ffe4e1; padding: 12px; border-radius: 12px; margin-bottom: 10px; font-style: italic;}
.dark-mode {background-color: #4B0082; color: #E6E6FA;}
</style>
""", unsafe_allow_html=True)

st.markdown('<div class="main">', unsafe_allow_html=True)
st.title("🎶 MelodyMood 💖")
st.write("Select your mood and get a personalized music track or inspirational quote! 🌈✨")

# Mood options
moods = ["Happy 😄", "Sad 😢", "Stressed 😌", "Motivated ⚡", "Sleepy 🥱", "Excited 🥳"]

# Recommendations: music + quotes for all moods
recommendations = {
    "Happy 😄": [
        {"type": "Music", "content": "'Happy' by Pharrell Williams 🎵"},
        {"type": "Music", "content": "'Good Day' by Nappy Roots 🎶"},
        {"type": "Music", "content": "'Can't Stop the Feeling' by Justin Timberlake 💖"},
        {"type": "Music", "content": "'Shake It Off' by Taylor Swift 🪩"},
        {"type": "Quote", "content": "'Happiness is not something ready made. It comes from your own actions.' – Dalai Lama 💕"},
        {"type": "Quote", "content": "'Do more of what makes you happy! 😄'"},
    ],
    "Sad 😢": [
        {"type": "Music", "content": "'Fix You' by Coldplay 💔"},
        {"type": "Music", "content": "'Someone Like You' by Adele 😢"},
        {"type": "Music", "content": "'Lost Cause' by Billie Eilish 🌧️"},
        {"type": "Quote", "content": "'Tough times never last, but tough people do.' – Robert H. Schuller 🌙"},
        {"type": "Quote", "content": "'Even the darkest night will end and the sun will rise 🌅'"},
    ],
    "Stressed 😌": [
        {"type": "Music", "content": "'Weightless' by Marconi Union 💤"},
        {"type": "Music", "content": "'Clair de Lune' by Debussy 🎹"},
        {"type": "Quote", "content": "'Keep calm and carry on 😌'"},
        {"type": "Quote", "content": "'Stress is caused by being 'here' but wanting to be 'there'. – Eckhart Tolle 🌸'"},
    ],
    "Motivated ⚡": [
        {"type": "Music", "content": "'Eye of the Tiger' by Survivor 💪"},
        {"type": "Music", "content": "'Stronger' by Kanye West ⚡"},
        {"type": "Music", "content": "'Don't Stop Me Now' by Queen 🎶"},
        {"type": "Quote", "content": "'The harder you work for something, the greater you’ll feel when you achieve it 💖'"},
        {"type": "Quote", "content": "'Push yourself, because no one else is going to do it for you 🌟'"},
    ],
    "Sleepy 🥱": [
        {"type": "Music", "content": "'Weightless' by Marconi Union 💤"},
        {"type": "Music", "content": "'Lullaby' by Johannes Brahms 🎵"},
        {"type": "Music", "content": "'Night Owl' by Galimatias 🌙"},
        {"type": "Quote", "content": "'Sleep is the best meditation. – Dalai Lama 😴'"},
        {"type": "Quote", "content": "'Rest and recharge, tomorrow is a new day 🌸'"},
    ],
    "Excited 🥳": [
        {"type": "Music", "content": "'Happy' by Pharrell Williams 🎵"},
        {"type": "Music", "content": "'Can’t Stop the Feeling!' by Justin Timberlake 💖"},
        {"type": "Music", "content": "'I Gotta Feeling' by Black Eyed Peas 🎶"},
        {"type": "Quote", "content": "'Excitement is the energy that propels us forward! ⚡'"},
        {"type": "Quote", "content": "'Celebrate every little victory 🥳'"},
    ]
}

# Mood selector
selected_mood = st.selectbox("Select your current mood:", moods)

# Get random recommendation for a mood safely
def get_rec(mood, r_type=None):
    mood_options = recommendations.get(mood, [])
    options = [r for r in mood_options if (r_type is None or r['type'] == r_type)]
    if not options:
        return {"type": r_type or "Music", "content": "No recommendation available for this mood yet! 😅"}
    return random.choice(options)

# Music Recommendation
if st.button("Get Music Recommendation 🎧"):
    r = get_rec(selected_mood, "Music")
    st.markdown(f'<div class="card">🎵 **Music:** {r["content"]}</div>', unsafe_allow_html=True)

# Quote Recommendation
if st.button("Get Quote 💖"):
    q = get_rec(selected_mood, "Quote")
    st.markdown(f'<div class="quote">💌 **Quote:** {q["content"]}</div>', unsafe_allow_html=True)

# Surprise Me (mood-relevant + emojis)
if st.button("Surprise Me! ✨🎶"):
    r_type = random.choice(["Music", "Quote"])
    surprise = get_rec(selected_mood, r_type)
    st.markdown(f'<div class="card">🌈 **Mood:** {selected_mood}</div>', unsafe_allow_html=True)
    st.markdown(f'<div class="card">💖 **{r_type}:** {surprise["content"]}</div>', unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)
