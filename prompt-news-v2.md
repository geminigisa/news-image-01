# Prompt user — news-image-01 v2 (verbatim)

Catatan: brief di bawah disimpan verbatim dari pesan user 2026-11-14 03:03 WIB. Satu-satunya perubahan: karakter "│ " di awal tiap baris (artefak paste dari dokumen asal) dihapus; kata-kata, struktur, dan urutannya tidak diubah.

Act as an elite editorial art director, international news researcher, information designer, and meticulous coding agent.

MISSION
Build a competition-ready entry for:
https://make.fun/bounty/news-image-01
“Sum up 13 November’s world news in one image.”

Aim for a genuinely first-place-quality result through factual reporting, exceptional visual storytelling, and flawless technical execution—not judge manipulation.

ACCOUNT BOUNDARY
The owner handles account login, approval, and submission under @silver-fox-78. Do not log in, create an account or wallet, request credentials, or submit anything unless the owner subsequently authorizes it. Complete and validate the entry locally first.

FIRST: READ THE CURRENT RULES
Read:
- https://make.fun/skill.md
- https://make.fun/api/competitions/news-image-01/requirements
- https://make.fun/api/competitions/news-image-01

Treat the current official brief as authoritative if anything below differs. Check prerequisites, permitted assets, runtime dependencies, transcript requirements, and deadlines before building.

IMPORTANT COMPETITION CONTEXT
The image must summarize Friday, 13 November 2026.
The vision-capable AI judge compares two images at a time.
The judge has NO news feed: the image itself must communicate what happened and why it matters.

Optimize for a careful international picture editor choosing the most informative, accurate, visually compelling summary—not for a decorative poster that merely suggests “world news.”

PHASE 1 — RESEARCH BEFORE DESIGN
Research actual world news reported on 13 November 2026.

Never invent headlines, assume future events, reuse another year’s November 13 stories, or turn an unresolved claim into a confirmed fact.

Use reputable reporting such as Reuters, AP, BBC, established regional outlets, and primary sources. Distinguish the event date from publication and update dates. Use a consistent UTC research cutoff and record it.

Create a compact source ledger containing:
- Event and location.
- What actually happened.
- Why it matters internationally.
- Publication date and event date.
- Supporting URLs.
- Confidence and any material uncertainty.

For major or disputed claims, seek two independent credible sources where possible; syndications of the same wire report do not count as independent confirmation.

Select approximately 4–6 important stories, fewer if that materially improves clarity. Rank by international significance, same-day relevance, confidence, and visual distinctiveness. Represent the actual day’s news rather than forcing artificial geographic or topical quotas.

If you cannot access reliable reporting for the required date, explicitly report the blocker. Do not fabricate a news summary.

PHASE 2 — DEVELOP THREE DIFFERENT CONCEPTS
Before polishing, sketch three genuinely distinct editorial compositions.

Recommended lead concept:
“THE WORLD, IN ONE FRAME”

A premium international newspaper cover translated into one unified editorial image:
- One unmistakable lead story.
- Several secondary stories integrated into a coherent visual system.
- A clear reading path.
- Short, specific English headlines attached to their corresponding visuals.
- Restrained geographic cues that help viewers identify places accurately.

Do not assume a globe, map, or central metaphor is mandatory. Use one only if it improves comprehension. Avoid a generic planet surrounded by unrelated icons.

Compare the concepts for:
1. Accuracy and specificity.
2. Breadth of meaningful news coverage.
3. Immediate comprehension.
4. Legibility at normal viewing size.
5. Visual hierarchy and coherence.
6. Originality and editorial restraint.

Choose the strongest concept based on these criteria, not merely the prettiest thumbnail.

PHASE 3 — ART DIRECTION
The final image should feel like a bespoke, award-caliber editorial cover—not a dashboard template, slide deck, or random AI collage.

Design requirements:
- Prefer a 1024 × 1024 canvas unless the live rules say otherwise.
- Make the lead story visually dominant.
- Give secondary stories enough space to be understood.
- Establish hierarchy with scale, contrast, spacing, and typography.
- Use one coherent illustration language.
- Use a disciplined palette, for example ink navy, warm ivory, and a restrained vermilion accent; adjust when the reporting calls for something else.
- Include the visible date: “13 NOV 2026”.
- Use a brief masthead such as “THE WORLD TODAY” only if it earns its space.
- Prefer concise, concrete headlines: actor + action + location where useful.
- Add a short explanatory subline only when it resolves ambiguity.
- Keep headline text readable at 1024 px; test a 512 px preview for hierarchy.
- Use whitespace deliberately.

Every major visual must correspond to a verified story.
A viewer should understand which event each visual depicts without reading the repository.

If using maps, borders, flags, charts, or statistics, verify them. Avoid decorative charts with invented numbers. Do not imply a causal relationship between unrelated stories.

Sensitive events:
Depict conflict, disasters, and casualties with dignity. No sensational gore. Do not present generated imagery as authentic documentary photography. Prefer clearly editorial illustration when recreating events.

Typography:
Render final text programmatically with bundled, appropriately licensed fonts whenever possible. Do not rely on image generation to spell headlines correctly. Check clipping, wrapping, punctuation, and contrast.

Avoid:
- Dense paragraphs and tiny source footnotes.
- Excessive boxes, flags, icons, or competing focal points.
- Vague labels such as “WAR”, “ECONOMY”, and “CLIMATE” without concrete news.
- Unnecessary fake branding or news-organization logos.
- Unsupported claims, misleading symbolism, and gratuitous spectacle.
- Text telling the judge to choose this entry, claims of superiority, hidden instructions, or any evaluation manipulation.

Use brief source credits only if they remain readable and improve the image. Keep the complete sourcing ledger in the repository.

PHASE 4 — BUILD THE ACTUAL DELIVERABLE
Produce the program, not just an image-generation prompt or a mockup.

Expected technical constraints, to be verified against the current rules:
- Root entrypoint: main.py for Python 3.13 or main.ts for Node 22.
- Program writes /output/entry.png.
- One complete PNG or JPEG.
- Width and height each no greater than 1024 pixels.
- File size no greater than 1 MiB.
- No network access during execution.
- Two executions must produce identical bytes.

Prefer reliability:
Create and finalize the artwork during development, commit the final image asset, and let a minimal entrypoint copy it to /output/entry.png if the rules permit. This minimizes runtime, rendering, font, and nondeterminism failures.

If rendering at runtime, bundle all required fonts and assets and use only dependencies available in the actual sandbox. Eliminate timestamps, random seeds without fixed values, remote resources, and variable metadata.

Do not install dependencies or download assets during sandbox execution.
Do not place API keys, tokens, personal details, or authentication files in the repository.

Honor asset licenses and any AI-generated asset restrictions in the official rules. Include an appropriate OSI-approved license and required attribution.

PHASE 5 — QUALITY CONTROL AND LOCAL TOURNAMENT
Generate at least three materially different local drafts before final selection, within available time and authorized budget.

Critique them like an independent picture editor:
- Can I identify the lead event in three seconds?
- Can I explain each secondary story from this image alone?
- Is the news specific to 13 November 2026?
- Does every visual and headline agree with the sources?
- Is this a world-news summary rather than one-country coverage?
- Is anything attractive but informationally useless?
- Is any text too small?
- Does it still feel like one designed image?

If image-viewing or vision tools are available, inspect the actual rendered files. Do not claim to have visually inspected an image from code alone.

Compare candidates in both A/B and B/A order to reduce position bias. Do not treat your own ratings as the official competition score.

Revise the weakest substantive issue in the best candidate. Do not waste iterations on superficial decoration while factual or legibility issues remain.

PHASE 6 — TECHNICAL VALIDATION
Run the entry twice in clean, equivalent conditions using the official harness when available.

Verify:
- Correct output path.
- File decodes successfully.
- Correct dimensions.
- File size ≤ 1,048,576 bytes.
- Identical SHA-256 hashes across both executions.
- No network requirement.
- No missing fonts or external assets.
- All visible text is correct and unclipped.
- Image remains visually strong after compression.

Use lossless optimization or controlled palette reduction where appropriate. Reinspect the actual final file after optimization.

Preserve genuine agent transcripts from the beginning. Follow the official bundling and privacy-redaction procedure. Do not fabricate transcripts or remove build evidence.

If preparing a GitHub repository, verify it satisfies ownership and creation-time rules. Do not publish, push, or submit without the owner’s authorization.

FINAL HANDOFF
Provide:
1. Final image preview and file path.
2. Entrypoint and run command.
3. Dimensions, byte size, and matching SHA-256 results.
4. A concise explanation of the selected stories.
5. Source ledger.
6. Repository and transcript-bundle status.
7. Any remaining manual steps, stated precisely.

Do not claim a submission, score, ranking, or visual inspection that did not actually occur.

Work autonomously on reversible local research, design, coding, and validation. Ask only for access, expenditure, or decisions you genuinely cannot resolve.

Priority order:
FACTUAL ACCURACY → IMMEDIATE COMPREHENSION → EDITORIAL IMPACT → TECHNICAL RELIABILITY → DECORATIVE DETAIL.
