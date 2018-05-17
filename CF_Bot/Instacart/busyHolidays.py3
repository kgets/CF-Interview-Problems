import datetime as DT
def busyHolidays(shoppers, orders, leadTime):
    tformat = '%H:%M'
    d=dict() # {customer: (shoppers)}
    for x,customer in enumerate(orders):
        d[x]=list()
        customerEarliest = DT.datetime.strptime(customer[0],tformat)+DT.timedelta(minutes=leadTime[x])
        customerLatest = DT.datetime.strptime(customer[1],tformat)
        shpCount=0
        for shopper in shoppers:
            shopperEarliest = DT.datetime.strptime(shopper[0],tformat)+DT.timedelta(minutes=leadTime[x])
            shopperLatest = DT.datetime.strptime(shopper[1],tformat)
            #determine delivery window
            windowStart = max(customerEarliest,shopperEarliest)
            windowEnd = min(customerLatest,shopperLatest)
            #determine if can be delivered or not
            if windowEnd<windowStart:
                continue #cannot be delivered
            else:
                d[x].append(shopper)
                shpCount+=1
        #if 1:1 match remove shopper from customer pool
        if shpCount==1:
            shoppers.remove(d[x][0])
            del d[x]
        # if no valid shoppers return false
        elif shpCount==0:
            return False
    #match remaining shoppers and customers
    return dfs(shoppers,d)

def dfs(shopperList,d):
    if len(d)==0:
        return True
    for ok,ov in d.items(): #gets first item
        #dfs possible rem shoppers
        #pass updated dictionary, and updated list
        f=False
        updCustomerList=dict(d)
        del updCustomerList[ok]
        for shop in ov: #gets possible shoppers
            if shop in shopperList:
                updShopperList = list(shopperList)
                updShopperList.remove(shop)
                f=dfs(updShopperList,updCustomerList)
                if f:
                    break
        return f
