import glob,sqlite3


file=glob.glob('*.db')[0]

def sql(x,y=()):
    conn = sqlite3.connect(file)
    conn.cursor().execute(x,y)
    conn.commit()
    conn.close()

if __name__=="__main__":
    sizentesu=True
    while sizentesu:
        rarara=input(">>DBのデータのセットアップを行う(y/n)")
        if rarara=="y":
            sizentesu=False
            print(file+"と言うファイルで実行します")
            if input("間違っている場合表示のファイルを削除してください.\n変更の場合は(y)を入力してください。")=="y":
                input("セットアップを終了します")
                exit()
            try:
                sql("CREATE TABLE user(id INTEGER PRIMARY KEY AUTOINCREMENT,name STRING,password STRING,position STRING,isDelete STRING)")
                sql("CREATE TABLE chatRoom(id INTEGER PRIMARY KEY AUTOINCREMENT,day STRING,name STRING,isDelete STRING)")
                sql("CREATE TABLE chat(id INTEGER PRIMARY KEY AUTOINCREMENT,userid STRING,roomid STRING,text STRING)")
                print("実行しました")
                pass
            except Exception as e:
                input(f"""セットアップが実行されていた可能性があります
{e}""")
        elif rarara=="n":
            input("セットアップを終了します")
            exit()
