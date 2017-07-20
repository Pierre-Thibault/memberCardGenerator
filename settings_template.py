# -*- coding: utf-8 -*-

# Copy this file and renamed it settings.py and change the values for your own project

# The csv file containing the information about the member.
# There is three columns: The name, the email and the member type: 0 regular, 1 life time
CSV_FILE = "path to csv file"

# The svg file for regular member. {name} and {email} are going to be replaced with the corresponding values from the
# csv file
SVG_FILE_REGULAR = "path to svg regular member file"

# Same as SVG_FILE_REGULAR but for life time member
SVG_FILE_LIFE_TIME = "path to svg life time member file"

# Destination folder where the member cards will be generated. If the folder does not exist yet it will be created.
DEST_GENERATED_FOLDER = "path to folder that will contain the generated files"

# The message file used as the text body for the email message. UTF-8.
MSG_FILE = "/Users/pierre/Documents/LPA/CA/carte_membre_msg"

# SMTP configuration
SMPT_HOST = "myserver.com"
SMPT_PORT = 587
SMTP_USER = "user_name"
SMTP_PASSWORD = "password"

# Email configuration
EMAIL_FROM = "some_email@something.com"
EMAIL_SUBJECT = "subject"
EMAIL_PDF = "name of attachment file.pdf"
