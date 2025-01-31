import streamlit as st

MIN_FILM_DATE = "01/01/1970"
EXCLUDE_LANGUAGES = ["hi"]
USEFUL_COLUMNS = [
    "id",
    "imdb_id",
    "title",
    "adult",
    "original_language",
    "poster_path",
    "poster_path_updated",
    "release_date",
    "revenue",
    "runtime",
    "vote_average",
    "vote_count",
    "overview",
    "keywords",
    "cast",
    "director",
    "genres",
    "popularity",
]
GET_VALID_POSTER_PATHS = False
NUM_FILMS_TO_KEEP = 3500

# Main
C = 5.6  # Mean vote score.
m = 156  # 90th percentile of number of votes

POSTER_BASE_URL = "https://image.tmdb.org/t/p/original/"
TMDB_API_KEY = st.secrets["TMDB_API_KEY"]
DATA_PATH = "data/film_features.csv"
BASE_SIMILARITY_PATH = "data/similarity_matrices/"

# UI config
IMAGE_WIDTH = 175
NUM_POSTER_ROWS = 15
POSTERS_PER_ROW = 8
PARAMETER_CONTROL_MIN = 0.0
PARAMETER_CONTROL_MAX = 1.0
PARAMETER_CONTROL_DEFAULT = 0.5

APP_EXPLANATION = """
This is a hybrid content / collaborative based recommender system. It uses text based metadata from the films (content
based) such as cast, director, keywords and overview descriptive text and applies NLP methods (TF-IDF) to compute
features describing each film. It also considers the films liked by users with similar preferences (collaborative
based). Specifically, dimensionality reduction is performed on the set of user-film interactions to create a
representative set of users that encode the preferences of the population. Each of these approaches are used to
construct similarity matrices, with the rows and columns being the films and the numbers being how similar each film is
to another on a scale of 0-1. The net similarity is given by the average of these similarity matrices and the parameter
controls allow you to define how much weighting to give each method of similarity.
"""

SOURCE_CODE_LINK = "Source code: https://github.com/tomukmatthews/film-recommender-app"
