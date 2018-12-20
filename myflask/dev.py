from flask import Flask, request, render_template, send_from_directory
from flask.json import jsonify
import json
from POS_automation import *
app = Flask(__name__)

# @ signifies a decorator - way to wrap a function and modify its behavior
@app.route('/')
def index():
    start_time = datetime.now()
    start = int(time.time())
    title = "POS Tool"
    description = "Not that kind of POS"
    pageType = 'test'    
    metaID = 'test'

    df = pd.DataFrame() # create empty dataframe                       
    df = pd.read_csv('./filteredPOS/US_COMMERCIAL_current_data.csv',low_memory=False, usecols=["POS ID","Date","Sort Here","AM Credited","End Customer","Product ID","$$$","Ship-To","Sold-To","Party ID","Mode","Region","Operation","Area","SL2","SL1"])
    print(df)
    user = df[df['Sort Here'] == 'cecgonza']
    table = []
    for key, value in user.iterrows():
        tableRowDict = {}
        pos         = value['POS ID']
        date        = value['Date']
        sort        = value['Sort Here']
        am          = value['AM Credited']
        customer    = value['End Customer']
        pid         = value['Product ID']
        money       = value['$$$']
        shipTo      = value['Ship-To']
        soldTo      = value['Sold-To']
        party       = value['Party ID']
        mode        = value['Mode']
        region      = value['Region']
        op          = value['Operation']
        area        = value['Area']
        sl2         = value['SL2']
        sl1         = value['SL1']
        tableRowDict = {"POS ID":pos,"Date":date,"Sort Here":sort,"AM Credited":am,"End Customer":customer,"Product ID":pid,"$$$":money,"Ship-To":shipTo,"Sold-To":soldTo,"Party ID":party,"Mode":mode,"Region":region,"Operation":op,"Area":area,"SL2":sl2,"SL1":sl1}
        table.append(tableRowDict)
        #print(table)
    end_time = datetime.now()
    end = int(time.time())
    d = divmod(end - start,86400)  # days
    h = divmod(d[1],3600)  # hours
    m = divmod(h[1],60)  # minutes
    s = m[1]  # seconds
    print('Total run time = {0} minutes , {1} seconds'.format(m[0],s))
    return render_template("test.html", title=title, description=description, pageType=pageType, metaID=metaID, table=table)

if __name__ == "__main__":
    app.run(host='0.0.0.0',port=5001, debug=True)