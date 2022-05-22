from dropbox_methods import DropboxApp

REFRESH_TOKEN = "cmTG8X-z-SoAAAAAAAAAATifYiCEf0DJ6_q0mSD9XUvvBIufVJLEjKEp7czYVVgg"
AUTH = "Basic dmp5ejhnN2c5Z3JuMnZlOnBqemk3cWgyYTBna2t5cw=="

def before_feature(context, feature):
    """ 
    Create instance of DropboxApp class, which allows to access app folder in 
    dropbox by creating temporary access token from refresh token .
    """
    context.app = DropboxApp(REFRESH_TOKEN, AUTH)