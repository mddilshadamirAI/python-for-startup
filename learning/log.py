from flask import Flask, render_template, request, redirect, url_for, session, flash

app = Flask(__name__)
app.secret_key = 'super_secret_key_change_me'  # Essential for sessions

# Mock database
USER_DATA = {
    "admin": "password123"
}

@app.route('/')
def home():
    if 'username' in session:
        return f'Logged in as {session["username"]} | <a href="/logout">Logout</a>'
    return 'You are not logged in | <a href="/login">Login</a>'

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        # Check if credentials match our "database"
        if username in USER_DATA and USER_DATA[username] == password:
            session['username'] = username  # Create the session
            flash('Login Successful!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Invalid username or password', 'error')
            
    return '''
        <form method="post">
            <p><input type="text" name="username" placeholder="Username"></p>
            <p><input type="password" name="password" placeholder="Password"></p>
            <p><button type="submit">Login</button></p>
        </form>
    '''

@app.route('/logout')
def logout():
    session.pop('username', None)  # Remove user from session
    flash('You have been logged out.', 'info')
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)