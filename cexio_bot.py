import cexapi
import json
import datetime

username = 'up110333889'
api_key = 'fEfTQtwWsWCCJWi636POfXiKRZA'
api_secret = '5u89fdRgY0Eyx8sd1Az5lmpl2I'

couple = 'XRP/BTC'


api = cexapi.api(username, api_key, api_secret)

#print json.dumps(api.balance(),sort_keys=True, indent=4)

balance = api.balance()
 

for key, value in sorted(balance.iteritems()):
	if isinstance(value,dict):
		for key2, value2 in value.iteritems():
			print key, "%s : %s"%(key2, value2)
	elif(key == "timestamp"):
		print "%s : %s"%(key, datetime.datetime.fromtimestamp(int(value)).strftime('%Y-%m-%d %H:%M:%S'))
	else:
		print "%s : %s"%(key, value)
	
