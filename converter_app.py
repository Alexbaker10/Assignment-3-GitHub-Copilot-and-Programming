from flask import Flask, render_template, request

app = Flask(__name__)

# Conversion factors
CONVERSIONS = {
    'inches_to_yards': lambda x: x / 36,
    'yards_to_centimeters': lambda x: x * 91.44,
    'centimeters_to_inches': lambda x: x / 2.54,
    'yards_to_inches': lambda x: x * 36,
    'inches_to_centimeters': lambda x: x * 2.54,
    'centimeters_to_yards': lambda x: x / 91.44,
}

@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    if request.method == 'POST':
        value = float(request.form['value'])
        conversion = request.form['conversion']
        if conversion in CONVERSIONS:
            result = CONVERSIONS[conversion](value)
    return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)
