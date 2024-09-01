import setup,asyncio,sqlite3,time,re,yaml
from threading import Thread as th

with open('app.yml', encoding="utf-8") as file:
    app_setting = yaml.safe_load(file)
print(setup.file)
def oksusiki(x):
    return bool(re.match(r'^(?!.*\*\*\d{3,})[0-9+\-*/%()]+$',x))
def kesan(x):
    if oksusiki(x):
        return eval(x)
    else:
        raise ValueError("正しい数式を入力してください")
def sql(x,y=()):
    conn = sqlite3.connect(setup.file)
    cur=conn.cursor()
    cur.execute(x,y)
    anan=cur.fetchall()
    conn.commit()
    conn.close()
    return anan
def chatget(id_):
    id_
def adduser(name,password,position):
    sql("INSERT INTO user(name,password,position,isDelete) VALUES(?,?,?,'False');",(name,password,["student","teacher"][int(position)],))
def isuser(name,password):
    aaa=[list(i) for i in sql("SELECT name, password, isDelete, position FROM user;")]
    if name in [i[0] for i in aaa]:
        return aaa[0][1]==password and not aaa[0][2]=="True",aaa[0][3]
    else:
        return False,None
def deleteuser(ids):
    sql("UPDATE user SET isDelete='True' WHERE id=?;",(ids,))
def getuser():
    return [list(i) for i in sql("SELECT id, name, position FROM user WHERE isDelete ='False';")]

#while True:
#    print(kesan(input(">>")))
