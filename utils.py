import json

def load_candidates_from_json():
    with open('templates/candidates.json', 'r') as candidates:
        return json.load(candidates)

def get_candidate(candidate_id):
    result = []
    for i in load_candidates_from_json():
       if i['id'] == candidate_id:
            result.append(i)
    return result[0]


def get_candidates_by_name(candidate_name):
    result = []
    for i in load_candidates_from_json():
        if candidate_name.lower() in i['name'].lower():
            result.append(i)
    return result




def get_candidates_by_skill(skill_name):
    result = []
    for i in load_candidates_from_json():
        if skill_name.lower() in i['skills'].lower().split(', '):
            result.append(i)
    return result




