import requests

#  post
r = requests.post("http://127.0.0.1:5000/post", data={'username': 'mike'})
print(f"r.text: {r.text}")
print(f"r.status_code: {r.status_code}")

# put
r = requests.put("http://127.0.0.1:5000/post", data={'username': 'mike'})
print(f"r.text: {r.text}")
print(f"r.status_code: {r.status_code}")

# delete
r = requests.put("http://127.0.0.1:5000/post", data={'username': 'mike'})
print(f"r.text: {r.text}")
print(f"r.status_code: {r.status_code}")

# get
r = requests.get("http://127.0.0.1:5000/post", data={'username': 'mike'})
print(f"r.text: {r.text}")
print(f"r.status_code: {r.status_code}")

"""
getは入れていないので、以下のエラーが出る。
error:
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 3.2 Final//EN">
<title>405 Method Not Allowed</title>
<h1>Method Not Allowed</h1>
<p>The method is not allowed for the requested URL.</p>
"""
print("############################")


# employee post
r = requests.post("http://127.0.0.1:5000/employee", data={'name': 'Mike'})
print(f"r.text: {r.text}")

# employee put
r = requests.put("http://127.0.0.1:5000/employee", data={'name': 'Mike', 'new_name': 'Michel'})
print(f"r.text: {r.text}")

r = requests.post("http://127.0.0.1:5000/employee", data={'name': 'Mike'})
print(f"r.text: {r.text}")

# employee get
r = requests.get("http://127.0.0.1:5000/employee/Michel")
print(f"r.text: {r.text}")

# employee delete
r = requests.delete("http://127.0.0.1:5000/employee", data={'name': 'Mike'})
print(f"r.text: {r.text}")

# employees get
r = requests.get("http://127.0.0.1:5000/employees")
print(f"r.text: {r.text}")