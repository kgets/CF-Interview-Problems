import json, urllib.request
def exploringEarthquakes(c, r, sd, ed, m):
    def i(q):
        with urllib.request.urlopen(q) as url:
            return json.loads(url.read().decode()) 
    
    k='' ## REMOVED API KEY ##
    h='https://'
    f="features"
    
    q=h+'maps.googleapis.com/maps/api/geocode/json?address={}&key={}'.format(c.replace(" ", "%20"),k)
    d=i(q)
    d=d["results"][0]["geometry"]["location"]
    lat=d["lat"]
    lng=d["lng"]
    
    z=h+'earthquake.usgs.gov/fdsnws/event/1/query?format=geojson&minmagnitude=4&starttime={}&endtime={}'
    q=(z+'&latitude={}&longitude={}&maxradiuskm={}').format(sd, ed,lat,lng,r)
    d=i(q)[f]
    
    l=len(d)
    def c(d):
        return sum([x["properties"]["mag"] for x in d])/len(d)
    if m=="count":
        a=l
    elif m=="average":      
        a=(0 if l==0 else c(d))
    else:      
        v=c(d)
        q=z.format(sd, ed)
        a=v-c(i(q)[f])
    return a
