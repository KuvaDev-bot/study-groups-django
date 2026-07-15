# Study Groups

Elaborato di Back-end PPM 2026 - SINNI SEBASTIANO

## Tipo di progetto

Full-Stack Web Application

## Framework

Django 4.2

## Descrizione

Study Groups è una Web App per organizzare gruppi di studio autonomi.

Gli organizer possono creare, modificare ed eliminare i propri gruppi di studio, indicando materia, programma di studio, data, luogo e numero massimo di partecipanti.

Gli attendee possono visualizzare i gruppi disponibili, iscriversi se ci sono posti liberi, annullare le proprie iscrizioni e vedere la lista dei gruppi a cui sono iscritti.


## Funzionalità

### Utente non autenticato

- Visualizza elenco e dettagli dei gruppi di studio.
- Può creare un account o accedere.

### Attendee

- Visualizza gruppi di studio.
- Si iscrive a gruppi con posti disponibili.
- Non può iscriversi due volte allo stesso gruppo.
- Non può iscriversi a gruppi completi.
- Annulla una propria iscrizione.
- Visualizza la pagina "Le mie iscrizioni".

### Organizer

- Crea gruppi di studio.
- Modifica ed elimina solo i propri gruppi.
- Visualizza gli iscritti ai propri gruppi.
- Non può modificare o eliminare gruppi creati da altri organizer.

## Modello dei dati

- `User`: utente personalizzato con ruolo `ATTENDEE` oppure `ORGANIZER`.
- `StudyGroup`: gruppo di studio con materia, descrizione, data, luogo, capienza e organizer.
- `Registration`: iscrizione di un attendee a un gruppo di studio.

Relazioni principali:

- Un organizer può creare molti gruppi di studio.
- Un gruppo di studio può avere molte iscrizioni.
- Un attendee può essere iscritto a molti gruppi di studio.

## Installazione locale

Clona il repository e apri la cartella del progetto:

```bash
git clone https://github.com/KuvaDev-bot/study-groups-django.git
cd study-groups-django
```

Crea e attiva un virtual environment:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

Installa le dipendenze:

```bash
python -m pip install -r requirements.txt
```

Applica le migrazioni, se necessario:

```bash
python manage.py migrate
```

Avvia il server:

```bash
python manage.py runserver
```

Apri il progetto nel browser:

```text
http://127.0.0.1:8000/
```

## Database demo

Il file `db.sqlite3` è incluso nel repository e contiene dati demo: utenti, gruppi di studio e iscrizioni. Il progetto può quindi essere esplorato subito dopo il clone.

## Account demo

| Username | Password | Ruolo |
|---|---|---|
| `admin_demo` | `admin12345` | amministratore |
| `organizer_demo` | `organizer12345` | organizer |
| `attendee_demo` | `attendee12345` | attendee |
| `attendee_test` | `test12345` | attendee |

## Scenario di test

1. Accedi come `attendee_demo`.
2. Apri un gruppo non completo e clicca **Iscriviti al gruppo**.
3. Apri **Le mie iscrizioni** e verifica che il gruppo compaia nella lista.
4. Annulla l'iscrizione dal dettaglio del gruppo.
5. Accedi come `organizer_demo`.
6. Apri **I miei gruppi**, crea un gruppo e controlla la lista degli iscritti.
7. Prova ad accedere come organizer diverso e modificare un gruppo non tuo: l'operazione deve essere bloccata.
8. Prova a iscriverti a un gruppo completo: l'iscrizione deve essere bloccata.

## Deploy online

Il progetto è disponibile su Render:

https://study-groups-django.onrender.com
