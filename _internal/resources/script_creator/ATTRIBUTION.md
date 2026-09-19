# Script Creator knowledge — vendored from https://github.com/ricker72/Npc-Maker (MIT).

Files:
- system_prompt.txt — CRYSTAL_SERVER_SYSTEM_PROMPT
  (src/crystalServerKnowledge.js: technical knowledge extracted from
  https://github.com/zimbadev/crystalserver, protocol 15.24)
- Script type keys (src/crystalServerKnowledge.js SCRIPT_TYPES_KEYS):
  npc, action, talkaction, creaturescript, moveevent, globalevent, spell, other
- AI client contract (src/aiClient.js): OpenAI-style Chat Completions
  request, multi-format response parsing, first ```lua block extraction.
- Defaults (src/secureConfig.js): endpoint
  https://api.paxsenix.org/v1/chat/completions, model gpt-4o.
  No embedded key is vendored: the user provides their own API key.
