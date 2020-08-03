"""
fillorbust index (main) view.

URLs include:
/
"""
import flask
import arrow
from fillorbust import app, info


@app.route('/', methods=['GET', 'POST'])
def index():
    """Index route."""
    if flask.request.method == 'POST':
        # Check which form is coming in, then redirect to clear form
        # if 'newGame' in flask.request.form:
        return flask.redirect(flask.url_for('newGame'))
    info["numPlayers"] = 0
    return flask.render_template("index.html", **info)
