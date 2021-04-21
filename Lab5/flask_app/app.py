from flask import Flask, render_template, url_for, request
from cifrador import CifradorRSA

app = Flask(__name__)

@app.route('/')

def menu():
    return render_template("menu.html")

@app.route('/cifre/')

def show_cifre_oage():
    return render_template("cifre.html")

@app.route('/ct', methods=["POST", "GET"])

def cifre_text():

    if request.method == "POST":

        text = request.form["text"]
        values = request.form["values"]
        values = values.split()
    
        cif = CifradorRSA()

        try:

            if request.form.get("selection")=="1":
                cif.generate_random()

            else:
                cif.Select(int(values[0]), int(values[1]))
        
        except ValueError:
            return render_template("cifre.html", first="", text="Ambos numeros deben ser primos", second="", val="")
        
        except IndexError:
            return render_template("cifre.html", first="", text="Ningun dato ingresado", second="", val="")

        else:
            text = cif.cifre_message(text)

            return render_template("cifre.html", first="Texto cifrado", text=text, second="Llaves", val="p = {0} q = {1}".format(cif.p, cif.q))



@app.route("/cte")

def volver_cte():

    return render_template("menu.html")


@app.route('/descifre/')

def show_descifre():
    return render_template("descifre.html")

@app.route('/dt', methods=["POST"])

    
def descifre_text():

    if request.method == "POST":

        text = request.form["text"]
        values = request.form["values"]
        values = values.split()
    
        cif = CifradorRSA()

        try:
            cif.Select(int(values[0]), int(values[1]))
        
        except ValueError:
            return render_template("cifre.html", first="", text="Ambos numeros deben ser primos")
        
        except IndexError:
            return render_template("cifre.html", first="", text="Ningun dato ingresado")

        else:
            text = cif.descifre_message(text)

            return render_template("cifre.html", first="Texto descifrado", text=text)


@app.route("/dte")

def volver_dte():
    return render_template("menu.html")

if __name__ == "__main__":
    app.run(debug=True)

