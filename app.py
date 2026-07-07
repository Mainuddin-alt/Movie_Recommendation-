import streamlit as st
import joblib
import requests

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# --------------------------------------------------
# PAGE CONFIG
# --------------------------------------------------
st.set_page_config(
    page_title="Movie Recommendation System",
    page_icon="🎬",
    layout="wide"
)

# --------------------------------------------------
# LOAD DATA
# --------------------------------------------------
movies = joblib.load("new_movies.pkl")

# --------------------------------------------------
# CREATE SIMILARITY (Only once)
# --------------------------------------------------
@st.cache_resource
def create_similarity(data):
    tfidf = TfidfVectorizer(stop_words="english")
    vectors = tfidf.fit_transform(data["combined_features"])
    similarity = cosine_similarity(vectors)
    return similarity

similarity = create_similarity(movies)

# --------------------------------------------------
# TMDB API KEY
# --------------------------------------------------
API_KEY = st.secrets["TMDB_API_KEY"]

# --------------------------------------------------
# FETCH POSTER
# --------------------------------------------------
def fetch_poster(movie_id):

    try:
        url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={API_KEY}"

        response = requests.get(url, timeout=10)

        if response.status_code != 200:
            return None

        data = response.json()

        poster_path = data.get("poster_path")

        if poster_path:
            return f"https://image.tmdb.org/t/p/w500{poster_path}"

        return None

    except:
        return None

# --------------------------------------------------
# RECOMMEND FUNCTION
# --------------------------------------------------
def recommend(movie):

    movie_index = movies[movies["title"] == movie].index[0]

    distances = similarity[movie_index]

    movie_list = sorted(
        list(enumerate(distances)),
        reverse=True,
        key=lambda x: x[1]
    )[1:6]

    names = []
    posters = []

    for i in movie_list:

        index = i[0]

        names.append(
            movies.iloc[index]["title"]
        )

        posters.append(
            fetch_poster(
                movies.iloc[index]["id"]
            )
        )

    return names, posters

# --------------------------------------------------
# UI
# --------------------------------------------------
st.title("🎬 Movie Recommendation System")

st.write("Select a movie and get similar movie recommendations.")

selected_movie = st.selectbox(
    "Search or Select a Movie",
    movies["title"].values
)

if st.button("Recommend"):

    names, posters = recommend(selected_movie)

    cols = st.columns(5)

    for col, name, poster in zip(cols, names, posters):

        with col:

            if poster:
                st.image(poster)

            else:
                st.write("Poster Not Available")

            st.markdown(f"**{name}**")
