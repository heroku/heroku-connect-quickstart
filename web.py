import os
import re

import flask

app = flask.Flask(__name__)
host_re = re.compile(r'^([^.]+)\.herokuapp\.com$')
CREATE_URL = 'https://connect.heroku.com/dashboard-next/create-connection'


@app.route('/create')
def create_redirect():
    match = host_re.match(flask.request.host)
    if match:
        return flask.redirect(CREATE_URL + '?create=%s' % match.group(1))
    return flask.redirect(CREATE_URL)


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
