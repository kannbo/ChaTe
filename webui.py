from flask import *
import kyoiku as ki,time,setup

v="0.01"
update=False

app = Flask(__name__)
app.secret_key = "v54fsaf5a4s5c421sa5ds4af5safdsa5avfsbjhbuhuwtujkl餡db"

ki.app_setting


@app.route("/login.action",methods=["post"])
def retur():
    print(request.method)
    if request.method=="POST":
        print("helo")
        ref=dict(request.form)
        if ki.isuser(ref["username"],ref["password"])[0]:
            session["username"]=ref["username"]
            session["password"]=ref["password"]
            print(session)
            return redirect("/")
    return "ログインが失敗しました。 - action"


@app.route("/")
def homepage():
    if not session:
        session["username"]=""
        session["password"]=""
    return render_template("Login.html",website=ki.app_setting["app-name"],title="ログイン")
@app.route("/logoutt",methods=["post"])
def logoutpage():
    if request.method=="post":
        session["username"]=""
        session["password"]=""
    flash("ログアウトしました")
    return render_template("Login.html",website=ki.app_setting["app-name"],title="ログアウト")
@app.route("/logout",methods=["get"])
def logout():
    if not session:
        session["username"]=""
        session["password"]=""
    return render_template("Login.html",website=ki.app_setting["app-name"],title="ログアウト2")
@app.route("/admin-<page>")
def admin(page):
    print(session)
    print(ki.isuser(dict(session)["username"],dict(session)["password"]))
    if ki.app_setting["admin"] and page==ki.app_setting["admin-pageid"] and ki.isuser(dict(session)["username"],dict(session)["password"])[0] and ki.isuser(dict(session)["username"],dict(session)["password"])[1]=="teacher":
        return render_template("admin.html",users=ki.getuser(),v=v,db=setup.file)
    else:
        return None,404
@app.errorhandler(500)
def error500(e):
    with open("Error.log","a") as f:
        dsa="\n"
        f.write(f"{dsa}[{time.time()}]{e}")
    return render_template("Login.html",website=ki.app_setting["app-name"],title="fdwyagfyudyuaguy",error="不明なエラーの")
@app.errorhandler(404)
def error404(e):
    return render_template("Login.html",website=ki.app_setting["app-name"],title="fdwyagfyudyuaguy",error="存在しないページへの")


app.run(port=str(ki.app_setting["port"]))
