import requests  # For making HTTP requests
import pandas as pd  # For handling data in DataFrames
from sklearn.preprocessing import StandardScaler  # For normalizing data
from sklearn.metrics.pairwise import cosine_similarity  # For calculating similarity between users
def fetch_movie_data(api_key):# Function to fetch popular movie data from TMDb API
    response=requests.get(f'https://api.themoviedb.org/3/movie/popular?api_key={api_key}')#to get response with api key
    return response.json()#return in json format
def get_movie_details(movie_id,api_key):# Function to fetch detailed information about a specific movie
    response=requests.get(f'https://api.themoviedb.org/3/movie/{movie_id}?api_key={api_key}')
    return response.json()
def recommend_movies(user_id,similarity_matrix,user_item_matrix,api_key,preferred_genres=None,top_n=2):# Function to recommend movies based on user preferences and similar users
    user_index=user_id-1#check use index
    user_similarities=similarity_matrix[user_index]#creating user matrix
    similar_users=user_similarities.argsort()[-top_n:][::-1]#finding similarities
    recommendations={}#recommendation function
    for similar_user in similar_users:#loop each use in array
        items=user_item_matrix.iloc[similar_user]#stoing the similar values
        for movie_id in items.index:#seaching for movies for similar user
            if user_item_matrix.iloc[user_index][movie_id]==0:#if mach
                if movie_id not in recommendations:# if no moves in recommendaion
                    recommendations[movie_id]=0
                recommendations[movie_id]+=items[movie_id]#go for next movie
    recommended_movie_ids=sorted(recommendations.items(),key=lambda x:x[1],reverse=True)#sort he movie ids
    recommended_movies=[movie_id for movie_id,score in recommended_movie_ids]
    recommended_movies_info=[]#making info of movie id
    for movie_id in recommended_movies:#movies fom recommendaions
        movie_details=get_movie_details(movie_id,api_key)#get detaild for that movies
        movie_info={#gathering information of each movie
            'Title':movie_details.get('title'),
            'Genre':', '.join([genre['name'] for genre in movie_details.get('genres',[])]),
            'Overview':movie_details.get('overview'),
            'Release Date':movie_details.get('release_date'),
            'Vote Average':movie_details.get('vote_average'),
            'Poster':f"https://image.tmdb.org/t/p/original{movie_details.get('poster_path')}"
        }
        recommended_movies_info.append(movie_info)#adding information to each movies
    if preferred_genres:#adding ganres
        preferred_genres_set=set(preferred_genres.lower().split(', '))#gaining ganers from user
        recommended_movies_info=[
            movie for movie in recommended_movies_info
            if any(genre.lower() in preferred_genres_set for genre in movie['Genre'].lower().split(', '))# cheking for maching ganres form movies
        ]
    return recommended_movies_info
def main():# Main function to run the recommendation system
    api_key='c4a6c769f19c75738beb8c97dc20ae23'  # Replace with your TMDb API key
    movie_data=fetch_movie_data(api_key)# getting movie ata from AI key
    if 'results' not in movie_data:# resonce for no result
        print("No 'results' found in the API response.")
        print(f"API Response:{movie_data}")
        return
    movies_list=movie_data['results']
    movies=pd.DataFrame({# getting movie details with API
        'movieId':[movie['id'] for movie in movies_list],
        'movieTitle':[movie['title'] for movie in movies_list],
        'genre':[', '.join([str(genre) for genre in movie.get('genre_ids',[])]) for movie in movies_list]
    })
    ratings=pd.DataFrame({#creating predefined rating
        'userId':[1,1,1,2,2,2,3,3,3],
        'movieId':[movie['id'] for movie in movies_list[:9]],
        'rating':[5,3,4,4,2,5,4,5,4]
    })
    user_item_matrix=ratings.pivot(index='userId',columns='movieId',values='rating').fillna(0)#manupulating data
    scaler=StandardScaler()#using scaler
    normalized_matrix=scaler.fit_transform(user_item_matrix)#transforming user id matrix
    similarity_matrix=cosine_similarity(normalized_matrix)#cheking similarities
    user_id=int(input("Enter user ID(1-3): "))#getting user id
    preferred_genres=input("Enter your preferred genres (comma-separated): ")#printing result
    recommended_movies=recommend_movies(user_id,similarity_matrix,user_item_matrix,api_key,preferred_genres=preferred_genres)
    print(f"\nRecommended movies for user {user_id}:")# printing recommandation for each user id
    if recommended_movies:#loop for printing multiple movies
        for movie in recommended_movies:
            print(f"Title:{movie['Title']},\nGenre: {movie['Genre']},\nOverview: {movie['Overview']},\nRelease Date: {movie['Release Date']},\nVote Average: {movie['Vote Average']},\nPoster: {movie['Poster']}")
    else:#for no recomendations
        print("No recommendations found based on the given preferences.")
if __name__=="__main__":# running main loop
    main()
