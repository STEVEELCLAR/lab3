from flask import Flask, render_template, url_for, request, flash, redirect
from lab2 import addForm, updForm, searchform
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="steveclark09",
  database="student"
)

mycursor = mydb.cursor()

app = Flask(__name__)
app.config['SECRET_KEY'] = 'asdfged123qwkjasdasddqwqd4'

#Home
@app.route("/")
def home():
  return render_template('home.html' )  

#Add student
@app.route("/add_student", methods=['GET', 'POST'])
def add_student():
  form = addForm()
  if request.method == 'POST':
    id = request.form["id"].upper()
    lname = request.form["lname"].upper()
    fname = request.form["fname"].upper()
    course = request.form["course"].upper()
    year = request.form["year"].upper()
    gender = request.form["gender"].upper()

    sql = "INSERT INTO student_list (id, lastname, firstname, course, year , gender) VALUES (%s, %s, %s, %s, %s, %s)"
    val = (id, lname, fname, course, year, gender)
    mycursor.execute(sql, val)
    mydb.commit()


    flash('Operation Successfully Executed!')
    return redirect(url_for('view_user'))

  return render_template('add_student.html', form=form  )


#delete student by id
@app.route("/delete_id", methods=['GET', 'POST'])
def del_id():
  form = addForm()
  if request.method == 'POST':
    id = request.form["id"].upper()

    sql = "DELETE FROM student_list WHERE id = %s"
    adr = (id, )
    mycursor.execute(sql, adr)
    mydb.commit()

    flash('Operation Successfully Executed!')
    return redirect(url_for('view_user'))

  return render_template('del_id.html', form=form)


#delete student by last name
@app.route("/delete_lname", methods=['GET', 'POST'])
def del_lname():
  form = addForm()
  if request.method == 'POST':
    lname = request.form["lname"].upper()

    sql = "DELETE FROM student_list WHERE lastname = %s"
    adr = (lname, )
    mycursor.execute(sql, adr)
    mydb.commit()
    flash('Operation Successfully Executed!')
    return redirect(url_for('view_user'))

  return render_template('del_lname.html', form=form)

#delete student by first name
@app.route("/delete_fname", methods=['GET', 'POST'])

def del_fname():
  form = addForm()
  if request.method == 'POST':
    fname = request.form["fname"].upper()

    sql = "DELETE FROM student_list WHERE firstname = %s"
    adr = (fname, )
    mycursor.execute(sql, adr)
    mydb.commit()

    flash('Operation Successfully Executed!')
    return redirect(url_for('view_user'))

  return render_template('del_fname.html', form=form)


#delete student by course
@app.route("/delete_course", methods=['GET', 'POST'])
def del_course():
  form = addForm()
  if request.method == 'POST':
    course = request.form["course"].upper()

    sql = "DELETE FROM student_list WHERE course = %s"
    adr = (course, )
    mycursor.execute(sql, adr)
    mydb.commit()

    flash('Operation Successfully Executed!')
    return redirect(url_for('view_user'))

  return render_template('del_course.html', form=form)


#delete student by year
@app.route("/delete_year", methods=['GET', 'POST'])
def del_year():
  form = addForm()
  if request.method == 'POST':
    year = request.form["year"].upper()

    sql = "DELETE FROM student_list WHERE year = %s"
    adr = (year, )
    mycursor.execute(sql, adr)
    mydb.commit()

    flash('Operation Successfully Executed!')
    return redirect(url_for('view_user'))

  return render_template('del_year.html', form=form)


#delete student by gender
@app.route("/delete_gender", methods=['GET', 'POST'])
def del_gender():
  form = addForm()
  if request.method == 'POST':
    gender = request.form["gender"].upper()

    sql = "DELETE FROM student_list WHERE gender = %s"
    adr = (gender, )
    mycursor.execute(sql, adr)
    mydb.commit()

    flash('Operation Successfully Executed!')
    return redirect(url_for('view_user'))

  return render_template('del_gender.html', form=form)

  #update student by id
@app.route("/update_id", methods=['GET', 'POST'])
def upd_id():
  form =updForm()
  if request.method == 'POST':
    id = request.form["id"].upper()
    newid = request.form["newid"].upper()

    sql = "UPDATE student_list SET id = %s WHERE id = %s"
    val = (newid, id)
    mycursor.execute(sql, val)
    mydb.commit()

    flash('Operation Successfully Executed!')
    return redirect(url_for('view_user'))

  return render_template('upd_id.html', form=form)


#Update student by last name
@app.route("/update_lname", methods=['GET', 'POST'])
def upd_lname():
  form = updForm()
  if request.method == 'POST':
    lname = request.form["lname"].upper()
    newlname = request.form["newlname"].upper()

    sql = "UPDATE student_list SET lastname = %s WHERE lastname = %s"
    val = (newlname, lname)
    mycursor.execute(sql, val)
    mydb.commit()

    flash('Operation Successfully Executed!')
    return redirect(url_for('view_user'))

  return render_template('upd_lname.html', form=form)

#delete student by first name
@app.route("/update_fname", methods=['GET', 'POST'])
def upd_fname():
  form = updForm()
  if request.method == 'POST':
    fname = request.form["fname"].upper()
    newfname = request.form["newfname"].upper()

    sql = "UPDATE student_list SET firstname = %s WHERE firstname = %s"
    val = (newfname, fname)
    mycursor.execute(sql, val)
    mydb.commit()

    flash('Operation Successfully Executed!')
    return redirect(url_for('view_user'))

  return render_template('upd_fname.html', form=form)


#Update student by course
@app.route("/update_course", methods=['GET', 'POST'])
def upd_course():
  form = updForm()
  if request.method == 'POST':
    course = request.form["course"].upper()
    newcourse = request.form["newcourse"].upper()

    sql = "UPDATE student_list SET course = %s WHERE course = %s"
    val = (newcourse, course)
    mycursor.execute(sql, val)
    mydb.commit()

    flash('Operation Successfully Executed!')
    return redirect(url_for('view_user'))

  return render_template('upd_course.html', form=form)


#update student by year
@app.route("/update_year", methods=['GET', 'POST'])
def upd_year():
  form = updForm()
  if request.method == 'POST':
    year = request.form["year"].upper()
    newyear = request.form["newyear"].upper()

    sql = "UPDATE student_list SET year = %s WHERE year = %s"
    val = (newyear, year)
    mycursor.execute(sql, val)
    mydb.commit()

    flash('Operation Successfully Executed!')
    return redirect(url_for('view_user'))

  return render_template('upd_year.html', form=form)


#update student by gender
@app.route("/update_gender", methods=['GET', 'POST'])
def upd_gender():
  form = updForm()
  if request.method == 'POST':
    gender = request.form["gender"].upper()
    newgender = request.form["newgender"].upper()


    sql = "UPDATE student_list SET gender = %s WHERE gender = %s"
    val = (newgender, gender)
    mycursor.execute(sql, val)
    mydb.commit()

    flash('Operation Successfully Executed!')
    return redirect(url_for('view_user'))

  return render_template('upd_gender.html', form=form)


@app.route("/search", methods=['GET', 'POST'])
def search():
  form = searchform()
  if request.method == 'POST':
    info = request.form["info"].upper()

    sql = "SELECT * FROM student_list WHERE lastname = %s or id = %s or firstname = %s or course = %s or year = %s or gender = %s " 
    adr = (info, info, info, info, info, info )
    mycursor.execute(sql, adr)
    myresult = mycursor.fetchall()
    return render_template('view_student.html', myresult=myresult)

  return render_template('search.html', form=form)


@app.route('/view_student')
def view_user():
  #mycursor.execute("SELECT * FROM student_list")
  #myresult = mycursor.fetchall()
  #return render_template('view_student.html', myresult=myresult)

  sql = "SELECT \
  student_list.id AS id, \
  student_list.lastname   AS lastname, \
  student_list.firstname   AS firstname, \
  courses.course AS course, \
  student_list.year   AS year, \
  student_list.gender   AS gender \
  FROM student_list \
  INNER JOIN courses ON student_list.course = courses.id"

  mycursor.execute(sql)
  myresult = mycursor.fetchall()

  return render_template('view_student.html', myresult=myresult)


if __name__ =='__main__':
    app.run(debug=True)

