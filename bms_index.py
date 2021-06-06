import pymysql

from flask import Flask,render_template,request
#request inbuilt module of python,
#to access value from html control to python 
#render_template inbuilt class

app=Flask(__name__)

@app.route('/')
def hello():
    #return render_template("index.html")#render_template("Html name")
    return '''
                <div style="background-color: #40E0D0;
			height: 800px;">
                    <center>
                        <h1 align="center" style="color:darkorange;"><strong>Welcome to Bank Management System</strong></h1>

                        <a href="/signUp">Sign Up</a><br>
                        <a href="/signIn">Sign In</a>
	</center>

                </div>'''
                                

@app.route('/signUp')
def add_signUp():
    return render_template('signup.html')#render_template("Html name")

@app.route('/register',methods=['POST','GET'])
def save_record():
    if request.method=='POST':
        try:
            acct_nm=request.form["fname"]
            ph_no=request.form["p_no"]
            address=request.form["add"]
            acct_no=request.form["acct_num"]
            acct_pin=request.form["acct_p"]
            bal_amt=request.form["bal"]
            email_id=request.form["e_id"]
            user_nm=request.form["uname"]
            user_pw=request.form["pwd"]
            #create conn
            con=pymysql.connect(host="localhost",user='root',password='',database='bankserver')
            cur = con.cursor()
            cur.execute("insert into acct_holder_details values (%s,%s,%s,%s,%s,%s,%s,%s,%s)",(acct_nm,ph_no,address,acct_no,acct_pin,bal_amt,email_id,user_nm,user_pw))
            con.commit()#save record permanelty into table
            msg="Record successfully Added"
        except:
            msg="Record unsuccessfully Added"
        finally:
            con.close()
            return render_template('my_success.html',smsg=msg)

@app.route('/signIn')
def add_signIn():
    return render_template('signin.html')#render_template("Html name")

@app.route('/login',methods=['POST','GET'])
def validation():
    if request.method=='POST':
        try:
            user_nm=request.form["uname"]
            user_pw=request.form["pwd"]
            #conn
            conn=pymysql.connect(host="localhost",user='root',password='',database='bankserver')
            cur=conn.cursor()
            cur.execute("select * from acct_holder_details where username=%s and password=%s",(user_nm,user_pw))
            result=cur.fetchall()#fetching all data into tuple
            
        except:
            msg="error"
            return render_template('error.html',msg=msg)
        finally:
            conn.close()
            return render_template('my_display.html',dresult=result)

@app.route('/delete')
def del_data():
    return render_template('delete.html')

@app.route('/delete1',methods=['POST','GET'])
def delete_record1():
    msg=" "
    if request.method=='POST' :
        try:
            uname=request.form["uname"]
            #create connection
            con= pymysql.connect(host="localhost", user='root',password='',database='bankserver')   
            cur = con.cursor()
            cur.execute("delete from acct_holder_details where username=%s",(uname))
            con.commit()  #delete record permanently into table
            res=cur.fetchall()#fetching all data into tuple
            msg = "Customer Record successfully Deleted"  
        except:  
            msg = "We can not delete the customer data into table"
            return render_template("error.html",smsg=msg)
        finally:
            con.close()
            return render_template("my_display_all.html")

@app.route('/view_all')
def displayall():
     #create connection
    try:
            con= pymysql.connect(host="localhost", user='root',password='',database='bankserver')   
            cur = con.cursor()
            cur.execute("Select * from acct_holder_details")
            result=cur.fetchall() #create tuple of result which hold the all records from table
            con.close()
            return render_template('display1.html',result=result)
    except:
        msg="error"
        return render_template("error.html",smsg=msg)

@app.route('/update')
def update_data():
    return render_template('update.html')

@app.route('/update1',methods=['POST','GET'])
def update_record():
    msg=" "
    if request.method=='POST' :
        try:
            uname=request.form["uname"]
            pwd=request.form["pwd"]
            #create connection
            con= pymysql.connect(host="localhost", user='root',password='',database='bankserver')   
            cur = con.cursor()
            cur.execute("select * from acct_holder_details where username=%s and password=%s",( uname,pwd))
            res=cur.fetchall()#fetching all data into tuple
            msg = "Now,You are able to alter the data"  
        except:  
            msg = "Something going wrong"
            return render_template("error.html",smsg=msg)
        finally:
            con.close()
            return render_template("show_All.html",dresult=res)

@app.route('/update2',methods=['POST','GET'])
def update_table():
    msg=" "
    if request.method=='POST' :
        try:
            ac_no=request.form["ano"]
            cfield1=request.form["get_field1"]
            cdata1=request.form["set_data1"]
            #cfield2=request.form["get_field2"]
            #cdata2=request.form["set_data2"]
            #create connection
            con= pymysql.connect(host="localhost", user='root',password='',database='bankserver')   
            cur = con.cursor()
            cur.execute("UPDATE acct_holder_details SET password=%s WHERE acct_no=%s",(cdata1,ac_no))
            con.commit()  #update record permanently into table
            cur.execute("select * from acct_holder_details")
            res=cur.fetchall()#fetching all data into tuple
            msg = "Data updated"  
        except:  
            msg = "Something going wrong"
            return render_template("error.html",smsg=msg)
        finally:
            con.close()
            return render_template('show_All1.html',dresult=res)


#main program
app.run(debug=True)
