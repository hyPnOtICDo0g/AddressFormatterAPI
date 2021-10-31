import subprocess
from api.modules.api import api_init

app = api_init()
keep_alive = subprocess.Popen(["python3", "alive.py"])

if __name__ == '__main__':
   app.run(debug=True)
