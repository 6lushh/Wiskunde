from flask import Flask, request, render_template

DOCENT_WACHTWOORD = "p.assen"

def zoek_antwoord(vraag, bestand):
    with open(bestand, 'r', encoding='utf-8') as f:
        regels = f.readlines()
    antwoorden = []
    for regel in regels:
        if vraag.lower() in regel.lower():
            antwoorden.append(regel.strip())
    return antwoorden if antwoorden else ['Geen antwoord gevonden.']

def lees_theorie(bestand):
    try:
        with open(bestand, 'r', encoding='utf-8') as f:
            return f.read()
    except FileNotFoundError:
        return ""

def schrijf_theorie(bestand, inhoud):
    with open(bestand, 'w', encoding='utf-8') as f:
        f.write(inhoud)

def verwijder_theorie(bestand):
    open(bestand, 'w', encoding='utf-8').close()


app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    antwoorden = []
    if request.method == "POST":
        klas = request.cookies.get('klas')
        print(klas)
        vraag = request.form.get("vraag", "")
        if klas == 4:
            antwoorden = zoek_antwoord(vraag, "wiskunde4.txt")
        elif klas == 3:
            antwoorden = zoek_antwoord(vraag, "wiskunde3.txt")
        elif klas == 2:
            antwoorden = zoek_antwoord(vraag, "wiskunde2.txt")
        elif klas == 1:
            antwoorden = zoek_antwoord(vraag, "wiskunde1.txt")
    return render_template("index.html", antwoorden=antwoorden)

@app.route("/wiskunde1", methods=["GET", "POST"])
def wiskunde1():
    theorie = lees_theorie("wiskunde1.txt")
    foutmelding = ""
    if request.method == "POST":
        wachtwoord = request.form.get("wachtwoord", "")
        if wachtwoord != DOCENT_WACHTWOORD:
            foutmelding = "Onjuist wachtwoord!"
        else:
            actie = request.form.get("actie")
            if actie == "opslaan":
                nieuwe_theorie = request.form.get("theorie", "")
                schrijf_theorie("wiskunde1.txt", nieuwe_theorie)
                theorie = nieuwe_theorie
            elif actie == "verwijderen":
                verwijder_theorie("wiskunde1.txt")
                theorie = ""
    return render_template("wiskunde1.html", theorie=theorie, foutmelding=foutmelding)

@app.route("/wiskunde2", methods=["GET", "POST"])
def wiskunde2():
    theorie = lees_theorie("wiskunde2.txt")
    foutmelding = ""
    if request.method == "POST":
        wachtwoord = request.form.get("wachtwoord", "")
        if wachtwoord != DOCENT_WACHTWOORD:
            foutmelding = "Onjuist wachtwoord!"
        else:
            actie = request.form.get("actie")
            if actie == "opslaan":
                nieuwe_theorie = request.form.get("theorie", "")
                schrijf_theorie("wiskunde2.txt", nieuwe_theorie)
                theorie = nieuwe_theorie
            elif actie == "verwijderen":
                verwijder_theorie("wiskunde2.txt")
                theorie = ""
    return render_template("wiskunde2.html", theorie=theorie, foutmelding=foutmelding)

@app.route("/wiskunde3", methods=["GET", "POST"])
def wiskunde3():
    theorie = lees_theorie("wiskunde3.txt")
    foutmelding = ""
    if request.method == "POST":
        wachtwoord = request.form.get("wachtwoord", "")
        if wachtwoord != DOCENT_WACHTWOORD:
            foutmelding = "Onjuist wachtwoord!"
        else:
            actie = request.form.get("actie")
            if actie == "opslaan":
                nieuwe_theorie = request.form.get("theorie", "")
                schrijf_theorie("wiskunde3.txt", nieuwe_theorie)
                theorie = nieuwe_theorie
            elif actie == "verwijderen":
                verwijder_theorie("wiskunde3.txt")
                theorie = ""
    return render_template("wiskunde3.html", theorie=theorie, foutmelding=foutmelding)

@app.route("/wiskunde4", methods=["GET", "POST"])
def wiskunde4():
    theorie = lees_theorie("wiskunde4.txt")
    foutmelding = ""
    if request.method == "POST":
        wachtwoord = request.form.get("wachtwoord", "")
        if wachtwoord != DOCENT_WACHTWOORD:
            foutmelding = "Onjuist wachtwoord!"
        else:
            actie = request.form.get("actie")
            if actie == "opslaan":
                nieuwe_theorie = request.form.get("theorie", "")
                schrijf_theorie("wiskunde4.txt", nieuwe_theorie)
                theorie = nieuwe_theorie
            elif actie == "verwijderen":
                verwijder_theorie("wiskunde4.txt")
                theorie = ""
    return render_template("wiskunde4.html", theorie=theorie, foutmelding=foutmelding)


@app.route("/info")
def infoindex():
    return render_template("info.html")
if __name__ == "__main__":
    app.run(debug=True)