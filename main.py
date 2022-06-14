from flask import Flask, render_template, request
import smtplib
import requests

app = Flask(__name__)

url_endpoint = 'https://api.npoint.io/099f622924ab6663ad56'
response = requests.get(url=url_endpoint)
all_posts = response.json()

MY_EMAIL = 'burcealexandrandreea@gmail.com'
MY_PASSWORD = ''

@app.route('/')
def home():
    return render_template('index.html', all_posts=all_posts)

@app.route('/post/<int:index>')
def show_post(index):
    requested_post = None
    for blog_post in all_posts:
        if blog_post['id'] == index:
            requested_post = blog_post
    return render_template('post.html', post=requested_post)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact', methods=["GET", "POST"])
def contact():
    if request.method == 'POST':
        data = request.form
        print(data["username"])
        print(data["email"])
        print(data["phone"])
        print(data["message"])
        return render_template("contact.html", msg_sent=True)
    return render_template("contact.html", msg_sent=False)
    #     return "<h1>Successfully sent your message.</h1>    " \
    #            "<h2>Thank you!</h2>"
    # return render_template("contact.html", msg_sent=False)
def send_email(name, email, phone, message):
    email_message = f"Subject:New Message\n\n Name:{name}\n{email}\nPhone:{phone}\nMessage:{message}"
    with smtplib.SMTP('smtp.gmail.com') as connection:
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(MY_EMAIL, MY_EMAIL, email_message)
# @app.route('/contact')
# def contact():
#     return render_template('contact.html')
#
# @app.route("/form-entry", methods=["POST"])
# def receive_data():
#     name = request.form['username']
#     email = request.form['email']
#     phone = request.form['phone']
#     message = request.form['message']
#     # or data = request.form , print(data["name"]) etc
#     return f'<h1>Successfully sent your message </h1>'


if __name__ == '__main__':
    app.run(debug=True)