import os
import random
import datetime

def makeCommit(commit_date: str):
    commit_date_obj = datetime.datetime.strptime(commit_date, '%Y-%m-%d')
    commit_date_str = commit_date_obj.strftime('%Y-%m-%d')
    
    # Ensure more than 7 commits for this day (random between 8 and 15)
    num_commits = random.randint(8, 15)
    
    # Write commit messages to file
    with open('data.txt', 'a') as file:
        for _ in range(num_commits):
            file.write(f'{commit_date_str} <- this was the commit for the day!!\n')
    
    # Staging 
    os.system('git add data.txt')

    # Commit
    for _ in range(num_commits):
        os.system(f'git commit --date="{commit_date_str}" -m "Commit for {commit_date_str}"')

    # Push to the repository
    os.system('git push')

# Define the start and end date for the commits
start_date = '2024-06-01'
end_date = '2024-06-07'

# Convert string dates to datetime objects
start_date_obj = datetime.datetime.strptime(start_date, '%Y-%m-%d')
end_date_obj = datetime.datetime.strptime(end_date, '%Y-%m-%d')

# Generate a list of dates from start_date to end_date
current_date_obj = start_date_obj
while current_date_obj <= end_date_obj:
    commit_date = current_date_obj.strftime('%Y-%m-%d')
    makeCommit(commit_date)
    current_date_obj += datetime.timedelta(days=1)
