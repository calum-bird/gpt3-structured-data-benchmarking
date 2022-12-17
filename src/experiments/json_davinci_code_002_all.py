import json

from classes.OpenAIOptions import OpenAIOptions
from classes.Experiment import Experiment


prompt = """// A random json object, containing 3 fields
{"""

# Test whether we can load the resultant json
def test_output_fn(response):
  text = response["choices"][0]["text"]
  full_json = "{" + text + "}"
  fixed_json = ' '.join(full_json.split())
  json.loads(fixed_json)

# Create a new experiment for various temps and top_p
experiments = []
for i in range(0, 10):
  temp = i / 10
  
  for j in range(0, 10):
    top_p = j / 10
    
    options = OpenAIOptions(
      model="code-davinci-002",
      max_length=256,
      temperature=temp,
      top_p=top_p,
      stop_sequence=["\n}", "}\n\n"]
    )
    
    experiment = Experiment(
      f"json-code-davinci-002-T{temp}-P{top_p}",
      options,
      prompt,
      test_output_fn
    )
    experiments.append(experiment)