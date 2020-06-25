from flask import Flask, render_template, request, session
import datetime
app = Flask(__name__)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)
@app.route("/anan")
def index():
    return "Baban"
@app.route("/<string:name>")
def meraba(isim):
    isim = isim.capitalize()
    return f"<h2>meraba {isim}</h2>"
@app.route("/")
def asd():
    suan = datetime.datetime.now()
    keriz = suan.month == 1 and suan.day == 1
    if keriz == True:
        baban = "Bugün yılbaşı"
        xcn = ["baş", "yarak", "malafat-ül şflask akşak", "kamış"]
        return render_template("infox.html", baban=baban, keriz=keriz, xcn=xcn)
    else:
        baban = "Bugün yılbaşı değil"
        return render_template("infox.html", baban=baban, keriz=keriz)
@app.route("/baş", methods=["POST", "GET"])
def poget():
    if session.get["olay"] is None:
        session["olay"] = []
    if request.method == "POST":
        kafan = request.form.get("ka")
        session["olay"].append(kafan)
    return render_template("baş.html", kafan=session["olay"])


