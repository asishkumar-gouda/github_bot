import os
import random
import datetime

def makeCommits(start_date: str, end_date: str):
    start = datetime.datetime.strptime(start_date, '%Y-%m-%d')
    end = datetime.datetime.strptime(end_date, '%Y-%m-%d')
    
    current_date = start
    while current_date <= end:
        commit_date_str = current_date.strftime('%Y-%m-%d')
        
        # Decide the number of commits for this day (random between 1 and 10)
        num_commits = random.randint(1, 10)
        
        # Write commit messages to file
        with open('data.txt', 'a') as file:
            for _ in range(num_commits):
                file.write(f'{commit_date_str} <- this was the commit for the day!!\n')
        
        # Staging 
        os.system('git add data.txt')

        # Commit 
        os.system(f'git commit --date="{commit_date_str}" -m "Commit for {commit_date_str}"')

        # Move to the next day
        current_date += datetime.timedelta(days=1)

    # After committing for all days, push to the repository
    os.system('git push')

# Define the range of dates (Jan 1, 2024 to Mar 31, 2024)
start_date = '2024-01-01'
end_date = '2024-03-31'

makeCommits(start_date, end_date)
