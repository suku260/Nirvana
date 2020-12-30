
import os    
    
def setup():
        print("Getting the environment ready...")
        os.mkdir('Nirvana_Project')
        os.mkdir("Nirvana_Project/files")
        os.mkdir("Nirvana_Project/images")
        os.system("touch Nirvana_Project/info.py")
        info = open('Nirvana_Project/info.py', 'w') 
        info.write('''paths=[]
db=['sqlite3']
ip="127.0.0.1"
port="80"
def setup_info():
    stuff=[ip,port]
    return stuff
def paths():
    return paths
        ''')
        info.close()

        os.system("touch Nirvana_Project/paths.py")
        print("environment ready")

setup()