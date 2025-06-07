{
  "username": "myusername",
  "password": "mypassword"
}

{
  "access": "JWT_ACCESS_TOKEN",
  "refresh": "JWT_REFRESH_TOKEN"
}


{
  "participants": [1, 2]
}

{
  "conversation": 1,
  "content": "Hello, this is a test message."
}
Note: sender is automatically set to the authenticated user (due to perform_create() override).


?start_date=2025-01-01T00:00:00Z&end_date=2025-01-15T23:59:59Z
:

GET /api/conversations/
Expected Response:

{
  "detail": "Authentication credentials were not provided."
}
