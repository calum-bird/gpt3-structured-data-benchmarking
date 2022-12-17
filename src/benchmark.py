# Run each experiment n times (5 by default)
num_runs = 1

# Import all our experiments
from math import floor
from experiments.json_davinci_code_002 import experiment as json_davinci_code_003
from experiments.json_davinci_text_003 import experiment as json_davinci_text_003
from experiments.json_davinci_text_002 import experiment as json_davinci_text_002
from experiments.json_curie_text_001 import experiment as json_curie_text_001
from experiments.json_ada_text_001_all import experiments as json_ada_text_001_all
from experiments.json_babbage_text_001_all import experiments as json_babbage_text_001_all
from experiments.json_curie_text_001_all import experiments as json_curie_text_001_all

experiments = [
  json_curie_text_001,
  json_davinci_text_002,
  json_davinci_text_003,
  json_davinci_code_003,
]*num_runs
experiments.extend(json_ada_text_001_all)
experiments.extend(json_babbage_text_001_all)
experiments.extend(json_curie_text_001_all)

# Run all our experiments
experiment_results = []
for ex in experiments:
  print(f"Running {ex.name} ({ex.id})...", end=" ")
  experiment_results.append(ex.run())
  print("Done!", end="\n")
  
# Generate a result string for all the experiments in a nice format
# Be sure to include the experiment name, id, and result
result_str = ""
pass_count = 0
for i in range(len(experiments)):
  result_str += f"{experiments[i].name} ({experiments[i].id}): {experiment_results[i]}\n"
  if experiment_results[i][0]:
    pass_count += 1
    
result_str += f"\n{pass_count}/{len(experiments)} = {pass_count/len(experiments)*100}% passed"
  
# Write to results.txt
with open("results.txt", "w") as f:
  f.write(result_str)
  
print("Done! Results written to results.txt")