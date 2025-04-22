import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from dotenv import load_dotenv

load_dotenv()

def send_reset_email(to_email, to_name, reset_link):
    try:
        subject = "Password Reset | Blog System"
        body = f"""<center>
            <div style="font-family: Arial, sans-serif; padding: 20px;">
                <p>Hello {to_name},</p>
                <p>We received a request to reset your password. Please click the button below to continue:</p>

                <p style="margin: 20px 0;">
                    <a href="{reset_link}" style="background-color: #0d6efd; color: white; padding: 10px 20px; text-decoration: none; border-radius: 4px;">
                        Reset Password
                    </a>
                </p>

                <p>If the button doesn’t work, you can copy and paste this link into your browser:</p>
                <p style="word-break: break-all; color: #555;">{reset_link}</p>

                <p style="color: #e57878;">If you didn’t request a password reset, you can safely ignore this email.</p>
            </div></center>
        """

        msg = MIMEMultipart()
        msg['From'] = os.getenv('FORM_EMAIL')
        msg['To'] = to_email
        msg['Subject'] = subject
        msg.attach(MIMEText(body, 'html'))

        with smtplib.SMTP('smtp.gmail.com', 587) as server:
            if True:
                server.starttls()
            server.login(os.getenv('FORM_EMAIL'), os.getenv('FORM_PASSWORD'))
            server.send_message(msg)

        return True
    except Exception as e:
        print("Mail sending failed:", e)
        return False
