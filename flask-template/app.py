# Copyright 2021 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# ---- YOUR APP STARTS HERE ----
# -- Import section --


'''Partner's Name: Lorelyne Chavez'''
from flask import Flask
from flask import render_template
from flask import request
from model import test_capital


# -- Initialization section --
app = Flask(__name__)


# -- Routes section --
@app.route('/')
@app.route('/index')
def index():
    return render_template("index.html")


@app.route('/results', methods=['GET', 'POST'])
def results():
    answers = {"New York": request.form['New York'], "California": request.form['California'], "Texas": request.form['Texas'], "Montana": request.form['Montana'], "Ohio":request.form["Ohio"]}
    avaiable_capitals = ["New York: Albany",
     "California: Sacramento",
      "Texas: Austin",
       "Montana: Helena",
        "Ohio: Columbus"]
    for state, capital in answers.items():
        if not answers.get(state):
            return ("Error: Please fill up all of the boxes!")
    final_results = test_capital(answers)
    
    max_score = len(final_results["Correct"])
    return render_template("results.html", overall_score = max_score, all_answers = avaiable_capitals)
