def create_file (filename):  
    with open(filename , 'w') as f:
         pass
    print("File created successfully!")
    print("="*25)

def write_file (filename, data):
    with open(filename , 'w') as f:
         f.write(data)
    print("File written successfully!")
    print("="*25)

def read_file (filename):
    with open(filename , 'r') as f:
         content = f.read()
    print("File content:")     
    print(content)
    print("="*25)

def append_file (filename, data):
    with open(filename , 'a') as f:
         f.write(data)
    print("Data appended successfully")
    print("="*25)


