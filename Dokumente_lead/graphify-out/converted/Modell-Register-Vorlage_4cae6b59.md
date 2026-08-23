<!-- converted from Modell-Register-Vorlage.xlsx -->

## Sheet: Tabelle1
| Modell-ID | Modellname | Einsatzzweck | Kanal | Trainings datum | Letztes training | Nächstes Retraining | Aktuelle AUC | AUC bei Training | Status |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| M-001 | Lead-Scoring Q1 | Lead-Priorisierung | E-Mail | 2025-01-15 00:00:00 | 2025-01-15 00:00:00 | 2025-04-15 00:00:00 | 0.78 | 0.75 | Aktiv |  |  |  |  |  |  |  |
| M-002 | Churn-Prevention | Kündigungsrisiko | CRM | 2025-02-01 00:00:00 | 2025-02-01 00:00:00 | 2025-05-01 00:00:00 | 0.72 | 0.74 | Aktiv |  |  |  |  |  |  |  |
| M-003 | Produktempfehlung | Cross-Selling | Website | 2025-03-10 00:00:00 | 2025-03-10 00:00:00 | 2025-06-10 00:00:00 | 0.85 | 0.84 | Aktiv |  |  |  |  |  |  |  |
| - | - | - | - | - | - | - | - | - | - |  |  |  |  |  |  |  |
## Sheet: Tabelle3
| Modell-ID | Feature-Name | Feature-Typ | Datenquelle | Erlaubt für Vorhersage? |
| --- | --- | --- | --- | --- |
| M-001 | days_since_last_open | numerisch | E-Mail-Tool | Ja |
| M-001 | email_click_rate_7d | numerisch | E-Mail-Tool | Ja |
| M-001 | total_visits_30d | numerisch | Web-Analytics | Ja |
| M-001 | source_channel | kategorial | CRM | Ja |
| M-001 | age | numerisch | CRM | Nein (Bias-Risiko) |
## Sheet: Tabelle4
| Modell-ID | Auslöser | Aktion | Zuständig |
| --- | --- | --- | --- |
| Alle | AUC fällt um >0,1 | Automatische Benachrichtigung an Data Scientist | Data Scientist |
| Alle | AUC fällt um >0,15 nach Benachrichtigung | Modell deaktivieren, fallback auf Regel | Head of Marketing |
| M-001 | Kein Retraining nach 4 Monaten | Manueller Check durch Marketing Ops | Marketing Ops |
## Sheet: Tabelle2
| Datum | Modell-ID | Grund für Retraining | Neue AUC | AUC vorher | Veränderung | Verantwortlich |
| --- | --- | --- | --- | --- | --- | --- |
| 2025-04-15 00:00:00 | M-001 | Geplanter Zyklus | 0.82 | 0.78 | 0.039999999999999925 | M. Schmidt |
| - | - | - | - | - | - | - |