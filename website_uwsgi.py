import sys
import os.path
sys.path.insert(0, os.path.dirname(__file__))
from website import app as application, init_for
import models

models.db.create_all()
init_for('production')
