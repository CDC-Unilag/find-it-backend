import os

from flask_migrate import Migrate
from dotenv import load_dotenv

from find_it import create_app, db
from find_it.models import User

load_dotenv('dev.env')

app = create_app(os.environ.get('FlASK_ENV'))
migrate = Migrate(app, db)


@app.shell_context_processor
def make_shell_context():
    return dict(db=db, User=User)
