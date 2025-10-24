class Alarm:

    def __init__(self, alarm_type, threshold):
        self.alarm_type = alarm_type
        self.threshold = threshold
        self.triggered = False

    # Kontrollerar om larmet ska triggas baserat på aktuellt värde
    def check(self, current_value):

        if current_value >= self.threshold and not self.triggered:
            self.triggered = True
            return True
        elif current_value < self.threshold:
            self.triggered = False
        return False
    
    # Konverterar larm till dictionary för JSON-lagring
    def to_dict(self):

        return {
            'type': self.alarm_type,
            'threshold': self.threshold
        }
    
    # Skapar ett Alarm-objekt från en dictionary
    @staticmethod
    def from_dict(data):
        return Alarm(data['type'], data['threshold'])
    

class AlarmManager:

    def __init__(self, storage):
        self.alarms = []
        self.storage = storage
        self.last_triggered = {}

    def add_alarm(self, alarm_type, threshold):

        alarm = Alarm(alarm_type, threshold)
        self.alarms.append(alarm)
        self.save_alarms()

    def remove_alarm(self, alarm):

        if alarm in self.alarms:
            self.alarms.remove(alarm)
            self.save_alarms()

    def get_all_alarms(self):
        return self.alarms
    
    def get_sorted_alarms(self):
        return sorted(self.alarms, key=lambda alarm: alarm.alarm_type)
    
    def get_alarms_by_type(self, alarm_type):

        filtered = filter(lambda alarm: alarm.alarm_type == alarm_type, self.alarms)
        return sorted(filtered, key=lambda alarm: alarm.threshold, reverse=True)
    
    def check_alarms(self, stats):
        
        triggered = []

        # Mappar stats till larmtyper
        stat_mapping = {
            'CPU': stats['cpu'],
            'Memory': stats['memory_percent'],
            'Disk': stats['disk_percent']
        }
        
        # Kontrollera varje typ av larm
        for alarm_type, current_value in stat_mapping.items():
            type_alarms = self.get_alarms_by_type(alarm_type)
            
            if not type_alarms:
                continue
            
            # Hitta det närmaste larmet som är under aktuellt värde
            closest_alarm = None
            for alarm in type_alarms:
                if current_value >= alarm.threshold:
                    if closest_alarm is None or alarm.threshold > closest_alarm.threshold:
                        closest_alarm = alarm
            
            # Triggra endast det närmaste larmet
            if closest_alarm:
                # Kontrollera om detta är ett nytt larm som ska triggas
                if self.last_triggered.get(alarm_type) != closest_alarm.threshold:
                    triggered.append((alarm_type, closest_alarm.threshold))
                    self.last_triggered[alarm_type] = closest_alarm.threshold
            else:
                # Återställ om värdet är under alla trösklar
                if alarm_type in self.last_triggered:
                    del self.last_triggered[alarm_type]
        
        return triggered
    
    def save_alarms(self):
        self.storage.save_alarms(self.alarms)

    def load_alarms(self):
        self.alarms = self.storage.load_alarms()
        
