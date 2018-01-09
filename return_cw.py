"""
Main program
"""
import re
import os
from collections import namedtuple
import in_out
import exchange

#get names and emails using named tuples

NAMES_PATTERN = re.compile(r"""^\s+
                          (\w+)\s+
                          ([A-Za-z- ]+)\t
                          ([A-Za-z- ]+)\t
                          ([a-z-0-9]+\.[a-z-0-9]+\@student\.manchester\.ac\.uk)"""
                           , re.X)

# For testing use file with your own email
# NAMES_PATTERN = re.compile(r"""^\s+
#                           (\w+)\s+
#                           ([A-Za-z- ]+)\t
#                           ([A-Za-z- ]+)\t
#                           (joao.q.fonseca@gmail\.com)"""
#                            , re.X)



def get_students():
    """
    Get dictionary with student names and emails
    """
    student_dict = {}
    user = namedtuple('user',
                      ['first_name',
                       'last_name',
                       'email'])

    name_file = in_out.open_file()

    with open(name_file, 'r') as f_handle:
        for entry in iter(f_handle):
            match_name = NAMES_PATTERN.search(entry)
            if match_name:
                user_name = match_name.group(1)
                student = user._make(match_name.group(2, 3, 4))
                student_dict[user_name] = student
    return student_dict


def get_cwfiles():
    """
    Get dictionary with file paths and assignement names
    """
    cw_dict = {}
    user = namedtuple('user',
                      ['cw_file',
                       'assignement'])

    cw_list = in_out.open_files()

    for cw_file in cw_list:
        directory, file_name = os.path.split(cw_file)
        file_root, extension = os.path.splitext(file_name)
        file_pattern = re.compile(r"^(.+)_([a-z].+)_attempt_.+")
        match_file = file_pattern.search(file_root)
        if match_file:
            assignement = match_file.group(1)
            username = match_file.group(2)
            student = user._make([cw_file, assignement])
            cw_dict[username] = student
        else:
            print("Couldn't parse filename {}."
                  " Not a coursework file?").format(file_name)
    return cw_dict

def create_messages(students, cw_files, account):
    """
    Create messages to send out
    """
    msg_list = []

    for username in cw_files:
        assignement = cw_files[username].assignement
        cw_file = cw_files[username].cw_file
        email = students[username].email
        first_name = students[username].first_name
        last_name = students[username].last_name

        subject = ('{} coursework feedback').format(assignement)
        body = (
            '<p>Dear {},</p><p>Please see attached your '
            'marked {} coursework. Please see file for extra feedback.</p><p>Joao</p>'
            ).format(first_name, assignement)

        msg = exchange.compose_email(account, subject, body, email, cw_file)
        msg_list.append(msg)
    return msg_list

def return_cw():
    """
    Main function to send out coursework.
    """

    students = get_students()
    cw_files = get_cwfiles()
    login, passwd = in_out.get_username()
    account = exchange.get_account(login, passwd)
    msg_list = create_messages(students, cw_files, account)

    send_messages = input("Send {} messages? (y/(n))".format(len(msg_list)))

    if send_messages == 'y':
        for msg in msg_list:
            exchange.send_email(msg)
    else:
        quit()

if __name__ == '__main__':
    return_cw()
