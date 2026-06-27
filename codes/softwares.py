import os
import datetime

def get_recently_installed_software():
    program_files_32 = os.environ.get("ProgramFiles(x86)")
    program_files_64 = os.environ.get("ProgramFiles")

    if program_files_32:
        program_files_32 = os.path.join(program_files_32, "Installed Programs")
    if program_files_64:
        program_files_64 = os.path.join(program_files_64, "Installed Programs")

    installation_paths = [path for path in [program_files_32, program_files_64] if path and os.path.exists(path)]
    current_time = datetime.datetime.now()
    six_months_ago = current_time - datetime.timedelta(days=500)  # 180 days is roughly 6 months

    recently_installed_software = []

    for installation_path in installation_paths:
        for root, dirs, files in os.walk(installation_path):
            for file in files:
                file_path = os.path.join(root, file)
                installation_time = datetime.datetime.fromtimestamp(os.path.getctime(file_path))

                if six_months_ago <= installation_time <= current_time:
                    recently_installed_software.append((file, installation_time))

    return recently_installed_software

def save_to_text_file(installed_software_list, filename):
    with open(filename, "w") as file:
        for item in installed_software_list:
            file.write(f"Software Name: {item[0]}\nInstallation Date: {item[1]}\n\n")

if __name__ == "__main__":
    recently_installed_software = get_recently_installed_software()
    save_to_text_file(recently_installed_software, "recently_installed_software.txt")
