import pickle

with open("results.pkl", "rb") as f:
  results_by_name = pickle.load(f)
  
pass_rate_by_name = {}
for name in results_by_name:
  pass_count = 0
  for result in results_by_name[name].get("ex.id"):
    print(result)
    if result["success"]:
      pass_count += 1
  pass_rate = pass_count / len(results_by_name[name])
  pass_rate_by_name[name] = pass_rate
  
print(pass_rate_by_name)