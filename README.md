
# Song Recommendation System Using NLP

This project aims to recommend songs based on the similarity of their textual metadata—such as lyrics, genres, tags, or descriptions. By transforming text data into numerical vectors using TF-IDF and comparing them using cosine similarity, the system finds and ranks songs that are most similar to a given input song.
## Tech Stack

- **Excel:** For data exploration.

- **Python:** For data preprocessing.

- **Pandas/Matplotlib/SckitiLearn:** Libraries for further data manupulation, cleaning and machine learning.

- **NLTK/re:** For texual operations.

- **Streamlit:** For frontend and UI.

## Workflow

1. Data Collection:

Contains song metadata such as title, artist, genre, and lyrics.
Example fields used: Song Title, Artist, Lyrics, Genre.

2. Preprocessing:

Cleaning the text (removal of stop words, punctuation, lowercasing). Combining relevant features into a single textual field (e.g., lyrics + genre).

3. Feature Extraction (TF-IDF Vectorization):

Use a TfidfVectorizer to convert the text messages into numerical feature vectors based on the importance of each word.

This converts raw text into a sparse matrix of TF-IDF scores.

4. Cosine similarity:

Calculates similarity scores between the input song and all other songs.

Higher score = more similar.

5. Recommendation Engine:

Takes a song as input (by title or index).
Returns top-N most similar songs based on cosine similarity.
## Visuals

**Code:**

![Data](https://github.com/user-attachments/assets/906650b3-283c-442b-88d0-4d31d1a7233e)
![Code](https://github.com/user-attachments/assets/29af890c-fc35-4ff6-961d-9b864bf6be65)


**UI/Webpage:**

![UI](https://github.com/user-attachments/assets/7b537cdc-55a6-4785-be08-bcd06a7d2885)


## Authors

- Ashutosh Sharma
    - [Linkedin](https://www.linkedin.com/in/ashutosh-sharma28/)
    - [Github](https://github.com/btw-ImAsh)

