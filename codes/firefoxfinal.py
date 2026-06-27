from browser_history.browsers import Firefox
import os
from datetime import datetime, timedelta

# Create a folder to store the output files (if it doesn't exist)
output_folder = 'firefox_history'
os.makedirs(output_folder, exist_ok=True)

# Specify the output file path
output_file_path = os.path.join(output_folder, 'firefox_history.txt')

f = Firefox()
outputs = f.fetch_history()

# This is a list of (datetime.datetime, url) tuples
histories = outputs.histories

# Calculate the date three months ago from today
three_months_ago = datetime.now() - timedelta(days=90)

# Open the output file in write mode
with open(output_file_path, 'w', encoding='utf-8') as output_file:
    for history_entry in histories:
        timestamp = history_entry[0]  # Get the timestamp from the tuple
        url = history_entry[1]  # Get the URL from the tuple
        # Ensure timestamp is timezone-naive by removing timezone info
        timestamp = timestamp.replace(tzinfo=None)
        if timestamp >= three_months_ago:
            output_file.write(f"Timestamp: {timestamp}\n")
            output_file.write(f"URL: {url}\n")
            output_file.write("\n")

print(f"Firefox browser history from the past 3 months saved to {output_file_path}")
