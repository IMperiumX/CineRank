# **Movie Rankings API**

## **Overview**

This is a Django-based API that allows users to set and manage their top 100 movies. The application utilizes The Movie Database (TMDb) API to fetch movie data and provides basic CRUD (Create, Read, Update, Delete) functionality for users to add, list, and rank their movie selections.

## **Features**

- User authentication and authorization
- Movie data fetched from TMDb API
- Basic CRUD operations for movies: + Create: Add a new movie to a user's list + Read: Retrieve a user's movie list + Update: Edit a movie's ranking in a user's list + Delete: Remove a movie from a user's list
- Movie ranking and sorting system

## **Setup**

### Requirements

- Python 3.9+
- Django 3.2+
- TMDb API key (obtain from <http://tmdb.org>)

### Installation

1. Clone the repository: `git clone https://github.com/your-username/movie-rankings-api.git`
2. Install dependencies: `pip install -r requirements.txt`
3. Set up your TMDb API key as an environment variable: `export TMDB_API_KEY=your_api_key_here`
4. Run migrations: `python manage.py migrate`
5. Start the development server: `python manage.py runserver`

## **Usage**

### API Endpoints

- `/api/movies/`: Retrieve a user's movie list
- `/api/movies/<movie_id>/`: Retrieve a specific movie by ID
- `/api/movies/create/`: Create a new movie entry
- `/api/movies/<movie_id>/update/`: Update a movie's ranking
- `/api/movies/<movie_id>/delete/`: Delete a movie from a user's list

### Example Requests

- `GET /api/movies/`: Retrieve a user's movie list

```json
{
  "movies": [
    {
      "id": 1,
      "title": "Movie 1",
      "rank": 1
    },
    {
      "id": 2,
      "title": "Movie 2",
      "rank": 2
    }
  ]
}
```

- `POST /api/movies/create/`: Create a new movie entry

```json
{
  "title": "New Movie",
  "rank": 3
}
```

### Development

To contribute to this project, fork the repository and create a new branch for your feature or bug fix. Once you've made your changes, submit a pull request for review.

## **License**

This project is licensed under the MIT License. See [LICENSE](LICENSE) for details.

## **Acknowledgments**

- The Movie Database (TMDb) API for providing movie data
- Django for providing the backend framework

## **Contact**

If you have any questions or need help with the project, feel free to reach out to [your email address or GitHub username].

## Movie Ranking Engine

`CineRank` includes a powerful movie ranking engine designed to provide personalized movie recommendations. The engine leverages a combination of data-driven factors and user preferences to generate dynamic rankings.

### How It Works

1. **Weighted Factors:**

   - **Popularity (TMDB):** Indicates general interest and trendiness.
   - **Vote Average (TMDB):** Reflects critical and audience reception.
   - **Vote Count (TMDB):** Provides context to the average; higher counts mean more reliable averages.
   - **Revenue (if available):** Commercial success can be an indicator of quality or popularity.
   - **Recency:** Recent movies might be more relevant to users.
   - **User Ratings:** Personalized ratings directly influence recommendations.
   - **Genre Preferences:** User-selected genres are boosted in the rankings.

2. **Normalization & Scoring:** Each factor is normalized to a standard scale and combined using a weighted formula. The weights determine the importance of each factor, allowing for customization of the ranking logic.

3. **User Preferences:** The engine learns from user ratings and genre preferences (stored in the `UserMoviePreference` model) to tailor recommendations to individual tastes.
