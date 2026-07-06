import streamlit as st
import joblib
import requests

# -----------------------------
# PAGE CONFIG
# -----------------------------
st.set_page_config(
    page_title="Movie Recommendation System",
    page_icon="🎬",
    layout="wide"
)

# -----------------------------
# LOAD DATA
# -----------------------------
movies = joblib.load("movies.pkl")
similarity = joblib.load("similarity.pkl")

# -----------------------------
# API KEY
# -----------------------------
API_KEY = st.secrets["TMDB_API_KEY"]

# -----------------------------
# FETCH POSTER
# -----------------------------
def fetch_poster(movie_id):

    url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={API_KEY}"

    try:
        response = requests.get(url, timeout=10)

        print("Movie ID :", movie_id)
        print("Status Code :", response.status_code)

        data = response.json()
        print(data)

        if response.status_code != 200:
            return None

        poster_path = data.get("poster_path")

        if poster_path:
            return f"https://image.tmdb.org/t/p/w500{poster_path}"

        return None

    except Exception as e:
        print("Error :", e)
        return None


# -----------------------------
# RECOMMEND FUNCTION
# -----------------------------
def recommend(movie):

    movie_index = movies[movies["title"] == movie].index[0]

    distances = similarity[movie_index]

    movie_list = sorted(
        list(enumerate(distances)),
        reverse=True,
        key=lambda x: x[1]
    )[1:6]

    recommended_movies = []
    recommended_posters = []

    for i in movie_list:

        movie_id = movies.iloc[i[0]]["id"]

        recommended_movies.append(
            movies.iloc[i[0]]["title"]
        )

        recommended_posters.append(
            fetch_poster(movie_id)
        )

    return recommended_movies, recommended_posters


# -----------------------------
# UI
# -----------------------------
st.title("🎬 Movie Recommendation System")

selected_movie = st.selectbox(
    "Choose Movie",
    movies["title"].values
)

if st.button("Recommend"):

    names, posters = recommend(selected_movie)

    cols = st.columns(5)

    for col, name, poster in zip(cols, names, posters):

        with col:

            if poster:
                st.image(poster, use_container_width=True)
            else:
                st.write("❌ No Poster")

            st.caption(name)