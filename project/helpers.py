def build_personal_information_string(personal_information):
    try:
        name = personal_information["name"]
        email = personal_information["email"]
        location = personal_information["location"]
        print(f"{name} - {email} - {location}")
    except KeyError:
        print("Missing information in PERSONAL_INFORMATION")


def build_experience_string(experience):
    for i, exp in enumerate(experience):
        try:
            print(
                f"Experience {i + 1}:\n"
                f"Title: {exp['title']}\n"
                f"Company: {exp['company']}\n"
                f"Location: {exp['location']}\n"
                f"Start Date: {exp['start_date']}\n"
                f"End Date: {exp['end_date']}\n"
                f"Description: {exp['description']}"
            )
        except KeyError:
            print("Missing information in EXPERIENCE")


def build_education_string(education):
    for i, edu in enumerate(education):
        try:
            print(
                f"Education {i + 1}:\n"
                f"Degree: {edu['degree']}\n"
                f"School: {edu['school']}\n"
                f"Location: {edu['location']}\n"
                f"Start Date: {edu['start_date']}\n"
                f"End Date: {edu['end_date']}"
            )
        except KeyError:
            print("Missing information in EDUCATION")
