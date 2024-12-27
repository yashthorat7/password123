# 🔐 Password123  
A low-weight CLI tool to manage your passwords!  
**Password123** provides seamless password generation, encrypted storage, and a fully interactive terminal interface.  


## ✨ Features  

- 🔑 **Magic Password Generation**: Effortlessly generate strong and meaningful passwords.  
- 🛡️ **Encrypted Storage**: Protect your passwords using **Cryptography Fernet**.  
- 🎨 **Interactive Terminal**: A colorful, user-friendly interface for smooth interaction.  
- ⚙️ **Customizable Options**: Configure settings to suit your needs.  

---

## 📂 Directory Structure  

```plaintext
🌟 Password123
│
├── 💾 data
│   ├── alters.json       # AlterList for password generation
│   ├── passwords.enc     # Encrypted password storage
│   ├── settings.json     # User-specific settings
│   └── words.json        # Wordlist for password generation
│
├── 📂 src
│   ├── display.py        # Terminal UI and interaction
│   ├── encryption.py     # Encryption and decryption logic
│   ├── generator.py      # Password generation algorithms
│   └── settings.py       # Configuration management
│
├── .env                  # Environment variables
├── .gitignore            # Git ignore rules
├── app.py 🚀             # Main application entry point
├── README.md             # Documentation
└── requirements.txt      # Python dependencies
```  


## 🚀 Getting Started  

Follow these steps to set up Password123 on your system:  

### 1️⃣ Clone the Repository  
Clone or pull the latest version of the code:  
```bash
git clone https://github.com/yashthorat7/Password123.git
```  

### 2️⃣ Install Dependencies  
Use `requirements.txt` to install the necessary Python packages:  
```bash
pip install -r requirements.txt
```  

### 3️⃣ Set Up the Environment  
Configure the `.env` file to store your encryption key:  
```plaintext
MASTER_KEY=<your key>
```  

## 🛠️ How to Use  

Run the main application:  
```bash
python app.py
```  

## 🔧 Key Commands

- **Generate Password**: Easily create secure passwords through the terminal.  
- **View Passwords**: Access and decrypt your stored passwords (authentication required).  
- **Update Settings**: Customize preferences, such as password length or complexity.  



## 🔒 Security Features  

- 🧩 **Cryptography Fernet**: Robust AES encryption for all your passwords.  
- 🗝️ **Environment Keys**: Sensitive keys are securely managed using the `.env` file.  
- 🛑 **Interactive Safeguards**: Confirmation prompts to prevent unintended actions.  



## 📋 Requirements  

- 🐍 **Python**: Version 3.8 or higher.  
- 📜 **Dependencies**: Listed in `requirements.txt`.  


## ❤️ Developed By  

👨‍💻 **Yash Thorat**  
Feel free to contribute, suggest improvements, or report issues!  


⭐ Don’t forget to **star** this repository if you find it useful! 