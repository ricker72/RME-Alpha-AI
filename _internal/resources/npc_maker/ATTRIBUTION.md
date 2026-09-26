# NPC Maker catalogs — vendored from https://github.com/ricker72/Npc-Maker (MIT).

Files:
- colors.json  — 132 outfit colors {id, r, g, b, hex} (src/data/colors.json)
- mounts.json  — 257 mounts {id, clientId, name} (src/data/mounts.json + 15.30 top-up below)
- outfits.json — 275 outfits {type, lookType, name, gender} (src/data/outfits.json + 15.30 top-up below)
- shop_items.json — 1958 shop items {id, name} (src/data/items.json, picker search)

15.30 top-up (Summer 2026): lookTypes present in appearances 15.30
(dc4f4c01…, verified against the local 15.30 pack) but absent from the
upstream file were added with names from the 15.30-updated OTServ
registries (https://github.com/Levi999x/15.x-with-8.60 — outfits.xml,
mounts.xml; note upstream warns 2–3 names may differ from official Tibia):
8 outfits (Vampire Noble 1948/1949, Illuminated Warrior 1973/1974, Moon
Guardian 1976/1977, Captain 1940/1941), 6 mounts (Vampiric Hound 1945, Night
Hound 1946, Infernal Hound 1947, Jaracal 1962, Radiant Nimbus 1975, Broken
Moon 1978), plus older named gaps (e.g. Monk, Fiend Slayer … Aerial Disciple,
Reliable, Ninja Horse, Primal Demonosaur … Crimson Bay Predator). Correction:
the OTServ file called 1973/1974 Monk Master and 1976/1977 Illuminated
Warrior, but the TibiaWiki Outfit IDs table (columns Name/male/female,
cross-validated on Citizen, Vampire Noble, Aerial Disciple, Phoenix Evoker)
assigns 1973/1974 to Illuminated Warrior and 1976/1977 to Moon Guardian, with
no Monk Master row anywhere — matching the OTServ author's own warning; the
wiki naming wins. Captain 1940 (M) / 1941 (F) also comes from that table
(Captain's Outfits, 15.32 Great Expedition event; sprites already present in
the 15.30 pack). 28 further 15.30 lookTypes (1922–1926, 1938, 1943, 1944,
1950–1956, 1959–1961, 1963–1972) exist in the pack but in neither registry —
likely creature looks — and were deliberately left unnamed rather than
invented; they remain usable through the HUD LookType spinbox. 1942 exists
in neither the 15.24 nor the 15.30 pack.

The HUD filters outfits/mounts against the loaded appearances-*.dat
(category 2), so only lookTypes with real client art are offered.

colors.json hue-18 fix: ids 18/37/56/75/94/113 carried visibly wrong hexes
(e.g. 94 was #a4244f instead of the iconic pure red #ff0000). Corrected to
the values where three independent sources agree: OTClient
Outfit::getColor HSI math (src/client/outfit.cpp, HSI_H_STEPS=19), RME's
TemplateOutfitLookupTable (workspace_core/rendering/outfit_template.py) and
the real-client red-94. Remaining ±1/255 dust across ~50 entries is float
rounding noise between ports — invisible, left untouched. Known suspect
(not touched, single-source conflict): renderer table id 40 reads #BFAF8F
while the HSI formula and colors.json agree on #BF9F5F; needs visual proof
before changing render output.
