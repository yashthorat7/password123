# 🔐 Password123  
A low-weight CLI tool to manage your passwords!  
**Password123** provides seamless password generation, encrypted storage, and a fully interactive terminal interface.  


## ✨ Features  

- 🔑 **Magic Password Generation**: Effortlessly generate strong and meaningful passwords.  
- 🛡️ **Encrypted Storage**: Protect your passwords using **Cryptography Fernet**.  
- 🎨 **Interactive Terminal**: A colorful, user-friendly interface for smooth interaction.  
- ⚙️ **Customizable Options**: Configure settings to suit your needs.  
- 🔄 **Import/Export Functionality**: Seamlessly back up or transfer your password data.

## 📂 Directory Structure  

```
🌟 Password123/
├── 💾 data/
│   ├── alters.json                 # Alters for passwords
│   ├── passwords.json              # Encrypted passwords storage
│   ├── settings.json               # Application settings
│   └── words.json                  # Word dictionary for generation
│
├── 🗃️ src/
│   ├── 🖥️ display/
│   │   ├── display.py              # Display module
│   │   ├── display_data.py         # Data display module
│   │   ├── display_menu.py         # Menu display handler
│   │   ├── handle_add.py           # Handle adding new data
│   │   ├── handle_remove.py        # Handle removing data
│   │   └── handle_search.py        # Handle search functionality
│   │
│   ├── 🔐 encryption/
│   │   ├── decrypter.py            # Data decryption module
│   │   ├── encrypter.py            # Data encryption module
│   │   └── store_data.py           # Secure data storage
│   │
│   ├── 🔢 generate/
│   │   ├── generate.py             # Core password generation logic
│   │   ├── generate_length.py      # Handle password length
│   │   ├── generate_menu.py        # Menu for password generation
│   │   └── generate_password.py    # Password creation logic
│   │
│   ├── ⚙️ settings/
│   │   ├── data_handler.py         # Handle settings data
│   │   ├── import_export.py        # Import/export settings
│   │   ├── master_key.py           # Master key management
│   │   ├── password_settings.py    # Password-related settings
│   │   ├── settings.py             # Core settings module
│   │   └── settings_menu.py        # Settings menu handler
│   │
│   └── ✂️ utils/
│       ├── file_handler.py         # File management utilities
│       ├── table_handler.py        # Table display utilities
│       └── utils.py                # General utility functions
│
├── README.md                       # Project documentation
├── 🚀 app.py                       # Main application entry point
└── requirements.txt                # Project dependencies
```
---

## 📄 Getting Started  

Follow these steps to set up Password123 on your system:  

### 1️⃣ Clone the Repository  
Clone or pull the latest version of the code:  
bash
```
git clone https://github.com/yashthorat7/Password123.git
```

### 2️⃣ Install Dependencies  
Use requirements.txt to install the necessary Python packages:  
bash
```
pip install -r requirements.txt
```

### 3️⃣ Set Master Key  
open data/settings.json and change this line (IamBatman is default)
bash
```
"masterKey": "<new_master_key>"
```

## 🛠️ How to Run  

Run the main application:  
bash
```
python app.py
```

---

## 🔒 Security Features  

- 🧩 **Cryptography Fernet**: Robust AES encryption for all your passwords.  
- 🛑 **Interactive Safeguards**: Confirmation prompts to prevent unintended actions.  


## 📋 Requirements  

- 🐍 **Python**: Version 3.8 or higher.  
- 📜 **Dependencies**: Listed in requirements.txt.  


## ❤️ Developed By  

👨‍💻 **Yash Thorat**  
Feel free to suggest improvements, or report issues!  

⭐ Don’t forget to **star** this repository if you find it useful!