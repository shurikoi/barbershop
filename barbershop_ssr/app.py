from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def start_page():
    return render_template("startPage.html", title="Barbershop")

# Check if the script is executed directly (not imported) and then run the application.
# The application will start a development server that listens on localhost:5000 by default.
if __name__ == '__main__':
    app.run(debug=True)