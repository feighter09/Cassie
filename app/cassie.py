from app import app

@app.route("/")
def hello():
  return "Hello World!"

@app.route("/cassie")
def cassie():
  return "Hi EHHHRMMM CASSEHHHHHH"