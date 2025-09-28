import streamlit as st
import random

st.set_page_config(page_title="🎶 MelodyMood 💖", page_icon="🎧", layout="centered")

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
.card {background-color: #fff0f5; padding: 15px; border-radius: 12px; margin-bottom: 10px; color: #000000;}
.quote {background-color: #ffe4e1; padding: 12px; border-radius: 12px; margin-bottom: 10px; font-style: italic; color: #000000;}
.dark-mode {background-color: #4B0082; color: #E6E6FA;}
</style>
""", unsafe_allow_html=True)

st.markdown('<div class="main">', unsafe_allow_html=True)
st.title("🎶 MelodyMood 💖")
st.write("Pick your vibe and get music or quotes! 🌈✨")

vibes = ["Happy 😄", "Sad 😢", "Stressed 😌", "Motivated ⚡", "Sleepy 🥱", "Excited 🥳"]

picks = {
    "Happy 😄": [
        {"kind": "song", "text": "'Happy' by Pharrell Williams 🎵"},
        {"kind": "song", "text": "'Good Day' by Nappy Roots 🎶"},
        {"kind": "song", "text": "'Can't Stop the Feeling' by Justin Timberlake 💖"},
        {"kind": "song", "text": "'Shake It Off' by Taylor Swift 🪩"},
        {"kind": "quote", "text": "'Happiness is not something ready made. It comes from your own actions.' – Dalai Lama 💕"},
        {"kind": "quote", "text": "'Do more of what makes you happy! 😄'"},
    ],
    "Sad 😢": [
        {"kind": "song", "text": "'Fix You' by Coldplay 💔"},
        {"kind": "song", "text": "'Someone Like You' by Adele 😢"},
        {"kind": "song", "text": "'Lost Cause' by Billie Eilish 🌧️"},
        {"kind": "quote", "text": "'Tough times never last, but tough people do.' – Robert H. Schuller 🌙"},
        {"kind": "quote", "text": "'Even the darkest night will end and the sun will rise 🌅'"},
    ],
    "Stressed 😌": [
        {"kind": "song", "text": "'Weightless' by Marconi Union 💤"},
        {"kind": "song", "text": "'Clair de Lune' by Debussy 🎹"},
        {"kind": "quote", "text": "'Keep calm and carry on 😌'"},
        {"kind": "quote", "text": "'Stress is caused by being 'here' but wanting to be 'there'. – Eckhart Tolle 🌸'"},
    ],
    "Motivated ⚡": [
        {"kind": "song", "text": "'Eye of the Tiger' by Survivor 💪"},
        {"kind": "song", "text": "'Stronger' by Kanye West ⚡"},
        {"kind": "song", "text": "'Don't Stop Me Now' by Queen 🎶"},
        {"kind": "quote", "text": "'The harder you work for something, the greater you'll feel when you achieve it 💖'"},
        {"kind": "quote", "text": "'Push yourself, because no one else is going to do it for you 🌟'"},
    ],
    "Sleepy 🥱": [
        {"kind": "song", "text": "'Weightless' by Marconi Union 💤"},
        {"kind": "song", "text": "'Lullaby' by Johannes Brahms 🎵"},
        {"kind": "song", "text": "'Night Owl' by Galimatias 🌙"},
        {"kind": "quote", "text": "'Sleep is the best meditation. – Dalai Lama 😴'"},
        {"kind": "quote", "text": "'Rest and recharge, tomorrow is a new day 🌸'"},
    ],
    "Excited 🥳": [
        {"kind": "song", "text": "'Happy' by Pharrell Williams 🎵"},
        {"kind": "song", "text": "'Can't Stop the Feeling!' by Justin Timberlake 💖"},
        {"kind": "song", "text": "'I Gotta Feeling' by Black Eyed Peas 🎶"},
        {"kind": "quote", "text": "'Excitement is the energy that propels us forward! ⚡'"},
        {"kind": "quote", "text": "'Celebrate every little victory 🥳'"},
    ]
}

mood = st.selectbox("What's your vibe?", vibes)

def pick(vibe, what=None):
    opts = picks.get(vibe, [])
    choices = [x for x in opts if (what is None or x['kind'] == what)]
    if not choices:
        return {"kind": what or "song", "text": "Hmm, nothing for this vibe yet! 😅"}
    return random.choice(choices)

if st.button("Give me music 🎧"):
    song = pick(mood, "song")
    st.markdown(f'<div class="card">🎵 Tune: {song["text"]}</div>', unsafe_allow_html=True)

if st.button("Give me wisdom 💖"):
    wisdom = pick(mood, "quote")
    st.markdown(f'<div class="quote">💌 Words: {wisdom["text"]}</div>', unsafe_allow_html=True)

if st.button("Surprise me! ✨🎶"):
    what = random.choice(["song", "quote"])
    surprise = pick(mood, what)
    st.markdown(f'<div class="card">🌈 Vibe: {mood}</div>', unsafe_allow_html=True)
    st.markdown(f'<div class="card">💖 For you: {surprise["text"]}</div>', unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)
