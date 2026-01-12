import uuid
from flask import *
from database import *

admin=Blueprint('admin',__name__)

@admin.route('/adminhome')
def adminhome():
    return render_template('adminhome.html')

@admin.route('/manage_surevy_team',methods=['get','post']) 
def managesuvery():
   data={}
   q="SELECT * FROM `survey_team`"
   res=select(q)
   data['donation_tm']=res

   if 'action' in request.args:
         action=request.args['action']
         id=request.args['id']
   else:
      action=None

   if action=='update':
      qry1="select * from survey_team  where survey_team_id='%s'"%(id)
      data['up']=select(qry1)

      if 'update' in request.form:
         name=request.form['name']
         pnum=request.form['pnum']
         email=request.form['email']
         place=request.form['place']
         u="update survey_team set name='%s',phone='%s',email='%s',place='%s' where survey_team_id='%s'"%(name,pnum,email,place,id)
         update(u)
         return '''<script>alert("updated");window.location='/manage_surevy_team'</script>'''
      
   if action=="delete":
      ww="delete from survey_team where survey_team_id='%s'"%(id)
      delete(ww)
      return '''<script>alert("deleted");window.location='/manage_surevy_team'</script>'''
   


  
  
   if 'submit' in request.form:

    name = request.form['name']
    ph = request.form['pnum']
    email = request.form['email']
    place = request.form['place']
    uname = request.form['uname']
    psw = request.form['password']

    qry1 = "insert into login values(NULL,'%s','%s','surveyteam')"%(uname,psw)
    id = insert(qry1)
    qry = "insert into survey_team values(NULL,'%s','%s','%s','%s','%s')"%(id,name,ph,email,place)
    insert(qry)

    return redirect(url_for('admin.managesuvery'))

   return render_template('admin_manage_Survey_Team.html',data=data)
  
@admin.route("/verify_donation",methods=['get','post'])
def verify_donation():
    data={}
    q="SELECT * FROM `donation_team`"
    res=select(q)
    data['donation_tm']=res


   
    return render_template("verify_donation.html",data=data)


@admin.route("/view_survey",methods=['get','post'])
def view_survey():
   
   data={}
   qry="SELECT * FROM survey INNER JOIN  survey_team USING(survey_team_id)"
   res=select(qry)
   data['survey']=res

   return render_template("view_survey.html",data=data)


@admin.route("/view_donation",methods=['get','post'])
def view_donation():
   
   data={}
   qry="SELECT * FROM donation_wallet"
   res=select(qry)
   data['donation_wallet']=res
   return render_template("view_donation_wallet.html",data=data)
   

@admin.route("/manage_products",methods=['get','post'])
def manage_products():

      data={}
      qry="SELECT * FROM `products`"
      res=select(qry)
      data['products']=res

      if 'action' in request.args:
         action=request.args['action']
         id=request.args['id']
      else:
         action=None

      if action=='update':
         qry1="select * from products where product_id='%s'"%(id)
         data['up']=select(qry)

      if 'update' in request.form:
         product_name=request.form['pname']
         image=request.files['image']
         price=request.form['price']
         stock=request.form['stock']

         path="static/" + str(uuid.uuid4()) + image.filename
         image.save(path)

         u="update products set product_name='%s',image='%s',price='%s',stock='%s' where product_id='%s'"%(product_name,path,price,stock,id)
         update(u)
         return '''<script>alert("updated");window.location='/manage_products'</script>'''
      
      if action=="delete":
         ww="delete from products where product_id='%s'"%(id)
         delete(ww)
         return '''<script>alert("deleted");window.location='/manage_products'</script>'''


      if "submit" in request.form:
         product_name=request.form['pname']
         image=request.files['image']
         price=request.form['price']
         stock=request.form['stock']

         path="static/" + str(uuid.uuid4()) + image.filename
         image.save(path)

         qry1="insert into products values(NULL,'%s','%s','%s','%s')"%(product_name,path,price,stock)
         insert(qry1)
      return render_template("admin_manage_products.html",data=data)


       
@admin.route("/view_order",methods=['get','post'])
def view_order():
   
   data={}
   qry="SELECT * FROM order_details INNER JOIN order_master USING(`omaster_id`)"
   res=select(qry)
   data['order_details']=res
   return render_template("view_order_details.html",data=data)

@admin.route("/view_compliant",methods=['get','post'])
def view_compliant():
   
   data={}
   qry="SELECT * FROM complaints"
   res=select(qry)
   data['complaints']=res
   return render_template("view_complaints.html",data=data)
   