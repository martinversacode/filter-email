# 📧 Email Domain Filter Tool by Martin Versa

**Ever found yourself overwhelmed with a messy list of emails?** The Email Domain Filter Tool is here to help you effortlessly classify and sort emails by domain and country\! This **Command Line Interface (CLI)** tool is built for efficiency and ease of use, giving you back control over your email data.

-----

## ✨ Key Features

  * **Automated Organization:** Automatically categorizes emails into separate folders based on their country domain (e.g., `.id` for Indonesia, `.uk` for United Kingdom, `.de` for Germany, etc.).
  * **Global Domain Support:** Recognizes and processes popular global domains such as Gmail, Yahoo, Outlook, ProtonMail, and many more.
  * **Beautiful CLI Interface:** Enjoy a pleasant user experience with a visually appealing and intuitive CLI, powered by the [Rich](https://rich.readthedocs.io/en/stable/) library.
  * **Built with Python:** Developed entirely in **Python 3**, ensuring cross-platform compatibility, reliability, and easy extensibility.
  * **Free & Open Source:** This tool is completely free to use, modify, and distribute under the MIT License. Feel free to contribute\!

-----

## 🚀 Getting Started

Using the Email Domain Filter Tool is straightforward\! Follow the steps below to get it up and running on your system.

### Prerequisites

Before you begin, ensure you have **Python 3** installed on your system. You can download it from the [official Python website](https://www.python.org/downloads/).

### 1\. Installation

#### 1.1 Clone the Repository

First, clone the project repository to your local machine using Git:

```bash
git clone https://github.com/martinversacode/filter-email.git
```

#### 1.2 Navigate to the Project Directory

Change into the newly created project directory:

```bash
cd filter-email
```

#### 1.3 Install Dependencies

Install the required Python libraries using `pip`:

```bash
pip install colorama rich
```

### 2\. How to Use

#### 2.1 Prepare Your Email List

Create a text file (e.g., `emails.txt`) containing the list of emails you want to filter. **Each email address must be on a new line.**

**Example `emails.txt`:**

```
john.doe@example.com
jane.smith@mail.co.uk
user@google.com
another.user@domain.id
test@example.de
info@business.net
```

#### 2.2 Run the Script

Once your email list is ready, run the main script from your terminal within the `filter-email` directory:

```bash
python filter_email.py
```

#### 2.3 Input Your Email List Path

The script will prompt you to enter the full path to your email list file. For example, if `emails.txt` is in the same directory as `filter_email.py`, you can simply type `emails.txt`.

```
Enter the path to your email list file (e.g., emails.txt): emails.txt
```

### 3\. Output

After the processing is complete, all sorted output will be saved inside a new folder named `result/` in the same directory as the script. Your emails will be neatly grouped into subfolders based on their country domain (e.g., `result/id/`, `result/uk/`, `result/com/` etc.).

-----

## 📞 Contact

Got questions or just want to say hello? Feel free to reach out to me on Telegram: [@martinversa](https://t.me/martinversa)

-----
