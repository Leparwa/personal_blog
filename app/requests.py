def configure_request(app):
    global apiKey,base_url
    base_url = app.config['PITCHES_API_BASE_URL']