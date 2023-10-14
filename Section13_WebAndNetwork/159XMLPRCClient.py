import xmlrpc.client

# create an instance of the ServerProxy class
proxy = xmlrpc.client.ServerProxy("http://localhost:8000")

# call the methods exposed by the server
result = proxy.add(2, 3)
print(result)


with xmlrpc.client.ServerProxy("http://localhost:8000") as proxy:
    print(proxy.add(2, 3))
    print(proxy.multiply(2, 3))


# なんか処理が遅い
