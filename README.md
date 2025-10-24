Rapport – Systemutveckling i Python
Namn: Sam Jaudat
Klass: DOE25 (Chas Academy)
Datum: 24 oktober 2025
GitHub-länk: https://github.com/chakoch/python-final.git

1. Inledning
I detta projekt har jag utvecklat en övervakningsapplikation i Python som visar aktuell CPU-, minnes- och diskanvändning direkt i terminalen.
Programmet kan starta och stoppa övervakning, skapa och ta bort larm, samt köra ett övervakningsläge där larm triggas automatiskt om resursanvändningen överstiger en viss gräns. Syftet är att visa hur man kan använda objektorienterad programmering, filhantering och felhantering i Python för att bygga ett mindre men strukturerat DevOps-inspirerat verktyg.

2. Planering och design
Jag började med att analysera uppgiften och delade upp projektet enligt CRUD-designprincipen. Create, Read, Update and Delete. Jag använde CRUD som designprincip för att skapa en tydlig struktur som påminner om verkliga DevOps-flöden, där resurser (t.ex. larm) ofta hanteras via API:er på samma sätt.
Det innebar att jag identifierade vilka delar av applikationen som skapade data (skapande av larm), läste data (visning av systemstatus och larm), uppdaterade data (ändring av övervakningsstatus eller tröskelvärden) och raderade data (borttagning av larm). 
Denna uppdelning gjorde det enklare att strukturera logiken och förstå hur varje klass och funktion bidrar till helheten i applikationen.


3. Programstruktur
Programmet är uppdelat i flera moduler enligt en modulär och objektorienterad arkitektur.
Fil
Syfte
main.py
Huvudmeny, programflöde och användarinteraktion
monitor.py
Hämtar systeminformation med hjälp av psutil
alarm.py
Hanterar skapande, sortering och kontroll av larm
storage.py
Sparar och laddar larm till/från JSON-fil
logger.py
Loggar händelser i programmet
helpers.py
Samlar återanvändbara funktioner enligt DRY-principen
constants.py
centrala konstanter/mappningar för att undvika duplicerad data.


Kommunikationen mellan modulerna sker genom att objekt skickas som argument.
Exempel: main.py skapar instanser av AlarmManager, Logger, SystemMonitor och AlarmStorage, och dessa interagerar med varandra via metodanrop.


4. Viktiga funktioner eller klasser

Jag valde att lägga extra fokus på några centrala delar av koden:
SystemMonitor.get_current_stats()
Returnerar aktuell CPU-, RAM- och diskanvändning i en dictionary. Denna funktion använder psutil och utgör basen för både status vyn och larmhanteringen.
AlarmManager.check_alarms(stats)
Kontrollerar om något larm ska triggas genom att jämföra tröskelvärden mot realtidsdata. Den separerar logiken från presentationen, vilket gör koden renare och enklare att testa.
helpers.py
Jag samlade där gemensamma funktioner som print_section(), format_stats(), get_int_input() och render_alarms().
Detta följer DRY-principen (Don’t Repeat Yourself) och förbättrar läsbarheten avsevärt.

5. Bibliotek och verktyg
Jag använde både inbyggda och externa Python-bibliotek:
Bibliotek
Användning
psutil
Hämtar CPU-, minnes- och diskanvändning
os
Hantering av filer och rensning av terminalen
json
Sparar och läser in larm till/från fil
sys, tty, termios, msvcrt
Hanterar tangenttryckning utan Enter
time
Loopar och pauser i övervakningsläget

Versionshantering har skett med Git och GitHub.

6. Testning och felsökning
Jag testade varje menyval manuellt och verifierade larm triggers med olika tröskelvärden. Felaktig inmatning hanteras av get_int_input() och try/except. JSON-filen verifierades vid tillägg och borttagning av larm. Under utvecklingen identifierades och åtgärdades flera specifika buggar och förbättringspunkter:
Logger-attribut (self.log_file) – Ett felaktigt attributnamn i Logger-klassen orsakade att loggningen inte fungerade korrekt. Felet löstes genom att standardisera till self.log_file, vilket säkerställer att alla loggar skrivs till rätt fil.
Boolean-anrop (is_monitoring → variabel). Variabeln is_monitoring användes felaktigt som en funktion (is_monitoring()), vilket gav TypeError: 'bool' object is not callable. Felet rättades genom att ta bort parenteserna och hantera värdet som en ren boolean.
Miljöproblem (venv/psutil). På macOS uppstod problem med installationen av psutil på grund av systemhanterad Python. Detta löstes genom att skapa och aktivera en riktig virtuell miljö (python3 -m venv venv && source venv/bin/activate) och därefter installera biblioteket lokalt, vilket isolerar beroenden och förhindrar konflikter.
UX-förbättring (wait_for_key()) – Den tidigare “tryck valfri tangent”-lösningen fungerade endast i Windows. Funktionen byggdes om med plattformsanpassad logik: msvcrt används på Windows och sys/tty/termios på macOS/Linux. Därmed fungerar pauser och användarinmatning nu sömlöst på alla system utan att användaren behöver trycka Enter.
Efter dessa åtgärder kördes programmet stabilt i flera miljöer. Refaktorering Passet gav dessutom tydligare variabelnamn, färre specialfall (guard clauses) och borttagen duplicering via helpers.py och constants.py. Koden är nu mer robust, portabel och lättare att felsöka.
7. Resultat
Applikationen fungerar som planerat.
Övervakning kan startas och stoppas.
Larm kan skapas, listas, tas bort och triggas dynamiskt.
Data lagras permanent i en txt-fil.
Gränssnittet är tydligt och konsekvent med hjälp av helpers.py.


Jag är särskilt nöjd med att jag lyckades med att få projektet att följa både DRY-principen och CRUD-strukturen.

8. Reflektion och lärdomar
Jag har lärt mig mycket om objektorienterad programmering och modulär design i Python.
Att arbeta med flera filer och tydliga ansvarsområden gjorde det enklare att felsöka och utöka funktionaliteten.
Jag har också förstått hur viktigt det är att tänka på läsbarhet och underhåll, till exempel genom bra variabelnamn, konsekvent stil och återanvändbara hjälpfunktioner.

9. Möjliga förbättringar och vidareutveckling
Om jag hade mer tid skulle jag vilja:
Skicka notifieringar via e-post eller Slack när larm triggas.
Implementera enhetstester med unittest eller pytest.
Utöka loggern med tidsstämplar och loggnivåer.



10. Sammanfattning
Projektet visar hur Python kan användas för att bygga en robust och väldesignad systemövervakningslösning.
Jag har tillämpat objektorientering, felhantering, JSON-lagring, DRY-principen och Git-baserad versionshantering i praktiken.
Resultatet är ett program som är både funktionellt, pedagogiskt uppbyggt och lätt att vidareutveckla.

