"""
fillorbust new game view.

URLs include:
/newGame
"""
import flask
import arrow
from fillorbust import app, info


@app.route('/newGame/', methods=['GET', 'POST'])
def newGame():
    """New Game route."""
    if flask.request.method == 'POST':
        if 'numPlayers' in flask.request.form:
            info["numPlayers"] = int(flask.request.form['numPlayers'])
            return flask.render_template("newGame.html", **info)
        else:
            info["players"] = []
            for i in range(info["numPlayers"]):
                name = flask.request.form['player%s'%i]
                info["players"].append({"score":0, "name":name})
            print(info)
            return flask.redirect(flask.url_for('game'))

    return flask.render_template("newGame.html", **info)
