import re
import csv

# 替換成你的 .log 檔案路徑
log_file_path = 'logs/HalfCheetah/output.log'

# 正則表達式擷取 Episode、Total step、Total Reward
pattern = re.compile(r"Episode (\d+) \(Total step = (\d+)\): Total Reward = ([\d\.Ee+-]+)")

results = []

# 讀取檔案並搜尋符合的行
with open(log_file_path, 'r', encoding='utf-8') as file:
    for line in file:
        match = pattern.search(line)
        if match:
            episode = int(match.group(1))
            total_step = int(match.group(2))
            total_reward = float(match.group(3))
            results.append((episode, total_step, total_reward))

with open('output_rewards.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['Episode', 'Total Step', 'Total Reward'])
    writer.writerows(results)

