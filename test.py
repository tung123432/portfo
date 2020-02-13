from flask import Flask, render_template, url_for, request, redirect
import csv

app = Flask(__name__)
# đây là nơi tham số nhận từ url
@app.route('/')
def my_home():
    # name = request.args.get("name", "World")
    return render_template('index.html')
@app.route('/index.html')
def my_home_two():
    # name = request.args.get("name", "World")
    return render_template('index.html')
@app.route('/about.html')
def about():
    # name = request.args.get("name", "World")
    return render_template('about.html')
@app.route('/components.html')
def components():
    # name = request.args.get("name", "World")
    return render_template('components.html')
@app.route('/contact.html')
def contact():
    # name = request.args.get("name", "World")
    return render_template('contact.html')
@app.route('/work.html')
def work():
    # name = request.args.get("name", "World")
    return render_template('work.html')
@app.route('/works.html')
def works():
    # name = request.args.get("name", "World")
    return render_template('works.html')
@app.route('/submit_form',methods=['GET','POST'])
def submit_forma():
    if(request.method=="POST"):
        data = request.form.to_dict()
        Write_to_CSV(data)
        return render_template('/tmmt.html')
    else:
        return "some thing went wrong . Try Again !"

def Write_to_File(data):
    with open('database.txt',mode='a',encoding='utf-8') as database:
        Email = data['Email']
        Subject = data['Subject']
        Message = data['Message']
        database.write(f'\n{Email},{Subject},{Message}')

def Write_to_CSV(data):
    with open('database.csv',mode='a',newline='',encoding='utf-8') as database2:
        Email = data['Email']
        Subject = data['Subject']
        Message = data['Message']
        csv_writer = csv.writer(database2,delimiter=',',quotechar='"',quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([Email,Subject,Message])

@app.route('/Success')
def Success():
    return render_template('tmmt.html')
@app.route('/tmmt.html')
def login_success():
    return render_template('/tmmt.html')
