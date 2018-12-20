from flask import Flask, request, render_template, send_from_directory
from flask.json import jsonify
import json
from POS_automation import *
from dataTablePrep import pandasToDataTable
app = Flask(__name__)

# @ signifies a decorator - way to wrap a function and modify its behavior
@app.route('/')
def index():

    title = "POS Tool"
    description = "Not that kind of POS"
    pageType = 'test'    
    metaID = 'test'
    return render_template("test.html", title=title, description=description, pageType=pageType, metaID=metaID)

@app.route('/am/<cco>')
def am(cco):
    start_time = datetime.now()
    start = int(time.time())

    title = cco
    description = "Not that kind of POS"
    pageType = 'test'    
    metaID = cco

    global df
    table = pandasToDataTable(df,"Sort Here",cco)
        #print(table)
    end_time = datetime.now()
    end = int(time.time())
    d = divmod(end - start,86400)  # days
    h = divmod(d[1],3600)  # hours
    m = divmod(h[1],60)  # minutes
    s = m[1]  # seconds
    print('Total run time = {0} minutes , {1} seconds'.format(m[0],s))
    return render_template("am.html", title=title, description=description, pageType=pageType, metaID=metaID, table=table)

@app.route('/operation/<op>')
def operation(op):
    start_time = datetime.now()
    start = int(time.time())

    title = op
    description = "Not that kind of POS"
    pageType = 'test'    
    metaID = op

    global df
    table = pandasToDataTable(df,"Operation","South West Select Operation")
        #print(table)
    end_time = datetime.now()
    end = int(time.time())
    d = divmod(end - start,86400)  # days
    h = divmod(d[1],3600)  # hours
    m = divmod(h[1],60)  # minutes
    s = m[1]  # seconds
    print('Total run time = {0} minutes , {1} seconds'.format(m[0],s))
    return render_template("am.html", title=title, description=description, pageType=pageType, metaID=metaID, table=table)


if __name__ == "__main__":
    print("before loading df")
    df = pd.DataFrame() # create empty dataframe                       
    df = pd.read_csv('./filteredPOS/US_COMMERCIAL_current_data.csv',low_memory=False, usecols=["POS ID","Date","Sort Here","AM Credited","End Customer","Product ID","$$$","Ship-To","Sold-To","Party ID","Mode","Region","Operation","Area","SL2","SL1"])
    print(df) 
    print("after loading df")   
    app.run(host='0.0.0.0',port=5001, debug=True, use_reloader=False)
