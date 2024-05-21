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
[
  {
    "tmdb_id": 123,
    "imdb_id": "tt0123456",
    "title": "Movie Title",
    "genre": "Action",
    "production_company": "Warner Bros.",
    "production_country": "US",
    "collection": "DC Universe",
    "spoken_language": "en",
    "is_highly_rated": true,
    "poster_path": "/path/to/poster",
    "release_date": "2020-01-01",
    "vote_average": 8.5,
    "vote_count": 1000
  },
  {
    "tmdb_id": 456,
    "imdb_id": "tt6789012",
    "title": "Another Movie",
    "genre": "Comedy",
    "production_company": "Universal Pictures",
    "production_country": "US",
    "collection": null,
    "spoken_language": "en",
    "is_highly_rated": false,
    "poster_path": "/path/to/poster",
    "release_date": "2019-06-01",
    "vote_average": 7.2,
    "vote_count": 500
  }
]
```

Request: `GET api/movies/get_user_recommendations/`

Response:

```json

[
    {
        "tmdb_id": 123,
        "imdb_id": "tt0123456",
        "title": "Movie Title",
        "genre": "Action",
        "production_company": "Warner Bros.",
        "production_country": "US",
        "collection": "DC Universe",
        "spoken_language": "en",
        "is_highly_rated": true,
        "poster_path": "/path/to/poster",
        "release_date": "2020-01-01",
        "vote_average": 8.5,
        "vote_count": 1000,
        "ranking": 0.95
    },
    {
        "tmdb_id": 456,
        "imdb_id": "tt6789012",
        "title": "Another Movie",
        "genre": "Comedy",
        "production_company": "Universal Pictures",
        "production_country": "US",
        "collection": null,
        "spoken_language": "en",
        "is_highly_rated": false,
        "poster_path": "/path/to/poster",
        "release_date": "2019-06-01",
        "vote_average": 7.2,
        "vote_count": 500,
        "ranking": 0.85
    },
    ...
]

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

4. **Optimization:**
   - **Caching:** Rankings are cached for performance.
   - **Database Indexes:** Optimized for fast query execution.
   - **Precalculated Scores (Optional):** Can be implemented for further performance enhancement.

### Future Enhancements

- **Collaborative Filtering:** Explore incorporating collaborative filtering techniques to leverage similarities in user behavior for even more personalized recommendations.
- **Ranking Explanation:** Provide users with insights into why a movie was recommended (e.g., "Based on your love for sci-fi and high ratings, we think you'll enjoy...").
- **More Factors:** Experiment with additional factors like cast, crew, or keywords.

### Get Involved

We welcome contributions to improve and expand this movie ranking engine. Feel free to open issues for suggestions or submit pull requests with enhancements!
