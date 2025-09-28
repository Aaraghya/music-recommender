import streamlit as st
import random

st.set_page_config(page_title="Mood Recommender", page_icon="🎵", layout="centered")
st.markdown("""
<style>
.main{background-color:#FFF0DB;color:#000000;font-family:'Segoe UI',sans-serif;padding:20px;border-radius:15px}
.stButton>button{background-color:#654321;color:#FFF0DB;border-radius:10px;padding:8px 15px;font-weight:bold}
.stButton>button:hover{background-color:#805c3b;color:#ffffff}
</style>
""", unsafe_allow_html=True)

st.markdown('<div class="main">', unsafe_allow_html=True)
st.title("🎶 Mood-Based Recommender")
st.write("Select your mood and get a personalized music track or inspirational quote!")

m = ["Happy", "Sad", "Stressed", "Motivated", "Sleepy", "Excited"]

rec = {
    "Happy": [
        {"type": "Music", "content": "'Happy' by Pharrell Williams"},
        {"type": "Quote", "content": "'Happiness is not something ready made. It comes from your own actions.' – Dalai Lama"},
        {"type": "Music", "content": "'Good Day' by Nappy Roots"}
    ],
    "Sad": [
        {"type": "Music", "content": "'Fix You' by Coldplay"},
        {"type": "Quote", "content": "'Tough times never last, but tough people do.' – Robert H. Schuller"},
        {"type": "Music", "content": "'Someone Like You' by Adele"}
    ],
    "Stressed": [
        {"type": "Music", "content": "'Weightless' by Marconi Union"},
        {"type": "Quote", "content": "'You can do anything, but not everything.' – David Allen"},
        {"type": "Music", "content": "'Clair de Lune' by Debussy"}
    ],
    "Motivated": [
        {"type": "Music", "content": "'Eye of the Tiger' by Survivor"},
        {"type": "Quote", "content": "'Don't watch the clock; do what it does. Keep going.' – Sam Levenson"},
        {"type": "Music", "content": "'Stronger' by Kanye West"}
    ],
    "Sleepy": [
        {"type": "Music", "content": "'Weightless' by Marconi Union"},
        {"type": "Quote", "content": "'Sleep is the best meditation.' – Dalai Lama"},
        {"type": "Music", "content": "'Clocks' by Coldplay (soft instrumental)"}    
    ],
    "Excited": [
        {"type": "Music", "content": "'Can't Stop the Feeling' by Justin Timberlake"},
        {"type": "Quote", "content": "'The future depends on what you do today.' – Mahatma Gandhi"},
        {"type": "Music", "content": "'Happy Now' by Kygo ft. Sandro Cavazza"}
    ],
}

sel = st.selectbox("Select your current mood:", m)

def get_rec(mood):
    return random.choice(rec[mood])

if st.button("Get Recommendation"):
    r = get_rec(sel)
    st.markdown(f"**{r['type']} Recommendation:** {r['content']}")

if st.button("Surprise Me!"):
    rand_mood = random.choice(m)
    r = get_rec(rand_mood)
    st.markdown(f"**Mood:** {rand_mood}")
    st.markdown(f"**{r['type']} Recommendation:** {r['content']}")

st.markdown('</div>', unsafe_allow_html=True)