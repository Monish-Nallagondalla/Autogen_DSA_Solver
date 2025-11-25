import os
from dotenv import load_dotenv
from autogen_ext.models.openai import OpenAIChatCompletionClient
from config.constants import MODEL, OPENAI_API_KEY
load_dotenv()


api_key = os.getenv(OPENAI_API_KEY)


