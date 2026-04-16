# Newsletter Drafter Skill

## Trigger
When the user says "draft newsletter about [topic]" or "write newsletter on [topic]"

## What this skill does
1. Takes the topic from the user's message
2. Runs draft_newsletter.py with the topic as an argument
3. The script calls the Claude API and writes a newsletter to the newsletters folder
4. Confirms to the user where the file was saved

## How to run
```
python3 ~/.openclaw/workspace/skills/newsletter-drafter/draft_newsletter.py "[topic]"
```

## Output
Saves a .md file to ~/.openclaw/workspace/newsletters/ named with today's date and topic.
