import datetime
import os

# Date of start my dev-career
START_DATE = datetime.datetime(2023, 11, 8)

# Current date
CURRENT_DATE = datetime.datetime.now()

# My experience in days
EXPERIENCE_DAYS = (CURRENT_DATE - START_DATE).days

# Correct form of the word "day" (Russian version only)
DAY_WORD_FORM_RU = {
    (0, 5, 6, 7, 8, 9): 'дней',
    (2, 3, 4): 'дня',
    (1,): 'день'
}

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


def get_day_word_form_ru(days_value):
    """Gets the required form of a word from the dictionary."""
    last_digit = days_value % 10
    last_two_digits = days_value % 100

    if 11 <= last_two_digits <= 14:
        return 'дней'
    for key, value in DAY_WORD_FORM_RU.items():
        if last_digit in key:
            return value
    return 'дней'


for template_file, output_file in zip(TEMPLATE_FILES, OUTPUT_FILES):
    template_path = os.path.join(TEMPLATES_DIR, template_file)
    with open(template_path, 'r', encoding='utf-8') as file:
        content = file.read()

    updated_content = content.replace(
        '{EXPERIENCE_DAYS}', str(EXPERIENCE_DAYS)
    )

    if '{DAY_WORD_FORM_RU}' in content:
        day_word_form = get_day_word_form_ru(EXPERIENCE_DAYS)
        updated_content = updated_content.replace(
            '{DAY_WORD_FORM_RU}', day_word_form
        )

    with open(output_file, 'w', encoding='utf-8') as file:
        file.write(updated_content)
