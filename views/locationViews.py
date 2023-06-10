from connectDB import app,db
from flask import request,render_template,url_for,redirect,flash
from models import Location

@app.route('/')
def index():
    return render_template('base.html')
@app.route("/location", methods=['GET'])
def getLocations():
    locations = Location.query.all()
    result = []
    for location in locations:
        location_data = {'location_id': location.location_id}
        result.append(location_data)
    return render_template("location.html",locations=result)

@app.route('/addLocation', methods=['POST'])
def addLocation():
    try:
        if request.method=="POST":
            location_id=request.form["location_id"]
        location_data=Location(location_id=location_id)
        db.session.add(location_data)
        db.session.commit()
        flash('location added successfully')
        return redirect(url_for('getLocations'))
    except Exception as e:
        flash('an error occured')
        return redirect(url_for('getLocations'))

@app.route('/updateLocation',methods=['GET','POST'])
def updateLocation():
    try:
        if request.method=='POST':
            my_location=Location.query.get(request.form.get('location_id'))
            my_location.locationName=request.form['locationName']
            db.session.commit()
        flash("location updated successfully")
        return redirect(url_for('getLocations'))
    except Exception as e:
        flash('an error occured')
        return redirect(url_for('getLocations'))
