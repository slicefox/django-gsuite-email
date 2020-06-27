import base64
import threading

from django.conf import settings
from django.core.mail.backends.base import BaseEmailBackend
from django.core.mail.message import sanitize_address
from google.auth import exceptions
from google.oauth2 import service_account
from googleapiclient.discovery import build


class GSuiteEmailBackend(BaseEmailBackend):
    def __init__(self, fail_silently=False, **kwargs):
        self.fail_silently = fail_silently
        self.credentials = 'credentials/credentials.json' or settings.GSUITE_CREDENTIALS_FILE
        self.API_SCOPE =['https://www.googleapis.com/auth/gmail.send',]
        self.GSUITE_FROM_ACCOUNT = settings.GSUITE_FROM_ACCOUNT
        self.connection = None
        self._lock = threading.RLock()
    
    
    def _delegate_user(self,user_id):
        credentials = service_account.Credentials.from_service_account_file(self.credentials,scopes=self.API_SCOPE)
        credentials_delegated = credentials.with_subject(user_id)
        return credentials_delegated

    def send_messages(self, email_messages):
        """
        Send one or more EmailMessage objects and return the number of email
        messages sent.
        """
        if not email_messages:
            return 0
        with self._lock:
            num_sent = 0
            for message in email_messages:
                # maybe sanitize this message.from_email?
                new_conn_created = self.open(from_email=message.from_email)
                if not self.connection or new_conn_created is None:
                    # skip this message
                    continue

                
                sent = self._send(message)
                if sent:
                    num_sent += 1
            # not doing anything here
            # if new_conn_created:
            #     self.close()
        return num_sent



    def open(self,from_email=settings.GSUITE_FROM_ACCOUNT):
        """
        Ensure an open connection to the email server. Return whether or not a
        new connection was required (True or False) or None if an exception
        passed silently.
        """
        if self.connection and from_email==self.GSUITE_FROM_ACCOUNT:
            # Nothing to do if the connection is already open for same delegation
            return False

        try:
            credentials = self._delegate_user(from_email)
            self.connection = build("gmail","v1",credentials=credentials)
            return True
        except (exceptions.DefaultCredentialsError,exceptions.GoogleAuthError,exceptions.RefreshError,exceptions.TransportError):
            if not self.fail_silently:
                raise

    def close(self):
        """Close the connection to the email server."""
        if self.connection is None:
            return
        # do something
        return

    def _send(self, email_message):
        """A helper method that does the actual sending."""
        if not email_message.recipients():
            return False
        encoding = email_message.encoding or settings.DEFAULT_CHARSET
        # check this
        from_email = sanitize_address(email_message.from_email, encoding)            
        recipients = [sanitize_address(addr, encoding) for addr in email_message.recipients()]
        message = email_message.message()
        # https://developers.google.com/gmail/api/guides/sending#creating_messages
        raw = base64.urlsafe_b64encode(message.as_bytes())
        raw = raw.decode()
        binary_content = {'raw': raw}
        try:
            # need different login to check success
            self.connection.users().messages().send(userId='me', body=binary_content).execute()
            # self.connection.sendmail(from_email, recipients, message.as_bytes(linesep='\r\n'))
        except (exceptions.DefaultCredentialsError,exceptions.GoogleAuthError,exceptions.RefreshError,exceptions.TransportError):
            if not self.fail_silently:
                raise
            return False
        return True
