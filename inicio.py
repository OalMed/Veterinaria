from flask import Flask, render_template, request, redirect, url_for, flash
import pymysql
import math

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/index')
def inicio():
    return render_template('index.html')

@app.route('/area')
def areaT():
    return render_template('areaTriang.html')

@app.route('/temperatura')
def grados():
    return render_template('temperatura.html')

@app.route('/calificaciones')
def calif():
    return render_template('calificaciones.html')

@app.route('/viaje')
def viaje():
    return render_template('viaje.html')

@app.route('/tabla')
def tabla():
    return render_template('tablaMult.html')


@app.route('/areaT', methods=['POST'])
def calcArea():
    if request.method == 'POST':
        ba = float(request.form['base'])
        alt = float(request.form['altura'])
        area = (ba * alt)/2
        mensaje = f"El área del triángulo es: {area}"
    return render_template ('areaTriang.html', msj = mensaje, b = ba, h = alt)

@app.route('/grados', methods=['POST'])
def calcGrados():
    if request.method == 'POST':
        fah = float(request.form['faren'])
        cent = (fah - 32) * (5/9)
        mensaje = f"El equivalente de {fah}° Fahrenheit a centígrados es {cent}° Celsius."
    return render_template('temperatura.html', f = fah, msj = mensaje)
        
@app.route('/calificacion', methods=['POST'])
def calificar():
    if request.method == 'POST':
        note = int(request.form['calif'])
        mensaje = ""

        if note == 10:
                mensaje = "¡EXCELENTE!"

        elif note == 9 or note == 8:
            mensaje = "NOTABLE"

        elif note == 7:
            mensaje = "REGULAR"

        elif note == 6:
            mensaje = "SUFICIENTE"

        elif note >= 0 and note <= 5:
            mensaje = "REPROBADO"

        else:
            mensaje = "SOLO INTRODUCIR NÚMEROS ENTEROS DE 0 A 10."
        
        return render_template('calificaciones.html', nt = note, nota = mensaje)
    
@app.route('/costo', methods=['POST'])
def viaj():
    if request.method == 'POST':
        alum = int(request.form['alumnos'])
        costo = 0
        pago_alum = 0

        if alum < 30:
            costo = 3500
            pago_alum = costo / alum
        
        elif alum < 50:
            pago_alum = 95
            costo = pago_alum * alum

        elif alum < 100:
            pago_alum = 70
            costo = pago_alum * alum

        mensaje = f"El costo del viaje es ${costo}, y el pago por alumno es ${pago_alum}"

        return render_template('viaje.html', al = alum, msj = mensaje)
    
@app.route('/tabla', methods=['POST'])
def multi():
    if request.method == 'POST':
        num = int(request.form['num'])
        table = []
        for i in range(11):
            table.append(f"{num} x {i} = {num*i}")

        mensaje = f"Tabla del {num}:"
    
        return render_template('tablaMult.html', tab = table, n = num, msj = mensaje)



if __name__ == "__main__" :
    app.run(debug=True)