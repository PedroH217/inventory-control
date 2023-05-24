from App import app
from App.models.database import database_obj
from flask import render_template, redirect, url_for
from flask import request
from App.controllers.validate import val


@app.route('/', methods=['GET', 'POST'])
def home():
    return render_template('home.html')


@app.route('/insert', methods=['POST'])
def insert():

    product = request.form.get("product")
    price = request.form.get('price')
    amount = request.form.get('amount')
    
    if product or (product or amount) == '':
        try:
            # Validating the Product
            if product.isnumeric():
                raise ValueError(f'{product} is not a valid Product Name!')
            
            elif product == '':
                raise ValueError(f'Product field cannot be empty!')    
            
            # Validating the Price
            elif price == '':
                raise ValueError(f'Price field cannot be empty!')
            
            elif not val.validate_price(price):
                raise ValueError(f'{price} not a valid Price for the product{product}!')
            
            # Validating the Price
            elif amount == '':
                raise ValueError(f'The quantity field cannot be empty!')
            
            elif not amount.isnumeric():
                raise ValueError(f'The amount field must only contain numbers!')
            
            # Sending data for insertion in the post-validation database...
            msg = database_obj.insert_bd(product.capitalize(), float(price), int(amount))
            
        except ValueError as error:
            msg= error
            
            
        return render_template('insert.html', msg=msg)

    else:
        return render_template('insert.html', msg=None)


@app.route('/products', methods=['POST'])
def products():

    dct = database_obj.bd
    l = list()
    if request.method == 'POST':
        for product, values in dct.items():
            
            if request.form.get(product) is not None:
                l.append(product)
                
                
    for x in l:
        dct.pop(x)
    
    if dct:
        return render_template('products.html', dct=dct)
    
    return render_template('products.html', dct=None)