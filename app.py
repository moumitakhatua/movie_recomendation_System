import streamlit as st
import pickle
import pandas as pd
import requests

def fetch_poster(movie_id):
    response=requests.get("https://api.themoviedb.org/3/movie/{}?api_key=31959f07106a65fdbe955e86285baa30&language=en-US".format(movie_id))
    data=response.json()
    return "https://image.tmdb.org/t/p/w500/" + data["poster_path"]

def recommend(movie):
    movie_index=movies[movies['title']==movie].index[0]
    distances=similarity[movie_index]
    movies_list=sorted(list(enumerate(distances)),reverse=True,key=lambda x:x[1])[1:6]

    recommended_movies=[]
    recommended_movies_posters=[]
    for i in movies_list:
        movie_id=movies.iloc[i[0]].movie_id

        recommended_movies.append(movies.iloc[i[0]].title)

        recommended_movies_posters.append(fetch_poster(movie_id))
    return recommended_movies,recommended_movies_posters

# st.markdown("<h1 style='text-align: center; color: black;'>Movie Recommender System</h1>", unsafe_allow_html=True)
# st.markdown("<h4 style='text-align: center; color: black;'>Find a similar movie from a dataset of 5,000 movies!</h4>", unsafe_allow_html=True)
# st.markdown("<h4 style='text-align: center; color: black;'>Web App</h4>", unsafe_allow_html=True)


movies_dict = pickle.load(open(r"C:\Users\subha\OneDrive\Desktop\python\proj.py\movie_dict.pkl", "rb"))
movies=pd.DataFrame(movies_dict)

similarity=pickle.load(open(r"C:\Users\subha\OneDrive\Desktop\python\proj.py\similarity.pkl", "rb"))
st.title("Movie Recommender System")

selected_movie_name=st.selectbox(
    "How would you like?",
    movies["title"].values
)

if st.button('Recommend'):
    st.write("Recommended movies based on your interests are:")
    names,posters=recommend(selected_movie_name)

    col1,col2,col3,col4,col5=st.columns(5)
    with col1:
        st.text(names[0])
        st.image(posters[0])
    with col2:
        st.write(names[1])
        st.image(posters[1])
    with col3:
        st.write(names[2])
        st.image(posters[2])
    with col4:
        st.write(names[3])
        st.image(posters[3])
    with col5:
        st.write(names[4])
        st.image(posters[4])
st.title(" ")    
