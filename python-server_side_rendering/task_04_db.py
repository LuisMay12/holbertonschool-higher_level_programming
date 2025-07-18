from flask import Flask, render_template, request
import json
import csv
import sqlite3

app = Flask(__name__)

def read_json():
    try:
        with open('products.json', 'r') as f:
            return json.load(f)
    except Exception as e:
        print(f"JSON read error: {e}")
        return []

def read_csv():
    products = []
    try:
        with open('products.csv', 'r') as f:
            reader = csv.DictReader(f)
            for row in reader:
                row['id'] = int(row['id'])
                row['price'] = float(row['price'])
                products.append(row)
    except Exception as e:
        print(f"CSV read error: {e}")
    return products

def read_sql():
    try:
        conn = sqlite3.connect('products.db')
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM Products')
        rows = cursor.fetchall()
        products = [dict(row) for row in rows]
        conn.close()
        return products
    except Exception as e:
        print(f"SQL read error: {e}")
        return []

@app.route('/products')
def show_products():
    source = request.args.get('source')
    id_param = request.args.get('id')
    data = []
    error = None

    if source == 'json':
        data = read_json()
    elif source == 'csv':
        data = read_csv()
    elif source == 'sql':
        data = read_sql()
    else:
        error = "Wrong source"
        return render_template('product_display.html', error=error)

    if id_param:
        try:
            id_int = int(id_param)
            data = [item for item in data if int(item.get('id')) == id_int]
            if not data:
                error = "Product not found"
        except ValueError:
            error = "Invalid ID"

    return render_template('product_display.html', products=data, error=error)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
