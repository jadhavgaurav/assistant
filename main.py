import os

import eel

eel.init('www/')

os.system('start msedge.exe --app="http://localhost:5500/www/index.html"')

eel.start('www/index.html', mode = None, host = 'localhost', block=True)