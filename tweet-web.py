import os
from flask import Flask, redirect, render_template, request
from search_tweets import search_for_tweets

app= Flask(__name__)

@app.route("/")
def get_index():
    return render_template("index.html")

@app.route("/results")
def results():
    
    results = search_for_tweets(request.args['search'],10)
        
    return render_template("results.html", tweets = results)

if __name__ == '__main__':
    app.run(host=os.getenv('IP', '0.0.0.0'), port=int(os.getenv('PORT', 8080)), debug=True)