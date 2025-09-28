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

# Recommendations: 10 each
recommendations = {
    "Happy 😄": [
        {"type": "Music", "content": "'Happy' by Pharrell Williams 🎵"},
        {"type": "Music", "content": "'Good Day' by Nappy Roots 🎶"},
        {"type": "Music", "content": "'Can't Stop the Feeling' by Justin Timberlake 💖"},
        {"type": "Music", "content": "'Shake It Off' by Taylor Swift 🪩"},
        {"type": "Music", "content": "'Uptown Funk' by Mark Ronson ft. Bruno Mars 🎧"},
        {"type": "Music", "content": "'Dynamite' by BTS ✨"},
        {"type": "Music", "content": "'Best Day of My Life' by American Authors 🎵"},
        {"type": "Music", "content": "'Walking on Sunshine' by Katrina & The Waves 🌞"},
        {"type": "Music", "content": "'Roar' by Katy Perry 🐯"},
        {"type": "Music", "content": "'Firework' by Katy Perry 🎆"},
        {"type": "Quote", "content": "'Happiness is not something ready made. It comes from your own actions.' – Dalai Lama 💕"},
        {"type": "Quote", "content": "'The purpose of our lives is to be happy.' – Dalai Lama 🌸"},
        {"type": "Quote", "content": "'Happiness depends upon ourselves.' – Aristotle ✨"},
        {"type": "Quote", "content": "'Do more of what makes you happy! 😄'"},
        {"type": "Quote", "content": "'Smiles are contagious 😍'"},
        {"type": "Quote", "content": "'Joy is a net of love by which you can catch souls.' – Mother Teresa 🌈"},
        {"type": "Quote", "content": "'The best way to cheer yourself up is to try to cheer somebody else up! 💖'"},
        {"type": "Quote", "content": "'Happiness held is the seed; happiness shared is the flower 🌸'"},
        {"type": "Quote", "content": "'Life is short, smile while you still have teeth 😆'"}
    ],
    # Repeat similar structure for other moods with 10+ music + quotes each
    "Sad 😢": [
        {"type": "Music", "content": "'Fix You' by Coldplay 💔"},
        {"type": "Music", "content": "'Someone Like You' by Adele 😢"},
        {"type": "Music", "content": "'Lost Cause' by Billie Eilish 🌧️"},
        {"type": "Music", "content": "'All I Want' by Kodaline 💙"},
        {"type": "Music", "content": "'Stay With Me' by Sam Smith 💔"},
        {"type": "Music", "content": "'Skinny Love' by Bon Iver 🥀"},
        {"type": "Music", "content": "'When We Were Young' by Adele 🎵"},
        {"type": "Music", "content": "'Let Her Go' by Passenger 🎶"},
        {"type": "Music", "content": "'I Will Follow You Into The Dark' by Death Cab 💫"},
        {"type": "Music", "content": "'The Night We Met' by Lord Huron 🌌"},
        {"type": "Quote", "content": "'Tough times never last, but tough people do.' – Robert H. Schuller 🌙"},
        {"type": "Quote", "content": "'Sadness flies away on the wings of time.' – Jean de La Fontaine 🕊️"},
        {"type": "Quote", "content": "'Every human walks around with a certain kind of sadness.' – Brad Pitt 💔"},
        {"type": "Quote", "content": "'Tears come from the heart and not from the brain 😢'"},
        {"type": "Quote", "content": "'Even the darkest night will end and the sun will rise 🌅'"},
        {"type": "Quote", "content": "'It's okay to not be okay 🌸'"},
        {"type": "Quote", "content": "'You cannot protect yourself from sadness without protecting yourself from happiness 😌'"},
        {"type": "Quote", "content": "'Sadness is but a wall between two gardens 💜'"},
        {"type": "Quote", "content": "'Your sadness is a gift, not a curse 🎁'"},
        {"type": "Quote", "content": "'Sometimes you have to let yourself feel 💫'"}
    ],
    # Continue for Stressed, Motivated, Sleepy, Excited…
}

# Mood selector
selected_mood = st.selectbox("Select your current mood:", moods)

# Get random recommendation for a mood
def get_rec(mood, r_type=None):
    options = [r for r in recommendations[mood] if (r_type is None or r['type']==r_type)]
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
