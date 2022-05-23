from flask import Flask, redirect, url_for, render_template

app = Flask(__name__) #name is keyword and u allocate the main function to __name__ cuz python has no main func

@app.route("/")
def home():
  return render_template("index.html")
  #HTML5 no need for dash in headings

@app.route("/injurychart/feet.html")
def feet():
  return render_template("injury/injurychart/feet.html")
  #HTML5 no need for dash in headings

@app.route("/<name>") #<name> acts as a placeholder for any name
def user(name):
  #return f"Hello {name}"
  #if u want to go to homepage and display name,
  return render_template("index.html", content = name, r = 44)

@app.route("/admin")
def admin():
  return redirect(url_for("home"))
  #"home" == "/"
  #redirects to a certain url if a user stumbles across this site

if __name__ == "__main__":
  app.run()