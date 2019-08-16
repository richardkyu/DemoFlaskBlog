import os
import secrets
from PIL import Image
from flask import url_for
from flask_mail import Message
from flaskblog import app, mail

def save_picture(form_picture):
    #Generate a random_hex with 8 bytes to append to the beginning of the extension.
    random_hex = secrets.token_hex(8)
    _, f_ext = os.path.splitext(form_picture.filename)
    picture_fn = random_hex + f_ext
    picture_path = os.path.join(app.root_path, 'static/profile_pics', picture_fn) 
    

    output_size = (250, 250)
    i = Image.open(form_picture)
    i.thumbnail(output_size)
    i.save(picture_path)

    return picture_fn


#Non-route method to send the reset email to a user.
#This utilizes another flask extension called flask-mail.
def send_reset_email(user):
    token = user.get_reset_token() #this is a method in the models.py (30 min expiry)
    msg = Message('Password Reset Request', 
                    sender = 'noreply@demo.com', 
                    recipients = [user.email])


#_ext will give the absolute link associated with the full domain, rather than just a relative url.
    msg.body = f''' To reset your password, please visit the following link.
{url_for('users.reset_token', token=token, _external = True)}

If you did not make this request, then ignore this email and no changes will be made.
'''
    mail.send(msg)
    
