from flask import Flask

app = Flask(__name__)

@app.route("/") # / Front page 
def home():
    return """
        <h1>Dynamic Routes Demo</h1>
<h2>Try: These URLS</h2>
<ul>
    <li><a href="/user/john">User Profile: john</a></li>
    <li><a href="user/alice">User Profile: alice</a></li>
</ul>
    """

@app.route("/user/username", methods=['GET'])
def user_profile(username):
    # return "About Page!"
    return f"""
        <h1>User Profile</h1>
 <p>Username: <strong>{username}</strong></p>
 <p>Profile Type: {type(username).__name__}</p>
 <p>Welcome to {username}'s profile page!</p>
 <nav>
     <a href="/">Back to Homepage</a>
     <a href="/user/alice">Alice</a>
     <a href="/user/bob">Bob</a>
</nav>  
    """
@app.route('/calc/<int:num1>/<operation>/<int:num2>')
def calculator(num1,operation,num2):
    operations = {
        '+': num1 +num2,
        '-': num1 - num2,
        '*': num1 * num2,
        '/': num1 / num2 if num2 !=0 else "Error: Division by zero!"
    }
    if operation in operations:
        result = operations[operation]
        return f"{num1} {operation} {num2} = {result} "
    else:
        return f'Unknown operation! {operation}'
    
@app.route('/temp/<measurement>/<int:tempGiven>')
def tempconverter(measurement,tempGiven):
    FtoC = (32-tempGiven)*5/9
    CtoF = (tempGiven*5/9)+32
    if measurement == 'F':
        return f'{tempGiven}F = {FtoC}C'
    elif measurement == 'C':
        return f'{tempGiven}C = {CtoF}F'
    else:
        return "Invalid Measurement"

if __name__ == "__main__":
    app.run(debug=True)