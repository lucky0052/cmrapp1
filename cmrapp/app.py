from flask import Flask,render_template,url_for
import os
app = Flask(__name__)



details = [{
        "name":"lucky",
        "event1":"python",
        "image":"lucky.JPG",
        "section":"III-yr A",
        "Date1":"19-12-2000"
    },
    {
        "name":"Gourav",
        "event1":"Google Coding",
        "image":"lucky.JPG",
        "section":"III-yr A",
        "Date1":"19-10-2000"
    },
    {
        "name":"lucky",
        "event1":"Microsoft Coding",
        "image":"lucky.JPG",
        "section":"III-yr A",
        "Date1":"19-12-2020"
    },
    {
        "name":"lucky",
        "event1":"HackerRank",
        "image":"lucky.JPG",
        "section":"III-yr A",
        "Date1":"19-12-2000"
    },
    {
        "name":"Sourav",
        "event1":"CodeChef",
        "image":"lucky.JPG",
        "section":"III-yr A",
        "Date1":"19-09-2000"
    },
    {
        "name":"lucky",
        "event1":"python",
        "image":"lucky.JPG",
        "section":"III-yr A",
        "Date1":"19-12-2000"
    },
    {
        "name":"lucky",
        "event1":"java",
        "image":"lucky.JPG",
        "section":"III-yr A",
        "Date1":"19-12-2000"
    },
    {
        "name":"Karan",
        "event1":"MIT",
        "image":"lucky.JPG",
        "section":"III-yr A",
        "Date1":"19-12-2000"
    }]
    
participate =[
    {
        "name":'Lucky',
        'section':'Sec-A',
        'event':'python',
        'date':'19-12-2000'
    },
    {
        "name":'Gautam',
        'section':'Sec-C',
        'event':'Front-End',
        'date':'19-04-2020'
    },
    {
        "name":'Sourav',
        'section':'Sec-D',
        'event':'IBM',
        'date':'16-10-2021'
    },
    {
        "name":'Karan',
        'section':'Sec-B',
        'event':'Project',
        'date':'15-09-2021'
    }
]

organizer = [
    {
        "name":"Lucky",
        "event":"python",
        "date":"20-09-2021"
    },
    {
        "name":"xyz",
        "event":"SAP Scholarship",
        "date":"20-09-2021"
    },
    {
        "name":"Sohan",
        "event":"Google",
        "date":"20-09-2021"
    },
    {
        "name":"Rohan",
        "event":"python Certificate",
        "date":"20-09-2020"
    },
    
    
    ]


@app.route('/')
def home():
    return render_template("template1.html", details=details)

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html',details=participate)

@app.route('/profile')
def profile():
    return render_template('profile.html')

@app.route('/organize')
def organize():
    return render_template('organize.html')

@app.route('/activity')
def activity():
    return render_template('activity.html',details=organizer)

@app.context_processor
def override_url_for():
    return dict(url_for=dated_url_for)

def dated_url_for(endpoint, **values):
    if endpoint == 'static':
        filename = values.get('filename', None)
        if filename:
            file_path = os.path.join(app.root_path,
                                 endpoint, filename)
            values['q'] = int(os.stat(file_path).st_mtime)
    return url_for(endpoint, **values)



if __name__ == "__main__":
    app.run(debug=True)
    
