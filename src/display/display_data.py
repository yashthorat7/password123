from ..utils.utils import color_print
from ..utils.file_handler import read_json
from ..utils.table_handler import paginate_table
from ..encryption.decrypter import decrypt

tableClone = []

def display_data(master_key):
    """Decrypts and displays stored passwords in tabulated format."""
    try:
        global tableClone
        tableClone.clear()
        passwords = read_json('passwords.json')
        rows = []
        
        for i, entry in enumerate(passwords, start=1):
            website = entry.get('website', '')
            username = entry.get('username', '')
            encrypted_password = entry.get('password', '')
            
            decrypted_password = decrypt(encrypted_password, master_key)
            row_data = [str(i), website, username, decrypted_password]
            rows.append(row_data)
            tableClone.append(row_data)
         
        if not tableClone:
            color_print('No Data found\n', 'red')
            return False
            
        headers = ['Sr.no.', 'Website', 'Username', 'Password']
        styles = ['red', 'orange3', 'yellow', 'green']
        paginate_table(headers, tableClone, styles)
        return True
        
    except Exception as e:
        color_print(f'Error displaying data: {e}\n', 'red')
        return False 