# Pack C — Prompt Bank

## System Preface

```
You are an information-extraction assistant.
Extract every event mentioned in the text.
Return exactly the requested format. No explanations.
```

## Shells

### Plain shell

```
TASK: Extract every event in the text. For each event, write a line:
Event type: <TYPE>. Trigger: <TRIGGER>.

Text:
"{CHUNK}"

Rules:
- Include ALL events mentioned.
- One line per event; no extra commentary.
```

### <EVENTSEP> shell

```
TASK: Extract every event in the text. For each event, write a line:
<EVENTSEP> Event type: <TYPE>. Trigger: <TRIGGER>.

Text:
"{CHUNK}"

Rules:
- Use <EVENTSEP> exactly as the separator.
- Include ALL events mentioned.
- One line per event; no extra commentary.
```

## PLAIN — Shot Variants

### plain — 0-shot

> Paste this in a fresh chat. Replace `{{CHUNK}}` with your text.

```
You are an information-extraction assistant.
Extract every event mentioned in the text.
Return exactly the requested format. No explanations.

TASK: Extract every event in the text. For each event, write a line:
Event type: <TYPE>. Trigger: <TRIGGER>.

Text:
"{CHUNK}"

Rules:
- Include ALL events mentioned.
- One line per event; no extra commentary.
```

### plain — 1-shot

> Paste this in a fresh chat. Replace `{{CHUNK}}` with your text.

```
You are an information-extraction assistant.
Extract every event mentioned in the text.
Return exactly the requested format. No explanations.

Example
Text: "The project was an ambitious and risky venture aiming to conquer, with a thousand men, a kingdom with a larger regular army and a more powerful navy."
Output:
Event type: Self_motion. Trigger: venture.
Event type: Aiming. Trigger: aiming.
Event type: Conquering. Trigger: conquer.

--- Now do the same for:

TASK: Extract every event in the text. For each event, write a line:
Event type: <TYPE>. Trigger: <TRIGGER>.

Text:
"{CHUNK}"

Rules:
- Include ALL events mentioned.
- One line per event; no extra commentary.
```

### plain — 3-shot

> Paste this in a fresh chat. Replace `{{CHUNK}}` with your text.

```
You are an information-extraction assistant.
Extract every event mentioned in the text.
Return exactly the requested format. No explanations.

Example
Text: "The project was an ambitious and risky venture aiming to conquer, with a thousand men, a kingdom with a larger regular army and a more powerful navy."
Output:
Event type: Self_motion. Trigger: venture.
Event type: Aiming. Trigger: aiming.
Event type: Conquering. Trigger: conquer.
---
Example
Text: "The sea venture was the only desired action that was jointly decided by the"
Output:
Event type: Self_motion. Trigger: venture.
Event type: Self_motion. Trigger: action.
Event type: Deciding. Trigger: decided.
---
Example
Text: "The murder of Leigh Leigh, born Leigh Rennea Mears, occurred on 3 November 1989 while she was attending a 16-year-old boy's birthday party at Stockton Beach, New South Wales, on the east coast of Australia."
Output:
Event type: Coming_to_be. Trigger: occurred.
Event type: Committing_crime. Trigger: murder.
Event type: Participation. Trigger: attending.

--- Now do the same for:

TASK: Extract every event in the text. For each event, write a line:
Event type: <TYPE>. Trigger: <TRIGGER>.

Text:
"{CHUNK}"

Rules:
- Include ALL events mentioned.
- One line per event; no extra commentary.
```

### plain — 5-shot

> Paste this in a fresh chat. Replace `{{CHUNK}}` with your text.

```
You are an information-extraction assistant.
Extract every event mentioned in the text.
Return exactly the requested format. No explanations.

Example
Text: "The project was an ambitious and risky venture aiming to conquer, with a thousand men, a kingdom with a larger regular army and a more powerful navy."
Output:
Event type: Self_motion. Trigger: venture.
Event type: Aiming. Trigger: aiming.
Event type: Conquering. Trigger: conquer.
---
Example
Text: "The sea venture was the only desired action that was jointly decided by the"
Output:
Event type: Self_motion. Trigger: venture.
Event type: Self_motion. Trigger: action.
Event type: Deciding. Trigger: decided.
---
Example
Text: "The murder of Leigh Leigh, born Leigh Rennea Mears, occurred on 3 November 1989 while she was attending a 16-year-old boy's birthday party at Stockton Beach, New South Wales, on the east coast of Australia."
Output:
Event type: Coming_to_be. Trigger: occurred.
Event type: Committing_crime. Trigger: murder.
Event type: Participation. Trigger: attending.
---
Example
Text: "Her naked body was found in the sand dunes nearby the following morning, with severe genital damage and a crushed skull."
Output:
Event type: Bodily_harm. Trigger: crushed.
Event type: Damaging. Trigger: damage.
Event type: Know. Trigger: found.
---
Example
Text: "Matthew Grant Webster, an 18-year-old who acted as a bouncer at the event, pleaded guilty to her murder and was sentenced to 20 years in prison with a 14-year non-parole period."
Output:
Event type: Legal_rulings. Trigger: sentenced.
Event type: Request. Trigger: pleaded.
Event type: Committing_crime. Trigger: murder.

--- Now do the same for:

TASK: Extract every event in the text. For each event, write a line:
Event type: <TYPE>. Trigger: <TRIGGER>.

Text:
"{CHUNK}"

Rules:
- Include ALL events mentioned.
- One line per event; no extra commentary.
```

## EVENTSEP — Shot Variants

### eventsep — 0-shot

> Paste this in a fresh chat. Replace `{{CHUNK}}` with your text.

```
You are an information-extraction assistant.
Extract every event mentioned in the text.
Return exactly the requested format. No explanations.

TASK: Extract every event in the text. For each event, write a line:
<EVENTSEP> Event type: <TYPE>. Trigger: <TRIGGER>.

Text:
"{CHUNK}"

Rules:
- Use <EVENTSEP> exactly as the separator.
- Include ALL events mentioned.
- One line per event; no extra commentary.
```

### eventsep — 1-shot

> Paste this in a fresh chat. Replace `{{CHUNK}}` with your text.

```
You are an information-extraction assistant.
Extract every event mentioned in the text.
Return exactly the requested format. No explanations.

Example
Text: "The project was an ambitious and risky venture aiming to conquer, with a thousand men, a kingdom with a larger regular army and a more powerful navy."
Output:
<EVENTSEP> Event type: Self_motion. Trigger: venture.
<EVENTSEP> Event type: Aiming. Trigger: aiming.
<EVENTSEP> Event type: Conquering. Trigger: conquer.

--- Now do the same for:

TASK: Extract every event in the text. For each event, write a line:
<EVENTSEP> Event type: <TYPE>. Trigger: <TRIGGER>.

Text:
"{CHUNK}"

Rules:
- Use <EVENTSEP> exactly as the separator.
- Include ALL events mentioned.
- One line per event; no extra commentary.
```

### eventsep — 3-shot

> Paste this in a fresh chat. Replace `{{CHUNK}}` with your text.

```
You are an information-extraction assistant.
Extract every event mentioned in the text.
Return exactly the requested format. No explanations.

Example
Text: "The project was an ambitious and risky venture aiming to conquer, with a thousand men, a kingdom with a larger regular army and a more powerful navy."
Output:
<EVENTSEP> Event type: Self_motion. Trigger: venture.
<EVENTSEP> Event type: Aiming. Trigger: aiming.
<EVENTSEP> Event type: Conquering. Trigger: conquer.
---
Example
Text: "The sea venture was the only desired action that was jointly decided by the"
Output:
<EVENTSEP> Event type: Self_motion. Trigger: venture.
<EVENTSEP> Event type: Self_motion. Trigger: action.
<EVENTSEP> Event type: Deciding. Trigger: decided.
---
Example
Text: "The murder of Leigh Leigh, born Leigh Rennea Mears, occurred on 3 November 1989 while she was attending a 16-year-old boy's birthday party at Stockton Beach, New South Wales, on the east coast of Australia."
Output:
<EVENTSEP> Event type: Coming_to_be. Trigger: occurred.
<EVENTSEP> Event type: Committing_crime. Trigger: murder.
<EVENTSEP> Event type: Participation. Trigger: attending.

--- Now do the same for:

TASK: Extract every event in the text. For each event, write a line:
<EVENTSEP> Event type: <TYPE>. Trigger: <TRIGGER>.

Text:
"{CHUNK}"

Rules:
- Use <EVENTSEP> exactly as the separator.
- Include ALL events mentioned.
- One line per event; no extra commentary.
```

### eventsep — 5-shot

> Paste this in a fresh chat. Replace `{{CHUNK}}` with your text.

```
You are an information-extraction assistant.
Extract every event mentioned in the text.
Return exactly the requested format. No explanations.

Example
Text: "The project was an ambitious and risky venture aiming to conquer, with a thousand men, a kingdom with a larger regular army and a more powerful navy."
Output:
<EVENTSEP> Event type: Self_motion. Trigger: venture.
<EVENTSEP> Event type: Aiming. Trigger: aiming.
<EVENTSEP> Event type: Conquering. Trigger: conquer.
---
Example
Text: "The sea venture was the only desired action that was jointly decided by the"
Output:
<EVENTSEP> Event type: Self_motion. Trigger: venture.
<EVENTSEP> Event type: Self_motion. Trigger: action.
<EVENTSEP> Event type: Deciding. Trigger: decided.
---
Example
Text: "The murder of Leigh Leigh, born Leigh Rennea Mears, occurred on 3 November 1989 while she was attending a 16-year-old boy's birthday party at Stockton Beach, New South Wales, on the east coast of Australia."
Output:
<EVENTSEP> Event type: Coming_to_be. Trigger: occurred.
<EVENTSEP> Event type: Committing_crime. Trigger: murder.
<EVENTSEP> Event type: Participation. Trigger: attending.
---
Example
Text: "Her naked body was found in the sand dunes nearby the following morning, with severe genital damage and a crushed skull."
Output:
<EVENTSEP> Event type: Bodily_harm. Trigger: crushed.
<EVENTSEP> Event type: Damaging. Trigger: damage.
<EVENTSEP> Event type: Know. Trigger: found.
---
Example
Text: "Matthew Grant Webster, an 18-year-old who acted as a bouncer at the event, pleaded guilty to her murder and was sentenced to 20 years in prison with a 14-year non-parole period."
Output:
<EVENTSEP> Event type: Legal_rulings. Trigger: sentenced.
<EVENTSEP> Event type: Request. Trigger: pleaded.
<EVENTSEP> Event type: Committing_crime. Trigger: murder.

--- Now do the same for:

TASK: Extract every event in the text. For each event, write a line:
<EVENTSEP> Event type: <TYPE>. Trigger: <TRIGGER>.

Text:
"{CHUNK}"

Rules:
- Use <EVENTSEP> exactly as the separator.
- Include ALL events mentioned.
- One line per event; no extra commentary.
```
