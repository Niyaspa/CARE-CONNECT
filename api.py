from flask import*
from database import*

api=Blueprint('api',__name__)


@api.route('/login_api')
def login():
    data={}
    username=request.args['uname']
    password=request.args['pwd']

    qry="select * from login where username='%s' and password='%s'"%(username,password)
    res=select(qry)

    if res:
        data['status']="success"
        data['data']=res
    else:
        data['status']= "failed"

    return str(data)

@api.route("/send_com")
def send_com():
    data={}


    com=request.args['com']
    lid=request.args['logid']

    z="insert into complaints values(null,'%s','%s','pending',curdate())"%(lid,com)
    c=insert(z)

    if c:
        data['status']='success'
    else:
        data['status']='failed'
    data['method']='send'
    return str(data)


@api.route('/view_com')
def view_com():
    data={}
    logid=request.args['logid']

    qry="select * from complaints where sender_id='%s'"%(logid)
    res=select(qry)
    if res:
        data['status']="success"
        data['data']=res
    else:
        data['status']="failed"
    data['method']="view"
    return str(data)


@api.route('/view_profile')
def view_profile():
    data={}
    logid=request.args['logid']

    qry="SELECT * FROM survey INNER JOIN  USER USING(survey_id) where login_id='%s'"%(logid)
    print(qry)
    res=select(qry)
    if res:
        data['status']="success"
        data['data']=res
    else:
        data['status']="failed"
    data['method']="view"
    return str(data)



@api.route('/view_donationapi')
def view_donation():
    data={}
    id=request.args['logid']

    qry="SELECT * FROM user_wallet where user_id=(select user_id from user where login_id='%s')"%(id)
    print(qry)
    res=select(qry)
    print(res)
    if res:
        data['status']="success"
        data['data']=res
    else:
        data['status']="failed"
    data['method']="view"
    return str(data)




@api.route('/view_products')
def view_products():
    data={}
    id=request.args['logid']

    qry="SELECT * FROM products"
    print(qry)
    res=select(qry)
    print(res)
    if res:
        data['status']="success"
        data['data']=res
    else:
        data['status']="failed"
    data['method']="view"
    return str(data)

@api.route('/view_orderhistory')
def view_orderhistory():
    data={}
    id=request.args['logid']


    qry="SELECT * FROM order_details"
    print(qry)
    res=select(qry)
    print(res)
    if res:
        data['status']="success"
        data['data']=res
    else:
        data['status']="failed"
    data['method']="view"
    return str(data)


@api.route('/view_product_details')
def view_product_details():
    data={}
    id=request.args['id']


    qry="select * From products where product_id='%s'"%(id)
    print(qry)
    res=select(qry)
    print(res)
    if res:
        data['status']="success"
        data['data']=res
    else:
        data['status']="failed"  
    data['method']="view"
    return str(data)



@api.route('/Registration')
def Registeration():
        data={}

        name=request.args['name']
        place=request.args['place']
        phone=request.args['phone']
        email=request.args['email']
        username=request.args['uname']
        password=request.args['password']


        qry="insert   into login values(null,'%s','%s')"%(username,password)
        qry1="insert into  donation_team values(null,'%s','%s','%s')"
        res=insert(qry)
        print=(res)
        if res:
            data['status']="success"
            
        else:
            data['status']="failed"
        
        return    str(data)


        




        
        
        