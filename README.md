# 🎬 Movie Recommendation System

A content-based Movie Recommendation System built using **Machine Learning**, **Natural Language Processing (NLP)**, and **Streamlit**. The application recommends movies similar to the one selected by the user and displays movie posters using the TMDB API.

## 🚀 Live Demo

🔗 [https://YOUR-STREAMLIT-APP-URL.streamlit.app](https://ci8nim47rvcsyakefymtld.streamlit.app/)

## ✨ Features

- Recommend 5 similar movies based on content.
- Interactive and user-friendly Streamlit interface.
- Displays movie posters using the TMDB API.
- Search and select movies from a dropdown list.
- Fast recommendations using TF-IDF Vectorization and Cosine Similarity.

## 🛠️ Technologies Used

- Python
- Pandas
- NumPy
- Scikit-learn
- NLP (TF-IDF Vectorizer)
- Cosine Similarity
- Streamlit
- TMDB API
- Joblib
- Git & GitHub

## 🧠 Machine Learning Workflow

1. Data Collection
2. Data Preprocessing
3. Feature Engineering
4. TF-IDF Vectorization
5. Cosine Similarity Calculation
6. Movie Recommendation
7. Streamlit Deployment

## 📂 Project Structure

```
Movie_Recommendation/
│── app.py
│── movies.pkl
│── movies.csv
│── requirements.txt
│── README.md
│── Movie_Recommendation ML.ipynb
```

## ⚙️ Installation

Clone the repository

```bash
git clone https://github.com/YourUsername/Movie_Recommendation.git
```

Move into the project folder

```bash
cd Movie_Recommendation
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run the application

```bash
streamlit run app.py
```

## 🔑 TMDB API

This project uses the TMDB API to fetch movie posters.

Create a `.streamlit/secrets.toml` file and add:

```toml
TMDB_API_KEY = "YOUR_API_KEY"
```

## 📊 Future Improvements

- Display movie ratings
- Show movie overview
- Display genres and release year
- Add search autocomplete
- Improve recommendation accuracy
- Responsive UI

## 👨‍💻 Author

**Mainuddin Khan**

- GitHub: https://github.com/Mainuddin-alt
- LinkedIn: Add your LinkedIn profile here

## ⭐ Support

If you found this project helpful, please consider giving it a ⭐ on GitHub.
