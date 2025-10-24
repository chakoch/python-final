# 🐍 Systemövervakningsapplikation i Python

> Ett terminalbaserat verktyg för att övervaka CPU-, minnes- och diskanvändning – byggt med objektorienterad Python och DevOps-inspirerad arkitektur.

---

## 👤 Projektinformation
**Namn:** Sam Jaudat  
**Klass:** DOE25 (Chas Academy)  
**Datum:** 24 oktober 2025  
**GitHub:** [chakoch/python-final](https://github.com/chakoch/python-final)

---

## 📘 1. Inledning
Applikationen visar aktuell CPU-, minnes- och diskanvändning direkt i terminalen.  
Programmet kan starta/stoppa övervakning, skapa och ta bort larm, samt köra ett automatiskt övervakningsläge där larm triggas om resursanvändningen överskrider angivna gränser.  
Syftet är att demonstrera objektorienterad programmering, filhantering och felhantering i Python – tillämpat på ett mindre men strukturerat DevOps-verktyg.

---

## 🧩 2. Planering och design
Projektet är baserat på **CRUD-principen** (Create, Read, Update, Delete) för att skapa en tydlig och verklighetsnära struktur, likt hur resurser hanteras i DevOps-flöden via API:er.  
Detta gjorde logiken enkel att följa och varje klass fick ett tydligt ansvar inom helheten.

---

## 🏗️ 3. Programstruktur

| Fil | Syfte |
|------|-------|
| `main.py` | Huvudmeny och programflöde |
| `monitor.py` | Hämtar systemdata via `psutil` |
| `alarm.py` | Hanterar skapande och kontroll av larm |
| `storage.py` | Sparar och laddar larm från JSON-fil |
| `logger.py` | Loggar händelser i programmet |
| `helpers.py` | Samlar återanvändbara funktioner (DRY-principen) |
| `constants.py` | Centrala konstanter för att undvika duplicering |

Kommunikationen sker via objekt som skickas mellan modulerna (t.ex. `AlarmManager`, `SystemMonitor`, `Logger`, `AlarmStorage`).

---

## ⚙️ 4. Viktiga funktioner och klasser

1. **`SystemMonitor.get_current_stats()`** – Hämtar CPU, RAM och diskdata via `psutil`.  
2. **`AlarmManager.check_alarms(stats)`** – Jämför realtidsdata mot tröskelvärden och triggar larm.  
3. **`helpers.py`** – Innehåller generella funktioner (`print_section()`, `format_stats()`, `get_int_input()` m.fl.) enligt **DRY-principen**.

---

## 🧰 5. Bibliotek och verktyg

| Bibliotek | Användning |
|------------|------------|
| `psutil` | Systemstatistik (CPU, minne, disk) |
| `os` | Filhantering och terminalrensning |
| `json` | Spara/läsa larm till/från fil |
| `sys`, `tty`, `termios`, `msvcrt` | Tangenttryckningar utan Enter |
| `time` | Loopar och pauser i övervakningsläge |

Versionshantering sker via **Git och GitHub**.

---

## 🧪 6. Testning och felsökning
- Varje menyval testades manuellt.  
- Larmtriggers verifierades med olika tröskelvärden.  
- Felinmatning hanteras med `try/except`.  
- JSON-filen testades vid både tillägg och borttagning.  

### Identifierade och lösta buggar:
1. **Logger-attribut:** fel namn → fixat till `self.log_file`.  
2. **Boolean-anrop:** `is_monitoring()` → ändrat till korrekt variabel.  
3. **MacOS-problem:** `psutil` krävde virtuell miljö (`venv`).  
4. **UX-bugg:** `wait_for_key()` omskriven för plattformsstöd (Windows/macOS/Linux).

Resultatet blev stabil körning och renare kod genom refaktorering och DRY-principer.

---

## 🧾 7. Resultat
✅ Övervakning kan startas och stoppas  
✅ Larm kan skapas, listas, tas bort och triggas  
✅ Data lagras permanent i JSON-fil  
✅ Konsistent och användarvänlig terminalvy  

---

## 💭 8. Reflektion och lärdomar
Jag har utvecklat min förståelse för **objektorientering**, **modulär design** och **underhållbar kod**.  
Tydlig ansvarsdelning, konsekvent namngivning och återanvändbara funktioner gjorde projektet mer robust och lätt att utöka.

---

## 🚀 9. Vidareutveckling
Möjliga förbättringar:
- 📬 Skicka notifieringar (e-post/Slack) vid larm.  
- 🧩 Enhetstester med `pytest`.  
- 🕓 Utöka loggern med tidsstämplar och loggnivåer.

---

## 🧠 10. Sammanfattning
Projektet visar hur Python kan användas för att skapa en robust, väldesignad och modulär systemövervakningslösning.  
Jag har implementerat OOP, JSON-lagring, felhantering, DRY-principen och Git-baserad versionshantering – vilket resulterar i ett portabelt, lättunderhållet och DevOps-inspirerat verktyg.

---

📎 **Repo:** [https://github.com/chakoch/python-final](https://github.com/chakoch/python-final)
