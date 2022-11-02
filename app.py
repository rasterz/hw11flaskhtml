from utils import load_candidates_from_json, get_candidates_by_name, get_candidates_by_skill, get_candidate
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def main_page():
    candidates: list[dict] = load_candidates_from_json()
    return render_template('list.html', candidates=candidates)


@app.route('/candidate/<int:idx>')
def candidate_page(idx):
    candidate: dict = get_candidate(idx)
    if not candidate:
        return 'Такого кандидата нет'
    return render_template('card.html', candidate=candidate)


@app.route('/search/<candidate_name>')
def search_candidates_page(candidate_name):
    candidates: list[dict] = get_candidates_by_name(candidate_name)
    return render_template('search.html', candidates=candidates)


@app.route('/skills/<candidate_skill>')
def search_candidates_skills(candidate_skill):
    candidates: list[dict] = get_candidates_by_skill(candidate_skill)
    return render_template('skill.html', skill=candidate_skill, candidates=candidates)


app.run()
