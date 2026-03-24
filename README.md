# Movie Recommender System

A content-based movie recommendation system using TMDB 5000 dataset.

## Setup Instructions

1. Install required packages:
```bash
pip install streamlit pandas scikit-learn requests
```

2. Generate similarity file (first time only):
```bash
python generate_similarity.py
```

3. Run the application:
```bash
streamlit run app.py
```

## Files
- `app.py` - Main application
- `movie_dict.pkl` - Movie data
- `movies.pkl` - Processed movie data
- `generate_similarity.py` - Script to create similarity.pkl

## Note
The `similarity.pkl` file is too large for GitHub (176 MB). Run `generate_similarity.py` to create it locally.
