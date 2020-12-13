# movie_recommender
Student project at SPICED Academy Bootcamp: Building a movie recommender with a web interface.

![Berlin cinema](https://github.com/asyaparfenova/movie_recommender/blob/main/images/photo-1585331505473-7586f9cb0854.png?raw=true "Photo Credit: @edwinhooper|unsplash.com")

### The goals of this project were:
- store the MovieLens data in a Postgres database
- calculate cosine similarities between movies
- train a NMF model
- write a Flask web interface for the recommender

### How to launch the recommender:
- clone repository
- run the file application.py
  - from command line: navigate to the location of application.py (folder name flask_app) and run the command ```python application.py```
  - or open application.py in IDE of your choice and rung it from there
- when you see the message ```* Running on http://127.0.0.1:5000/``` open mentioned url (http://127.0.0.1:5000/) in browser of your choice

### How to use recommender
- on the home page choose three movies from the database and rate them from 1(bad) to 5(amazing)
- press submit
- you can see the recommendations, based on your input

### Behind the scenes
For this project I used:
- flask web-application framework for backend
- html, css and javascript for backend
- for autocompletion form I used slightly modified code from [w3scool Lesson](https://www.w3schools.com/howto/howto_js_autocomplete.asp?fbclid=IwAR1FcWSdj9JA7dfCT6pJFAN05ZKD__FJZos3aL5KV6X-jDDE-l_b8k-Wd34)

