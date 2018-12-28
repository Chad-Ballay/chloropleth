import requests
from bs4 import BeautifulSoup
import urllib3


urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


# Too lazy to find an api to get state/population so I just manually found the data and wrote a dictionary

state_pop_dictionary = {"alabama": 4888949, "alaska": 738068, "arizona": 7123898, "arkansas": 3020327,
                        "california": 39776830, "colorado": 5684203, "connecticut": 3588683,
                        "delaware": 971180, "florida": 21312211, "georgia": 10545138, "hawaii": 1426393,
                        "idaho": 1753860, "illinois": 12768320, "indiana": 6699629, "iowa": 3160553,
                        "kansas": 2918515, "kentucky": 4472265, "louisiana": 4682509, "maine": 1341582,
                        "maryland": 6079602, "massachusetts": 6895917, "michigan": 9991177,
                        "minnesota": 5628162, "mississippi": 2982785, "missouri": 6135888,
                        "montana": 1062330, "nebraska": 1932549, "nevada": 3056824, "new hampshire": 1350575,
                        "new jersey": 9032872, "new mexico": 2090708, "new york": 19862512,
                        "north carolina": 10390149, "north dakota": 755238, "ohio": 11694664,
                        "oklahoma": 3940521, "oregon": 4199563, "pennsylvania": 12823989,
                        "rhode island": 1061712, "south carolina": 5088916, "south dakota": 877790,
                        "tennessee": 6782564, "texas": 28704330, "utah": 3159345, "vermont": 623960,
                        "virginia": 8525660, "washington": 7530552, "west virginia": 1803077,
                        "wisconsin": 5818049, "wyoming": 573720}

url = "http://corporate.walmart.com/our-story/locations/united-states/"

f = open("dataset.csv", "w")
f.writelines("State,Walmart Retail Units Per 100000\n")
for state, population in state_pop_dictionary.iteritems():
    url_friendly_state = state.replace(' ', '-')
    temp_url = url + url_friendly_state
    raw_html = requests.get(temp_url, verify=False).text
    html = BeautifulSoup(raw_html, 'html.parser')
    for p in html.find_all("ul", class_="map-content-stats-list"):
        q = p.find("li", class_="map-content-stats-item")
        r = q.find("span", class_="value")
        msg = state + "," + `float(r.text.strip())/population*100000` + "\n"
        print (msg)
        f.write(msg)

