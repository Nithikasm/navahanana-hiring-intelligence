# src/preprocessing/candidate_text_builder.py

def build_candidate_text(candidate: dict) -> str:
    """
    Convert structured candidate data into a single text document
    for semantic embedding and retrieval.
    """

    sections = []

    profile = candidate.get("profile", {})

    sections.append(
        f"Title: {profile.get('current_title', '')}"
    )

    sections.append(
        f"Headline: {profile.get('headline', '')}"
    )

    sections.append(
        f"Summary: {profile.get('summary', '')}"
    )

    # Skills
    skills = candidate.get("skills", [])

    skill_names = []

    for skill in skills:
        if isinstance(skill, dict):
            name = skill.get("name", "")
            proficiency = skill.get("proficiency", "")
            duration = skill.get("duration_months", "")
            endorsements = skill.get("endorsements", "")

            skill_text = (
                f"{name} "
                f"(proficiency: {proficiency}, "
                f"duration: {duration} months, "
                f"endorsements: {endorsements})"
            )

            skill_names.append(skill_text)
            
    sections.append("Skills: " + ", ".join(skill_names))
    

    # Career history
    careers = candidate.get("career_history", [])

    for career in careers:  
        title = career.get("title", "")
        start_date = career.get("start_date", "") 
        end_date = career.get("end_date") or "Present" 
        company = career.get("company", "") 
        description = career.get("description", "") 
        duration = career.get("duration_months", "") 
        industry = career.get("industry", "") 
        company_size = career.get("company_size", "") 
        is_current = career.get("is_current", False) 
        
        sections.append( 
            f"Experience: {title} at {company} " 
            f"from {start_date} to {end_date}. " 
            f"Duration: {duration} months. " 
            f"Industry: {industry}. " 
            f"Company size: {company_size}. " 
            f"Current role: {is_current}. " 
            f"{description}" 
        )


    return "\n".join(sections)