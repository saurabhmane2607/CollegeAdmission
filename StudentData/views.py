import random
import string
from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
import mysql.connector
from .forms import StudForm
from .models import Stud


def welcome(request):
    return HttpResponse("Hello Student, Register Yourself into our college to get direction towards bright future.")

def register(request):
    email = request.GET.get("email")
    password = request.GET.get("password")
    NameOfStudent =request.GET.get("NameOfStudent")
    test = mysql.connector.connect(host="localhost", user="root", password="admin123", database="CollegeRegistration")
    crs = test.cursor()
    query = "select * from StudentInfo02 where email = '" + email + "'"
    crs.execute(query)
    data = crs.fetchone()
    dict= {}
    if data is None:
        query= "insert into StudentInfo02 values ('" + email + "','" + password + "','" + NameOfStudent + "')"
        crs.execute(query)
        test.commit()
        dict['message']= 'registered'
    else:
        dict['message']='You are already registered user'
    return JsonResponse(dict)

def login(request):
    email = request.GET.get("email")
    password = request.GET.get("password")
    NameOfStudent = request.GET.get("NameOfStudent")
    test = mysql.connector.connect(host="localhost", user="root", password="admin123", database="CollegeRegistration")
    crs = test.cursor()
    query = "select * from StudentInfo02 where email = '" + email + "'"
    crs.execute(query)
    data = crs.fetchone()
    str= ""
    if data is None:
        str="You are not registered user"
    else:
        if data[0]==password:
            str= "You are valid user"
        else:
            str= "Your password is not correct"
    return HttpResponse(str)

def field(request):
    branch = request.GET.get("branch")
    year = request.GET.get("year")
    test = mysql.connector.connect(host="localhost", user="root", password="admin123", database="CollegeRegistration")
    crs = test.cursor()
    query = "select * from field where branch = '" + branch + "'"
    crs.execute(query)
    info = crs.fetchone()
    dict = {}
    if info is None:
        query = "insert into field values ('" + branch + "','" + year + "')"
        crs.execute(query)
        test.commit()
        dict['message'] = 'Branch And Admission inserted successfully.'
    else:
        dict['message'] = 'You are already selected branch'
    return JsonResponse(dict)

def getStudentInformation(request):
    test = mysql.connector.connect(host="localhost", user="root", password="admin123", database="CollegeRegistration")
    crs = test.cursor()
    query = "select * from StudentInfo02 "
    crs.execute(query)
    data = crs.fetchall()
    dict = {}
    list=[]
    if data is None:
        dict['message']='No registered user'
    else:
        for l in data:
            d={}
            d['email']=l[0]
            d['password']=l[1]
            list.append(d)
        dict['data']=list
    return JsonResponse(dict)

def marks(request):
    english = request.GET.get("english")
    math = request.GET.get("math")
    science =request.GET.get("science")
    test = mysql.connector.connect(host="localhost", user="root", password="admin123", database="CollegeRegistration")
    crs = test.cursor()
    query = "select * from StudentMarks where english = '" + english + "'"
    crs.execute(query)
    data = crs.fetchone()
    dict= {}
    if data is None:
        query= "insert into StudentMarks values ('" + english + "','" + math + "','" + science + "')"
        crs.execute(query)
        test.commit()
        dict['message']= 'Your 12th Marks Inserted Successfully'
    else:
        dict['message']='Marks Already Inserted.'
    return JsonResponse(dict)

def aadhar(request):
    aadhar = request.GET.get("aadhar")
    state =request.GET.get("state")
    test = mysql.connector.connect(host="localhost", user="root", password="admin123", database="CollegeRegistration")
    crs = test.cursor()
    query = "select * from StudentAadhar where aadhar = '" + aadhar + "'"
    crs.execute(query)
    data = crs.fetchone()
    dict= {}
    if data is None:
        query= "insert into StudentAadhar values ('" + aadhar + "','" + state + "')"
        crs.execute(query)
        test.commit()
        dict['message']= 'Your Aadhar number uploaded successfully'
    else:
        dict['message']='Aadhar is already in used.'
    return JsonResponse(dict)


def regii(request):
    title= "New Student Registration"
    form= StudForm(request.POST or None)

    if form.is_valid():
        name= form.cleaned_data['student_name']
        clas= form.cleaned_data['class_year']
        addr= form.cleaned_data['address']
        mail= form.cleaned_data['email']

        p= Stud(student_name=name,class_year=clas,address=addr,email=mail)

    context= {
        "title":title,
        "form":form,
    }
    return render(request,'register.html',context)
