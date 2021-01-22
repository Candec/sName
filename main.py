import requests
import os
import json
import itertools

escape = ["quit", "q", "esc", "escape", "close", "salir"]
halp = ["ajuda", "ayuda", "sos", "help", "h"]

validSet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j",
			"k", "l", "m", "n", "o", "p", "q", "r", "s", "t",
			"u", "v", "w", "x", "y", "z", "0", "1", "2", "3",
			"4", "5", "6", "7", "8", "9", "_"]

# def createChars():
# 	lst = ["a"]
# 	while lst[-1] != 'z':
# 		char = chr(ord(lst[-1]) + 1)
# 		lst.append(char)
# 	return lst

# def createDigits():
# 	lst = ["0"]
# 	while lst[-1] != '9':
# 		intiger = chr(ord(lst[-1]) + 1)
# 		lst.append(intiger)
# 	return lst

# def charSet():
# 	validSig = ['_']
# 	valid = []
# 	valid += createChars() + createDigits() + validSig
# 	return valid

def sizeSelection():
	while True:
		try:
			x = input("\nHow many letter/numbers or underscores '_' should the name have?\n\n")
			if x in escape:
				break
			elif x in halp:
				print("this is help")
				continue
			else:
				numb = int(x)
			break
		except ValueError:
			print("error, invalid argument\n")
	return numb

def initial(numb):
	word = []
	x = input("\nType '1' if you want to start from the begining\nType '2' if you want to define the starting characters\n\n")
	if x == '1':
		i = 0
		while i < numb:
			word.append('a')
			i += 1
		return word
	elif x == '2':
		while True:
			x = input("Select your {} starting characters".format(numb))
			lenght = 0
			for i in x:
				length += length + 1
			if length == numb:
				for letter in x:
					if letter not in validSet:
						continue
					else:
						return list(x)
			elif length < numb:
				print("Need more characters")
				continue
			else:
				print("Too many characters")
				continue

# def product(*args, repeat=1):
# 	# product('ABCD', 'xy') --> Ax Ay Bx By Cx Cy Dx Dy
# 	# product(range(2), repeat=3) --> 000 001 010 011 100 101 110 111
# 	pools = [tuple(pool) for pool in args] * repeat
# 	result = [[]]
# 	for pool in pools:
# 		result = [x+[y] for x in result for y in pool]
# 	for prod in result:
# 		yield tuple(prod)


# def main():
# 	size = sizeSelection()
# 	initWord = initial(size)

# for val in com:
# 	finalstr += ',' + ''.join(val)

# nameLst = finalstr.split(",",100)

# for x in nameLst:
# 	print(x + "\n\n")

# print("%(first)d combinaciones encontradas"% {"first":i})


# To set your enviornment variables in your terminal run the following line:
# export 'BEARER_TOKEN'='<your_bearer_token>'


def auth():
	return os.environ.get("BEARER_TOKEN")


# def create_url(username):
def create_url(usernames):
    # Specify the usernames that you want to lookup below
    # You can enter up to 100 comma-separated values.
    #username = "jCandec"
    # user_fields = "user.fields=description,created_at"
    # User fields are adjustable, options include:
    # created_at, description, entities, id, location, name,
    # pinned_tweet_id, profile_image_url, protected,
    # public_metrics, url, username, verified, and withheld
	# url = "https://api.twitter.com/2/users/by/username/{}".format(username)
    # url = "https://api.twitter.com/2/users/by/username/{}".format(username)
	# url = "https://api.twitter.com/2/users/by?{}".format(usernames)
	url = "https://api.twitter.com/2/users/by?usernames={}".format(usernames)
	return url


def create_headers(bearer_token):
	headers = {"Authorization": "Bearer {}".format(bearer_token)}
	return headers


def connect_to_endpoint(url, headers):
	response = requests.request("GET", url, headers=headers)
	print(response.status_code)
	if response.status_code != 200:
		raise Exception(
			"Request returned an error: {} {}".format(
				response.status_code, response.text
			)
		)
	return response.json()

def divide_chunks(l, n):

	# looping till length l
	for i in range(0, len(l), n):
		return l[i:i + n]

def main():
	nameList = itertools.product(validSet, repeat = sizeSelection())
	bearer_token = auth()
	n = 100
	s = ","
	start_index = 0
	allNames = []
	while i < 1000:

	for x in nameList:
		allNames.append(''.join(x))
	hundredNames = [allNames[i * n:(i + 1) * n] for i in range((len(allNames) + n - 1) // n )]
	for y in hundredNames:
		string = s.join(y)
		url = create_url(string)
		headers = create_headers(bearer_token)
		json_response = connect_to_endpoint(url, headers)
		with open('answer.json', 'a') as f:
			f.write(json.dumps(json_response, indent=4, sort_keys=True))
		# print(json.dumps(json_response, indent=4, sort_keys=True))
	f.close()



if __name__ == "__main__":
	main()
