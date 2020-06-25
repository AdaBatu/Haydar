from flask import Flask, render_template
import datetime
app = flask(__name__)

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
        xcn = ["baş", "yarak", "malafat-ül şakşak", "kamış"]
        return render_template("infox.html", baban=anan, keriz=keriz, xcn=xcn)
    else:
        baban = "Bugün yılbaşı değil"
        return render_template("infox.html", baban=anan, keriz=keriz)
@app.route("/baş")
def baş():
    return render_template("baş.html")

