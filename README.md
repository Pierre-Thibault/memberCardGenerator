# memberCardGenerator

This a small project I made for a non profit organization. It is an email card membership sender. The idea is to send to all members of the organization their member cards my email as a PDF file so they can print the card themselves.

SVG files are used as model for the cards. An CSV file contains the names and emails of the members to send cards to.

For this project I have two kind of card:

* Regular member
* Life time member

I have two fields on the card:

* Name
* Email

You will have to adapt the project for your needs. A basic knowledge of Python is needed.

## Requirements

* Bash
* Inkscape
* Python (I upgraded to 3.7.2)
* An SMTP server to send the emails

## Artifacts to produce

* SVG file regular member
* SVG file for life time member
* A text file (UFT-8) containing the text for the body of the email sent
* An CVS file containing the names and the addresses of the members

### SVG files

Create one SVG file for regular members and another for life time members. Use {name} and {email} as placeholder for the name and email of the member. Make {name} and {email} left justified. SVG image editor are using x and y coordinate to position text so {name} and {email} are not going to be well centered of right justified if their length changes.

### Text body file

Type the text for the body of the email and save it as a UTF-8 text file.

### CSV member list

Create a CVS file for the member list receiving cards. They are three column:

* Name of the member
* Member email
* Member type: 0 regular, 1 life time

## Preparing the project

You need to create your own settings and you also need to adap the bash script. Last but not least you need to install the Python requirements.

### Set the settings

Copy `settings_template.py` to `settings.py`. Edit `settings.py` to match the locations of your artifacts, change the STMP settings for your server and finally change the email settings for your messages.

### Adapt `memberCardConvertToPdf_template` bash script

Copy `memberCardConvertToPdf_template` to `memberCardConvertToPdf`. Change INKSCAPE to point the location of the Inkscape binary then change DEST_GENERATED_FOLDER to point the folder where the generated SVG files are.

Make the file executable: `chmod +x memberCardConvertToPdf`

### Install the Python requirements

You can install the Python requirements using `pip install -r requirements.txt`. I suggest to virualenv to do so.

## Generate the cards and send them

The first step is to generate the cards. To do so:

    python memberCardGenerator.py --simple-settings=settings
    
This will generated all the cards for the members. They are named 0.svg, 1.svg and so on.

Next generate the PDF files from the svg files:

    ./memberCardConvertToPdf
    
And finally send the emails:

    python memberSendCardByEmail.py --simple-settings=settings
