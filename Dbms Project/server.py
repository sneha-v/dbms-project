import mysql.connector as con
from flask import Flask , render_template, request, redirect, url_for, session
import check_credential
import insert
import retriever

check = check_credential.credential()
inn = insert.insert()
re = retriever.retrieve()


app = Flask("__name__")
app.secret_key = "learn as if you are gonna teach others"
@app.route("/")
def index():
    if 'username' in session:
        return render_template("choice.html",uname='username')
    return render_template("home.html")

@app.route("/login", methods=['GET', 'POST'])
def login():
    sample = False
    clear = False
    error = None
    if 'username' in session:
        return render_template("choice.html",uname='username')

    if request.method == 'POST':
        email = request.form['mail']
        password = request.form['pass']
        sample = check.login(email, password)
        clear = True
    if clear == False:
        return render_template("login.html", error = error)
    else:
        if sample == True:
            na = re.get_name(email)
            session['username'] = email
            return render_template("choice.html",uname = na)
        else:
            error = 'Invalid Credentials. Please try again.'
            return render_template("login.html", error = error)


@app.route("/signin", methods=['GET', 'POST'])
def signin():
    sample = False
    clear = False
    error = None
    if 'username' in session:
        return render_template('choice.html', uname = 'username')
    if request.method == 'POST':
        name = request.form['uname']
        phone = request.form["uphone"]
        email = request.form['umail']
        password = request.form['upass']
        if len(name)==0 or len(phone)==0 or len(email)==0 or len(password)==0:
            error="please enter the correct values"
            return render_template("signin.html",error=error)
        sample = check.signin(email)
        clear = True
    if not clear:
        return render_template("signin.html", error= error)
    else:
        if sample == False:
            session['username'] = email
            inn.insert_user(name,password,phone,email)
            return render_template("choice.html", uname=name)
        else:
            error = "Email already exist!please enter new email"
            return render_template("signin.html", error=error)


@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('index'))


@app.route("/courses", methods=['GET', 'POST'])
def courses():
    ch = False
    course = re.get_cour()
    topic = re.top_disp()
    cids = re.get_cidli()
    uid = re.get_id(session['username'])
    for i in cids:
        che = re.check_enroll(i,uid)
        if che == True:
            cid = i
            ch = True
            break
    if ch == True:
        cname = re.get_cname(cid)
        top = re.topic_cou(cname)
        col = re.col_cou(cname)
        return render_template("course.html", topic=top , coll = col , cname = cname)
    else:
        return render_template("courses.html",course=course, topic=topic)

@app.route("/courses/<cname>" ,methods =['GET','POST'])
def cou_name(cname):
    #clear = False
    cid , uid = re.enroll(cname,session['username'])
    check = re.check_enroll(cid,uid)
    if check == False:
        inn.enroll_user(cid,uid)

    top = re.topic_cou(cname)
    col = re.col_cou(cname)
    return render_template("course.html", topic=top , coll = col,cname = cname)

@app.route("/test/<cname>" ,methods =['GET','POST'])
def take_test(cname):
    testli = re.test_sheet(cname)
    return render_template("test.html",test = testli, cname = cname)

@app.route("/test/<cname>/answers" ,methods =['GET','POST'])
def take_answers(cname):
    testli = re.test_sheet(cname)
    username = re.get_name(session['username'])
    return render_template("testans.html",test = testli, uname =username ,cname=cname)



@app.route("/profile/<cname>/<username>")
def profile(cname, username):
    cid , uid = re.enroll(cname,session['username'])
    inn.insert_profile(cid,uid)
    re.delete_enroll(cid,uid)
    prof_li=re.prof_list(uid)
    cou_c = re.cou_count(prof_li)
    rem, cou = re.remove_dup(cou_c)
    username = re.get_name(session['username'])
    return render_template("profile.html", name = username, li=rem, cou_li=cou, total=sum(cou))

@app.route("/profile/<username>")
def profile_ach(username):
    uid = re.get_id(session['username'])
    prof_li=re.prof_list(uid)
    cou_c = re.cou_count(prof_li)
    rem,cou = re.remove_dup(cou_c)
    username = re.get_name(session['username'])
    return render_template("profile.html", name = username, li=rem, cou_li=cou,total=sum(cou))

if __name__ == "__main__":
    app.jinja_env.auto_reload = True
    app.config['TEMPLATES_AUTO_RELOAD'] = True
    app.run(debug = True)
