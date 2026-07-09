# API_DOCUMENTATION

Version: 1.0  
Status: Zielarchitektur  
Projekt: Nurovelle  
Dokumenttyp: Technische Dokumentation

---

# 1. Zweck

Dieses Dokument beschreibt die geplanten API-Endpunkte des Nurovelle-Systems.

Abgedeckt werden:

- Website Leads
- Potenzialanalyse
- Reports
- Notion CRM
- Resend E-Mail
- Agenten
- Webhooks
- Retry Queue

---

# 2. API-Grundlagen

## Base Path

```http
/api
```

## Datenformat

```http
Content-Type: application/json
```

## Authentifizierung

Öffentliche Endpunkte:

- Lead-Formulare
- Analyse-Wizard

Geschützte Endpunkte:

- Admin
- Agenten
- Retry Queue
- CRM Sync

Empfohlene Schutzmechanismen:

- API Token
- Rate Limiting
- CSRF-Schutz für Formulare
- Server-seitige Validierung

---

# 3. Standard Response Format

## Erfolg

```json
{
  "success": true,
  "data": {},
  "error": null
}
```

## Fehler

```json
{
  "success": false,
  "data": null,
  "error": {
    "code": "VALIDATION_ERROR",
    "message": "Required field missing",
    "details": {}
  }
}
```

---

# 4. Lead API

## POST /api/leads

Erstellt oder aktualisiert einen Lead.

### Request

```json
{
  "email": "kunde@example.com",
  "first_name": "Max",
  "last_name": "Muster",
  "company_name": "Muster GmbH",
  "source": "Website",
  "source_detail": "Homepage CTA",
  "newsletter_opt_in": true,
  "privacy_consent": true
}
```

### Response

```json
{
  "success": true,
  "data": {
    "lead_id": "lead_123",
    "status": "New"
  },
  "error": null
}
```

### Validierung

Pflicht:

- email
- source
- privacy_consent

---

## GET /api/leads/{lead_id}

Lädt einen Lead.

### Response

```json
{
  "success": true,
  "data": {
    "lead_id": "lead_123",
    "email": "kunde@example.com",
    "status": "Nurturing",
    "segment": "Warm"
  },
  "error": null
}
```

---

## PATCH /api/leads/{lead_id}

Aktualisiert Lead-Daten.

### Request

```json
{
  "status": "Appointment Booked",
  "segment": "Hot",
  "tags": ["KI-Potenzialanalyse", "Engineering"]
}
```

---

# 5. Analysis API

## POST /api/analysis/start

Startet eine neue Analyse.

### Request

```json
{
  "lead_id": "lead_123",
  "analysis_type": "Basic",
  "industry_module": "Engineering"
}
```

### Response

```json
{
  "success": true,
  "data": {
    "analysis_id": "analysis_123",
    "status": "Started"
  },
  "error": null
}
```

---

## POST /api/analysis/{analysis_id}/answers

Speichert eine Antwort.

### Request

```json
{
  "question_id": "Q_AI_001",
  "answer_value": 4
}
```

### Response

```json
{
  "success": true,
  "data": {
    "answer_id": "answer_123",
    "progress": 42
  },
  "error": null
}
```

---

## POST /api/analysis/{analysis_id}/complete

Schließt eine Analyse ab.

### Request

```json
{
  "finalize": true
}
```

### Response

```json
{
  "success": true,
  "data": {
    "analysis_id": "analysis_123",
    "status": "Completed",
    "score_total": 72,
    "report_id": "report_123"
  },
  "error": null
}
```

---

## GET /api/analysis/{analysis_id}

Lädt Analyseinformationen.

### Response

```json
{
  "success": true,
  "data": {
    "analysis_id": "analysis_123",
    "analysis_type": "Basic",
    "status": "Completed",
    "score_total": 72,
    "scores": {
      "ai_maturity": 68,
      "process": 74,
      "data": 61,
      "infrastructure": 70,
      "risk": 38
    }
  },
  "error": null
}
```

---

# 6. Report API

## POST /api/reports/generate

Erzeugt einen Report für eine Analyse.

### Request

```json
{
  "analysis_id": "analysis_123",
  "format": "pdf"
}
```

### Response

```json
{
  "success": true,
  "data": {
    "report_id": "report_123",
    "pdf_url": "https://example.com/report.pdf"
  },
  "error": null
}
```

---

## GET /api/reports/{report_id}

Lädt Reportdaten.

### Response

```json
{
  "success": true,
  "data": {
    "report_id": "report_123",
    "analysis_id": "analysis_123",
    "pdf_url": "https://example.com/report.pdf",
    "created_at": "2026-06-15T10:00:00Z"
  },
  "error": null
}
```

---

# 7. CRM API

## POST /api/crm/sync/lead

Synchronisiert einen Lead mit Notion.

### Request

```json
{
  "lead_id": "lead_123"
}
```

### Response

```json
{
  "success": true,
  "data": {
    "notion_page_id": "notion_abc",
    "sync_status": "synced"
  },
  "error": null
}
```

---

## POST /api/crm/sync/analysis

Synchronisiert eine Analyse mit Notion.

### Request

```json
{
  "analysis_id": "analysis_123"
}
```

---

## PATCH /api/crm/status

Aktualisiert Pipeline-Status.

### Request

```json
{
  "lead_id": "lead_123",
  "status": "Appointment Booked"
}
```

---

# 8. Email API

## POST /api/email/send

Sendet eine einzelne E-Mail.

### Request

```json
{
  "lead_id": "lead_123",
  "template": "analysis_result_basic",
  "variables": {
    "report_url": "https://example.com/report.pdf"
  }
}
```

### Response

```json
{
  "success": true,
  "data": {
    "message_id": "msg_123",
    "status": "sent"
  },
  "error": null
}
```

---

## POST /api/email/sequence/start

Startet eine Nurturing-Sequenz.

### Request

```json
{
  "lead_id": "lead_123",
  "sequence_id": "seq_trust_001"
}
```

---

## POST /api/email/unsubscribe

Meldet einen Kontakt ab.

### Request

```json
{
  "email": "kunde@example.com",
  "reason": "user_clicked_unsubscribe"
}
```

---

# 9. Agent API

## POST /api/agents/multiprocessor/run

Startet den Multiprocessor.

### Request

```json
{
  "source_document_id": "doc_123",
  "source_type": "whitepaper"
}
```

---

## POST /api/agents/atomizer/run

Startet den Content Atomizer.

### Request

```json
{
  "source_document_id": "doc_123",
  "target_audience": "KMU",
  "funnel_stage": "Awareness"
}
```

---

## POST /api/agents/repurposing/run

Erstellt neue Content-Formate.

### Request

```json
{
  "atom_ids": ["atom_1", "atom_2"],
  "output_format": "linkedin_post",
  "platform": "LinkedIn"
}
```

---

## POST /api/agents/report/run

Startet den Report Agent.

### Request

```json
{
  "analysis_id": "analysis_123"
}
```

---

## POST /api/agents/appointment-guide/run

Erzeugt einen Gesprächsleitfaden.

### Request

```json
{
  "lead_id": "lead_123",
  "appointment_id": "appointment_123"
}
```

---

# 10. Appointment API

## POST /api/appointments/webhook

Verarbeitet Terminbuchungen.

### Request

```json
{
  "email": "kunde@example.com",
  "appointment_time": "2026-06-20T10:00:00+02:00",
  "meeting_url": "https://example.com/meeting"
}
```

### Response

```json
{
  "success": true,
  "data": {
    "appointment_id": "appointment_123",
    "lead_id": "lead_123"
  },
  "error": null
}
```

---

# 11. Webhook API

## POST /api/webhooks/resend

Verarbeitet Resend Events.

### Unterstützte Events

- delivered
- opened
- clicked
- bounced
- complained
- unsubscribed

### Request

```json
{
  "type": "email.clicked",
  "data": {
    "email": "kunde@example.com",
    "message_id": "msg_123",
    "link": "https://example.com"
  }
}
```

---

## POST /api/webhooks/notion

Optionaler Endpunkt für Notion Events.

### Request

```json
{
  "event_type": "page.updated",
  "page_id": "notion_abc"
}
```

---

# 12. Retry API

## POST /api/retry

Legt einen Retry-Eintrag an.

### Request

```json
{
  "action_type": "NotionSync",
  "payload": {
    "lead_id": "lead_123"
  },
  "error_message": "Notion API timeout",
  "max_retries": 5
}
```

---

## POST /api/retry/{retry_id}/run

Führt einen Retry manuell aus.

### Response

```json
{
  "success": true,
  "data": {
    "retry_id": "retry_123",
    "status": "Resolved"
  },
  "error": null
}
```

---

## GET /api/retry/pending

Lädt offene Retry-Einträge.

### Response

```json
{
  "success": true,
  "data": [
    {
      "retry_id": "retry_123",
      "action_type": "NotionSync",
      "retry_count": 2,
      "next_retry_at": "2026-06-15T12:00:00Z"
    }
  ],
  "error": null
}
```

---

# 13. Admin API

## GET /api/admin/health

Systemstatus.

### Response

```json
{
  "success": true,
  "data": {
    "api": "ok",
    "notion": "ok",
    "resend": "ok",
    "report_engine": "ok",
    "retry_queue": "ok"
  },
  "error": null
}
```

---

## GET /api/admin/metrics

Lädt technische Kennzahlen.

### Response

```json
{
  "success": true,
  "data": {
    "leads_total": 120,
    "analyses_completed": 84,
    "emails_sent": 430,
    "retry_pending": 2,
    "reports_failed": 0
  },
  "error": null
}
```

---

# 14. Fehlercodes

| Code | Bedeutung |
|---|---|
| VALIDATION_ERROR | Eingabe ungültig |
| AUTH_REQUIRED | Authentifizierung erforderlich |
| PERMISSION_DENIED | Zugriff verweigert |
| NOT_FOUND | Ressource nicht gefunden |
| DUPLICATE_LEAD | Lead existiert bereits |
| NOTION_API_ERROR | Notion Fehler |
| RESEND_API_ERROR | Resend Fehler |
| REPORT_GENERATION_ERROR | Reportfehler |
| AGENT_ERROR | Agentenfehler |
| RETRY_LIMIT_REACHED | Max. Retry erreicht |

---

# 15. Offene technische Folgeaufgaben

- Exakte Routen an bestehendes Backend anpassen
- Authentifizierungsmodell finalisieren
- Rate Limits definieren
- API Tests ergänzen
- OpenAPI-Spezifikation erzeugen
- Webhook Signaturprüfung ergänzen
