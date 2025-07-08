import sys
import os

# Assicurati che il path root del progetto sia incluso
sys.path.append('/home/abotabo007/check-list3')

from fleets import create_app

# Crea l'app Flask
app = create_app()

if __name__ == "__main__":
    app.run()


