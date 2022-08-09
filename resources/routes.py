
from .auth import SignupApi, LoginApi, RefreshApi

from .movie import MoviesApi, MovieApi




# Initialize Routes
def initialize_routes(api):
    api.add_resource(SignupApi, '/auth/signup')
    api.add_resource(LoginApi, '/auth/login')

    api.add_resource(RefreshApi, '/auth/refesh') 

    api.add_resource(MoviesApi, '/api/movies')
    api.add_resource(MovieApi, '/api/movies/<id>') 

