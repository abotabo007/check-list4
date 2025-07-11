from flask import redirect, render_template, session, flash, g
from functools import wraps
from datetime import datetime


def feedback(message, page, dict="", var="", code=400, **kwargs):
    """Render message as an apology to user."""
    #par = "var=dict"
    dict_to_pass = {var:dict}
    for key in kwargs:
        dict_to_pass[key] = kwargs[key]
    #print(dict_to_pass)
    flash(message, 'error')
    return render_template(page, **dict_to_pass), code
    '''
    def escape(s):
        """
        Escape special characters.

        https://github.com/jacebrowning/memegen#special-characters
        """
        for old, new in [("-", "--"), (" ", "-"), ("_", "__"), ("?", "~q"),
                         ("%", "~p"), ("#", "~h"), ("/", "~s"), ("\"", "''")]:
            s = s.replace(old, new)
        return s
    return render_template("apology.html", top=code, bottom=escape(message)), code'''


def login_required(f):
    """
    Decorate routes to require login.

    https://flask.palletsprojects.com/en/1.1.x/patterns/viewdecorators/
    """
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if g.user is None:
            return redirect("/login")
        return f(*args, **kwargs)
    return decorated_function

def permissions_required(f):
    """
    Decorate routes to require permissions "owner" or "admin".

    https://flask.palletsprojects.com/en/1.1.x/patterns/viewdecorators/
    """
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if g.user is None or g.user["role"] is None or g.user["role"] not in ["owner", "admin"]:
            flash("User does not have permissions to use this feature")
            return redirect("/")
        return f(*args, **kwargs)
    return decorated_function

def check_password(password):
    '''Check if password follows requirements'''
    if password:
        return False
    else:
        return True

def as_dict(rows):
    '''Return a list of dictionaries to be user to query the db'''
    return list(map(dict,rows))

def to_dict(im_dict):
    """Converts an ImmutableMultiDict like request.form to Dictionary taking out password and confirmation"""
    obj = {}
    for key in im_dict.keys():
        if key not in ["password", "confirmation"]:
            obj[key] = im_dict.get(key)
    return obj

def check_inputs(obj, array = [], ignore = True):
    '''Check if the inputs are blank or none with the option to pass
        in an array to either ignore or to just enforce the ones provided'''
    if not ignore:
        for key in array:
            if key not in obj.keys():
                return [True, key]
    for key in obj.keys():
        if ignore:
            if  key not in array and (not obj.get(key) or obj.get(key) == "" or obj.get(key) == "None" or obj.get(key) == None):
                return [True, key]
        else:
            if key in array and (not obj.get(key) or obj.get(key) == "" or obj.get(key) == "None" or obj.get(key) == None):
                return [True, key]

    return [False, ""]


def best_fit(X, Y, y):
    """Calculate the best fit line for a set of point (X, Y) and returns the corresponding value x for the y provided"""
    if len(X) == 0 or len(Y) == 0 or not y:
        return 0
    xbar = sum(X)/len(X)
    ybar = sum(Y)/len(Y)
    n = len(X) # or len(Y)

    numer = sum(xi*yi for xi,yi in zip(X, Y)) - n * xbar * ybar
    denum = sum(xi**2 for xi in X) - n * xbar**2

    if denum == 0:
        return 0

    b = numer / denum
    a = ybar - b * xbar

    return (y - a) / b