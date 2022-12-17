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

options = OpenAIOptions(
  model="text-curie-001",
  max_length=256,
  temperature=1.0,
  top_p=1.0,
  stop_sequence=["// END"]
)


test_output_fn = lambda x: json.loads("{" + x["choices"][0]["text"] + "}")

experiment = Experiment(
  "json-text-curie-001",
  options,
  prompt,
  test_output_fn
)