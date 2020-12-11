from flask import Flask, render_template, request
import ml_models


app = Flask(__name__)


@app.route('/recommend')
def recommend():
    input = dict(request.args)
    print(input)
    user_input = {input['movie1']:input['rating1'],
                  input['movie2']:input['rating2'],
                  input['movie3']:input['rating3']}
    print("USER INPUT:", user_input)
    prediction = ml_models.nmf_recommender(user_input)
    results = prediction.index.tolist()
    print(results)
    print(type(results))
    print("RESULT[0]", results[0])
    return render_template("recommend.html", results=results)


@app.route("/index")
@app.route("/")
def input_page():
    return render_template("index.html")


@app.errorhandler(404)
@app.errorhandler(500)
def page_not_found(e):
    # note that we set the 404 status explicitly
    return render_template('404.html'), 404


if __name__ == '__main__':
    app.run() # for debugging mode (debug=True); #port=5000 - optional + other things