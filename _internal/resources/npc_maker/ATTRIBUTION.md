# NPC Maker catalogs — vendored from https://github.com/ricker72/Npc-Maker (MIT).

Files:
- colors.json  — 132 outfit colors {id, r, g, b, hex} (src/data/colors.json)
- mounts.json  — 231 mounts {id, clientId, name} (src/data/mounts.json)
- outfits.json — 242 outfits {type, lookType, name, gender} (src/data/outfits.json)
- shop_items.json — 1958 shop items {id, name} (src/data/items.json, picker search)

The HUD filters outfits/mounts against the loaded appearances-*.dat
(category 2), so only lookTypes with real client art are offered.
