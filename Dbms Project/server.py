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
    re.comm()
    sample = False
    clear = False
    error = None
    if 'username' in session:
        return render_template("choice.html",uname='username')

    if request.method == 'POST':
        email = request.form['mail']
        password = request.form['pass']
        sample = check.login(email, password)
        if sample == True:
            uid = re.get_id(email)
            if uid  == 1:
                return redirect(url_for("admin"))
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
    re.comm()
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
            re.comm()
            return render_template("choice.html", uname=name)
        else:
            error = "Email already exist!please enter new email"
            return render_template("signin.html", error=error)


@app.route('/logout')
def logout():
    session.pop('username', None)
    re.comm()
    return redirect(url_for('index'))


@app.route("/courses", methods=['GET', 'POST'])
def courses():
    re.comm()
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
    re.comm()
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

@app.route("/admin",methods=['GET', 'POST'])
def admin():
    return render_template("admin.html")

@app.route("/addcourses",methods=['GET', 'POST'])
def addcourses():
    if request.method == 'POST':
        cname = request.form['cname']
        cdur = request.form['cdur']
        err = inn.insert_courses(cname,cdur)
        if err==None:
            return render_template("admin.html")
        else:
            return render_template("addcourses.html" , error=err)
    return render_template("addcourses.html")

@app.route("/addtopics",methods=['GET', 'POST'])
def addtopics():
    if request.method == 'POST':
        cname = request.form['cname']
        tname = request.form['tname']
        tdur = request.form['tdur']
        err = inn.topics(cname,tname,tdur)
        if err==None:
            return render_template("admin.html")
        else:
            return render_template("addtopics.html" , error=err)
    return render_template("addtopics.html")

@app.route("/addcoll",methods=['GET', 'POST'])
def addcoll():
    if request.method == 'POST':
        tname = request.form['tname']
        coname = request.form['coname']
        cotype = request.form['cotype']
        err = inn.collection(tname,coname,cotype)
        if err==None:
            return render_template("admin.html")
        else:
            return render_template("addcoll.html" , error=err)
    return render_template("addcoll.html")

@app.route("/addquestions",methods=['GET', 'POST'])
def addquest():
    if request.method == 'POST':
        cname = request.form['cname']
        qname = request.form['qname']
        ans = request.form['ans']
        options = request.form['option']
        err = inn.quest(cname,qname,ans,options)
        if err==None:
            return render_template("admin.html")
        else:
            return render_template("addquest.html" , error=err)
    return render_template("addquest.html")

if __name__ == "__main__":
    app.jinja_env.auto_reload = True
    app.config['TEMPLATES_AUTO_RELOAD'] = True
    app.run(debug = True)
