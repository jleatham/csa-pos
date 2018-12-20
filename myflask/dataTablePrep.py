import pandas as pd
from datetime import date
from dateutil.relativedelta import relativedelta


def pandasToDataTable(df,column,value):
    df['Date'] = pd.to_datetime(df['Date'])
    #today = date.today()
    #six_months = today - relativedelta(months=+6)
    #df = df[(df['Date'] > pd.Timestamp(six_months)) & (df['Date'] <= pd.Timestamp(today))]
    #df['Date'] = df['Date'].dt.strftime('%Y-%m-%d')
    data = df[df[column] == value]
    data.sort_values(by=['Date'], inplace=True, ascending=False)
    data = data.reset_index(drop=True)
    data['Date'] = data['Date'].dt.strftime('%Y-%m-%d')
    data.truncate(after=10000)
    print(data)
    table = []
    for key, value in data.iterrows():
        tableRowDict = {}
        pos         = value['POS ID']
        posdate     = value['Date']
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
        tableRowDict = {"POS ID":pos,"Date":posdate,"Sort Here":sort,"AM Credited":am,"End Customer":customer,"Product ID":pid,"$$$":money,"Ship-To":shipTo,"Sold-To":soldTo,"Party ID":party,"Mode":mode,"Region":region,"Operation":op,"Area":area,"SL2":sl2,"SL1":sl1}
        table.append(tableRowDict)
    return table