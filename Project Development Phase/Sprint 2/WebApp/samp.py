from flask import Flask, render_template, request, url_for, redirect

app = Flask(__name__)

@app.route('/')
@app.route('/register')
def landingPage():
    return render_template('index.html')

@app.route('/test/<int:tid>')
def register(tid):
    if(tid==1):
        return redirect(url_for('user', id=tid))
    else:
        return redirect(url_for('user', name='Hello'))

@app.route('/home', methods=['POST'])
def home():
    if request.method == 'POST':
        userName = request.form['UserName']
    return render_template('home.html', user=userName)

@app.route('/user/<int:id>', methods=['GET'])
def user(id):
    return 'User ' + str(id) + ' has requested!'

@app.route('/user/<name>', methods=['GET'])
def user_by_name(name):
    return 'User ' + name + ' has requested!'

if __name__ == "__main__":
    app.run(debug=True)

# #*create database connection

# import ibm_db

# try:
#     conn = ibm_db.connect("DATABASE=bludb; HOSTNAME=2f3279a5-73d1-4859-88f0-a6c3e6b4b907.c3n41cmd0nqnrk39u98g.databases.appdomain.cloud; PORT=30756; SECURITY=SSL; SSLServerCertificate=DigiCertGlobalRootCA.crt; UID=mbx07408; PWD=ht0PtgwaHfFfEE2C", "", "")
#     print("Connected")
# except:
#     print("Failed to connect")
