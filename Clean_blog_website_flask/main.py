# this is modules
from flask import Flask,render_template,request,session,redirect
from flask_sqlalchemy import SQLAlchemy #for database
from datetime import datetime
import json
import os
import math
from werkzeug.utils import secure_filename
from email.message import EmailMessage
import ssl, smtplib                    # this is for the mail

file = "config.json" # never put json file in any folder it shoud be free  and dont use this mehtod to read a file

with open ("config.json",'r') as c: # write file direct if you dont write then you will face the problem aapki facebook open nhi hogi so please filename yhi likhe
    params = json.load(c)['params']
    # print(params)


local_server = True
# this is app structure
app = Flask(__name__)
app.secret_key= 'super-secret-key'
app.config['UPLOAD_FOLDER'] = params['upload_location']


if local_server:
    app.config['SQLALCHEMY_DATABASE_URI'] = params['local_uri'] #database 
else:
    app.config['SQLALCHEMY_DATABASE_URI'] = params['prod_uri'] #database 

db = SQLAlchemy(app)#database

# this is database class
class Contacts(db.Model):
    '''sno, name, phone_num, msg, date, email'''
    sno = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=False, nullable=False)
    phone_num = db.Column(db.String(12), unique=False, nullable=False)
    msg = db.Column(db.String(150), unique=False, nullable=False)
    date = db.Column(db.String)
    email = db.Column(db.String(50), unique=False, nullable=False)
class Posts(db.Model):
    '''sno, title, slug, content, img_file, date'''
    sno = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50), unique=False, nullable=False)
    tagline = db.Column(db.String(50), unique=False, nullable=False)
    slug = db.Column(db.String(50), unique=False, nullable=False)
    img_file = db.Column(db.String(50), unique=False, nullable=False)
    content = db.Column(db.String(150), unique=False, nullable=False)
    date = db.Column(db.String)

# @app.route('/')
# def hello():
#     return "hello World"

@app.route('/')
def home():
    posts =Posts.query.filter_by().all()
    last = math.ceil(len(posts)/int(params['number_of_posts']))
    page = request.args.get('page')
    if (not str(page).isnumeric()):
        page =1
    page = int(page)
        
    posts = posts[(page-1)*int(params['number_of_posts']):(page-1)*int(params['number_of_posts'])+int(params['number_of_posts'])]
    
    # pagination logic
    #first
    if page==1:
        prev = '#'
        next= "/?page=" + str(page+1)
    #last
    elif page==last:
        prev= "/?page=" + str(page-1)
        next = '#'
    #middle
    else:
        prev= "/?page=" + str(page-1)
        next= "/?page=" + str(page+1)




    # posts =Posts.query.filter_by().all()[0:params['number_of_posts']] #----- yeb phele thi kyuki iski jrurat thi so we have to paste it here now we dont need any type of this parameters
    return render_template('/index.html',params=params,posts=posts,prev=prev,next=next)
@app.route('/about')
def about():
    return render_template('/about.html',params=params)

@app.route('/dashbord', methods=['GET','POST'])
# this is for making the login page info------------------------  This is important for me in future so take care about it dont waste time 
def Dashbord():
    if 'user' in session and session['user'] == params['admin_user']:
        posts = Posts.query.all()
        return render_template('/dashbord.html',params=params,posts=posts)
    if request.method =='POST':
        username = request.form.get('uname')
        userpass = request.form.get('pass')
        if username == params['admin_user'] and userpass == params['admin_password']:
            session['user'] = username
            posts = Posts.query.all()
            return render_template('/dashbord.html',params=params,posts=posts)
    
    return render_template('/login.html',params=params)


# post request start here 
@app.route('/post/<string:post_slug>',methods=['GET'])
def post_route(post_slug):
    post = Posts.query.filter_by(slug=post_slug).first()
    return render_template('/post.html',params=params,post=post)

# contact request start here
@app.route('/edit/<string:sno>',methods=['GET','POST'])
def edit(sno):
    if 'user' in session and session['user'] == params['admin_user']:
        if request.method=='POST':
            box_title = request.form.get('title')
            tagline= request.form.get('tagline')
            slug= request.form.get('slug')
            img_file= request.form.get('image_file')
            content= request.form.get('content')
            date = datetime.now()

            if sno=='0':
                post=Posts(title=box_title, slug=slug, tagline=tagline,content=content,img_file=img_file,date=date)
                db.session.add(post)
                db.session.commit()
                return redirect('/dashbord')
                
            elif sno!='0':

                box_title = request.form.get('title')
                tagline= request.form.get('tagline')
                slug= request.form.get('slug')
                img_file= request.form.get('image_file')
                content= request.form.get('content')
                date = datetime.now()
# updting the posts
                post = Posts.query.filter_by(sno=sno).first()
                post.title = box_title
                post.tagline = tagline
                post.slug = slug
                post.img_file = img_file
                post.content = content
                post.date = date
                db.session.add(post)
                db.session.commit()
                return redirect('/dashbord')
    post = Posts.query.filter_by(sno=sno).first()
    return render_template('/edit.html',params=params,post=post)
@app.route('/delete/<string:sno>')
def delete(sno):
    post = Posts.query.filter_by(sno=sno).first()
    db.session.delete(post)
    db.session.commit()
    # print(allTodo)
    return redirect("/dashbord")

@app.route('/uploader', methods=['GET','POST'])
def uploader():
    if 'user' in session and session['user'] == params['admin_user']:
        if(request.method=='POST'):
            f = request.files['file1']
            f.save(os.path.join(os.path.abspath(os.path.dirname(__file__)),app.config['UPLOAD_FOLDER'],secure_filename(f.filename)))#its really took my time so be respect of yourr time
            return "susscessful"

@app.route('/logout')
def logout():
    session.pop('user')
    return redirect('/dashbord')
    



@app.route('/contact',methods=['GET','POST'])
def contact():
    if(request.method=='POST'):
        name=request.form.get('name')
        phone=request.form.get('phone')
        email=request.form.get('email')
        message=request.form.get('message')

        entry=Contacts(name=name, phone_num=phone,date=datetime.now(), email=email, msg=message)
        db.session.add(entry)
        db.session.commit()
# ---------------------------------------------------------------mail startup very hard
        email_sender = params['gmail_user']
        email_password = params['gmail_password']
        email_reciver= 'dajek48046@webonoid.com'

        subject = email+" / "+ phone

        body ="client name is "+name+'\n'+ message

        em = EmailMessage()

        em['From'] = email_sender
        em['To'] = email_reciver
        em['Subject']= subject

        em.set_content(body)

        context= ssl.create_default_context()

        with smtplib.SMTP_SSL('smtp.gmail.com', 465 , context=context) as smtp:
            smtp.login(email_sender, email_password)
            smtp.sendmail(email_sender,email_reciver, em.as_string())   
    return render_template('/contact.html',params=params)





if __name__ == "__main__":
    app.run(debug=True )                                                    
