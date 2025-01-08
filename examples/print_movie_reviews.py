import nested_dir.movie_pb2
import nested_dir.critic_pb2
import nested_dir.movie_reviews_pb2


def print_movie_reviews():
    all_reviews = movie_reviews_pb2.MovieReviews()

    du_levande_review = all_reviews.reviews.add()
    du_levande_review.movie.title = "Du Levande"
    du_levande_review.movie.release_date.seconds = 1263272400
    du_levande_review.movie.director = "Roy Andersson"
    du_levande_review.critic.full_name = "Roger Ebert"
    du_levande_review.critic.publisher = "rogerebert.com"
    du_levande_review.score_out_of_ten = 10

    print(all_reviews)
