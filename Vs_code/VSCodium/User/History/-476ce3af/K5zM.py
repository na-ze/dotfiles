import requests
def ge_info_by_ip(ip='127.0.0.1'):
	try:
		pass
	except requests.exceptions.ConnectionError:
		print('[!])