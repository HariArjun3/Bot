def skill_config(file):
    # To read file as string (assuming a text file):
    content = file.read().decode("utf-8")

    # Process the file content
    skills = [skill.strip() for skill in content.splitlines()]

    # Display the processed skills
    return skills


def matched_skills(text, skill_file):
    return [skill for skill in skill_file if skill.lower().strip() in text.lower().strip()]


def matching_skills(text, skill_file):
    total_skills = sum(1 for skill in skill_file if skill.lower().strip() in text.lower().strip())
    percentage = (total_skills / len(skill_file)) * 100
    return f"Skills found: {percentage:.2f}%"
