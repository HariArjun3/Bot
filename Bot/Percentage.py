def skill_config(self, file):
    with open(file, 'r') as file:
        return [skill.strip() for skill in file]


def matched_skills(self, text, skill_file):
    return [skill for skill in skill_file if skill.lower().strip() in text.lower().strip()]


def matching_skills(self, text, skill_file):
    total_skills = sum(1 for skill in skill_file if skill.lower().strip() in text.lower().strip())
    percentage = (total_skills / len(skill_file)) * 100
    return f"Skills found: {percentage:.2f}%"
