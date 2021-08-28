import os

class Config:
    
    '''
    General class configurations
    '''
    BASE_URL= 'https://leresi-blog-api.herokuapp.com/main{}'
    # BASE_URL='http://127.0.0.1:4000/main{}'
 
    SECRET_KEY = os.urandom(12)
    # SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://leresipitchdb:pitchidea@localhost/pitches'
  

    
    
class ProdConfig(Config):
    # SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL').replace("://", "ql://", 1)
    SECRET_KEY ='lkjelkjdskjdjwjepjdhah'

class DevConfig(Config):


    DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig
}