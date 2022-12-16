import uuid
from helpers.oai import send_request
from classes.OpenAIOptions import OpenAIOptions

class Experiment:
  def __init__(self, name: str, openai_options: OpenAIOptions, prompt: str, test_output_fn: any):
    self.id = uuid.uuid4()
    self.name = name
    self.openai_options = openai_options
    self.prompt = prompt
    self.test_output_fn = test_output_fn
    
  def run(self):
    # Send our request
    oai_response = send_request(self.prompt, self.openai_options)
    
    # Now check if the output passes our test
    passed = False
    try:
      test_output = self.test_output_fn(oai_response)
      passed = True
    except Exception as e:
      test_output = str(e) + " :: " + str(oai_response["choices"][0]["text"])
      
    return passed, test_output
  
  def __str__(self):
    return f"Experiment: {self.name} ({self.id})"