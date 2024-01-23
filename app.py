from flask import Flask, render_template, request
from forms import UserForm

app = Flask(__name__)

# Initialize an empty dictionary to store data
data = {}
user_id_counter = 1

@app.route("/")
def index():
    return render_template("form.html")

@app.route("/users")
def users():
    return render_template("users.html", users=data.values())

@app.route("/submit", methods=["POST"])
def submit():
    global data  # Declare data as a global variable
    try:
        form = UserForm(request.form)

        if form.validate():
            global user_id_counter

            # Get the form data
            username = request.form["username"]
            email = request.form["email"]

            # Add data to the dictionary
            data[user_id_counter] = {'id': user_id_counter, 'username': username, 'email': email}
            user_id_counter += 1

            return "User added successfully"
        else:
            # Display error messages
            return 'Invalid form data, please try again.'
    except Exception as e:
        return f"An error occurred: {str(e)}"

if __name__ == "__main__":
    app.run(debug=True)
