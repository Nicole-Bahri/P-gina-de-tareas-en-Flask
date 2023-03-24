from flask import Flask, render_template,request,redirect
app= Flask(__name__)
tareas1=[]
#ruta
@app.route("/")
#vista
def index():
    return  render_template('index.html', tareas=tareas1)
@app.route('/agregar',methods=['GET','POST'])
def agregar():
    if request.method=='POST':
      nueva_tarea=request.form.get('tarea')
      tareas1.append(nueva_tarea) 
    return redirect('/') 
@app.route('/done/<int:id>')
def done(id):
    tareas1.pop(id)
    return redirect('/')
if __name__ == "main" :
    app.run(debug=True)