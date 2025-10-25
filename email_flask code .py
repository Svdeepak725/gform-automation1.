from flask import Flask
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

app = Flask(__name__)

@app.route('/')
def send_email():
    # --- Sender and Receiver Info ---
    from_addr = "svdeepak725@gmail.com"          # Your Gmail
    password = "qlce conc sfhy ersr"             # Your Gmail App Password

    # Recipients
    to_addrs = ["tech@themedius.ai"]             # Primary recipient
    cc_addrs = ["hr@themedius.ai"]               # CC recipient(s)

    # --- Email Setup ---
    msg = MIMEMultipart('alternative')
    msg['From'] = from_addr
    msg['To'] = ", ".join(to_addrs)
    msg['Cc'] = ", ".join(cc_addrs)
    msg['Subject'] = "Python (Selenium) Assignment - Deepak S"

    # --- HTML Email Body with Updated Links ---
    html_body = """
    <html>
    <body>
    <p>Hi Team,</p>

    <p>Please find my assignment submission below:</p>

    <ol>
      <li>Screenshots: <a href="https://drive.google.com/drive/folders/1MyINsDDPzMjfHpNsUZa3ClKDSvMAWiKG?usp=sharing" target="_blank">View Screenshots (Google Drive)</a></li>
      <li>Source Code: <a href="https://github.com/Svdeepak725/gform-automation" target="_blank">GitHub Repository</a></li>
      <li>Brief Documentation / Assignment: <a href="https://drive.google.com/file/d/12W0V-1x6y9YHzavjPxAlg6Fmw8ONV_cr/view?usp=drive_link" target="_blank">View Assignment (Google Drive)</a></li>
      <li>Resume: <a href="https://drive.google.com/file/d/15I_BrQW4MWyKSZMtIneLQF7QcqVVHb6z/view?usp=drive_link" target="_blank">View My Resume (Google Drive)</a></li>
      <li>Project Links: <a href="https://github.com/Svdeepak725/testing-and-automation" target="_blank">GitHub Projects</a></li>
      <li>Availability: Available full-time (10 AM – 7 PM) for the next 3–6 months.</li>
    </ol>

    <p>Regards,<br>
    <b>Deepak S</b></p>
    </body>
    </html>
    """

    msg.attach(MIMEText(html_body, 'html'))

    # --- Send Email ---
    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(from_addr, password)
        all_recipients = to_addrs + cc_addrs  # send to both TO and CC
        server.send_message(msg, from_addr=from_addr, to_addrs=all_recipients)
        server.quit()
        return "✅ Email sent successfully to tech@themedius.ai with CC to hr@themedius.ai!"
    except Exception as e:
        return f"❌ Failed to send email: {e}"

if __name__ == "__main__":
    app.run(debug=True)
