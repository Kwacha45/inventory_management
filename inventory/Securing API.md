To secure the API, we use Django REST Framework's token-based authentication with JSON Web Tokens (JWT).
1.Install Required Libraries:
	pip install djangorestframework-simplejwt
2.Update Django Settings:
	Add the following settings to settings.py:
	INSTALLED_APPS += [
   	 'rest_framework',
    'rest_framework_simplejwt',
	]

	REST_FRAMEWORK = {
   	 'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
   	 ),
	}
3.Configure URLs:
Add authentication endpoints to your urls.py:
	from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

	urlpatterns += [
  	  path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    	path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
	]
4.Testing the Setup:
	Use curl commands to obtain token:

	curl -X POST http://localhost:8000/api/token/ \
     	-H "Content-Type: application/json" \
     	-d '{"username": "testuser", "password": "password"}'
	Use the token to access secured endpoints:
	curl -X GET http://localhost:8000/api/inventory/ \
     -H "Authorization: Bearer <your_token>"



