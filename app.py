from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/',methods=["GET","POST"])
def home():
    return render_template("home.html")

@app.route('/contact',methods=["Get","POST"])
def contact():
    return render_template("contact.html")


if __name__ == '__main__':
    app.run(debug=True)
