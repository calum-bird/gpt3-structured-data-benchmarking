import json

from classes.OpenAIOptions import OpenAIOptions
from classes.Experiment import Experiment


prompt = """// A JSON object with some random data
{
  "some_data": "some_value",
  "array": [
    "some_value",
    "some_value",
  ],
  "object": {
    "some_data": "some_value",
    "array": [
      "some_value"
    ]
  }
}

// Another JSON object with some data
{"""

# Test whether we can load the resultant json
test_output_fn = lambda x: json.loads("{" + x["choices"][0]["text"] + "}")

# Create a new experiment for various temps and top_p
experiments = []
for i in range(0, 10):
  temp = i / 10
  
  for j in range(0, 10):
    top_p = j / 10
    
    options = OpenAIOptions(
      model="text-babbage-001",
      max_length=256,
      temperature=temp,
      top_p=top_p,
      stop_sequence=["\n}"]
    )
    
    experiment = Experiment(
      f"json-text-babbage-001-{temp}-{top_p}",
      options,
      prompt,
      test_output_fn
    )
    experiments.append(experiment)