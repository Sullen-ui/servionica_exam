import argparse, json

def reading():
    try:
        open('storage.data', 'r', encoding = 'UTF-8')
    except IOError:
        open('storage.data', 'w+') 

    with open('storage.data', 'r', encoding = 'UTF-8') as f:           
        raw_data = f.read()
        if raw_data:
            return json.loads(raw_data)
        return {}

def writing(key, value):
    data = reading()
    if key in data:
        data[key] = data[key] + [value]
    else:
        data.update({key: [value]})

    with open('storage.data', 'w',encoding = 'UTF-8') as f:
        f.write(json.dumps(data))
        f.close()

def find(key, value):
    data = reading()
    if key in data and [value] is None:
        return None
    else:   
        return  data.get(key)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--key', help='Enter key name')
    parser.add_argument('--val', help='Enter value')
    args = parser.parse_args()

    if args.key and args.val:
        writing(args.key, args.val)
    elif args.key:
        print(*find(args.key, args.val) , sep=',')
    else:
        print('Non-existent argument')