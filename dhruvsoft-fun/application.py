from flask import Flask, redirect, url_for, session,render_template,request
# from flask_oauth import OAuth
from functools import wraps
try:
    from urllib.request import Request, urlopen
    from urllib.error import URLError
except Exception as e:
    from urllib2 import Request, urlopen, URLError
import random
from flask_cors import CORS, cross_origin

# You must configure these 3 values from Google APIs console
# https://code.google.com/apis/console
GOOGLE_CLIENT_ID = '693805920931-m7d69j7eti5m8mmvv4f49ogkkdmd8l01.apps.googleusercontent.com'
GOOGLE_CLIENT_SECRET = 'G5V1ZIxe8nha4o4SrnAwZYWA'
REDIRECT_URI = '/authorized'  # one of the Redirect URIs from Google APIs console
BASE_URL = "https://dhruvsoft-fun.herokuapp.com/"


SECRET_KEY = 'development key'
DEBUG = True

app = Flask(__name__)
CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'
app.config['STATIC_FOLDER'] = "static/"
app.debug = False
app.secret_key = SECRET_KEY
# oauth = OAuth()

d= {
  'OWN LATE ACHES AIM MEN HIT': 'ONLY TAKES A MINUTE',
  'FRANCE WIDTH BEEN OUTFITS': 'FRIENDS WITH BENEFITS',
  'SPED DOORS WALL HOE': 'SPLIT OR SWALLOW',
  'EYE WON ABEE TICK TOCH FAY MOUS': 'I WANNA BE TIK TOK FAMOUS',
  'HINTS TUG RAMS HOLE LEPER TEA': 'INSTAGRAM CELEBRITY',
  'SHIEK CCONS HOOP FUR THISTLE': 'CHICKEN SOUP FOR THE SOUL',
  'DAWN BIAFRA EIGHT DUFF DEED ARC': 'DON’T BE AFRAID OF THE DARK',
  'DAWN WAYS MIGHT I’M': 'DON’T WASTE MY TIME',
  'CORE AND TEEN SOCKS': 'QUARANTINE SUCKS',
  'SPOTTED FRY PRE MEDIUM': 'SPOTIFY PREMIUM',
  'FIN DAY HOE GAINS': 'VIDEO GAMES',
  'LOAF FAN DULLS': 'LOVE HANDLES',
  'DAWN DUTCH MICE TOUGH': 'DON’T TOUCH MY STUFF',
  'LEE ON HARD ODIE CAP RIO': 'LEONARDO DECAPRIO',
  'HIS CAT TIN OUGHT INNER EAR': 'IT’S GETTING HOT IN HERE',
  'WANDER HER WOMB HEN': 'WONDER WOMEN',
  'TAD SWAT CHEESE HEAD': 'THAT’ S WHAT SHE SAID ',
  'MOOR NIM BUR WRATH': 'MORNING BREATH ',
  'BUFFERS TOLL LED MEAT ACHE US ELF FEE': 'BUT FIRST,LET ME TAKE A SELFIE: ',
  'DOE AN TOUCH A BOO GOODBYE DISCOVER': 'DON’ T JUDGE A BOOK BY ITS COVER ',
  'CAR MUSH UP ITCH': 'KARMA IS A BITCH ',
  'TICK HER  WORN IN': 'TRIGGER WARNING',
  'WAR DA TOY LEPT PAY HER': 'WHERE’S THE TOILET PAPER',
  'MY LIFE': 'A JOKE',
  'SHRINE BRIDE LIE KEA DIE MOUND': 'SHINE BRIGHT LIKE A DIAMOND',
  'CANOE KEY PACE HE GRIT': 'CAN U KEEP A SECRET',
  'DOME HUTCH CHIN FIRM HEY SHUN': 'TOO MUCH INFORMATION',
  'TAD SWAT CHEESE HEAD': 'THAT’S WHAT SHE SAID',
  'STALK  HINT OF RENDS OWN': 'STUCK IN THE FRIEND ZONE',
  'EEW ACHE WHO GULLS URGE': 'DO A GOOGLE SEARCH',
  'POLICED HYMN DELIGHTS': 'PLEASE DIM THE LIGHTS',
  '': 'I WANNA BE TIK TOK FAMOUS',
  'CANNED ACHE MY HIGH SAW FEW': 'CAN’T TAKE MY EYES OFF YOU',
  'YEAH SKEW WEEN': 'YES QUEEN',
  'KNEW FOAM HOOD IS': 'NEW PHONE,WHO THIS??',
  'HISS SIT TINNY IT': 'IS IT IN YET?',
  'WIND HER RITZ CUN INK': 'WINTER IS COMING',
  ' ESSAY MADDER ROUGH ACT': 'AS A MATTER OF FACT',
  'UKE ANT AN DELL TAT RUTH': 'YOU CAN’T HANDLE THE TRUTH',
  'FUN ELLE EYES': 'VANILLA ICE',
  'FORD WENT HE': '420',
  'HINT TURN ED ROLLS': 'INTERNET TROLLS',
  'SICK STEAMY KNITS': '60 MINUTES',
  'MEOW TIN DEH WHEW': 'MOUNTAIN DEW',
  'MY CROWS OFF TEX SELL': 'MICROSOFT EXCEL',
  'HAYSTACK UP HANK ACHES': 'A STACK OF PANCAKES',
  'TETHERS DISS RALL': 'THE THIRST IS REAL',
  'CAR OWN HU FIRE US': 'CORONAVIRUS',
  'FOAL HIP CUB': 'FLIP CUP',
  'ACE LIP PUFF THAT HUNG': 'A SLIP OF THE TONGUE',
  'BULL LAG FRIED HAY': 'BLACK FRIDAY',
  'TOCK TOOTHY AND': 'TALK TO THE HAND',
  'CALM HEED AT TEA': 'CALL ME DADDY',
  'MADE DIVORCE PEA WHIFF EWE': 'MAY THE FORCE BE WITH YOU',
  'MUFF HEATER GOLD': 'MY FEET ARE COLD',
  'HOOP HEARD RIFE FAIR': 'UBER DRIVER',
  'PAR DAVE OWL': 'PARTY OWL',
  'GNOME MORSE GHOUL': 'NO MORE SCHOOL',
  'DITCH CHEWS HAZE HUM THINN': 'DID YOU SAY SOMETHING',
  'SUPS CUR RIPE TOMB EYE SHAM NULL': 'SUBSCRIBE TO MY CHANNEL',
  'STIR RANGE EARTH INKS': 'STRANGER THINGS',
  'ABE AURA HER SHE’S CHALK LIT': 'A BAR OF HERSHEY’S CHOCOLATE',
  'REAL AGENTS SHIP GULLS': 'RELATIONSHIP GOALS',
  'TEST BRIT HOW SURVIVES': 'DESPERATE HOUSEWIVES',
  'SEW SHALL DISS TEN SING': 'SOCIAL DISTANCING',
  'MERE ORES ELF FREE': 'MIRROR SELFIE',
  'BAT TREE SNOT INK LOOTED': 'BATTERIES NOT INCLUDED',
  'NOSED RING SAT HATCHED': 'NO STRINGS ATTACHED',
  'WAS ESTRANGE LANK WEDGE': 'WHAT A STRANGE LANGUAGE',
  'HOOP SIDE HID DITTO KEN': 'OOPS I DID IT AGAIN',
  'LIB FULL HALF ALL OF': 'LIVE,LAUGH,LOVE',
  'EYE YAM STEW PEED': 'I AM STUPID',
  'MOOR NIM BUR WRATH': 'MORNING BREATH',
  'CHEST WHO WIT': 'JUST DO IT',
  'HOOD PUBES AVERY WON': 'GOOD NEWS EVERYONE',
  'BONE APPLE TEETH': 'BON APPETIT',
  'EWE KNIGHT TAKING DUMB': 'UNITED KINGDOM',
  'THIRDS TEETH OR STAY': 'THIRSTY THURSDAY',
  'PIE JUAN KIT WON FURRY': 'BUY 1 GET 1 FREE',
  'PULL EASE LEAF MIA ALONE': 'PLEASE LEAVE ME ALONE',
  'YEW LOGIN LIE UGH SNAP': "YOU LOOKIN' LIKE A SNACK",
  'THIRST RUG EL ISREAL': 'THE STRUGGLE IS REAL',
  'MUH KNEES HOT': 'MONEY SHOT',
  'HUE ONLY LEE LEAF ONE': 'YOU ONLY LEAVE ONCE',
  'SHELF DRY FINK CURSE': 'SELF DRIVING CARS',
  'WEIGH CUP TOOTHY FAX': 'WAKE UP TO THE FACTS',
  'HUG CUP CALLED SURE': 'HOOKUP CULTURE',
  'POLE EDDY CLICKER WRECKED': 'POLITICALLY CORRECT',
  'TECH A GEL PEL': 'TAKE A CHILL PILL',
  'PRETTY SHACK SCENT': 'BRITISH ACCENT',
  'ALL HUCK EACH ARM': 'A LUCKY CHARM',
  'PHASE POKE OFF HIS SHOAL': 'FACEBOOK OFFICIAL',
  'HIGH LIE KIT HER OF': 'I LIKE IT ROUGH',
  'TOY LIT ISSUE': 'TOILET TISSUE',
  'SORE HAY NODS ORE HEE': 'SORRY NOT SORRY',
  'SUN NAB SHAT FILLED HER': 'SNAPSHOT FILTER',
  'DEZ PUS SEED HOE': 'DESPACITO',
  'DONUT HAWK TWOS TRAIN JAZZ': 'DONOT TALK TO STRANGERS',
  'ENTER NET VAIN MUSS': 'INTERNET FAMOUS',
  'UTAH KIN TOMB HE': 'YOU TALKING TO ME ??',
  'FISH HITS BIN HERS': 'FIDGET SPINNERS',
  'CHEST IN BEE BEAR': 'JUSTIN BEIBER',
  'IGLOO TIN FRY YEE': 'GLUTEN -FREE',
  'EYE LOW VES ALLS AGE': 'I LOVE SAUSAGE',
  'FOYER INN FORM HAY SHUN': 'FOR YOUR INFORMATION'
}

# google = oauth.remote_app('google',
#                           base_url='https://www.google.com/accounts/',
#                           authorize_url='https://accounts.google.com/o/oauth2/auth',
#                           request_token_url=None,
#                           request_token_params={'scope': 'https://www.googleapis.com/auth/userinfo.email',
#                                                 'response_type': 'code', 'hd': "dhruvsoft.com"},
#                           access_token_url='https://accounts.google.com/o/oauth2/token',
#                           access_token_method='POST',
#                           access_token_params={'grant_type': 'authorization_code'},
#                           consumer_key=GOOGLE_CLIENT_ID,
#                           consumer_secret=GOOGLE_CLIENT_SECRET)




# def check_login(f):
#     @wraps(f)
#     def decorated_function(*args, **kwargs):
#         if session.get('access_token') is None:
#             return redirect(BASE_URL + url_for('login'))
#         return f(*args, **kwargs)

#     return decorated_function


@app.route('/')
def index():
    # access_token = session.get('access_token')
    # if access_token is None:
    #     return render_template("login.html")

    

    # access_token = access_token[0]


    # headers = {'Authorization': 'OAuth '+access_token}
    # req = Request('https://www.googleapis.com/oauth2/v1/userinfo',
    #               None, headers)
    # try:
    #     res = urlopen(req)
    # except Exception as  e:
    #     if e.code == 401:
    #         # Unauthorized - bad token
    #         session.pop('access_token', None)
    #         return redirect(url_for('login'))
    #     return res.read()

    return render_template("index.html")


@app.route("/q")
@cross_origin()
def ques():
    return random.choice(list(d.keys()))

@app.route("/ans")
@cross_origin()
def ans():
    p = request.args.get('p')
    return d[p]

@app.route('/login')
def login():
    callback=url_for('authorized', _external=True)
    return google.authorize(callback=callback)


# @app.route('/static/img/<logo>')
# def stati(logo):
#   return os.path.join("/static/img/"+logo)
# @app.route(REDIRECT_URI)
# @google.authorized_handler
# def authorized(resp):
#     access_token = resp['access_token']
#     session['access_token'] = access_token, ''
#     return redirect(url_for('index'))


# @google.tokengetter
def get_access_token():
    return session.get('access_token')


@app.route('/logout')
# @check_login
def logout():
    session.permanent = False
    session.pop('access_token', None)
    return redirect(BASE_URL + url_for('index'))


def main():
    app.run(debug=True)


if __name__ == '__main__':
    main()






