import os
import requests
import urllib.parse
import urllib.request

LOGIN_URL = "https://trade.matsui.co.jp/mgap/login"
MEMBER_URL = "https://trade.matsui.co.jp/mgap/member"

matsui_id = os.environ["MATSUI_ID"]
matsui_password = os.environ["MATSUI_PASSWORD"]

sess = requests.Session()

params = {
    "user": matsui_id,
    "password": matsui_password,
}
encoded_params = urllib.parse.urlencode(params)
headers = {"Content-Type": "application/x-www-form-urlencoded"}

resp = sess.post(
    LOGIN_URL,
    headers=headers,
    data=encoded_params,
    allow_redirects=False,
)
resp.raise_for_status()
print(resp.status_code)
print(resp.headers)

resp = sess.get(MEMBER_URL)
resp.raise_for_status()
print(resp.status_code)
print(resp.headers)
