# 📩 Monday Motivation Emailer

A tiny Python automation script that sends a random motivational quote to your inbox every **Monday** (weekday index `0`) via Gmail's SMTP server.

## ✨ Features

- Picks a random quote from `quotes.txt`
- Sends it via Gmail SMTP using an App Password (no plaintext secrets in code)
- Easy to schedule with cron, Task Scheduler, or GitHub Actions

## 🛠️ Setup

1. **Clone the repo**
   ```bash
   git clone https://github.com/NinjaVinja/monday-motivation.git
   cd monday-motivation
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Create a Gmail App Password**
   - Enable 2-Step Verification on your Google Account
   - Go to **Google Account → Security → App Passwords**
   - Generate a new app password (do NOT use your real Gmail password)

4. **Configure environment variables**

   Copy `.env.example` to `.env` and fill in your real values:
   ```bash
   cp .env.example .env
   ```
   ```env
   EMAIL_ADDRESS=your_email@gmail.com
   EMAIL_APP_PASSWORD=your_16_char_app_password
   TO_ADDRESS=recipient_email@gmail.com
   ```

   ⚠️ `.env` is already listed in `.gitignore` — never commit it.

5. **Run it**
   ```bash
   python monday_motivation.py
   ```

## ⏰ Scheduling

To run it automatically every week, use:
- **Linux/Mac:** `cron`
- **Windows:** Task Scheduler
- **Cloud:** GitHub Actions scheduled workflow (`on: schedule`)

## 📂 Project Structure

```
monday-motivation/
├── monday_motivation.py
├── quotes.txt
├── requirements.txt
├── .env.example
├── .gitignore
└── README.md
```

## 🔒 Security Note

This project never hardcodes credentials. All secrets are loaded from a local `.env` file which is excluded from version control. Feel free to fork and use your own `.env`.

## 📄 License

MIT License — feel free to use and modify.
