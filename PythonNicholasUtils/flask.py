from flask import Flask, render_template
class app():
  def _init_(self):
    self.app = Flask(__name__)
def create_app():
  a = app()
  return a

def page(p, g, a):
  app = a.app
  @app.route(p)
  def page():
    return render_template(g)

def start_app(a):
  app.run(host='0.0.0.0', port=8080)