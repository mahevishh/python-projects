import streamlit as st
import requests

# --- Config ---
st.set_page_config(page_title="Mood & Genre Music Recommender", layout="wide")


def set_dark_theme():
    st.markdown("""
        <style>
        /* Background and General Text */
        .stApp {
            background-color: #000000;
            color: white;
        }

        /* Force all label text to white */
        label, .css-1cpxqw2, .css-1offfwp, .css-14xtw13 {
            color: white !important;
            font-weight: 600;
        }

        /* Selectbox, Buttons, Text Inputs */
        .stSelectbox > div, .stButton > button, .stTextInput > div {
            background-color: #1e1e1e;
            color: white;
            border-radius: 6px;
            border: 1px solid #444;
        }

        /* Headings and markdown */
        .stMarkdown, .css-10trblm, .css-hxt7ib, h1, h2, h3 {
            color: white !important;
        }

        /* Google Font - Roboto */
        @import url('https://fonts.googleapis.com/css2?family=Roboto:wght@400;700&display=swap');
        html, body, [class*="css"]  {
            font-family: 'Roboto', sans-serif;
        }

        </style>
    """, unsafe_allow_html=True)



# --- API Setup ---
API_KEY = "AIzaSyA8MDmtaVB2sJk-78Ku6KOyVoZEusxhyrI"

def fetch_youtube_videos(mood, genre, max_results=5):
    search_query = f"{mood} {genre} music playlist"
    url = "https://www.googleapis.com/youtube/v3/search"

    params = {
        "part": "snippet",
        "q": search_query,
        "key": API_KEY,
        "maxResults": max_results,
        "type": "video"
    }

    response = requests.get(url, params=params)
    data = response.json()

    videos = []
    if "items" in data:
        for item in data["items"]:
            video_id = item["id"]["videoId"]
            title = item["snippet"]["title"]
            video_url = f"https://www.youtube.com/watch?v={video_id}"
            videos.append((title, video_id, video_url))
    return videos

# --- Init Favorites ---
if "favorites" not in st.session_state:
    st.session_state.favorites = []

# --- Top Button to View Favorites ---
if st.button("⭐ View Favorites"):
    st.subheader("Your Saved Favorites:")
    if st.session_state.favorites:
        for fav in st.session_state.favorites:
            st.markdown(f"**{fav['title']}**")
            st.video(f"https://www.youtube.com/watch?v={fav['video_id']}")
    else:
        st.info("No favorites yet.")

st.title("🎧 Mood & Genre-Based Music Recommender")
st.write("Select your mood and favorite genre, and get auto-generated music recommendations from YouTube and Spotify!")

# --- Input ---
mood = st.selectbox("💬 What's your mood today?", ["Happy", "Sad", "Energetic", "Chill"])
genre = st.selectbox("🎶 Choose a music genre", ["Pop", "Hindi", "K-Pop", "J-Pop", "Lo-fi", "Instrumental"])

# --- Set Background Color ---
set_dark_theme()



st.markdown("---")
st.subheader(f"🎬 YouTube Music for *{mood}* + *{genre}*")

# --- Fetch & Show Videos ---
videos = fetch_youtube_videos(mood, genre, max_results=25)


if videos:
    for title, video_id, url in videos:
        cols = st.columns([1, 6, 1])  # favorite | video | download

        with cols[0]:
            if st.button("❤️", key=f"fav_{video_id}"):
                fav_obj = {"title": title, "video_id": video_id}
                if fav_obj not in st.session_state.favorites:
                    st.session_state.favorites.append(fav_obj)
                    st.success(f"Added to favorites: {title}")

        with cols[1]:
            st.markdown(f"**{title}**")
            st.video(f"https://www.youtube.com/watch?v={video_id}")
            st.markdown(
                f"[🎧 Listen on Spotify](https://open.spotify.com/search/{mood}%20{genre})", unsafe_allow_html=True)

        with cols[2]:
            download_link = f"https://www.y2mate.com/youtube/{video_id}"
            st.markdown(f"[⬇️ Download]({download_link})", unsafe_allow_html=True)
else:
    st.warning("No results found. Try a different mood or genre.")

st.markdown("---")
st.markdown("Made with ❤️ by **Shora Mahevish** using Streamlit & YouTube API")
