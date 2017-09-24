from flask import Flask, session ,redirect, url_for, escape, render_template, jsonify ,json, request
import MySQLdb
import uuid
app=Flask(__name__)
app.secret_key = 'like seriously you want it ?'

db = MySQLdb.connect("localhost", "root", "root", "moviebuzz")
db.autocommit(True)

#
# @app.route("/")
# def hello():
#     return "Hello World"


@app.route('/')
def index():
    if 'username' in session:
        username_session = escape(session['username']).capitalize()
        return render_template('index.html', session_user_name=username_session)
    return redirect(url_for('login'))


@app.route("/user/<username>")
def user(username):
    return render_template('userHome.html', name=username)


@app.route('/showAddMovie')
def showAddWish():

    return render_template('addMovie.html')



@app.route('/addMovie/<_title>/<_timing>/<_location>')
def addMovie(_title,_timing,_location):
    try:
        print("logged in user ",session.get('user'))
        _user = session.get('user')
        print("logged in user = ",_user)
        cursor = db.cursor()
        uuid.uuid4();
        sql="INSERT INTO moviebuzz.movie_master(movie_id, movie_name, movie_timing, movie_location ,inserted_date, added_by ) VALUES ('"+str(uuid.uuid4())+"','"+_title+"', '"+_timing+"','"+_location+"',now(), '"+_user+"')"
        print("check sql "+sql)
        cursor.execute(sql)
        data = cursor.fetchall()
        print(data)
        if len(data) > 0:
            print(len(data))
            cursor.commit()
            return redirect('/showDashboard')
        else:
            return render_template('error.html',error = 'An error occurred!')
    except Exception as e:
        return render_template('error.html',error = str(e))
    finally:
        True


# @app.route('/updateMovie/<_title>/<_timing>/<_location>')
# def updateMovie(_title,_timing,_location):
#     try:
#         print("logged in user ",session.get('user'))
#         _user = session.get('user')
#         print("logged in user = ",_user)
#         cursor = db.cursor()
#         uuid.uuid4();
#         sql="INSERT INTO moviebuzz.movie_master(movie_id, movie_name, movie_timing, movie_location ,inserted_date, added_by ) VALUES ('"+str(uuid.uuid4())+"','"+_title+"', '"+_timing+"','"+_location+"',now(), '"+_user+"')"
#         print("check sql "+sql)
#         cursor.execute(sql)
#         data = cursor.fetchall()
#         print(data)
#         if len(data) > 0:
#             print(len(data))
#                 #cursor.connection()
#             cursor.commit()
#             return redirect('/showDashboard')
#         else:
#             return render_template('error.html',error = 'An error occurred!')
#     except Exception as e:
#         return render_template('error.html',error = str(e))
#     finally:
#         True



@app.route('/movieUpdateDelete')
def userHome():
    if session.get('user'):
        return render_template('userHome.html')
    else:
        return render_template('error.html',error = 'Unauthorized Access')



@app.route("/lotsOfData")
def people():
    myPeople={"Suraj":1,"Sukumar":2,"Laxmi":3,"Sushant":4}
    return jsonify(myPeople)

@app.route('/login')
def showSignUp():
    return render_template('signin.html')


@app.route('/validateLogin', methods=['POST','GET'])
def validateLogin():
    try:
        # _username = request.args.get('userName')
        _username = request.form['inputEmail']
        _password = request.form['inputPassword']
        print(_username,_password)
        # connect to mysql
        cursor = db.cursor()
        cursor.execute("SELECT * from user where user_name='" + _username + "' and user_password='" + _password + "'")
        data = cursor.fetchone()
        print(data)
        if data is not None:
            if True:
                session['user'] = data[1][0]
                return redirect('/showDashboard')
            else:
                return render_template('error.html', error='Wrong Email address or Password.')
        else:
            return render_template('error.html', error='Wrong Email address or Password.')

        cursor.close()
    except Exception as e:
        return render_template('error.html', error=str(e))
    finally:
        True



@app.route('/showDashboard')
def showDashboard():
    return render_template('dashboard.html')


@app.route('/getAllMovies')
def getAllMovies():
    try:
        if session.get('user'):
            cursor = db.cursor()
            cursor.execute('select movie_id, movie_name, movie_timing, movie_location from movie_master')
            result = cursor.fetchall()
            print("get all movies ",result)
            wishes_dict = []
            for wish in result:
                wish_dict = {
                    'Id': wish[0],
                    'Title': wish[1],
                    'Description': wish[2],
                    'FilePath': wish[3]}
                wishes_dict.append(wish_dict)

            return json.dumps(wishes_dict)
        else:
            return render_template('error.html', error='Unauthorized Access')
    except Exception as e:
        return render_template('error.html', error=str(e))




@app.route('/getMoviesUpdateDelete', methods=['POST'])
def getAllMoviesUpdateDelete():
    try:
        if session.get('user'):
            _user = session.get('user')
            _offset = request.form['offset']

            cursor = db.cursor()
            cursor.execute('select movie_id, movie_name, movie_timing, movie_location from movie_master')
            result = cursor.fetchall()
            print("get all movies ", result)
            wishes_dict = []
            for wish in result:
                wish_dict = {
                    'Id': wish[0],
                    'Title': wish[1],
                    'Description': wish[2],
                    'FilePath': wish[3]}
                wishes_dict.append(wish_dict)

            response = []

            response.append(wishes_dict)
            response.append({'total': len(wishes_dict)})

            return json.dumps(response)
        else:
            return render_template('error.html', error='Unauthorized Access')
    except Exception as e:
        return render_template('error.html', error=str(e))


@app.route('/getMovieById', methods=['POST'])
def getMovieById():
    try:
        if session.get('user'):
            _id = request.form['id']
            print(_id)
            cursor = db.cursor()
            cursor.execute("select movie_id, movie_name,DATE_FORMAT(movie_timing, '%Y-%m-%d %H:%i') , movie_location from movie_master where movie_id = '"+_id+"'")
            result = cursor.fetchall()
            print(result)
            wish = []
            wish.append(
                {'Id': result[0][0], 'Name': result[0][1], 'Time': result[0][2], 'Location': result[0][3],
                })
            print(wish)
            return json.dumps(wish)
        else:
            return render_template('error.html', error='Unauthorized Access')
    except Exception as e:
        return render_template('error.html', error=str(e))


@app.route('/updateMovie', methods=['POST'])
def updateMovie():
    try:
        if True:
            _user = session.get('user')
            _title = request.form['name']
            _timing = request.form['time']
            _location = request.form['location']
            _id = request.form['id']
            cursor = db.cursor()
            sql = "UPDATE moviebuzz.movie_master SET  movie_name='" +_title+"', movie_timing='"+ _timing+"' , movie_location='"+_location+"' where movie_id= '"+_id+"'" ;

            print("check sql " + sql)
            cursor.execute(sql)
            data = cursor.fetchall()
            print(data)
            if len(data) is 0:
                return json.dumps({'status': 'OK'})
            else:
                return json.dumps({'status': 'ERROR'})
    except Exception as e:
        return json.dumps({'status': 'Unauthorized access'})
    finally:
        True


@app.route('/deleteMovie',methods=['POST'])
def deleteMovie():
    try:
        if True:
            _id = request.form['id']
            cursor = db.cursor()
            cursor.execute("delete from moviebuzz.movie_master where movie_id='"+_id+"'")
            result = cursor.fetchall()

            if len(result) is 0:

                return json.dumps({'status':'OK'})
            else:
                return json.dumps({'status':'An Error occured'})
        else:
            return render_template('error.html',error = 'Unauthorized Access')
    except Exception as e:
        return json.dumps({'status':str(e)})
    finally:
        cursor.close()
        True



if __name__=="__main__":
    app.run(debug=True)