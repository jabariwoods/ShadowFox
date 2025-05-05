import pandas as pd

data = [
    {"over": 1, "ball": 2, "fielder": "PlayerA", "action": "catch", "outcome": "success"},
    {"over": 3, "ball": 5, "fielder": "PlayerB", "action": "run out", "outcome": "failure"},
    {"over": 7, "ball": 1, "fielder": "PlayerC", "action": "stop", "outcome": "success"},
]
df = pd.DataFrame(data)

fielding_summary = df.groupby(['fielder', 'action', 'outcome']).size().unstack(fill_value=0)
print(fielding_summary)

df.to_csv("fielding_analysis.csv", index=False)
