import requests
import json

URL_UPL = "https://content.dropboxapi.com/2/files/upload"
URL_GET = "https://api.dropboxapi.com/2/files/get_metadata"
URL_DEL = "https://api.dropboxapi.com/2/files/delete_v2"
URL_LST = "https://api.dropboxapi.com/2/files/list_folder"
URL_GEN_TOKEN = "https://api.dropboxapi.com/oauth2/token"

class DropboxApp:
    """ Class, which allows to get files metadata, upload and delete files from dropbox app folder """
    def __init__(self, token, auth):
        headers = {
            "Authorization": auth,
            "Content-Type": "application/x-www-form-urlencoded"
        }
        data = {
            "grant_type": "refresh_token",
            "refresh_token": token
        }
        self.token = requests.post(URL_GEN_TOKEN, headers=headers, data=data).json()["access_token"]
        self.basic_headers = {
            "Authorization": f"Bearer {self.token}",
            "Content-Type": "application/json"
        }
        self.latest_request = {}

    def upload_file(self, file):
        # Upload file.
        headers = {
            "Authorization": f"Bearer {self.token}",
            "Content-Type": "application/octet-stream",
            "Dropbox-API-Arg": f"{{\"path\":\"/{file}\"}}"
        }
        with open(f"files/{file}", "rb") as f:
            self.latest_request = requests.post(URL_UPL, headers=headers, data=f.read())

    def get_metadata(self, file):
        # Get file metadata.
        data = {
            "path": f"/{file}"
        }
        self.latest_request = requests.post(URL_GET, headers=self.basic_headers, data=json.dumps(data))

    def delete_file(self, file):
        # Delete file.
        data = {
            "path": f"/{file}"
        }
        self.latest_request = requests.post(URL_DEL, headers=self.basic_headers, data=json.dumps(data))

    def status_ok(self):
        # Check if request was completed with status code 200.
        return self.latest_request.status_code == 200

    def find_file(self, file):
        # Check if file exists in the app folder.
        data = {
            "path": ""
        }
        req = requests.post(URL_LST, headers=self.basic_headers, data=json.dumps(data))
        for dict in req.json()["entries"]:
            if dict["name"] == file:
                return True
        return False

    def check_upload(self, file):
        # Check if file was uploaded.
        return self.status_ok() and self.find_file(file)

    def check_metadata(self, file):
        # Check if metadata for the right file was obtained.
        return self.status_ok() and self.latest_request.json()['name'] == file

    def check_delete(self, file):
        # Check if file was deleted.
        return self.status_ok() and not self.find_file(file)