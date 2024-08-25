import json

def extract_route(request):
    lista_palavras = request.split()
    route = lista_palavras[1]
    route = route[1:]
    return route

def read_file(path):
    with open(path, 'rb') as file:
        return file.read()

def load_data(filename):
    path = f"data/" + filename
    with open(path, 'r') as file:
        data = json.load(file)
        return data
    
def load_template(filename):
    path = "templates/" + filename 
    with open(path, 'r') as file:
        string = file.read()
        return string

def add_note(note):
    path = "data/notes.json"
    with open(path, 'r+') as file:
        data = json.load(file)
        data.append(note)
        file.seek(0)
        json.dump(data, file, indent=4)
        file.truncate()


def build_response(body='', code=200, reason="OK", headers=''):
    if headers == '':
        res = f'HTTP/1.1 {code} {reason}\n\n{body}'
    else:
        res = f'HTTP/1.1 {code} {reason}\n{headers}\n\n{body}'
    return res.encode()











