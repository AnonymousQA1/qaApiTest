import requests

BOT_TOKEN = "8350380830:AAF8dGJCGjC9xPqoiXyYKlIP4B2eplyCXW8"
CHAT_ID = "-4999854678"
ALLURE_HTML_PATH = "./allure-report.html"

def send_allure_report():
    with open(ALLURE_HTML_PATH, "rb") as f:
        files = {"document": f}
        data = {
            "chat_id": CHAT_ID,
            "caption": "📝 Allure Test Report"
        }
        url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendDocument"
        response = requests.post(url, files=files, data=data)
        if response.status_code == 200:
            print("✅ Allure report sent to Telegram!")
        else:
            print(f"❌ Failed to send report: {response.text}")

if __name__ == "__main__":
    send_allure_report()