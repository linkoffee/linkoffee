import datetime
import os

# Date of start my dev-career
START_DATE = datetime.datetime(2023, 11, 8)

# Current date
CURRENT_DATE = datetime.datetime.now()

# My experience in days
EXPERIENCE_DAYS = (CURRENT_DATE - START_DATE).days

# Directory with template files for update
TEMPLATES_DIR = 'templates'

# Files to be overwritten
OUTPUT_FILES = [
    'README.md', 'README_EN.md', 'README_AR.md',
    'README_CN.md', 'README_ES.md', 'README_UA.md'
]

# Template files for updating
TEMPLATE_FILES = [
    'README_template.md', 'README_EN_template.md', 'README_AR_template.md',
    'README_CN_template.md', 'README_ES_template.md', 'README_UA_template.md'
]

for template_file, output_file in zip(TEMPLATE_FILES, OUTPUT_FILES):
    template_path = os.path.join(TEMPLATES_DIR, template_file)
    with open(template_path, 'r', encoding='utf-8') as file:
        content = file.read()

    updated_content = content.replace(
        '{EXPERIENCE_DAYS}', str(EXPERIENCE_DAYS)
    )

    with open(output_file, 'w', encoding='utf-8') as file:
        file.write(updated_content)
