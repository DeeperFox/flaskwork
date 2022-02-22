from flask import *
import pymysql
from login_limit import login_limit
import os
import time
app = Flask(__name__)
app.config["SECRET_KEY"] = 'TPmi4aLWRbyVq8zu9v82dWYW1'
app.secret_key = 'abc123'
from werkzeug.utils import secure_filename

# 主页
@app.route('/')
def mainpage():
    return render_template('mainpage.html')


# 登录
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    if request.method == 'POST':
        accountname = request.form.get('accountname')
        password = request.form.get('password')
        db = pymysql.connect(host='localhost', user='root', password='js1110923', database='takeaway platform')
        cursor = db.cursor()
        cursor.execute("select password,type from member where accountname = '%s'" % accountname)
        result = cursor.fetchone()
        if result[0] == password:
            print("登陆成功")
            session['accountname'] = accountname
            session['type'] = result[1]
            session.permanent = True
            cursor.close()
            print(result[1])
            if result[1] == '0':
                return render_template('UserCenter.html')
            elif result[1] == '1':
                return render_template('UserCenter2.html')
            elif result[1] == '2':
                return render_template('UserCenter3.html')


# 登录状态保持
@app.context_processor
def login_status():
    # 从session中获取
    accountname = session.get('accountname')
    type = session.get('type')
    if type == '0':
        type = '用户'
    elif type == '1':
        type = '商家'
    elif type == '2':
        type = '骑手'

    if accountname:
        try:
            db = pymysql.connect(host='localhost', user='root', password='js1110923', database='takeaway platform')
            cursor = db.cursor()
            cursor.execute("select accountname,type,password from member where accountname = '%s'" % accountname)
            result = cursor.fetchone()
            if result:
                return {'accountname': accountname, 'password': result[2], 'type': type}
        except Exception as e:
            raise e
    # 如果信息不存在，则未登录，返回空
    return {}


# 用户注销
@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for(('mainpage')))


# 注册
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'GET':
        return render_template('register.html')
    if request.method == 'POST':
        accountname = request.form.get('accountname')
        password = request.form.get('password')
        password2 = request.form.get('password2')
        type = request.form.get('type')
        if password != password2:
            return render_template('error.html')
        else:
            db = pymysql.connect(host='localhost', user='root', password='js1110923', database='takeaway platform')
            cursor = db.cursor()
            cursor.execute("insert into member(accountname,password,type) values(%s,%s,%s)",
                           [accountname, password, type])
            db.commit()
            print('注册成功', type)
            return render_template('suc1.html')


# 修改密码
@app.route('/user/changePW', methods=['GET', 'POST'])
def change1():
    if request.method == 'GET':
        return render_template('changepw.html')
    if request.method == 'POST':
        newpassword = request.form.get('password')
        newpassword2 = request.form.get('password2')
        accountname = session.get('accountname')
        if newpassword != newpassword2:
            return render_template('error.html')
        else:
            db = pymysql.connect(host='localhost', user='root', password='js1110923', database='takeaway platform')
            cursor = db.cursor()
            cursor.execute("update member set password = '%s' where accountname = '%s'" % (newpassword, accountname))
            db.commit()
            return render_template('UserCenter.html')

#修改店铺信息
@app.route('/shop/changeshop', methods=['GET','POST'])
def changeshop():
    if request.method=='GET':
        return render_template('change_shop.html')
    if request.method=='POST':
        accountname=session.get('accountname')
        shopname = request.form.get('shopname')
        describtion = request.form.get('describtion')
        type = request.form.get('type')
        f = request.files['file']
        basepath = os.path.dirname(__file__)
        upload_path = os.path.join(basepath, 'static\img', secure_filename(f.filename))
        path = os.path.join('\static\img', secure_filename(f.filename))
        f.save(upload_path)
        db = pymysql.connect(host='localhost', user='root', password='js1110923', database='takeaway platform')
        cursor = db.cursor()
        cursor.execute("insert into shop(shop_name,type,describtion,accountname,img) values(%s,%s,%s,%s,%s)",[shopname,type,describtion,accountname,path])
        db.commit()
        print('编辑成功', type)
        return render_template('UserCenter2.html')

#店铺详情
@app.route('/shop/detail/<id>', methods=['GET','POST'])
def shop_detail(id):
    if request.method=='GET':
        type = session.get('type')
        db = pymysql.connect(host='localhost', user='root', password='js1110923', database='takeaway platform')
        cursor = db.cursor()
        cursor.execute("select shop_name,type,describtion,accountname,img from shop where accountname = '%s'" % id)
        form = cursor.fetchone()
        cursor.execute("select name,price,describtion,img from issue where accountname = '%s'" % id)
        form1=cursor.fetchall()
        cursor.close()
        print(form1)
        return render_template('shop.html',form=form,form1=form1,type=type)



#上传菜品
@app.route('/shop/detail/uplord', methods=['GET','POST'])
def uplord():
    if request.method == 'GET':
       return render_template('shopuplord.html')
    if request.method=='POST':
        accountname=session.get('accountname')
        name=request.form.get('name')
        price = request.form.get('price')
        describtion = request.form.get('describtion')
        f = request.files['file']
        basepath = os.path.dirname(__file__)
        upload_path = os.path.join(basepath, 'static\img', secure_filename(f.filename))
        path=os.path.join('\static\img', secure_filename(f.filename))
        f.save(upload_path)   #上传图片
        db = pymysql.connect(host='localhost', user='root', password='js1110923', database='takeaway platform')
        cursor = db.cursor()
        cursor.execute("insert into issue(name,price,describtion,img,accountname) values(%s,%s,%s,%s,%s)",[name,price,describtion,path,accountname])
        db.commit()
        return redirect(url_for(('usercenter')))


#个人中心
@app.route('/usercenter')
def usercenter():
    type=session.get('type')
    if type=='0':
        return render_template('UserCenter.html')
    elif type=='1':
        return render_template('UserCenter2.html')
    elif type=='2':
        return render_template('UserCenter3.html')
#接单页面
@app.route('/rider/oder_receiving', methods=['GET'])
def oder_receiving():
        db = pymysql.connect(host='localhost', user='root', password='js1110923', database='takeaway platform')
        cursor = db.cursor()
        cursor.execute("select 下单时间,下单人,住址,订单店铺,订单内容,id from order_receiving where 订单状态='0'")
        form = cursor.fetchall()
        return render_template('oder_receiving.html',form=form)



#我的订单
@app.route('/user/show_order')
def show_oder():
    accountname=session.get('accountname')
    db = pymysql.connect(host='localhost', user='root', password='js1110923', database='takeaway platform')
    cursor = db.cursor()
    cursor.execute("select 下单时间,下单人,住址,订单店铺,订单内容,订单状态,接单时间,送达时间,骑手 from order_receiving where 下单人='%s'" % accountname)
    form = cursor.fetchall()
    return render_template('show_order.html', form=form)


# 点餐
@app.route('/user/order', methods=['GET', 'POST'])
def order():
    if request.method=='GET':
        db = pymysql.connect(host='localhost', user='root', password='js1110923', database='takeaway platform')
        cursor = db.cursor()
        cursor.execute("select * from shop")
        form = cursor.fetchall()
        return render_template('oder.html',form=form)
    if request.method=='POST':     #点餐没搞好
        # db = pymysql.connect(host='localhost', user='root', password='js1110923', database='takeaway platform')
        # cursor = db.cursor()
        # cursor.execute("insert into oder receiving(下单时间,下单人,住址,订单店铺,订单内容) values(%s,%s,%s,%s,%s)",[x,x,x,x,x])

        return redirect(url_for(('usercenter')))


#接单
@app.route('/rider/oder_receiving/<id>')
def take_oder(id):
    accountname=session.get('accountname')
    print(accountname)
    time1=time.strftime('%Y/%m/%d %H:%M',time.localtime())
    db = pymysql.connect(host='localhost', user='root', password='js1110923', database='takeaway platform')
    cursor = db.cursor()
    cursor.execute("update order_receiving set 订单状态 ='%s',接单时间='%s',送达时间='%s',骑手='%s' where id='%s'"%(1,time1,time1,accountname,id))#送达时间不会搞
    db.commit()
    print('接单成功')
    return redirect(url_for(('my_taking')))


#我接的单
@app.route('/rider/oder_receiving/my_taking')
def my_taking():
    accountname = session.get('accountname')
    db = pymysql.connect(host='localhost', user='root', password='js1110923', database='takeaway platform')
    cursor = db.cursor()
    cursor.execute("select 下单时间,下单人,住址,订单店铺,订单内容,订单状态,接单时间,送达时间,骑手 from order_receiving where 骑手='%s'" % accountname)
    form = cursor.fetchall()
    return render_template('my_receiving.html', form=form)


if __name__ == '__main__':
    app.run()
