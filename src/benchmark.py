import pickle

# Run each experiment n times (5 by default)
num_runs = 5

# Import all our experiments
from experiments.json_ada_text_001_all import experiments as json_ada_text_001_all
from experiments.json_babbage_text_001_all import experiments as json_babbage_text_001_all
from experiments.json_curie_text_001_all import experiments as json_curie_text_001_all
from experiments.json_davinci_text_001_all import experiments as json_davinci_text_001_all
from experiments.json_davinci_text_002_all import experiments as json_davinci_text_002_all
from experiments.json_davinci_text_003_all import experiments as json_davinci_text_003_all
from experiments.json_davinci_code_002_all import experiments as json_davinci_code_002_all

experiments = []
experiments.extend(json_ada_text_001_all)
experiments.extend(json_babbage_text_001_all)
experiments.extend(json_curie_text_001_all)
experiments.extend(json_davinci_text_001_all)
experiments.extend(json_davinci_text_002_all)
experiments.extend(json_davinci_text_003_all)
experiments.extend(json_davinci_code_002_all)

# Run all our experiments
experiment_results = []
results_by_name = {}
for ex in experiments:
  print(f"Running {ex.name} ({ex.id})...", end=" ", flush=True)
  ex_result = ex.run()
  experiment_results.append(ex_result)
  success = ex_result[0]
  
  if ex.name not in results_by_name:
    results_by_name[ex.name] = []
  
  results_by_name[ex.name].append({"ex.id": {"success": success, "result": ex_result[1]}})
  
  print("Done (" + ("success" if success else "failure") + ")", end="\n")
  
  
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
  
# Pickl results_by_name for later analysis
pickle.dump(results_by_name, open("results.pkl", "wb"))

  
print("Done! Results written to results.txt")