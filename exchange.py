"""
Functions for generating and sending emails
"""
import os
from exchangelib import (DELEGATE, Account, Credentials, HTMLBody,
                         Message, FileAttachment, Mailbox)

def get_account(email, password):
    """ Log in and get access to email account """
    credentials = Credentials(username=email, password=password)
    account = Account(primary_smtp_address=email, credentials=credentials,
                      autodiscover=True, access_type=DELEGATE)
    return account

def compose_email(account, subject, body, recipient, attachment_file_path):
    """ Create html email and attach file"""
    msg = Message(
        account=account,
        folder=account.sent,
        subject=subject,
        body=HTMLBody(body),
        to_recipients=[Mailbox(email_address=recipient)]
    )
    fn = os.path.basename(attachment_file_path)
    with open(attachment_file_path, 'rb') as f:
        attch_file = FileAttachment(name=fn, content=f.read())
    msg.attach(attch_file)
    return msg

def send_email(msg):
    """ Send email """
    msg.send_and_save()
