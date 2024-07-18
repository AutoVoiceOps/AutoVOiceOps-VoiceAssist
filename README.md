# README

**1. Introduction**
This is a voice authentication application that uses Azure Cognitive Services for speech recognition and PostgreSQL for storing user data. The application is built using Streamlit and is organized into multiple modules for better maintainability and scalability.

**2. Directory Structure**
```
voice_auth_app/
├── app.py
├── config.py
├── database.py
├── feature_extraction.py
├── recording.py
├── recognition.py
├── user_registration.py
├── user_authentication.py
└── requirements.txt
```

**3. Setup**
- Clone the repository to your local machine.
- Ensure Python (version 3.7 or higher) is installed.
- Install the required dependencies using pip:
  ```
  pip install -r requirements.txt
  ```
- Create a `.env` file in the root directory and add your Azure Speech Service and PostgreSQL credentials:
  ```
  AZURE_SPEECH_KEY=your_azure_speech_key
  AZURE_SERVICE_REGION=your_azure_service_region
  DB_HOST=your_database_host
  DB_NAME=your_database_name
  DB_USER=your_database_user
  DB_PASS=your_database_password
  ```

**4. Running the Application**
- Navigate to the project directory.
- Run the Streamlit application:
  ```
  streamlit run app.py
  ```

**5. File Descriptions**
- **app.py**: Main entry point of the Streamlit app.
- **config.py**: Configuration for Azure Speech Service and PostgreSQL connection.
- **database.py**: Handles database connection and ensures the users table exists.
- **feature_extraction.py**: Extracts features from audio files using librosa.
- **recording.py**: Records audio using pyaudio.
- **recognition.py**: Recognizes speech from audio files using Azure Cognitive Services.
- **user_registration.py**: Streamlit UI and logic for registering a user.
- **user_authentication.py**: Streamlit UI and logic for authenticating a user.
- **requirements.txt**: Lists Python dependencies for the project.

**6. How to Register a User**
- Open the Streamlit application.
- Navigate to the "Register User" page using the sidebar.
- Enter a username (letters and numbers only).
- Click the "Record and Register" button to record your voice and register.

**7. How to Authenticate a User**
- Open the Streamlit application.
- Navigate to the "Authenticate User" page using the sidebar.
- Enter your registered username.
- Click the "Record and Authenticate" button to record your voice and authenticate.

**8. Additional Information**
- The `temp` directory stores temporary audio files recorded during registration and authentication.
- Ensure the PostgreSQL server is running and accessible before starting the application.
- Verify Azure Speech Service key and region settings if there are issues with speech recognition.