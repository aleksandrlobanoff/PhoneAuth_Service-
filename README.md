# Phone Authorization Service API

This project implements an API for phone number authentication and user management functionality.

## Project Description

This project provides functionality for user authentication through phone numbers, activation and management of invite codes, and user interaction via an API.

## Installation and Project Setup

1. Install all the dependencies mentioned in the requirements.txt file:

   pip install -r requirements.txt

2. Apply the database migrations:

   python manage.py migrate

3. Run the development server:

   python manage.py runserver

## Endpoints

### User Authentication

URL: /auth/

Method: POST

Description: Checks if the user exists in the database and returns a one-time code for authorization.

Request Parameters:
- phone_number (required) - User's phone number.

Sample Request:

{
    "phone_number": "89123456789"
}

Response:

{
    "otp_code": "1234"
}

### Update Authentication Code

URL: /auth/

Method: PUT

Description: Verifies the user's authentication code and returns an access token for further API access.

Request Parameters:
- phone_number (required) - User's phone number.
- otp_code (required) - Verification code received after authentication.

Sample Request:

{
    "phone_number": "89123456789",
    "otp_code": "1234"
}

Response:

{
    "access_token": "..."
}

### User Profile Retrieval

URL: /profile/

Method: GET

Description: Returns information about the user's profile, including their phone number and other details.

Sample Response:

{
    "phone_number": "89123456789",
    "invite_code": "ABCD123",
    "other_profile_invite_code": "EFGH456",
    "invited_users": [
        "89543210987",
        "89765432109"
    ]
}

### Activation of Another User's Invite Code

URL: /profile/

Method: POST

Description: Allows the user to activate someone else's invite code in their own profile.

Request Parameters:
- other_profile_invite_code (required) - Another user's invite code.

Sample Request:

{
    "other_profile_invite_code": "EFGH456"
}

Response:

{
    "message": "The other user's invite code was successfully activated in the user's profile."
}

## Running the Project

1. Install all the required dependencies mentioned in the requirements.txt file.

2. Apply the necessary database configurations and settings, ensuring the correct environment variables are set.

3. Execute the command python manage.py migrate to apply the database migrations.

4. Start the development server using the command python manage.py runserver.

5. You can now send requests to the API endpoints from your application.

# Running the project with Docker

1. Install Docker on your machine if you haven't done so already.

2. Build the Docker image using the following command:

docker build -t phone-auth-service .

3. Run the Docker container with the following command:

docker run -p 8000:8000 phone-auth-service

4. Now you can send requests to the API endpoints from your application.