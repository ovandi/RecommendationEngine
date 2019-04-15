import os
basedir = ps.path.abspath(os.path.dirname(__file__))

class Config(object):
    # export DATABASE_URL="postgresql://localhost/postgres"
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or\
                              'postgresql://' + os.path.join(basedir,'postgres.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
