from connectDB import app,db
from flask import request,render_template,url_for,redirect,flash
from models import Product


@app.route("/product", methods=['GET'])
def getProducts():
    products = Product.query.all()
    result = []
    for product in products:
        product_data = {'product_id': product.product_id}
        result.append(product_data)
    return render_template("product.html",products=result)

@app.route('/addProduct', methods=['POST'])
def addProduct():
    try:
        if request.method=="POST":
            product_id=request.form["product_id"]
            product_data=Product(product_id=product_id)
            db.session.add(product_data)
            db.session.commit()
            flash('product added successfully')
            return redirect(url_for('getProducts'))
    except Exception as e:
        flash('an error occured')
        return redirect(url_for('getProducts'))


@app.route('/updateProduct',methods=['GET','POST'])
def updateProduct():
    try:
        if request.method=='POST':
            my_product=Product.query.get(request.form.get('product_id'))
            my_product.product_id=request.form['new_product_id']
            db.session.commit()
        flash("product updated successfully")
        return redirect(url_for('getProducts'))
    except Exception as e:
        flash('an error occured')
        return redirect(url_for('getProducts'))
