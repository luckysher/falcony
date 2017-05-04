# settings for falcony Rest api

APP_NAME = 'Falcony'

dbConfig = {
    'DbName': 'falcony',
    'Username': 'falcony',
    'Password': 'falcony',
    'Host': 'localhost',
    'Port': 5432
}

db_url = 'postgresql://%s:%s@%s/%s' % (dbConfig['Username'], dbConfig['Password'], dbConfig['Host'], dbConfig['DbName'])
