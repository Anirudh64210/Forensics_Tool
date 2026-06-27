import os
import sqlite3
import time
import shutil

def copy_browser_database(browser_name):
    # Path to the original browser database
    if browser_name == "chrome":
        original_db_path = os.path.expanduser("~\\AppData\\Local\\Google\\Chrome\\User Data\\Default\\History")
    elif browser_name == "firefox":
        original_db_path = os.path.expanduser("~\\AppData\\Roaming\\Mozilla\\Firefox\\Profiles\\<profile_name>\\places.sqlite")
        # Replace <profile_name> with your Firefox profile name

    if not os.path.exists(original_db_path):
        return None  # Database file does not exist

    # Create a copy of the database
    copy_db_path = f"{original_db_path}.copy"
    shutil.copy2(original_db_path, copy_db_path)

    return copy_db_path

def get_browser_history(browser_name):
    browser_data = []

    db_copy_path = copy_browser_database(browser_name)

    if db_copy_path:
        try:
            connection = sqlite3.connect(db_copy_path)
            cursor = connection.cursor()

            current_time = int(time.time())
            seven_days_ago = current_time - 7 * 24 * 60 * 60

            query = f"SELECT url, title, last_visit_date FROM {browser_name}_history WHERE last_visit_date >= {seven_days_ago}"
            cursor.execute(query)

            for row in cursor.fetchall():
                url = row[0]
                title = row[1]
                visit_time = time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime(row[2] / 1000000))
                browser_data.append((url, title, visit_time))

            connection.close()

        except sqlite3.Error as e:
            print(f"Error accessing browser history database: {e}")

        finally:
            os.remove(db_copy_path)  # Remove the copy of the database

    return browser_data

# Rest of the code remains the same
"""
The copy_browser_database function creates a copy of the browser's database file, and it returns the path to the copy.

If the copy is successfully created, the code connects to the copy of the database for querying.

After querying the data, it removes the copy of the database to clean up.

Make sure to replace <profile_name> with your actual Firefox profile name as needed in the original_db_path variable. This approach ensures that you don't interfere with the browser's database while accessing the data.
"""

""" The "database is locked" error typically occurs when multiple processes or threads attempt to access the same SQLite database simultaneously. In your case, it's possible that the browser's database is in use by the browser itself while your code is trying to access it.

To tackle this problem, you can try the following approaches:

Close the Browser: Make sure the browser is completely closed before running your code to ensure that the database is not in use by the browser.

Retry Logic: Implement a retry mechanism to attempt database access multiple times with a delay between attempts. This gives the browser more time to release the lock on the database.

Database Copy: Instead of accessing the database directly, you can make a copy of the database file (e.g., History file for Chrome or places.sqlite for Firefox) and then access the copy. This way, you won't interfere with the browser's operation."""