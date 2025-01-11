from ..utils import color_print, paginate_data
from ..encryption import DecryptPassword, ReadPasswords

tableClone = []

def display_data(master_key):
    try:
        global tableClone
        tableClone = []
        lines = ReadPasswords()
        rows = []
        
        for i, line in enumerate(lines, start=1):
            columns = line.strip().split('\t')
            if len(columns) == 3:
                website, username, password = columns
                decrypted_password = DecryptPassword(password, master_key)
                row_data = [str(i), website, username, decrypted_password]
                rows.append(row_data)
                tableClone.append(row_data)
                
        if not tableClone:
            color_print('No Data found\n', 'red')
            return False
            
        headers = ['Sr.no.', 'Website', 'Username', 'Password']
        styles = ['orange3', 'cyan', 'red', 'yellow']
        paginate_data(headers, rows, styles)
        return True
        
    except Exception as e:
        color_print(f'Error displaying data: {e}\n', 'red')
        return False 