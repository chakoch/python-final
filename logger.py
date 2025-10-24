
import os
from datetime import datetime

class Logger:
    
    # Initierar Logger-objektet och skapar loggfilen
    def __init__(self, log_dir="logs"):
        self.log_dir = log_dir
        self.log_file = None
        self._create_log_directory()
        self._create_log_file()
    
    # Skapar loggmappen om den inte finns
    def _create_log_directory(self):
    
        if not os.path.exists(self.log_dir):
            os.makedirs(self.log_dir)
    
    # Skapar en ny loggfil med dynamiskt namn baserat på datum och tid
    def _create_log_file(self):

        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        self.log_file = os.path.join(self.log_dir, f"log_{timestamp}.txt")
        
        # Skapa filen och lägg till header
        with open(self.log_file, 'w', encoding='utf-8') as f:
            f.write("="*60 + "\n")
            f.write("SYSTEMÖVERVAKNINGSAPPLIKATION - LOGGFIL\n")
            f.write(f"Skapad: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
            f.write("="*60 + "\n\n")

    # Loggar en händelse till loggfilen
    def log(self, message):

        timestamp = datetime.now().strftime("%d/%m/%Y_%H:%M:%S")
        log_entry = f"{timestamp}_{message}\n"
        
        try:
            with open(self.log_file, 'a', encoding='utf-8') as f:
                f.write(log_entry)
        except Exception as e:
            print(f"Fel vid loggning: {e}")

    # Returnerar sökvägen till aktuell loggfil
    def get_log_file_path(self):
        return self.log_file