# importing modules from flask library
from flask import Flask , render_template

# creating instance of class Flask, by providing __name__ keyword as argument
app = Flask(__name__)

# write the routes using decorator functions
# default route or 'URL'
@app.route("/")
def home():

    name = "Tista" # write your name
    age = "15" # write your age

    return render_template('index.html' , name = name , age = age)

# define the route to father webpage
@app.route("/father")
def father():
    father_name = "Dibyendu"
    father_age = "47"
    return render_template('father.html', father_name=father_name, father_age=father_age)



# define the route to mother webpage
@app.route("/mother")
def mother():
    mother_name = "Dipti"
    mother_age = "40"
    return render_template('mother.html' , mother_name=mother_name , mother_age=mother_age)


# define the route to friends webpage
@app.route("/friend")
def friend():
    friend_name = "Classmates"
    friend_age = "15"
    return render_template('friend.html', friend_name=friend_name , friend_age=friend_age)


# add other routes, if you want




# run the file
if __name__  ==  '__main__':
    app.run(debug=True)
