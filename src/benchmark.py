# Run each experiment 5 times by default
num_runs = 5

# Import all our experiments
from math import floor
from experiments.json_davinci_code_002 import experiment as json_davinci_code_003
from experiments.json_davinci_text_003 import experiment as json_davinci_text_003
from experiments.json_davinci_text_002 import experiment as json_davinci_text_002
from experiments.json_curie_text_001 import experiment as json_curie_text_001
experiments = [
  json_curie_text_001
]*num_runs

# Run all our experiments
experiment_results = []
for ex in experiments:
  experiment_results.append(ex.run())
  
# Generate a result string for all the experiments in a nice format
# Be sure to include the experiment name, id, and result
result_str = ""
pass_count = 0
for i in range(len(experiments)):
  result_str += f"{experiments[i].name} ({experiments[i].id}): {experiment_results[i]}\n"
  if experiment_results[i][0]:
    pass_count += 1
    
result_str += f"\n{pass_count}/{len(experiments)} = {floor(pass_count/len(experiments)*100)}% passed"
  
# Write to results.txt
with open("results.txt", "w") as f:
  f.write(result_str)
  
print("Done! Results written to results.txt")