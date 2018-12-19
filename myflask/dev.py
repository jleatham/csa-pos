from flask import Flask, request, render_template, send_from_directory
from flask.json import jsonify
import json
from POS_automation import *
app = Flask(__name__)

# @ signifies a decorator - way to wrap a function and modify its behavior
@app.route('/')
def index():

    except:
        print("cannot process files as report is being ran")

    title = "POS Tool"
    description = "Not that kind of POS"
    pageType = 'test'    
    metaID = 'test'
    return render_template("test.html", title=title, description=description, pageType=pageType, metaID=metaID)

if __name__ == "__main__":
    app.run(host='0.0.0.0',port=5001, debug=True)