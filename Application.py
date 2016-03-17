from libs.bottle import route, static_file, run
import json

import services.Activite.rest_activites as act
#from services.Activite.rest_activites import *
from services.equipement.Equipement import *
from services.installation.Installation import *


#TODO
activitesTab = act.allActivites()
for row in activitesTab:
    print(row[0])
