import smtplib

def generate_message(name):
    return f"Subject: Hello {name}\n\nHi {name}, this is an AI automated email!"

email = "your_email@gmail.com"
password = "your_app_password"
receiver = "receiver@gmail.com"

message = generate_message("Carlson")

server = smtplib.SMTP("smtp.gmail.com", 587)
server.starttls()
server.login(email, password)
server.sendmail(email, receiver, message)

print("Email sent successfully!")
