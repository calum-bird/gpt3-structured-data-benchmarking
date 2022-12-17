from classes.OpenAIOptions import OpenAIOptions

import openai
import os

# Set our OpenAI API key
openai.api_key = os.environ.get("OPENAI_API_KEY", None)
openai.api_base = "https://oai.valyrai.com/v1"
assert openai.api_key is not None

def send_request(prompt: str, openai_options: OpenAIOptions):
  response = openai.Completion.create(
    engine=openai_options.model,
    prompt=prompt,
    max_tokens=openai_options.max_length,
    temperature=openai_options.temperature,
    top_p=openai_options.top_p,
    stop=openai_options.stop_sequence
  )
  return response