import os
from dotenv import load_dotenv

from elevenlabs.client import ElevenLabs
from elevenlabs.conversational_ai.conversation import Conversation
from elevenlabs.conversational_ai.default_audio_interface import DefaultAudioInterface

# Load .env
load_dotenv()
API_KEY = os.getenv("ELEVENLABS_API_KEY")
AGENT_ID = os.getenv("AGENT_KEY")

if not API_KEY or not AGENT_ID:
    raise ValueError("ELEVENLABS_API_KEY or AGENT_KEY missing in .env")

client = ElevenLabs(api_key=API_KEY)

# Callbacks
def print_agent_response(response):
    print(f"Agent: {response}")

def print_user_transcript(transcript):
    print(f"User: {transcript}")

conversation = Conversation(
    client=client,
    agent_id=AGENT_ID,
    requires_auth=True,
    audio_interface=DefaultAudioInterface(),
    callback_agent_response=print_agent_response,
    callback_user_transcript=print_user_transcript,
)

print("Start speaking — agent will respond based on your voice input...")
conversation.start_session()




# The session stays open until you end it manually


