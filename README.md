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

Clonare questo repository:

```bash
git clone URL_DEL_TUO_REPOSITORY
cd study_groups