import requests
import _thread
import os
import time
import json
from graphdb import *
import hashlib
# from rooms import Room,CODE
# from posts import Post
# from user import User
from datetime import datetime as dt
from flask import Flask
from flask import render_template
from flask import request
from flask import redirect
from flask import make_response
from flask import url_for
from flask import abort
from flask import Response
import random
app = Flask(__name__)
rooms = {
    "default":{
        "posts":{}
    }
}
users = {
}
random_texts = """
Contemporary climate change includes both global warming and its impacts on Earth's weather patterns. There have been previous periods of climate change, but the current rise in global average temperature is more rapid and is primarily caused by humans.[2][3] Burning fossil fuels adds greenhouse gases to the atmosphere, most importantly carbon dioxide (CO2) and methane. Smaller contributions come from agriculture, industrial processes, and forest loss.[4] Greenhouse gases warm the air by absorbing heat radiated by the Earth, trapping the heat near the surface. Greenhouse gas emissions amplify this effect, causing the Earth to take in more energy from sunlight than it can radiate back into space.

Due to climate change, deserts are expanding, while heat waves and wildfires are becoming more common.[5] Increased warming in the Arctic has contributed to melting permafrost, glacial retreat and sea ice loss.[6] Higher temperatures are also causing more intense storms, droughts, and other weather extremes.[7] Rapid environmental change in mountains, coral reefs, and the Arctic is forcing many species to relocate or become extinct.[8] Climate change threatens people with food and water scarcity, increased flooding, extreme heat, more disease, and economic loss. Human migration and conflict can also be a result.[9] The World Health Organization (WHO) calls climate change the greatest threat to global health in the 21st century.[10] Even if efforts to minimise future warming are successful, some effects will continue for centuries. These include sea level rise, and warmer, more acidic oceans.[11]

Many of these impacts are already felt at the current 1.2 °C (2.2 °F) level of warming. Additional warming will increase these impacts and may trigger tipping points, such as the melting of the Greenland ice sheet.[12] Under the 2015 Paris Agreement, nations collectively agreed to keep warming "well under 2 °C". However, with pledges made under the Agreement, global warming would still reach about 2.7 °C (4.9 °F) by the end of the century.[13] Limiting warming to 1.5 °C will require halving emissions by 2030 and achieving net-zero emissions by 2050.[14]

Bobcat Fire in Monrovia, CA, September 10, 2020
Bleached colony of Acropora coral
A dry lakebed in California, which is experiencing its worst megadrought in 1,200 years.[15]
Some effects of climate change, clockwise from top left: Wildfire intensified by heat and drought, worsening droughts compromising water supplies, and bleaching of coral caused by ocean acidification and heating.
Making deep cuts in emissions will require switching away from burning fossil fuels and towards using electricity generated from low-carbon sources. This includes phasing out coal-fired power plants, vastly increasing use of wind, solar, and other types of renewable energy, and taking measures to reduce energy use. Electricity generated from non-carbon-emitting sources will need to replace fossil fuels for powering transportation, heating buildings, and operating industrial facilities.[16][17] Carbon can also be removed from the atmosphere, for instance by increasing forest cover and by farming with methods that capture carbon in soil.[18] While communities may adapt to climate change through efforts like better coastline protection, they cannot avert the risk of severe, widespread, and permanent impacts.
Before the 1980s, when it was unclear whether the warming effect of increased greenhouse gases were stronger than the cooling effect of some aerosols, scientists used the term inadvertent climate modification to refer to human impacts on the climate.[20]

In the 1980s, the terms global warming and climate change became more common. Though the two terms are sometimes used interchangeably,[21] scientifically, global warming refers only to increased surface warming, and climate change describes the full effect of greenhouse gases on the climate.[20] Global warming—used as early as 1975[22]—became the more popular term after NASA climate scientist James Hansen used it in his 1988 testimony in the U.S. Senate.[23] Since the 2000s, the term climate change increased in popularity.[24] Global warming usually refers to human-induced warming of the Earth system, whereas climate change can more broadly refer to natural or anthropogenic change.[25]

Various scientists, politicians and media figures have adopted the terms climate crisis or climate emergency to talk about climate change, and global heating instead of global warming.[26] The policy editor-in-chief of The Guardian said they included this language in their editorial guidelines "to ensure that we are being scientifically precise, while also communicating clearly with readers on this very important issue".[27] In 2019, Oxford Languages chose climate emergency as its word of the year, defining it as "a situation in which urgent action is required to reduce or halt climate change and avoid potentially irreversible environmental damage resulting from it.
Multiple independent instrumental datasets show that the climate system is warming.[32] The 2011–2020 decade warmed to an average 1.09 °C [0.95–1.20 °C] compared to the pre-industrial baseline (1850–1900).[33] Surface temperatures are rising by about 0.2 °C per decade,[34] with 2020 reaching a temperature of 1.2 °C above the pre-industrial era.[35] Since 1950, the number of cold days and nights has decreased, and the number of warm days and nights has increased.[36]

There was little net warming between the 18th century and the mid-19th century. Climate information for that period comes from climate proxies, such as trees and ice cores.[37] Thermometer records began to provide global coverage around 1850.[38] Historical patterns of warming and cooling, like the Medieval Climate Anomaly and the Little Ice Age, did not occur at the same time across different regions. Temperatures may have reached as high as those of the late-20th century in a limited set of regions.[39] There have been prehistorical episodes of global warming, such as the Paleocene–Eocene Thermal Maximum.[40] However, the modern observed rise in temperature and CO2 concentrations has been so rapid that even abrupt geophysical events in Earth's history do not approach current rates.[41]

Evidence of warming from air temperature measurements are reinforced with a wide range of other observations.[42][43] There has been an increase in the frequency and intensity of heavy precipitation, melting of snow and land ice, and increased atmospheric humidity.[44] Flora and fauna are also behaving in a manner consistent with warming; for instance, plants are flowering earlier in spring.[45] Another key indicator is the cooling of the upper atmosphere, which demonstrates that greenhouse gases are trapping heat near the Earth's surface and preventing it from radiating into space.[46]
Regions of the world warm at differing rates. The pattern is independent of where greenhouse gases are emitted, because the gases persist long enough to diffuse across the planet. Since the pre-industrial period, the average surface temperature over land regions has increased almost twice as fast as the global-average surface temperature.[47] This is because of the larger heat capacity of oceans, and because oceans lose more heat by evaporation.[48] The thermal energy in the global climate system has grown with only brief pauses since at least 1970, and over 90% of this extra energy has been stored in the ocean.[49][50] The rest has heated the atmosphere, melted ice, and warmed the continents.[51]
Greenhouse gases are transparent to sunlight, and thus allow it to pass through the atmosphere to heat the Earth's surface. The Earth radiates it as heat, and greenhouse gases absorb a portion of it. This absorption slows the rate at which heat escapes into space, trapping heat near the Earth's surface and warming it over time.[62] Before the Industrial Revolution, naturally-occurring amounts of greenhouse gases caused the air near the surface to be about 33 °C warmer than it would have been in their absence.[63][64] While water vapour (~50%) and clouds (~25%) are the biggest contributors to the greenhouse effect, they increase as a function of temperature and are therefore feedbacks. On the other hand, concentrations of gases such as CO2 (~20%), tropospheric ozone,[65] CFCs and nitrous oxide are not temperature-dependent, and are therefore external forcings.[66]

Human activity since the Industrial Revolution, mainly extracting and burning fossil fuels (coal, oil, and natural gas),[67] has increased the amount of greenhouse gases in the atmosphere, resulting in a radiative imbalance. In 2019, the concentrations of CO2 and methane had increased by about 48% and 160%, respectively, since 1750.[68] These CO2 levels are higher than they have been at any time during the last 2 million years. Concentrations of methane are far higher than they were over the last 800,000 years.[69]
The Northern Hemisphere and the North Pole have warmed much faster than the South Pole and Southern Hemisphere. The Northern Hemisphere not only has much more land, but also more seasonal snow cover and sea ice. As these surfaces flip from reflecting a lot of light to being dark after the ice has melted, they start absorbing more heat.[52] Local black carbon deposits on snow and ice also contribute to Arctic warming.[53] Arctic temperatures are increasing at over twice the rate of the rest of the world.[54] Melting of glaciers and ice sheets in the Arctic disrupts ocean circulation, including a weakened Gulf Stream, further changing the climate.[55]""".split(".")
first_names = [
    "Timothy",
    "Brian",
    "Arnold",
    "Isaac",
    "Ray",
    "Michelle",
    "Babra",
    "Melinda",
    "Shalom",
    "Laureen",
    "Amber",
    "Aaron",
    "Ingrid",
    "Perry",
    "Irah",
    "Bakr",
    "Spongebob",
    "Shem"
]
import difflib
def string_similarity(str1, str2):
    result =  difflib.SequenceMatcher(a=str1.lower(), b=str2.lower())
    return result.ratio()
surnames = [
    "Brooks",
    "Kingsley",
    "Fry",
    "Einstein",
    "Mabonga",
    "Okoed",
    "Jamokit",
    "Kisolo",
    "Kikonde",
    "Johnson",
    "Walker",
    "Lusfer",
    "Loud",
    "Aisu"
]
for i in range(200):
    name1 = random.choice(first_names)
    name2 = random.choice(surnames)
    users[name1.lower()+name2.lower()+"@gmail.com"] = {
        "username":name1 + " " + name2,
    }

for i in range(1000):
    content = f"{random.choice(random_texts)} {random.choice(random_texts)}"
    ide = hashlib.sha256(str((dt.now().timestamp())).encode("utf-8")).hexdigest()
    email = random.choice(list(users.keys()))
    p = {"id":ide,"content":content,"likes":[],"shares":0,"author":email,"birthdate":dt.now().strftime("%I:%M %p on %d %B,%Y"),"comments":[]}
    rooms["default"]["posts"].update({ide:p})


# _thread.start_new_thread(makeFakePost,())
users["example@gmail.com"] = {
    "username":"Michael Greener",
    "password":hashlib.sha512("200634".encode("utf-8")).hexdigest(),
    "estdate":dt.now().strftime("%d %B,%Y"),
    "rooms":[],
    "pic":"av0"
}
def partition(l, r, nums):
    pivot, ptr = nums[r][1], l
    for i in range(l, r):
        if nums[i][1] >= pivot:
            nums[i], nums[ptr] = nums[ptr], nums[i]
            ptr += 1
    nums[ptr], nums[r] = nums[r], nums[ptr]
    return ptr


def quicksort(l, r, nums):
    if len(nums) == 1:
        return nums
    if l < r:
        pi = partition(l, r, nums)
        quicksort(l, pi-1, nums)
        quicksort(pi+1, r, nums)
    return nums


images = {
    "av0":"/static/dump/avatar.png",
    "av1":"/static/images/avatars/av1",
    "av2":"/static/images/avatars/av2",
    "av3":"/static/images/avatars/av3",
    "av4":"/static/images/avatars/av4",
    "av5":"/static/images/avatars/av5",
    "av6":"/static/images/avatars/av6",
    "av7":"/static/images/avatars/av7",
    "av8":"/static/images/avatars/av8",
    "av9":"/static/images/avatars/av9",
    "av10":"/static/images/avatars/av10"
}
def authUser(email,password,hashed=False):
    if not hashed:
        password = hashlib.sha512(password.encode("utf-8")).hexdigest()
    try:
        if password == users[email]["password"]:
            return users[email]
        else:
            return {}
    except KeyError:
        return {}
@app.route('/')
def index():
    return render_template("index.html")
@app.route('/log')
def log():
    import requests
    r = requests.post(
        "https://api.deepai.org/api/text-generator",
        data={
            'text': 'Climate change is bad',
        },
        headers={'api-key': 'quickstart-QUdJIGlzIGNvbWluZy4uLi4K'}
    )
    return str(r.json())
@app.route('/login')
def login():
    return render_template("login.html")

@app.route("/signup")
def signup():
    return render_template("signup.html")

@app.route("/feed")
def feed():
    return render_template("feeds.html")
@app.route("/signup_form",methods=["POST"])
def signup_form():
    global users
    username = request.form["username"]
    email = request.form["email"]
    password = request.form["password"]
    if email in users:
        return render_template("signup.html",error="User already exists")
    users[email] = {
        "username":username,
        "password":hashlib.sha512(password.encode("utf-8")).hexdigest(),
        "estdate":dt.now().strftime("%d %B,%Y"),
        "pic":"av0"
    }
    resp = make_response(redirect(url_for("feed")))
    resp.set_cookie("email",email)
    resp.set_cookie("password",users[email]["password"])
    return resp
@app.route("/changepic")
def changepic():
    email = request.args.get("email")
    return images[users[email]["pic"]]
@app.route("/login_form",methods=["POST"])
def login_form():
    email = request.form["email"]
    password = hashlib.sha512(request.form["password"].encode("utf-8")).hexdigest()
    try:
        result = users[email]
        if result["password"] != password:
            return render_template("login.html",error="Wrong password")
        resp = make_response(redirect(url_for("feed")))
        resp.set_cookie("email",email)
        resp.set_cookie("password",result["password"])
        return resp
    except KeyError:
        return render_template("login.html",error="User does not exist")
@app.route("/save")
def save():
    post = request.args.get("post")
    return Response(rooms["default"]["posts"][post]["content"],mimetype='text/plain')
@app.route("/getdata",methods=["POST"])
def getdata():
    email = request.form["email"]
    password = request.form["password"]
    return authUser(email,password,True)
@app.route("/getpost")
def getpost():
    try:
        return random.choice(list(rooms["default"]["posts"].values()))
    except IndexError:
        return {}
@app.route("/search")
def search():
    q = request.args.get("q")
    results = []
    for i in list(rooms["default"]["posts"].values()):
        results.append((i,string_similarity(q,i["content"])))
    results = quicksort(0,len(results)-1,results)
    new = []
    for i in results:
        if i[1] == 0:
            break
        new.append(i[0])
    del results
    return {"results":new}
@app.route("/makepost",methods=["POST"])
def makepost():
    email = request.form["email"]
    password = request.form["password"]
    content = request.form["content"]
    if authUser(email,password,True) == {}:
        return {}
    default = rooms["default"]
    p = {"id":hashlib.sha256((email+content+"default").encode("utf-8")).hexdigest(),"content":content,"likes":[],"shares":0,"author":email,"birthdate":dt.now().strftime("%I:%M %p on %d %B,%Y"),"comments":[]}
    default["posts"].update({hashlib.sha256((email+content+"default").encode("utf-8")).hexdigest():p})
    return json.dumps(p)

@app.route("/getname")
def getname():
    email = request.args.get("email")
    return users[email]["username"]
@app.route("/checkroomname")
def checkroomname():
    name = request.args.get("name")
    return str(name in rooms)
@app.route("/joinroom")
def joinroom():
    email = request.form["email"]
    password = request.form["password"]
    name = request.form["name"]
    if authUser(email,password,True) == {}:
        return "e"
    users[email]["rooms"].append(name)
    return "ok"
@app.route("/like",methods=["POST"])
def like():
    email = request.form["email"]
    password = request.form["password"]
    post = request.form["post"]
    group = request.form["group"]
    if authUser(email,password,True) == {}:
        return "e"
    rooms[group]["posts"][post]["likes"] = set(rooms[group]["posts"][post]["likes"])
    rooms[group]["posts"][post]["likes"].add(email)
    rooms[group]["posts"][post]["likes"] = list(rooms[group]["posts"][post]["likes"])
    return str(len(rooms[group]["posts"][post]["likes"]))
@app.route("/nolikes")
def nolikes():
    post = request.args.get("post")
    group = request.args.get("group")
    return str(len(rooms[group]["posts"][post]["likes"]))
@app.route("/comment",methods=["POST"])
def comment():
    email = request.form["email"]
    password = request.form["password"]
    post = request.form["post"]
    content = request.form["content"]
    if authUser(email,password,True) == {}:
        return "e"
    rooms["default"]["posts"][post]["comments"].append({"user":users[email]["username"],"content":content})
    return {"user":users[email]["username"],"content":content}
@app.route("/getcomments")
def getcomments():
    post = request.args.get("post")
    return {"posts":rooms["default"]["posts"][post]["comments"]}