import requests
import send_email
import variables

def send_mail(msg):
    formatted_message = f"""\
Subject: News on Your Topics

{msg}
    """
    send_email.email(formatted_message, "utf-8")

# Set up url
topic = "artificial_intelligence"
url = f"https://newsapi.org/v2/everything?q={topic}&sortBy=publishedAt&apiKey={variables.get_api_key()}&language=en"

# Make request to get a dict
request = requests.get(url)
content = request.json()

message = ""
for article in content["articles"]:
    message += (f"{article["title"]}\n"
                f"{article["description"]}\n"
                f"{article["url"]}\n\n")

send_mail(message)