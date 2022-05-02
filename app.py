# Flask
from flask import Flask, render_template, url_for, request, redirect

# Database queries
import data

app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        name = request.form['name']
        price = request.form['price']

        try:
            price = float(price)
        except:
            products = data.select(None)
            return render_template('index.html', message="Price must be a valid number. (e.g X or X.X)", products=products)
        
        new_product = (None, name, price,)

        try:
            data.insert(new_product)
            return redirect("/")
        except:
            return render_template('index.html', message='There was an error while attempting to write to database.')
    else:
        products = data.select(None)
        return render_template('index.html', products=products)


@app.route('/search')
def search():
    query = request.args.get('query')

    if query:
        products = data.select(query)
        return render_template('search.html', products=products)
    else:
        return render_template('search.html') 


@app.route('/delete/<int:id>')
def delete(id):
    try:
        data.delete(id)
        print(request.referrer)
        return redirect(request.referrer)
    except:
        return "There was an error when deleting that task."

if __name__ == "__main__":
   app.run(host='0.0.0.0')
