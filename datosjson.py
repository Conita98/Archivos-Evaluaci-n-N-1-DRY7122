import json

with open('/home/devasc/labs/devnet-src/parsing/myfile.json', 'r') as f:
   ourjson = json.load(f)

access_token = ourjson['access_token']
expires_in = ourjson['expires_in']
refresh_token = ourjson['refresh_token']
refreshtokenexpires_in = ourjson['refreshtokenexpires_in']

print("Valor del access token: ", access_token)
print("Tiempo restante del access token: ", expires_in)
print("Valor del refresh token: ", refresh_token)
print("Tiempo restante del refresh token: ", refreshtokenexpires_in)
