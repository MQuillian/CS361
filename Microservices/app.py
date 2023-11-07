from flask import Flask, render_template, jsonify, request, flash, redirect, url_for, sessions, session

app = Flask(__name__)


class Recipe:
    def __init__(self, name, rating, ingredients, instructions):
        self.name = name
        self.rating = rating
        self.ingredients = ingredients
        self.instructions = instructions


rec1 = Recipe("Moscow Mule", 8, "20z vodka\n1/2oz lime juice\n4oz ginger beer\nIce cubes\n1 copper mug (essential)\nLime wedge or mint spring garnish (optional)", "Pour vodka and lime juice in mug\nAdd ginger beer and stir gently\nAdd ice cubes and garnish as desired\nEnjoy!")
rec2 = Recipe("London Fog", 9, "1 Earl Grey teabag (2 if extra-strength desired)\nMilk (2% preferred)\nVanilla or lavender as desired\nWater (obviously)", "Boil water and add tea bags\nLet steep to desired strength and remove tea bags\nFroth the milk or the purists will froth at the mouth and pour it in\nAdd vanilla or lavender as preferred\nStir and enjoy!")

fakedb = {"MQuills": []}
fakedb["MQuills"].append(rec1)
fakedb["MQuills"].append(rec2)


@app.route('/', methods=["GET", "POST"])
def index():
    if request.method == "POST":
        username = request.form['username']
        if username in fakedb:
            session['username'] = username
            return redirect(url_for('home'))
        else:
            flash("Login failed. Please login with correct credentials or create an account")
            return redirect(url_for('index'))

    return render_template('index.html')


@app.route('/accounts/create', methods=["GET", "POST"])
def create_account():
    if request.method == "POST":
        username = request.form['username']
        password = request.form['password']
        conf_password = request.form['conf_password']

        if not 5 < len(username) < 25:
            flash("Username is not correct length - must be 6-24 characters long")
            return redirect(url_for('create_account'))
        elif not 5 < len(password) < 25:
            flash("Password is not correct length - must be 6-24 characters long")
            return redirect(url_for('create_account'))
        elif password != conf_password:
            flash("Passwords did not match- please enter and confirm a matching password")
            return redirect(url_for('create_account'))

        fakedb[username] = []
        session['username'] = username
        return redirect(url_for('home'))
    else:
        return render_template("create_account.html")


@app.route('/home', methods=["GET"])
def home():
    recipes = fakedb[session['username']]
    return render_template('home.html', recipes=recipes)


@app.route('/recipes/create', methods=["GET", "POST"])
def create_recipe():
    if request.method == "POST":
        new_recipe = Recipe(request.form['name'], request.form['rating'], request.form['ingredients'], request.form['instructions'])
        user = session['username']
        fakedb[user].append(new_recipe)

        return redirect(url_for('view_recipes'))

    return render_template('create_recipe.html')


@app.route('/recipes', methods=["GET"])
def view_recipes():
    user = session['username']
    return render_template('view_recipes.html', recipes=fakedb[user])


@app.route('/recipes/<id>', methods=["GET"])
def view_recipe(id):
    user = session['username']
    recipe = fakedb[user][int(id)]
    return render_template('view_recipe.html', recipe=recipe)


@app.route('/recipes/<id>/delete')
def delete_recipe(id):
    user = session['username']
    del(fakedb[user][int(id)])
    return redirect(url_for('view_recipes'))


@app.route('/books/create', methods=["GET", "POST"])
def create_book():
    # NOT IMPLEMENTED YET
    return render_template('create_book.html')


@app.route('/books', methods=["GET"])
def view_books():
    # NOT (really) IMPLEMENTED YET
    return render_template('view_books.html')


@app.route('/books/<id>', methods=["GET"])
def view_book(id):
    # NOT (really) implemented yet
    recipes = fakedb[session['username']]
    return render_template('view_book.html', recipes=recipes)


if __name__ == '__main__':
    app.secret_key = 'totally secret'
    app.config['SESSION_TYPE'] = 'filesystem'

    app.run(port=8001)
