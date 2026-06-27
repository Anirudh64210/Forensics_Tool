import sqlite3
import shutil
import os
import datetime
import platform

# Determine the Chrome user data directory based on the OS
if platform.system() == 'Windows':
    user_data_dir = os.path.join(os.getenv('LOCALAPPDATA'), 'Google', 'Chrome', 'User Data')
elif platform.system() == 'Darwin':  # macOS
    user_data_dir = os.path.expanduser('~/Library/Application Support/Google/Chrome')
else:  # Linux and others
    user_data_dir = os.path.expanduser('~/.config/google-chrome')

# Define the source and destination file paths
source_path = os.path.join(user_data_dir, 'Default', 'History')
destination_path = 'history.txt'

# Calculate a timestamp for 3 months ago
three_months_ago = datetime.datetime.now() - datetime.timedelta(days=90)

# Copy the history file to the destination
shutil.copy(source_path, destination_path)

# Connect to the copied History database
conn = sqlite3.connect(destination_path)
cursor = conn.cursor()

# Query to retrieve URLs visited in the last 3 months
query = f"SELECT url, title, last_visit_time FROM urls WHERE last_visit_time >= {three_months_ago.timestamp()}"

# Execute the query and fetch the results
cursor.execute(query)
results = cursor.fetchall()

# Close the database connection
conn.close()

# Save the results to a text file with UTF-8 encoding
with open('history.txt', 'w', encoding='utf-8') as output_file:
    for row in results:
        url, title, last_visit_time = row
        output_file.write(f"Title: {title}\nURL: {url}\nLast Visit Time: {last_visit_time}\n\n")

print("Browsing history saved to history.txt")
