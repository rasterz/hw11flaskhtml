import json


def load_candidates_from_json() -> list [dict]:
    """
    Возвращает список всех кандидатов
    """
    with open("candidates.json", "r", encoding='utf-8') as file:
        return json.load(file)


def get_candidate(candidate_id: int) -> dict:
    """
    возвращает одного кандидата по его id
    """
    return load_candidates_from_json()[candidate_id - 1]


def get_candidates_by_name(candidate_name: str) -> list[dict]:
    """
    Возвращает кандидатов по имени
    """
    list_of_candidates = []
    for candidate in load_candidates_from_json():
        if candidate['name'] == candidate_name:
            list_of_candidates.append(candidate)
    return list_of_candidates


def get_candidates_by_skill(skill_name: str) -> list[dict]:
    """
    Возвращает кандидатов по навыку
    """
    list_of_candidates = []
    for candidate in load_candidates_from_json():
        if skill_name in candidate['skills'].lower().split(', '):
            list_of_candidates.append(candidate)
    return list_of_candidates
