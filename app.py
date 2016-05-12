# -*- coding: utf-8 -*-
""""""
from flask import Flask, Response, render_template, request, redirect, url_for
import os


app = Flask(__name__)
app.config['TITLE'] = os.environ.get('TITLE', 'WordPress.com')
app.config['JUSTICE_URL'] = 'https://www.youtube.com/watch?v=dQw4w9WgXcQ'
app.config['JUSTICE_MSG'] = 'Forgive me father, for I have snooped.\n'
app.config['SNOOP_CHARS'] = '\'"\r\n\b\t\x1a\\%_<>'


@app.route('/wp-login.php', methods=['GET', 'POST'])
def login():
    """Provide a login form, and handle posts."""
    error = False
    username = ''
    if request.method == 'POST':
        username = request.form.get('log', '')
        password = request.form.get('pwd', '')
        for c in app.config['SNOOP_CHARS']:
            if c in username or c in password:
                # Let justice be done unto those who snoop
                rv = Response(app.config['JUSTICE_MSG'])
                rv.status_code = 303
                rv.headers['Location'] = app.config['JUSTICE_URL']
                return rv
        error = True
    return render_template('login.html', title=app.config['TITLE'],
                           error=error, username=username)


if __name__ == '__main__':
    app.run(debug=True)
