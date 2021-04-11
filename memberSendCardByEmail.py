from email.mime.image import MIMEImage as _MIMEImage
from email.mime.multipart import MIMEMultipart as _MIMEMultipart
from email.mime.text import MIMEText as _MIMEText
import mimetypes as _mimetypes
from os import path as _path
import base64 as _base64
import smtplib as _smtplib
from simple_settings import settings as _settings


def encode_base64(s: str) -> str:
    encoded_text = _base64.b64encode(s.encode('utf-8')).decode('ascii')
    return f'=?utf-8?b?{encoded_text}?='


def format_named_address(name: str, adr: str) -> str:
    return f'{encode_base64(name)} <{adr}>'


if __name__ == "__main__":
    with open(_settings.CSV_FILE) as csv_file, open(_settings.MSG_FILE) as msg_file:
        # Smtp login:
        smtp = _smtplib.SMTP(_settings.SMPT_HOST, _settings.SMPT_PORT)
        try:
            smtp.starttls()  # enable TLS
            smtp.login(_settings.SMTP_USER, _settings.SMTP_PASSWORD)

            # Read message body:
            body = msg_file.read()

            for index, line in enumerate(csv_file):
                # Read names and emails:
                line = line.strip()
                if line:
                    name, email, _ = line.split(",")

                    # Create the container (outer) email message.
                    outer = _MIMEMultipart()
                    outer['Content-Type'] = 'text/plain; charset=utf-8'
                    outer['Subject'] = encode_base64(_settings.EMAIL_SUBJECT)
                    outer['From'] = format_named_address(_settings.EMAIL_FROM_NAME, _settings.EMAIL_FROM_ADR)
                    outer['To'] = format_named_address(name, email)

                    # Get source svg name:
                    source_pdf = _path.join(_settings.DEST_GENERATED_FOLDER, f"{index}.pdf")

                    # Set the content of the attachment:
                    ctype, encoding = _mimetypes.guess_type(source_pdf)
                    maintype, subtype = ctype.split('/', 1)
                    with open(source_pdf, 'rb') as fp:
                        msg = _MIMEImage(fp.read(), _subtype=subtype)

                    # Set the filename parameter
                    msg.add_header('Content-Disposition', 'attachment', filename=_settings.EMAIL_PDF)
                    outer.attach(msg)

                    # Add our message:
                    part1 = _MIMEText(body, 'plain', 'UTF-8')
                    outer.attach(part1)

                    # Now send the message
                    smtp.sendmail(_settings.SMTP_USER, email, outer.as_bytes())
        finally:
            smtp.quit()
