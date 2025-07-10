from flask import Flask, render_template, request, redirect, url_for, flash
import smtplib
from email.message import EmailMessage

app = Flask(__name__)
app.secret_key = '1111' 

# ====== Email Function ======
def send_email(name, email, message):
    msg = EmailMessage()
    msg['Subject'] = 'New Contact Form Message'
    msg['From'] = 'ahmedk32410@gmail.com'  # your Gmail address
    msg['To'] = 'ahmedk32410@gmail.com'    # your Gmail address (same or another)
    msg.set_content(f"Name: {name}\nEmail: {email}\n\nMessage:\n{message}")

    try:
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            smtp.login('ahmedk32410@gmail.com', 'lpvu ntte wikx nmiz')  # app password, NOT Gmail password
            smtp.send_message(msg)
        return True
    except Exception as e:
        print("Error sending email:", e)
        return False

# ====== Routes ======

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/projects')
def projects():
    return render_template('projects.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']

        if send_email(name, email, message):
            flash('✅ Message sent successfully!')
        else:
            flash('❌ Failed to send message. Please try again.')

    return render_template('contact.html')

if __name__ == '__main__':
    app.run(debug=True)