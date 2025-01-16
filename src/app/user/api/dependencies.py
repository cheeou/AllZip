from src.app.user.model.user import Profile, User
from src.app.user.model.user_data import UserData
from src.app.user.repository.user import ProfileRepository, UserRepository
from src.app.user.repository.user_data import UserDataRepository
from src.app.user.service.user import UserService
from src.app.user.service.user_data import UserDataService
from src.core.dependencies.auth import jwt_service
from src.app.user.service.social_auth.google import GoogleOAuthService
from src.app.user.repository.social_user import SocialUserRepository


user_repository = UserRepository(User)
profile_repository = ProfileRepository(Profile)
user_service = UserService(user_repository, profile_repository, jwt_service)

user_data_repository = UserDataRepository(UserData)
user_data_service = UserDataService(user_data_repository)

social_user_repository = SocialUserRepository(User)
google_oauth_service = GoogleOAuthService(social_user_repository)