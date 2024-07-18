import os
from dotenv import load_dotenv
import azure.cognitiveservices.speech as speechsdk

load_dotenv()

# Azure Speech Service Configuration
speech_key = os.getenv("AZURE_SPEECH_KEY")
service_region = os.getenv("AZURE_SERVICE_REGION", "southeastasia")
speech_config = speechsdk.SpeechConfig(subscription=speech_key, region=service_region)

# PostgreSQL connection setup
db_host = os.getenv("DB_HOST")
db_name = os.getenv("DB_NAME")
db_user = os.getenv("DB_USER")
db_pass = os.getenv("DB_PASS")
