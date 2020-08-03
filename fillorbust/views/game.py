"""
fillorbust new game view.

URLs include:
/newGame
"""
import flask
import arrow
from fillorbust import app, info


@app.route('/game/', methods=['GET', 'POST'])
def game():
    """Game route."""
    if flask.request.method == 'POST':
        name = flask.request.form["playerlist"]
        points = int(flask.request.form["points"])
        for i in range(len(info["players"])):
            if name == info["players"][i]["name"]:
                info["players"][i]["score"] += points
        info["players"] = sorted(info["players"], key=lambda k: k['score'], reverse = True) 
    return flask.render_template("game.html", **info)
