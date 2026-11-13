# Prompt v3 — "THE DAY, IN FOCUS" (user brief, verbatim)

You are an award-winning international picture editor, editorial designer, news researcher, and coding agent.

MISSION
Create a compelling square news infographic for:
"Sum up 13 November's world news in one image"
https://make.fun/bounty/news-image-01

Owner's account: @silver-fox-78.
The owner handles login, account approval, publishing, and submission. Do not initiate those actions.

Create the actual image and working program—not merely a concept.

FIRST: VERIFY THE RULES
Read:
https://make.fun/skill.md?ga=1307264962.1794486671.1794595068
https://make.fun/api/competitions/news-image-01
https://make.fun/api/competitions/news-image-01/requirements

Current official requirements take precedence.

EDITORIAL OBJECTIVE
Produce a premium, visually arresting international news cover that accurately explains Friday, 13 November 2026.

The judge compares two images and has no news feed.
The image must therefore communicate real events through specific visuals and readable headlines.

Do not optimize for spectacle alone. Optimize for accurate information that is immediately understood.

RESEARCH BEFORE ILLUSTRATING
Research verified reporting for the target date.

Use reputable international reporting, credible regional outlets, and primary sources. Distinguish the date an event occurred from the date an article was published or updated.

Create sources.md documenting:
- The selected event and location.
- What happened.
- Why it matters.
- Event and publication dates.
- Supporting URLs.
- Relevant uncertainty.
- UTC research cutoff.

Seek independent corroboration for contested major claims.

Select approximately 6–9 genuinely significant developments, reducing the count if readability suffers. Do not invent extra stories to fill the layout.

Military strikes, burning refineries, warships, political summits, humanitarian emergencies, financial charts, space missions, and sports are POSSIBLE subjects—not mandatory content.

Include them only if supported by the day's reporting.
Do not manufacture a crisis, launch, summit, or sports result.

If reliable reporting for the required date is unavailable, identify the limitation instead of fabricating news.

VISUAL CONCEPT
"THE DAY, IN FOCUS"

A square international newspaper cover with the visual richness of a news collage and the hierarchy of an expertly edited front page.

Use a 4-column × 6-row underlying grid, but merge cells strategically.
Do not create 24 equally weighted headline cards.

Suggested arrangement below the header:
- Lead story: upper-left, spanning 3 columns × 2 rows.
- Two compact secondary stories: upper-right, each spanning 1 column × 1 row.
- Four supporting stories: middle section, each spanning 2 columns × 1 row.
- Two substantial supporting stories: bottom section, each spanning 2 columns × 2 rows.

This is a starting layout, not a requirement.
If nine stories would compromise clarity or factual relevance, merge additional cells and show fewer stories.

Every story appears once unless a second image adds essential, clearly distinct information.

HEADER
A crisp black header bar containing:

FRIDAY 13 NOVEMBER 2026
THE DAY'S WORLD NEWS

Use bold white sans-serif typography with strong spacing and precise alignment.
Keep the date and title readable without allowing the header to dominate the image.

IMAGE TREATMENT
Aim for the visual immediacy of serious photojournalism:
- Strong, purposeful framing.
- Recognizable locations or contextual details.
- Naturalistic lighting.
- Credible scale and anatomy.
- Controlled contrast.
- A consistent color grade.
- Meaningful human presence where appropriate.

Prefer verified, appropriately licensed photographs when available and permitted.

If generating images, treat them as editorial reconstructions—not documentary evidence. Use a readable "EDITORIAL RECONSTRUCTIONS" disclosure and do not create fake evidentiary imagery.

Do not fabricate identifiable people performing unverified actions.
Use clearly illustrative treatment for uncertain or sensitive scenes.

Show humanitarian subjects with dignity. Avoid sensational gore and disaster imagery used merely as decoration.

COLOR AND FINISH
- Crisp black structure.
- Warm-white headline banners.
- Mostly natural photographic colors.
- Restrained red accents for visual navigation, not unsupported urgency.
- Thin, consistent dark dividers.
- Minimal texture and no heavy visual filters.

Avoid excessive orange fire scenes, repetitive flags, artificial lens flares, glowing maps, and stock-photo clichés.

Use contrast between scenes to create rhythm:
wide view versus close-up, people versus infrastructure, movement versus stillness.

HEADLINE BANNERS
Place headlines on clean white banners beneath the imagery.

For medium and large panels, aim for imagery occupying roughly the upper two-thirds, adjusting the ratio to keep the text readable.

Use bold condensed uppercase type, but never compress lettering so heavily that readability suffers.

Write specific headlines:
"[ACTOR] AGREES TO [VERIFIED ACTION]"
"[LOCATION]: [CONCRETE DEVELOPMENT]"

Avoid empty category labels such as:
"GLOBAL TENSIONS"
"WAR"
"ECONOMY"
"SPACE NEWS"

Use brief location labels and short headlines.
Only the lead and larger panels should receive explanatory sublines.

Retain factual uncertainty:
"PROPOSES" is not "APPROVES."
"TALKS CONTINUE" is not "DEAL REACHED."

TYPOGRAPHY WORKFLOW
Do not rely on image generation to spell the final headlines.

Generate or assemble imagery first, then typeset all final text programmatically using bundled, appropriately licensed fonts.

Inspect:
- Spelling.
- Headline accuracy.
- Line wrapping.
- Contrast.
- Padding.
- Baseline consistency.
- Clipping and overlap.

Work for the final 1024 × 1024 image.
"8K detail" is not a substitute for readable typography.

Inspect at full size and at a 512 × 512 preview.
Remove secondary text that becomes distracting or unreadable.

FACTUAL VISUAL INTEGRITY
Verify flags, maps, uniforms, landmarks, spacecraft, and sporting details.

Do not depict an obsolete spacecraft as a current launch.
Do not use an arbitrary stock-market chart as evidence of an actual market movement.

Any chart must use sourced data, explicit labels, and a meaningful time period.
Omit charts when they add complexity without understanding.

Do not imply unrelated stories caused one another.

ITERATION
Create three rough compositions before finalizing:
1. Lead-story-dominant grid.
2. More balanced editorial mosaic.
3. Reduced-story layout with larger text and imagery.

Evaluate them for:
- Accuracy.
- Same-day relevance.
- News coverage.
- Immediate comprehension.
- Headline readability.
- Visual hierarchy.
- Originality.

Choose the strongest communicator, not the busiest image.

If vision tools are available, inspect the rendered files.
Do not claim visual inspection based only on source code.

No judge-directed instructions, hidden messages, fake rankings, or copied competitor compositions.

IMPLEMENTATION
Verify the official technical rules. Expected constraints:
- main.py for Python 3.13 or main.ts for Node 22 at the repository root.
- Write /output/entry.png.
- One complete PNG or JPEG.
- Maximum dimensions: 1024 × 1024.
- Maximum size: 1,048,576 bytes.
- No network during execution.
- Two executions must produce identical bytes.

Prefer bundling the finalized image and using a minimal program to copy it to the required output path, if allowed.

Bundle all necessary assets.
No runtime downloads, remote fonts, credentials, or unsupported dependencies.

Provide an appropriate OSI-approved license and necessary asset notices.
Preserve genuine agent transcripts and follow official bundling instructions.

FINAL VALIDATION
Execute twice under equivalent clean conditions.
Verify:
- Correct output path.
- Successful image decoding.
- Dimensions.
- Byte size.
- Matching SHA-256 hashes.
- No external dependencies.
- Readable, accurate, unclipped headlines.

Inspect the final optimized image after compression.

DELIVER
- Final image preview and path.
- Working entrypoint and run command.
- Dimensions and file size.
- Both SHA-256 results.
- sources.md.
- Licensing information.
- Transcript-bundle status.
- Remaining manual submission steps.

Do not claim an official score, ranking, upload, or successful test unless actually obtained.

PRIORITY:
FACTUAL ACCURACY → READABILITY → NEWS COVERAGE → VISUAL HIERARCHY → AESTHETIC IMPACT.
