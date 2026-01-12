from flask import *

from database import *
public=Blueprint('public',__name__)


@public.route('/')
def home():
    return render_template('home.html')

@public.route('/login',methods=['post','get'])
def login():

    if 'sum' in request.form:

        usname=request.form['usname']
        psw=request.form['psw']

        a="select * from login where username='%s' and password='%s'"%(usname,psw)
        res=select(a)
        print(res,"///////////////////////")

        if res:
            if res[0]['usertype']=='admin':
                return redirect(url_for("admin.adminhome"))
            
    return render_template('login.html')

@public.route('/registration',methods=['post','get'])
def registration():
    if 'sum' in request.form:
        name = request.form['fname']
        place= request.form['place']
        phone = request.form['pnum']
        email = request.form['email']
        username = request.form['uname']
        password = request.form['pass']

        qry1 = "insert into login values(NULL,'%s','%s','donation_team')"%(username,password)
        id=insert(qry1)
        qry2= "insert into donation_team values(NULL,'%s','%s','%s','%s','%s')"%(id,name,place,phone,email)
        insert(qry2)
        
    return render_template('registration.html')
