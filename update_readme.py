import datetime

start_date = datetime.datetime(2023, 11, 8)
current_date = datetime.datetime.now()
experience_days = (current_date - start_date).days

files_to_update = [
    "README.md", "README_EN.md", "README_AR.md",
    "README_CN.md", "README_ES.md", "README_UA.md"
]

for file_name in files_to_update:
    with open(file_name, "r", encoding="utf-8") as file:
        content = file.read()

    updated_content = content.replace(
        "{experience_days}", str(experience_days)
    )

    with open(file_name, "w", encoding="utf-8") as file:
        file.write(updated_content)
