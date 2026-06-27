import os
import time

def get_downloaded_files():
    downloads_folder = os.path.expanduser("~/Downloads")
    current_time = time.time()

    downloaded_files = []

    # Calculate the time threshold for the past 3 months (90 days)
    three_months_ago = current_time - 90 * 24 * 60 * 60

    for root, dirs, files in os.walk(downloads_folder):
        for file in files:
            file_path = os.path.join(root, file)
            modification_time = os.path.getmtime(file_path)
            
            # Check if the file was modified within the last 3 months
            if modification_time >= three_months_ago:
                downloaded_files.append(file_path)

    return downloaded_files

def save_to_text_file(file_list, filename):
    with open(filename, "w") as file:
        for item in file_list:
            file.write("%s\n" % item)

downloaded_files = get_downloaded_files()
save_to_text_file(downloaded_files, "downloaded_files_3_months.txt")