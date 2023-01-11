from flask import Flask, render_template
from utils import *



app = Flask(__name__)

@app.route('/')
def main():
    cand = load_candidates_from_json()
    name_cand = load_candidates_from_json()[1]['name']
    return render_template('list.html', cand=cand, name_cand=name_cand)

@app.route("/candidate/<int:id>")
def get_cand(id):
    cand = get_candidate(id)
    return render_template('card.html', cand=cand)

@app.route("/search/<candidate_name>")
def get_search(candidate_name):
    cand = get_candidates_by_name(candidate_name)
    return render_template('search.html', cand=cand)

@app.route('/skill/<skill_name>')
def skills(skill_name):
    skills =  get_candidates_by_skill(skill_name)
    return render_template('skill.html',skills=skills, skill_name=skill_name)




app.run()



