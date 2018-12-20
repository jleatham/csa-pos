from dev import df

def pandasToDataTable(column,value):
    global df
    data = df[df[column] == value]
    table = []
    for key, value in data.iterrows():
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
    return table