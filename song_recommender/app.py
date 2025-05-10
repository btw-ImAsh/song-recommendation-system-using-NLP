import streamlit as st
from sklearn.metrics.pairwise import cosine_similarity
import pickle as pk
import requests
import base64
from dotenv import load_dotenv
import os
load_dotenv()

SPOTIFY_CLIENT_ID = os.getenv('SPOTIFY_CLIENT_ID')
SPOTIFY_CLIENT_SECRET = os.getenv('SPOTIFY_CLIENT_SECRET')

@st.cache_data(ttl=3600)
def get_access_token(client_id, client_secret):
    auth_url = 'https://accounts.spotify.com/api/token'
    auth_header = {
        'Authorization': 'Basic ' + base64.b64encode(f"{client_id}:{client_secret}".encode()).decode()
    }
    data = {'grant_type': 'client_credentials'}
    response = requests.post(auth_url, headers=auth_header, data=data)
    response.raise_for_status()
    return response.json()['access_token']

def get_album_images(song_id, access_token):
    url = f"https://api.spotify.com/v1/tracks/{song_id}"
    headers = {'Authorization': f'Bearer {access_token}'}
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    data = response.json()
    selected_img = data['album']['images'][1]
    width = selected_img['width'] // 2
    track_url = f"http://open.spotify.com/track/{song_id}"
    return width, selected_img['url'], track_url

songs=pk.load(open('songs.pkl','rb'))
track_id=songs['track_id'].values
songs_list=songs['track_name'].values
combined_matrix= pk.load(open('combined_matrix.pkl','rb'))
st.title('🎵 Song Recommender System')

selected_song=st.selectbox(
'Select a song of your choice:',
songs_list
)

def recommend(song, top_n=8):
    song_index = songs[songs['track_name'] == song].index[0]
    vec = combined_matrix[song_index]
    sim_scores = cosine_similarity(vec, combined_matrix).flatten()
    top_indices = sim_scores.argsort()[::-1][1:top_n + 1]

    recommended_songs_id=[]
    recommended_songs=[]
    for i in top_indices:
        recommended_songs_id.append(songs.iloc[i].track_id)
        recommended_songs.append(songs.iloc[i].track_name)
    return recommended_songs_id, recommended_songs


if st.button('Get Me Songs'):
    img_width=[]
    img_url=[]
    track_url=[]
    song_ids, songs_names = recommend(selected_song)
    for i in range(8):
        if song_ids[i]:
            try:
                token = get_access_token(SPOTIFY_CLIENT_ID, SPOTIFY_CLIENT_SECRET)
                image_width, image_url, song_url = get_album_images(song_ids[i], token)
                img_width.append(image_width)
                img_url.append(image_url)
                track_url.append(song_url)
            except Exception as e:
                st.error(f"Error fetching song info: {str(e)}")
    st.subheader("Songs Recommended For You ▶︎•၊၊||၊|။||||။၊|။•")
    col1, col2, col3, col4 = st.columns(4, gap = 'medium')
    with col1:
        st.text(songs_names[0])
        st.html(f"""<a href="{track_url[0]}">
    <img src="{img_url[0]}" width='{img_width[0]}'>
    </a>""")

    with col2:
        st.text(songs_names[1])
        st.html(f"""<a href="{track_url[1]}">
            <img src="{img_url[1]}" width='{img_width[1]}'>
            </a>""")

    with col3:
        st.text(songs_names[2])
        st.html(f"""<a href="{track_url[2]}">
            <img src="{img_url[2]}" width='{img_width[2]}'>
            </a>""")

    with col4:
        st.text(songs_names[3])
        st.html(f"""<a href="{track_url[3]}">
            <img src="{img_url[3]}" width='{img_width[3]}'>
            </a>""")

    st.divider()

    col5, col6, col7, col8 = st.columns(4, gap = 'medium')

    with col5:
        st.text(songs_names[4])
        st.html(f"""<a href="{track_url[4]}">
            <img src="{img_url[4]}" width='{img_width[4]}'>
            </a>""")

    with col6:
        st.text(songs_names[5])
        st.html(f"""<a href="{track_url[5]}">
            <img src="{img_url[5]}" width='{img_width[5]}'>
            </a>""")

    with col7:
        st.text(songs_names[6])
        st.html(f"""<a href="{track_url[6]}">
            <img src="{img_url[6]}" width='{img_width[6]}'>
            </a>""")

    with col8:
        st.text(songs_names[7])
        st.html(f"""<a href="{track_url[7]}">
            <img src="{img_url[7]}" width='{img_width[7]}'>
            </a>""")