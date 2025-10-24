"""
Monitor-modul för systemövervakning
Hanterar CPU, minne och diskanvändning
"""

import psutil

class SystemMonitor:
    """Klass för att övervaka systemresurser"""
    
    def __init__(self):
        """Initierar systemövervakaren"""
        self.is_monitoring = False
    
    def start_monitoring(self):
        """Startar övervakning"""
        self.is_monitoring = True
    
    def stop_monitoring(self):
        """Stoppar övervakning"""
        self.is_monitoring = False
    
    def get_cpu_usage(self):
        """
        Hämtar CPU-användning i procent
        
        Returns:
            float: CPU-användning i procent
        """
        return psutil.cpu_percent(interval=1)
    
    def get_memory_usage(self):
        """
        Hämtar minnesanvändning
        
        Returns:
            dict: Minnesstatistik med total, använt, procent
        """
        memory = psutil.virtual_memory()
        return {
            'total': memory.total / (1024 ** 3),  # GB
            'used': memory.used / (1024 ** 3),    # GB
            'percent': memory.percent
        }
    
    def get_disk_usage(self):
        """
        Hämtar diskanvändning
        
        Returns:
            dict: Diskstatistik med total, använt, procent
        """
        disk = psutil.disk_usage('/')
        return {
            'total': disk.total / (1024 ** 3),    # GB
            'used': disk.used / (1024 ** 3),      # GB
            'percent': disk.percent
        }
    
    def get_current_stats(self):
        """
        Hämtar alla aktuella systemstatistik
        
        Returns:
            dict: Komplett systemstatistik
        """
        memory = self.get_memory_usage()
        disk = self.get_disk_usage()
        
        return {
            'cpu': self.get_cpu_usage(),
            'memory_percent': memory['percent'],
            'memory_total': memory['total'],
            'memory_used': memory['used'],
            'disk_percent': disk['percent'],
            'disk_total': disk['total'],
            'disk_used': disk['used']
        }