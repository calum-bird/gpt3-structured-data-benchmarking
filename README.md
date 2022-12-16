# Benchmarking GPT-3 on structured data formats

## Why does this exist

Certain use-cases for generating text using GPT-3 may find generating structured data beneficial. However, this comes with some risks. Namely, GPT-3 will occasionally fail to adhere to the rules of particular structured data formats. For instance, when generating JSON, the model may hallucinate an extra parenthesis, or miss a double-quote.

These errors cause the generated data to be effectively useless. The goal of this repo is to benchmark the error-rate of GPT-3 when generating structured data across numerous formats. It is highly extensible for ease of use in future experiments.

## Running the benchmarks

Ensure you have set your OpenAI API key: `export OPENAI_API_KEY=sk_...`

Then, run the benchmark: `python src/benchmark.py`

Results will be outputed into `results.txt`

## Adding an experiment

Experiments are defined using the `Experiment` class. At its core, every experiment is effectively an OpenAI request, fed into
a test lambda function that should error out upon failure to parse.

Here is an example for a simple json test:

````python
import json

from classes.OpenAIOptions import OpenAIOptions
from classes.Experiment import Experiment


prompt = """// A JSON object with some data
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
      "some_value",
    ],
  },
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
  top_p=0.0,
  stop_sequence=["// END"]
)

test_output_fn = lambda x: json.loads("{" + x["choices"][0]["text"])

experiment = Experiment(
  "json-text-davinci-003",
  options,
  prompt,
  test_output_fn
)```
````
