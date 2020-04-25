# post = {"user_id":209, "message":"D5 E5 C5 C4 G4", "language":"English", "datetime":"20230215T124231Z",
# "location":(44.590533, -104.715556)}

# post2 = dict(message="SS Cotopaxi", language="English")
# print(post2)

# post2['user_id'] = 209
# post2['datetime'] = "19771116T093001Z"

# print(post['message'])

# print(post2.get('location', None)) # method that returns a pattern value 'None' if the dict does not have the key value

# if('location' in post2):
#     print(post2['location'])
# else:
#     print("The post2 does not have a location value.")

# try:
#     print(post2['location'])
# except KeyError:
#     print("Post2 does not have the key inserted")


# for key in post.keys():
#     value = post[key]
#     print(key, "=", value)

# for key, value in post.items():
#     print(key, "=", value)

# print(help(post.popitem))

# print(dir(dict))
# print(help(dict.update))

bicicletas = dict(mountain="white", velocidade="black", de_crianca="blue")

print(bicicletas)

novas_bicicletas = dict(mountain="green", velocidade="white", de_crianca="red")

bicicletas.update(novas_bicicletas)

print(bicicletas)