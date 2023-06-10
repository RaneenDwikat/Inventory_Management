from connectDB import app,db
from flask import request,render_template,url_for,redirect,flash
from models import ProductMovement,Product,Location
from datetime import datetime

@app.route("/movement", methods=['GET'])
def getMovements():
    movements = ProductMovement.query.all()
    products = Product.query.all()
    locations = Location.query.all()
    result = []
    for movement in movements:
        from_location=movement.from_location
        to_location=movement.to_location
        
        if from_location ==None:
            from_location=''
            print(from_location)
        if to_location ==None:
            to_location=''
            print(to_location)
        movement_data = {'movement_id': movement.movement_id,'productId':movement.productId,'qty':movement.qty,
            'from_location':from_location,'to_location':to_location,'timestamp':  movement.timestamp}
        result.append(movement_data)
    return render_template("productMovement.html",movements=result,locations=locations,products=products)

def check_before_adding(from_location,productId,qty):
    print('in')
    movements= ProductMovement.query.all()
    for movement in movements:
        if( movement.productId==productId) and (movement.from_location== from_location) and (movement.qty > qty):
            return True
        else:
            return False

@app.route('/addMovement', methods=['POST'])
def addMovement():
    try:
        if request.method=="POST":
            productId=request.form["productId"]
            qty=request.form["qty"]
            from_location=request.form["from_location"]
            to_location=request.form["to_location"]
            if from_location=='':
                from_location=None
            if to_location=='':
                to_location=None
            timestamp=datetime.utcnow()
            if check_before_adding(from_location=from_location,productId=productId,qty=qty):
                movement_data=ProductMovement(productId=productId,qty=qty,from_location=from_location,to_location=to_location,timestamp=timestamp)
                db.session.add(movement_data)
                db.session.commit()
                flash('movement added successfully')
                return redirect(url_for('getMovements'))
            else:
               flash('you cannot move')
               return redirect(url_for('getMovements')) 
    except Exception as e:
        flash('an error occured')
        return redirect(url_for('getMovements'))

@app.route('/updateMovement',methods=['GET','POST'])
def updateMovement():
    try:
        if request.method=='POST':
            my_movement=ProductMovement.query.get('1')
            from_location=request.form['from_location']
            to_location=request.form['to_location']
            if from_location=='':
                from_location=None
            if to_location=='':
                to_location=None
            my_movement.qty=request.form['qty']
            my_movement.productId=request.form['productId']
            my_movement.from_location=from_location
            my_movement.to_location=to_location
            my_movement.timestamp= datetime.utcnow()
            db.session.commit()
        flash("movement updated successfully")
        return redirect(url_for('getMovements'))
    except Exception as e:
        flash('an error occured')
        return redirect(url_for('getMovements'))
    
@app.route('/productBalance',methods=['GET'])
def productBalance():
    movements= ProductMovement.query.all()
    products = Product.query.all()
    locations = Location.query.all()
    results=[]
    for product in products:
        for location in locations:
            results.append([product.product_id,location.location_id,0])
    for movement in movements:
        for result in results:
            if result[0]== movement.productId:
              if movement.to_location != None and result[1]==movement.to_location:
                  result[2]=result[2]+movement.qty
              if movement.from_location != None and result[1]==movement.from_location:
                  result[2]=result[2]-movement.qty

    return render_template('productBalance.html', result=results)

