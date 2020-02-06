from state import State
from button import Button

from googleapiclient.http import MediaFileUpload
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

import pickle
import os.path

class GoogleDriveState(State):
    creds = None
    SCOPES = ["https://www.googleapis.com/auth/drive.file"]

    def on_load(self):
        super().on_load()

        self.upload_data_file_button = Button(self.app.win, pos=(0, 0.5), size=(1, 0.5), text="Upload Data File", on_click=self.upload_file)
        self.new_data_file_button = Button(self.app.win, pos=(0,0), size=(1, 0.5), text="New Data File", on_click=print)
        self.back_button = Button(self.app.win, pos=(0, -0.5), size=(1, 0.5), fillColor=(1,0,0), text="Back", on_click=self.return_to_admin_state)
        
        self.subviews = [self.upload_data_file_button, self.new_data_file_button, self.back_button]
        
    def return_to_admin_state(self):
        self.app.transition_to("admin")

    def get_creds(self):
        if os.path.exists('token.pickle'):
            with open('token.pickle', 'rb') as token:
                self.creds = pickle.load(token)
        if not self.creds or not self.creds.valid:
            if self.creds and self.creds.expired and self.creds.refresh_token:
                self.creds.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_config(
                    'client_secret_49278191793-faegrgao52qm3runfg6nfadrrgnptflv.apps.googleusercontent.com.json',
                    self.SCOPES)
                self.creds = flow.run_local_server(port=0)

            with open('token.pickle', 'wb') as token:
                pickle.dump(self.creds, token)

    def upload_file(self):
        file_metadata = {'name': 'test.csv'}
        media = MediaFileUpload('Constants/subject-data.csv', mimetype='text/csv')

        drive_service = build('drive', 'v3', credentials=self.creds)

        file = drive_service.files().create(body=file_metadata, media_body=media, fields='id').execute()

        print('File ID: ' + file.get('id'))

