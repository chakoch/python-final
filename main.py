
import time
from monitor import SystemMonitor
from alarm import AlarmManager
from logger import Logger
from storage import AlarmStorage
from helpers import (
    wait_for_key, 
    clear_screen, 
    print_header, 
    print_separator,
    show_screen_with_header,
    get_valid_threshold,
    format_percentage,
    format_storage
)
from constants import (
    ALARM_TYPE_NAMES,
    ALARM_TYPE_WARNINGS,
    MENU_TO_ALARM_TYPE,
    MENU_TO_ALARM_TYPE_SWEDISH
)


def show_main_menu():
    print_header("SYSTEMÖVERVAKNINGSAPPLIKATION")
    print("1. Starta övervakning")
    print("2. Lista aktiv övervakning")
    print("3. Skapa larm")
    print("4. Visa larm")
    print("5. Starta övervakningsläge")
    print("6. Ta bort larm")
    print("0. Avsluta programmet")
    print_separator()

# Startar övervakningen om den inte redan är aktiv
def start_monitoring(monitor, logger):
    show_screen_with_header("STARTA ÖVERVAKNING")

    if monitor.is_monitoring:
        print("\nÖvervakning är redan aktiv!")
    else:
        monitor.start_monitoring()
        logger.log("Övervakning_startad")
        print("\n✓ Övervakning har startats!")
    
    wait_for_key()

# Visar aktuell övervakningsstatus
def list_monitoring_status(monitor):
    show_screen_with_header("ÖVERVAKNINGSSTATUS")
    
    if not monitor.is_monitoring:
        print("\nIngen övervakning är aktiv.")
    else:
        stats = monitor.get_current_stats()
        
        # Extrahera värden för bättre läsbarhet
        cpu_usage = stats['cpu']
        memory_percent = stats['memory_percent']
        memory_used = stats['memory_used']
        memory_total = stats['memory_total']
        disk_percent = stats['disk_percent']
        disk_used = stats['disk_used']
        disk_total = stats['disk_total']
        
        # Formatera och visa information
        print(f"\nCPU Användning: {format_percentage(cpu_usage)}")
        print(f"Minnesanvändning: {format_percentage(memory_percent)} "
              f"{format_storage(memory_used, memory_total)}")
        print(f"Diskanvändning: {format_percentage(disk_percent)} "
              f"{format_storage(disk_used, disk_total)}")
    
    print_separator()
    wait_for_key()

# Meny för att skapa nya larm
def create_alarm_menu(alarm_manager, logger):

    while True:
        show_screen_with_header("SKAPA LARM")
        print("1. Konfigurera larm - CPU användning")
        print("2. Konfigurera larm - Minnesanvändning")
        print("3. Konfigurera larm - Diskanvändning")
        print("0. Tillbaka till huvudmeny")
        print_separator()
        
        menu_choice = input("\nVälj alternativ: ").strip()
        
        if menu_choice == '0':
            break
        elif menu_choice in MENU_TO_ALARM_TYPE:
            alarm_type = MENU_TO_ALARM_TYPE[menu_choice]
            alarm_type_swedish = MENU_TO_ALARM_TYPE_SWEDISH[menu_choice]
            
            if create_single_alarm(alarm_manager, logger, alarm_type, alarm_type_swedish):
                break
        else:
            print("\n✗ Ogiltigt val!")
            wait_for_key()

# Hjälpfunktion för att skapa ett enskilt larm
# Extraherad för att minska upprepning i create_alarm_menu
def create_single_alarm(alarm_manager, logger, alarm_type, alarm_type_swedish):

    threshold = get_valid_threshold()
    
    if threshold is not None:
        alarm_manager.add_alarm(alarm_type, threshold)
        logger.log(f"{alarm_type}_Användningslarm_Konfigurerat_{threshold}_Procent")
        print(f"\n✓ Larm för {alarm_type_swedish} satt till {threshold}%")
        wait_for_key()
        return True
    else:
        wait_for_key()
        return False

# Visar alla konfigurerade larm
def show_alarms(alarm_manager):
    show_screen_with_header("KONFIGURERADE LARM")
    
    alarms = alarm_manager.get_sorted_alarms()
    
    if not alarms:
        print("\nInga larm är konfigurerade.")
    else:
        for alarm in alarms:
            alarm_display_name = ALARM_TYPE_NAMES.get(alarm.alarm_type, alarm.alarm_type)
            print(f"{alarm_display_name} {alarm.threshold}%")
    
    print_separator()
    wait_for_key()

# Meny för att ta bort befintliga larm
def remove_alarm_menu(alarm_manager, logger):
    show_screen_with_header("TA BORT LARM")
    
    alarms = alarm_manager.get_sorted_alarms()
    
    if not alarms:
        print("\nInga larm är konfigurerade.")
        wait_for_key()
        return
    
    print("\nVälj ett konfigurerat larm att ta bort:\n")
    
    # Visa alla larm med numrering
    display_alarm_list(alarms)
    
    print("0. Avbryt")
    print_separator()
    
    # Hantera användarens val
    handle_alarm_removal(alarms, alarm_manager, logger)
    
    wait_for_key()

# Visar listan över larm med numrering
def display_alarm_list(alarms):

    for index, alarm in enumerate(alarms, 1):
        alarm_display_name = ALARM_TYPE_NAMES.get(alarm.alarm_type, alarm.alarm_type)
        print(f"{index}. {alarm_display_name} {alarm.threshold}%")

# Hanterar logiken för att ta bort ett valt larm
def handle_alarm_removal(alarms, alarm_manager, logger):

    try:
        menu_choice = input("\nVälj larm att ta bort: ").strip()
        choice_number = int(menu_choice)
        
        if choice_number == 0:
            return
        elif 1 <= choice_number <= len(alarms):
            removed_alarm = alarms[choice_number - 1]
            alarm_manager.remove_alarm(removed_alarm)
            logger.log(f"{removed_alarm.alarm_type}_Larm_{removed_alarm.threshold}_Procent_Borttaget")
            print(f"\n✓ Larm har tagits bort!")
        else:
            print("\n✗ Ogiltigt val!")
    except ValueError:
        print("\n✗ Felaktig input!")

# Startar övervakningsläget
def monitoring_mode(monitor, alarm_manager, logger):
    show_screen_with_header("ÖVERVAKNINGSLÄGE")
    print("\nÖvervakningsläge startat!")
    logger.log("Övervakningsläge_startat")
    
    if not monitor.is_monitoring:
        monitor.start_monitoring()
    
    try:
        run_monitoring_loop(monitor, alarm_manager, logger)
    except KeyboardInterrupt:
        print("\n\nÅtergår till huvudmenyn...")
        logger.log("Övervakningsläge_avslutat")
        time.sleep(1)

# Kör huvudloopen för övervakningsläget
def run_monitoring_loop(monitor, alarm_manager, logger):

    while True:
        stats = monitor.get_current_stats()
        
        # Kontrollera och visa larm
        triggered_alarms = alarm_manager.check_alarms(stats)
        if triggered_alarms:
            display_alarm_warnings(triggered_alarms, logger)
        
        print("\rÖvervakning är aktiv, tryck Ctrl+C för att återgå till menyn...", 
              end='', flush=True)
        time.sleep(2)

# Visar larmvarningar för triggade larm
def display_alarm_warnings(triggered_alarms, logger):

    for alarm_type, threshold in triggered_alarms:
        warning_text = ALARM_TYPE_WARNINGS.get(alarm_type, alarm_type)
        print(f"\n{'*'*60}")
        print(f"*** VARNING, LARM AKTIVERAT, {warning_text} ÖVERSTIGER {threshold}% ***")
        print(f"{'*'*60}\n")
        logger.log(f"{alarm_type}_Användningslarm_aktiverat_{threshold}_Procent")

# Initialiserar alla komponenter som behövs för programmet
def initialize_components():

    logger = Logger()
    storage = AlarmStorage()
    alarm_manager = AlarmManager(storage)
    monitor = SystemMonitor()
    
    return logger, storage, alarm_manager, monitor

# Laddar tidigare sparade larm från fil
def load_previous_alarms(alarm_manager):

    print("\nLoading previously configured alarms...")
    alarm_manager.load_alarms()
    loaded_alarm_count = len(alarm_manager.get_all_alarms())
    
    if loaded_alarm_count > 0:
        print(f"✓ {loaded_alarm_count} larm inlästa.")

# Hanterar användarens menyval
def handle_menu_choice(menu_choice, monitor, alarm_manager, logger):

    if menu_choice == '1':
        start_monitoring(monitor, logger)
    elif menu_choice == '2':
        list_monitoring_status(monitor)
    elif menu_choice == '3':
        create_alarm_menu(alarm_manager, logger)
    elif menu_choice == '4':
        show_alarms(alarm_manager)
    elif menu_choice == '5':
        monitoring_mode(monitor, alarm_manager, logger)
    elif menu_choice == '6':
        remove_alarm_menu(alarm_manager, logger)
    elif menu_choice == '0':
        print("\nAvslutar programmet...")
        logger.log("Program_avslutat")
        return False
    else:
        print("\n✗ Ogiltigt val! Försök igen.")
        wait_for_key()
    
    return True

# Huvudfunktionen som startar programmet
def main():
    # Initiera komponenter
    logger, storage, alarm_manager, monitor = initialize_components()
    
    logger.log("Program_startat")
    
    # Ladda tidigare larm
    load_previous_alarms(alarm_manager)
    
    # Huvudloop
    while True:
        clear_screen()
        show_main_menu()
        
        menu_choice = input("\nVälj alternativ: ").strip()
        logger.log(f"Menyval_{menu_choice}")
        
        # Hantera menyval och avsluta om användaren väljer det
        if not handle_menu_choice(menu_choice, monitor, alarm_manager, logger):
            break


if __name__ == "__main__":
    main()