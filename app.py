from flask import Flask, request, render_template

app = Flask(__name__)
    
@app.route('/',methods=["GET","POST"])
def home():
    return render_template("home.html")

@app.route('/contact',methods=["GET","POST"])
def contact():
    return render_template("contact.html")

@app.route('/mission',methods=["GET","POST"])
def mission():
    return render_template("mission.html")

@app.route('/call',methods=["GET","POST"])
def emergency():
    return render_template("call.html")

@app.route('/maps',methods=["GET","POST"])
def maps():
    return render_template("maps.html")

@app.route("/chatbot")
def chatbot():
    return render_template("chatbot.html")

@app.route("/progress")
def workouts():
    return render_template("workouts.html")

@app.route("/get")
#function for the bot response
def get_bot_response():
    userText = request.args.get('msg')
    return str(englishBot.get_response(userText))

if __name__ == "__main__":
    app.run(debug=True)
