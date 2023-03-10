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

```python
import json

from classes.OpenAIOptions import OpenAIOptions
from classes.Experiment import Experiment


prompt = """// A random json object, containing 3 fields
{"""

options = OpenAIOptions(
  model="text-davinci-003",
  max_length=256,
  temperature=1.0,
  top_p=0.0,
  stop_sequence=["\n}", "}\n\n"]
)

def test_output_fn(response):
  text = response["choices"][0]["text"]
  full_json = "{" + text + "}"
  fixed_json = ' '.join(full_json.split())
  json.loads(fixed_json)

experiment = Experiment(
  "json-text-davinci-003",
  options,
  prompt,
  test_output_fn
)
```

Now that you have created an experiment, import it into `src/benchmark.py` and add it to the `experiments` array. By default we run each experiment 5 times. You can change this by updating the `num_runs` variable.

You're good to go! Results including your new experiment will be written to `results.txt` on the next run.
