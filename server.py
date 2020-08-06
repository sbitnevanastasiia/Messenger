from flask import Flask,request,Response
import time

app = Flask(__name__)

messages = [
    {'name': 'Dima', 'time': time.time(), 'text': 'Hello'},
    {'name': 'Kostya', 'time': time.time(), 'text': 'Hi'}
]

@app.route("/send", methods=['POST'])
def send():
    name = request.json.get('name')
    text = request.json.get('text')
    if not name or isinstance(name,str) or not text or isinstance(text,str):
        return Response(status=400)
    message = {'name': name, 'time': time.time(), 'text': text}
    messages.append(message)
    return Response(status=200)

def filter_by_key(elements,key,treshold):
    filtered_elements = []
    for element in elements:
        if element[key] > treshold:
            filtered_elements.append(element)
    return filtered_elements 


@app.route("/messages")
def messages_view():
    try:
        after = float(request.args['after'])
    except:
        return Response(status=400)
        
    filtered = filter_by_key(messages,key = 'time', treshold = after)
    return {
        'messages': filtered
    }

@app.route("/")
def hello():
    return "Hello, World!"

@app.route("/status")
def status():
    return {
        "status": True, "name": 'Name', "time": time.time()
    }

app.run()