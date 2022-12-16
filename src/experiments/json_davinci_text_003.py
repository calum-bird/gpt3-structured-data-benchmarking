import json

from classes.OpenAIOptions import OpenAIOptions
from classes.Experiment import Experiment


prompt = """// A JSON object with some random data
// START
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
// END

// Another JSON object with some data
// START
{
"""

options = OpenAIOptions(
  model="text-davinci-003",
  max_length=256,
  temperature=1.0,
  top_p=1.0,
  stop_sequence=["// END"]
)


test_output_fn = lambda x: json.loads("{" + x["choices"][0]["text"])

experiment = Experiment(
  "json-text-davinci-003",
  options,
  prompt,
  test_output_fn
)