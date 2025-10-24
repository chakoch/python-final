import json
import os
from alarm import Alarm

class AlarmStorage:
    # Hanterar lagring av larm i en JSON-fil

    def __init__(self, file_path="alarms.json"):
        self.file_path = file_path

    def save_alarms(self, alarms):

        try:
            alarm_data = [alarm.to_dict() for alarm in alarms]

            with open(self.file_path, 'w', encoding='utf-8') as f:
                json.dump(alarm_data, f, indent=4, ensure_ascii=False)

        except Exception as e:
            print(f"Fel vid sparande av larm: {e}")

    def load_alarms(self):
        if not os.path.exists(self.file_path):
            return []
        
        try:
            with open(self.file_path, 'r', encoding='utf-8') as f:
                alarm_data = json.load(f)
            
            # Konvertera dictionaries till Alarm-objekt
            alarms = [Alarm.from_dict(data) for data in alarm_data]
            return alarms
        
        except Exception as e:
            print(f"Fel vid laddning av larm: {e}")
            return []
    
    def clear_alarms(self):

        if os.path.exists(self.storage_file):
            os.remove(self.storage_file)