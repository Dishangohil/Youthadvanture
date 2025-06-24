from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/manali-tour')
def manali_tour():
    return render_template('manali.html')  # ✅ changed from manali-tour.html

@app.route("/leh-itinerary")
def leh_itinerary():
    return render_template("leh-itinerary.html")


@app.route("/beachside-experiences")
def beachside_experiences():
    return render_template("beachside-experiences.html")


@app.route('/destinations')
def destinations():
    return render_template('destinations.html')

@app.route('/theme')
def theme():
    return render_template('theme.html')

@app.route('/ladakh-tour')
def ladakh_tour():
    return render_template('ladakh-tour.html')

@app.route('/family-tour')
def family_tour():
    return render_template('family-tour.html')

@app.route("/motorbike-tour")
def motorbike_tour():
    return render_template("motorbike-tour.html")

@app.route('/romantic-tour')
def romantic_tour():
    return render_template('romantic-tour.html')

@app.route('/college-tour')
def college_tour():
    return render_template('college-tour.html')

@app.route('/weekend-tour')
def weekend_tour():
    return render_template('weekend-tour.html')

@app.route('/women-tour')
def women_tour():
    return render_template('women-tour.html')


@app.route('/activities')
def activities():
    return render_template('activities.html')


@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/blogs')
def blogs():
    return render_template('blog.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/pay')
def pay():
    return render_template('pay.html')

if __name__ == '__main__':
    app.run(debug=True)
