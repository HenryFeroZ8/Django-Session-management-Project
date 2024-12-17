from django.shortcuts import render,redirect
import mysql.connector as sql

# Create your views here.
def login(request):
            try:
                autologemail = request.session['email']
                autologpassword = request.session['password']
                print(autologemail,autologpassword)
                
                con = sql.connect(host="localhost",user="root",password="",database="student_django")
                cursor = con.cursor(dictionary=True)
                query = "select * from session where email ='{}' And password = '{}'".format(autologemail,autologpassword)
                cursor.execute(query)
                result = cursor.fetchone()
                print(result)
                con.commit()
                if result != None:
                    return redirect("/edit/"+str(result['id']))
                    
            except:    
                    print("session not found")

            global email,password
            if request.method =="POST":
                con = sql.connect(host="localhost",user="root",database="student_django")
                cursor = con.cursor(dictionary=True)
                csrf = request.POST
                for key,value in csrf.items():
                    if key == "email":
                        email=value
                    if key == "password":
                        password=value    
                query = "select * from session where email = '{}' and password = '{}'".format(email,password)
                cursor.execute(query)
                result = cursor.fetchone()
                con.commit()
                if result != None:
                    request.session['email'] = email 
                    request.session['password'] = password 
                    request.session['id'] = result['id'] 
                    return redirect("/edit/"+str(result['id']))
                else:
                    if email == "admin@gmail.com":
                         if password == "4321":
                              request.session['email'] = email 
                              request.session['password'] = password 
                              return redirect('/index')
                    return render(request,"login.html",{"error":"Login Failed !"})       
            return render(request,"login.html") 



     
           