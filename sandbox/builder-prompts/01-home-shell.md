# Page prompt: Home, LAYOUT ONLY (shell), native Taft elements

Paste this alone in a fresh builder conversation.

---

Build the layout for a website Home page using only Taft's own page-builder elements. I will type all the words myself afterward, so DO NOT WRITE ANY COPY.

## Words
Every text element contains only a short bracketed label such as [HEADLINE], [PARAGRAPH], [BUTTON 1 LABEL], [STAT 1 NUMBER], [QUOTE 1], [NAME 1]. Do not add taglines, testimonials, statistics, names, logos, claims, or descriptions. The only non-bracket text allowed is the digits 01 to 05 on the numbered list. Where a label would be empty, leave the bracket label in it.

## Elements
Use only native builder elements: sections, rows, columns, headings, paragraphs, buttons, bullet lists, dividers, images, and the built-in icon element. Do NOT use custom code blocks, HTML or CSS embeds, hand-drawn SVGs, or generated images. Every piece of text must be its own editable heading, paragraph, or button so I can click it and change it. Do not use image-based text.

## Heading tags
Use H1 once (the hero headline). Use H2 only for section headlines and H3 only for card titles. Everything else (small labels, stat numbers, quotes, names, roles, list items) is a paragraph, not a heading.

## Look
Calm, editorial, lots of whitespace. Use the brand colors already in the theme: bronze #BF8756 (buttons, accents, hover #A3703E), teal #56ADBF (tiny labels only), deep charcoal #252830 (dark bands), charcoal #3D4148, cream #FAF8F5 (page), warm gray #F0EDE8 (alternate bands), white cards. Italic accent color #9E6D41 on light backgrounds, #BF8756 on dark. Fonts: Cormorant Garamond for headings, DM Sans for everything else. Do not use any other font.

Type sizes (desktop / phone): hero headline 64px / 38px; section headlines 44px / 32px; card titles 28px / 24px; stat numbers 36px / 30px; list lines 24px / 20px; body 17px / 16px; small labels 13px, letter-spaced. Section padding about 100px top and bottom on desktop, 70px on phones. Content width about 1120px; text blocks no wider than 680px.

Buttons: rectangular, 2px radius. Primary = bronze fill, white text. Secondary = transparent with a 1px outline. On dark sections the secondary outline and text are cream.

Cards: white, soft shadow, 1px light border, 32px padding. No stars, no quote-mark icons, no avatar circles, no stock photos of people, no animation beyond a light fade-up.

## Sections, in order
1. **Hero** (dark charcoal, no image): small label [LABEL], very large headline [HEADLINE] with the last sentence set in italic bronze [ITALIC SENTENCE], paragraph [LEDE], two buttons side by side [BUTTON 1 LABEL] (primary) and [BUTTON 2 LABEL] (secondary), small muted line [NOTE]. A thin bronze-to-teal line along the bottom edge.
2. **Stats strip** (white band, hairline rules): four equal columns, each a bronze serif [STAT 1 NUMBER] over a small [STAT 1 CAPTION] (through 4).
3. **Hard to see** (cream): two columns. Left: [HEADLINE], [PARAGRAPH], and a white card holding a large serif italic [PULL QUOTE] with a bronze left border. Right: small lead line [LEAD LINE], then five rows, each with an italic bronze numeral 01 to 05 and a large serif [ITEM N], separated by hairline rules.
4. **Two ways** (warm gray): [HEADLINE], then two equal cards side by side. Card 1 is white with a bronze top border; card 2 is deep charcoal with a teal top border and cream text. Each card: small [LABEL], H3 [TITLE], [PARAGRAPH], and a text-style link button [LINK LABEL] with an arrow. Under the cards, one muted line [NOTE].
5. **About** (cream): two columns. Left: an image placeholder, 4:5 portrait, 2px radius, soft shadow, with a bronze offset frame behind it (leave it empty; I will add my photo). Right: [HEADLINE], [PARAGRAPH 1], [PARAGRAPH 2], [PARAGRAPH 3], and a text link [LINK LABEL].
6. **Testimonials** (warm gray): three equal white cards with a thin bronze top border. Each: serif italic [QUOTE N], a hairline, then [NAME N] and [ROLE N] in small muted text. Below, one quiet row of three text labels [ORG 1] [ORG 2] [ORG 3] (text only, no logos).
7. **Closing** (dark charcoal): [HEADLINE], [PARAGRAPH], two buttons [BUTTON 1 LABEL] and [BUTTON 2 LABEL], small line [EMAIL LINE].

Do NOT build a header or footer. Do not add any sections beyond these seven. Leave button link fields blank (do not invent links). In the page SEO settings leave title, description, author, keywords, and social image blank, and do not set noindex.
