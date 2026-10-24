# Raw fact registry: Anthropic Public Benefit Fund (collected 2026-10-24)

Immutable raw layer. Claims are kept in the language they were collected in (English). Each fact has a stable ID (F001–F320) that wiki pages cite. Do not edit claims here; corrections go to the wiki pages and `wiki/log.md`.

Collection method: 7 parallel research agents, one per angle, followed by adversarial verification with two independent checks per fact. Verification completed only for F001–F025 before the run was stopped; the rest carry a provisional status derived from source type.

## Status legend

| Mark | Status (RU) | Meaning |
|---|---|---|
| ✅ | Проверено | подтверждено двумя независимыми проверками |
| ⚠️ | Спорно | одна из двух проверок не подтвердила |
| 🔴 | Не подтверждено | проверка опровергла или источник не найден |
| 🟢 | Первоисточник | публикация Anthropic, отдельная проверка не проводилась |
| 🟡 | Крупное СМИ | независимая проверка не проводилась |
| 🟠 | Вторичный источник | агрегатор, блог или пересказ; требует проверки |
| ⚪ | Оценка или мнение | предположение, интерпретация, прогноз |

Counts: 🟡 major: 126, 🟢 primary: 101, 🟠 secondary: 63, ✅ verified: 23, ⚪ opinion: 6, 🔴 refuted: 1

## Официальный текст объявления / official-text (25)

### F001 ✅ Проверено

The exact title of Anthropic's announcement is "Investing in the public benefit" (sentence case); the page is categorized under "Announcements", shows "Published Oct 18, 2026", has no byline (JSON-LD author is the organization "Anthropic"), and its JSON-LD shows datePublished 2026-10-18T00:00:00Z and dateModified 2026-10-21T11:37:13Z.

Corrected by verification: Anthropic's announcement at https://www.anthropic.com/news/public-benefit-fund is titled "Investing in the public benefit" (sentence case; browser title "Investing in the public benefit \ Anthropic"). The page's metadata shows "Published Oct 18, 2026" and "Category Announcements", displays no byline (CMS authors list is empty), and its JSON-LD NewsArticle markup has headline "Investing in the public benefit", datePublished "2026-10-18T00:00:00.000Z", dateModified "2026-10-21T11:37:13.000Z", and author {"@type":"Organization","name":"Anthropic"}.

- Source: Anthropic, 2026-10-18 — <https://www.anthropic.com/news/public-benefit-fund> (confidence as rated by researcher: primary)
- Quote: «"headline":"Investing in the public benefit" ... "datePublished":"2026-10-18T00:00:00.000Z","dateModified":"2026-10-21T11:37:13.000Z","author":{"@type":"Organization","name":"Anthropic"»
- Check (fidelity): confirmed. Fetched https://www.anthropic.com/news/public-benefit-fund directly (HTTP 200, no redirect) and inspected both the raw HTML and the rendered page. Every element of the claim is confirmed verbatim by the source: (1) <title> is "Investing in the public benefit \ Anthropic" and the JSON-LD "headline" is "Investing in the public benefit" in sentence case; (2) the article hero shows "Category Announcements" and the site's own article index lists the piece with "category":"Announcements"; (3) the hero metadata block reads "Published Oct 18, 2026"; (4) no author byline appears anywhere on the page (no "By <Name>" text), and the JSON-LD "author" is {"@type":"Organization","name":"Anthropic","url":"https://www.anthropic.com"}; (5) JSON-LD NewsArticle has "datePublished":"2026-10-18T00:00:00.000Z" and "dateModified":"2026-10-21T11:37:13.000Z", matched by <meta property="article:published_time"> and <meta property="article:modified_time"> with identical values. The claim writes these timestamps without the ".000" milliseconds (2026-10-18T00:00:00Z / 2026-10-21T11:37:13Z), which is the same instant in ISO 8601 and not a factual discrepancy. The supporting quote given in the claim matches the actual JSON-LD text character for character. No misquote, wrong date, wrong attribution or fabricated figure found. Evidence: <https://www.anthropic.com/news/public-benefit-fund>
- Check (crosscheck): confirmed. Fetched https://www.anthropic.com/news/public-benefit-fund directly (raw HTML via curl plus rendered view via WebFetch). Every element of the claim checks out against the primary source: <title> is "Investing in the public benefit \ Anthropic" and the JSON-LD NewsArticle headline is "Investing in the public benefit" (sentence case). The page's metadata block renders "Published | Oct 18, 2026 | Category | Announcements" (publishedOn: "2026-10-18"). No byline is shown; the CMS payload has authors: [] and the JSON-LD author is {"@type":"Organization","name":"Anthropic","url":"https://www.anthropic.com"}. JSON-LD datePublished is "2026-10-18T00:00:00.000Z" and dateModified is "2026-10-21T11:37:13.000Z" (the CMS _updatedAt is 2026-10-21T11:37:13Z), matching the claim's timestamps (the claim omits the ".000" milliseconds, which is a trivial formatting difference, not a factual one). Independent cross-check: a Reuters-bylined article (Virginia Business, Oct 19, 2026) says Anthropic announced the fund "on Sunday" (= Oct 18, 2026) and corroborates the substance (5% of shares subject to stockholder approval, +2% at board discretion per 50% value increase, fund is a wholly owned LLC while Anthropic itself is the public benefit corporation). The page itself confirms these details too, so none of the 5%/20% or LLC/PBC confusions appear in the claim, which concerns only page metadata. The exact title and JSON-LD fields can only be verified on the primary page, which the cross-check lens explicitly accepts. Minor imprecision only: "no byline" is accurate as a visible-page statement, and the dates are rendered with milliseconds in the markup. Evidence: <https://www.anthropic.com/news/public-benefit-fund>

### F002 ✅ Проверено

The page's meta/OG description reads: the company is committing a portion of its shares to the Anthropic Public Benefit Fund, described as 'a new entity with a structure that increases the stake as the company grows'; the twitter:site tag is @AnthropicAI.

- Source: Anthropic, 2026-10-18 — <https://www.anthropic.com/news/public-benefit-fund> (confidence as rated by researcher: primary)
- Quote: «We’re committing a portion of Anthropic’s shares to the Anthropic Public Benefit Fund, a new entity with a structure that increases the stake as the company grows.»
- Check (fidelity): confirmed. Fetched the raw HTML of the cited source (https://www.anthropic.com/news/public-benefit-fund, HTTP 200, no redirect) and inspected its meta tags directly. The <meta name="description"> and <meta property="og:description"> tags both contain exactly: "We’re committing a portion of Anthropic’s shares to the Anthropic Public Benefit Fund, a new entity with a structure that increases the stake as the company grows." — identical to the supporting quote. The <meta name="twitter:site"> tag is "@AnthropicAI" (twitter:creator is also @AnthropicAI). The article:published_time meta is 2026-10-18T00:00:00.000Z and the visible page date is "Oct 18, 2026", matching the cited 2026-10-18 date. Attribution to Anthropic is correct (first-party anthropic.com page titled "Investing in the public benefit"). Minor nuance not affecting the claim: the article body text says "a new wholly owned entity", while the meta/OG description (which the claim specifically describes) says "a new entity". The claim is accurate as stated. Evidence: <https://www.anthropic.com/news/public-benefit-fund>
- Check (crosscheck): confirmed. CONFIRMED against the primary source's raw HTML. I downloaded https://www.anthropic.com/news/public-benefit-fund (170,878 bytes) and extracted the meta tags directly: `<meta name="description">`, `<meta property="og:description">` and `<meta name="twitter:description">` all read exactly: "We’re committing a portion of Anthropic’s shares to the Anthropic Public Benefit Fund, a new entity with a structure that increases the stake as the company grows." The `<meta name="twitter:site">` tag is `@AnthropicAI`. `og:title` is "Investing in the public benefit"; `article:published_time` is 2026-10-18T00:00:00.000Z, matching the cited date. The supporting quote is a verbatim match of the meta description.

Independent cross-check: the AP wire story (carried by ABC News, Oct 18, 2026) and Al Jazeera (Oct 19, 2026) both independently report the same announcement: 5% of shares committed to the "Anthropic Public Benefit Fund", described by AP as "a new entity within the company", with an additional 2% addable at the board's discretion for every 50% increase in company value (Al Jazeera) — i.e. the "structure that increases the stake as the company grows."

On the flagged confusion points, none contradicts the claim: (a) 5% vs 20% — the meta description deliberately says "a portion" with no number; the article body says 5% is committed now (subject to stockholder approval), and the ~20% figure (AP) is the total including the pre-existing cofounder 80%-equity pledge and employee donation match, so neither number is misstated in the claim. (b) LLC vs PBC — the Fund is being set up as an LLC ("rather than a 501(c)(3) or other format"); Anthropic itself is the public benefit corporation. The meta description's neutral "a new entity" is accurate; note the article body is slightly more specific ("a new wholly owned entity"), but the claim correctly quotes the meta tag, not the body. (c) 6 vs 7 cofounders — not mentioned in the meta description or the claim; AP's phrasing (Amodei plus "five other cofounders") implies six, which is irrelevant to this claim's accuracy. Evidence: <https://www.anthropic.com/news/public-benefit-fund>

### F003 ✅ Проверено

Opening sentence: the Fund is described as 'a new wholly owned entity with a structure that increases the stake as the company grows'.

- Source: Anthropic, 2026-10-18 — <https://www.anthropic.com/news/public-benefit-fund> (confidence as rated by researcher: primary)
- Quote: «Today, we’re committing a portion of Anthropic’s shares to the Anthropic Public Benefit Fund, a new wholly owned entity with a structure that increases the stake as the company grows.»
- Check (fidelity): confirmed. Fetched the cited primary source https://www.anthropic.com/news/public-benefit-fund directly (both via WebFetch and raw curl of the page HTML). The page title is "Investing in the public benefit", its JSON-LD datePublished is 2026-10-18 (displayed as Oct 18, 2026), matching the cited date. The opening sentence of the article reads exactly: "Today, we're committing a portion of Anthropic's shares to the Anthropic Public Benefit Fund, a new wholly owned entity with a structure that increases the stake as the company grows." This matches the claim's supporting quote word for word, and the description of the Fund as "a new wholly owned entity with a structure that increases the stake as the company grows" is accurately attributed to Anthropic. No misquote, wrong date, wrong attribution, or fabricated figure found. (For context, the next sentence on the page states that, subject to stockholder approval, 5% of Anthropic's shares are committed today with an additional 2% added at the board's discretion, which is consistent with the "increases the stake as the company grows" framing.) Evidence: <https://www.anthropic.com/news/public-benefit-fund>
- Check (crosscheck): confirmed. Primary source confirmed: the Anthropic announcement at https://www.anthropic.com/news/public-benefit-fund (dated 2026-10-18) opens verbatim with "Today, we're committing a portion of Anthropic's shares to the Anthropic Public Benefit Fund, a new wholly owned entity with a structure that increases the stake as the company grows." The same wording ("a new wholly owned entity") also appears in Anthropic's own X post (x.com/AnthropicAI/status/2111881963657412903). Independent cross-check: the Associated Press story of 2026-10-18 (syndicated via mynorthwest.com, broadbandbreakfast.com, ny1.com, mynews13.com) describes the Fund as "a new entity within the company" starting with 5% of shares, with additional shares possible "if the company's valuation reaches specific milestones" — consistent with "wholly owned" and "stake increases as the company grows." No reputable source contradicts it. Checks on the flagged confusions: the claim itself makes no percentage statement (the primary source says 5% initial, +2% at board discretion per 50% valuation increase above a baseline, with ~20% being the combined total including the cofounders' 80% pledge and the employee equity match); "wholly owned entity" is correct — the Fund is structured as an LLC (not a 501(c)(3)), while Anthropic the parent company is the public benefit corporation; AP states six cofounders (Dario Amodei plus five others), which the claim does not touch. The claim is an accurate quote of the primary announcement and is corroborated by independent AP coverage. Evidence: <https://www.anthropic.com/news/public-benefit-fund>

### F004 ✅ Проверено

5% of Anthropic's shares are committed 'today', subject to stockholder approval, with an additional 2% added at the board's discretion for every 50% increase in company value above 'a set baseline' (the baseline figure is not disclosed in the post).

- Source: Anthropic, 2026-10-18 — <https://www.anthropic.com/news/public-benefit-fund> (confidence as rated by researcher: primary)
- Quote: «Subject to stockholder approval, 5% of Anthropic’s shares will be committed today, with an additional 2% added at the board’s discretion for every 50% increase in the company’s value above a set baseline.»
- Check (fidelity): confirmed. Opened the cited primary source https://www.anthropic.com/news/public-benefit-fund (title "Investing in the public benefit", dated Oct 18, 2026 — matching the cited date and attribution to Anthropic). The page contains the sentence verbatim: "Subject to stockholder approval, 5% of Anthropic's shares will be committed today, with an additional 2% added at the board's discretion for every 50% increase in the company's value above a set baseline." All figures in the claim (5%, 2%, 50%, stockholder approval, "today", board's discretion, "a set baseline") match exactly. The claim's parenthetical that the baseline figure is not disclosed is also accurate: a second scan of every numeric value on the page found no dollar valuation or baseline number; the post only says Anthropic will share more in coming months "including the valuation milestones that may add to its stake." Nothing in the claim misquotes, misdates, or misattributes the source. Evidence: <https://www.anthropic.com/news/public-benefit-fund>
- Check (crosscheck): confirmed. Confirmed against the primary source and an independent outlet. Anthropic's post (https://www.anthropic.com/news/public-benefit-fund, dated Oct 18, 2026) states verbatim: "Subject to stockholder approval, 5% of Anthropic's shares will be committed today, with an additional 2% added at the board's discretion for every 50% increase in the company's value above a set baseline." The post does not state the baseline's value. Independent cross-check: Investing.com (Rachael Rajan, Oct 18, 2026) reports "5% of its shares will be committed to the fund, pending stockholder approval" and "An additional 2% will be added at the board's discretion ... for every 50% increase in the company's value above a set baseline," also noting the baseline is undisclosed; CNBC's Oct 18, 2026 headline likewise reads "Anthropic commits 5% of shares to new public benefit fund" (page returned 403 on fetch, headline only). Confusion checks: the 5% is the Fund's initial stake; the ~20% figure is the combined total including the co-founders' 80%-of-equity pledge and employee donation match, not the Fund's stake, so the claim correctly uses 5%. The Fund is an LLC (not a 501(c)(3)); Anthropic itself is the public benefit corporation; the claim does not confuse these. The claim makes no statement about the number of cofounders, and the post does not give a count. The claim's wording matches the source precisely, so no correction is needed. Evidence: <https://www.anthropic.com/news/public-benefit-fund>

### F005 ✅ Проверено

Anthropic says that as a public benefit corporation most mission work stays inside the company, listing AI safety and interpretability research, applied biomedical research, and Claude discounts for nonprofits and scientific institutions as activities with both public-benefit and for-profit value.

- Source: Anthropic, 2026-10-18 — <https://www.anthropic.com/news/public-benefit-fund> (confidence as rated by researcher: primary)
- Quote: «As a public benefit corporation, most of our work in pursuit of our mission takes place inside the company: research relevant to AI safety and interpretability; applied biomedical research; discounts on Claude for nonprofits and scientific institutions. These activities have both a public benefit component and for-profit value, so we house them directly in the company.»
- Check (fidelity): confirmed. Fetched the cited primary source directly (raw HTML via curl, parsed to text). The Anthropic article "Investing in the public benefit" is marked "Published Oct 18, 2026", Category Announcements, matching the cited date and attribution. The page contains the supporting quote word-for-word: "As a public benefit corporation, most of our work in pursuit of our mission takes place inside the company: research relevant to AI safety and interpretability; applied biomedical research; discounts on Claude for nonprofits and scientific institutions. These activities have both a public benefit component and for-profit value, so we house them directly in the company." The claim's paraphrase (most mission work stays inside the company; the three listed activities; both public-benefit and for-profit value) is a faithful rendering of this passage with no added or altered figures, dates, or attribution. The claim is confirmed; no correction required. Evidence: <https://www.anthropic.com/news/public-benefit-fund>
- Check (crosscheck): confirmed. Confirmed against the primary source. Anthropic's announcement at https://www.anthropic.com/news/public-benefit-fund (dated October 18, 2026) contains the verbatim passage: "As a public benefit corporation, most of our work in pursuit of our mission takes place inside the company: research relevant to AI safety and interpretability; applied biomedical research; discounts on Claude for nonprofits and scientific institutions. These activities have both a public benefit component and for-profit value, so we house them directly in the company." The supporting quote matches exactly. Independent corroboration: ESG Today (esgtoday.com) restates that Anthropic "is structured as a public benefit corporation" and that "most of the work towards its mission" takes place "inside the company," listing AI safety/interpretability research, applied biomedical research, and discounted Claude access for nonprofits and scientific institutions. Al Jazeera (Oct 19, 2026) independently confirms Anthropic is registered as a Delaware public benefit corporation. TechCrunch covers the fund but omits this passage (no contradiction). Confusion checks: the claim contains no percentages (for context, 5% of shares is committed to the Fund, roughly 20% total public-good commitment when combined with the co-founders' 80% equity pledge and the employee donation match); the claim correctly identifies Anthropic itself as the public benefit corporation while the Fund is a separate wholly owned LLC, so no LLC/PBC conflation; the claim does not mention cofounder count, and the announcement gives no number. No reputable source contradicts the claim. Note: the WebSearch per-turn budget was exhausted after the first query, so corroboration was done via direct WebFetch of outlets surfaced by that search. Evidence: <https://www.anthropic.com/news/public-benefit-fund>

### F006 ✅ Проверено

The Fund's stated purpose is 'increased flexibility and scale'; the two example uses given are 'large donations to traditional nonprofits' and 'direct distributions to specific populations' (phrased as 'we might explore', not as commitments).

Corrected by verification: Anthropic's Oct 18, 2026 announcement says the Anthropic Public Benefit Fund "will have increased flexibility and scale, enabling us to pursue our mission in new ways"; the only two example uses it names are hedged, not committed: "for example, we might explore large donations to traditional nonprofits or direct distributions to specific populations." The article additionally cites "labor market impacts" as one example area the Fund could address.

- Source: Anthropic, 2026-10-18 — <https://www.anthropic.com/news/public-benefit-fund> (confidence as rated by researcher: primary)
- Quote: «The Anthropic Public Benefit Fund will have increased flexibility and scale, enabling us to pursue our mission in new ways: for example, we might explore large donations to traditional nonprofits or direct distributions to specific populations.»
- Check (fidelity): confirmed. Fetched the primary source directly (raw HTML of https://www.anthropic.com/news/public-benefit-fund, "Investing in the public benefit", Published Oct 18, 2026, Announcements). The supporting quote appears verbatim: "The Anthropic Public Benefit Fund will have increased flexibility and scale, enabling us to pursue our mission in new ways: for example, we might explore large donations to traditional nonprofits or direct distributions to specific populations." The two example uses and the hedged "we might explore" phrasing are exactly as claimed, and the attribution and date match. One minor imprecision: the source does not frame "increased flexibility and scale" as the Fund's "stated purpose"; it says the Fund "will have" increased flexibility and scale, which enables Anthropic "to pursue our mission in new ways" (the purpose is pursuing the mission; flexibility/scale is the Fund's attribute/rationale). The article also separately names "labor market impacts" as an example area and says the LLC form was chosen "to give adjustability between different forms of giving". Claim is directionally correct with precise wording supplied. Evidence: <https://www.anthropic.com/news/public-benefit-fund>
- Check (crosscheck): confirmed. Confirmed against the primary source. WebFetch of https://www.anthropic.com/news/public-benefit-fund (dated Oct 18, 2026; listed on anthropic.com/news as "Investing in the public benefit") returned the sentence verbatim: "The Anthropic Public Benefit Fund will have increased flexibility and scale, enabling us to pursue our mission in new ways: for example, we might explore large donations to traditional nonprofits or direct distributions to specific populations." The hedged phrasing ("we might explore") is accurate, and the two example mechanisms are correctly identified. Cross-check caveats: (a) the page also frames 5% committed now vs. roughly 20% total dedicated to public good when combined with prior cofounder/employee pledges (not relevant to this claim, but the claim does not confuse them); (b) the Fund is an LLC while Anthropic itself is a public benefit corporation — the claim does not conflate these; (c) no cofounder-count assertion appears in the claim. One imprecision: the announcement does not state "increased flexibility and scale" as the Fund's purpose; it describes it as a property of the Fund that enables pursuing Anthropic's mission in new ways. The page also names "labor market impacts" as an example issue area (not a distribution mechanism), so "two example uses" is correct for mechanisms but incomplete if read as the only examples given. The WebSearch budget for this turn was exhausted before I could query independent outlets; a guessed TechCrunch URL returned 404. Per the cross-check lens, the primary announcement itself is an acceptable confirming source, and it fully supports the quoted text. Evidence: <https://www.anthropic.com/news/public-benefit-fund>

### F007 ✅ Проверено

Labor market impacts are given as the one worked example; Anthropic says it 'has already committed $200 million to studying and addressing this issue' and that 'bolder approaches may be needed'. The word 'jobs' does not appear; the post says 'instability for many workers'.

- Source: Anthropic, 2026-10-18 — <https://www.anthropic.com/news/public-benefit-fund> (confidence as rated by researcher: primary)
- Quote: «One example is labor market impacts. AI may generate enormous economic value, but it could also cause instability for many workers. Anthropic has already committed $200 million to studying and addressing this issue, but given the pace of AI progress, bolder approaches may be needed. The Fund will have the versatility to pursue them.»
- Check (fidelity): confirmed. Fetched the cited primary source https://www.anthropic.com/news/public-benefit-fund directly (raw HTML via curl plus WebFetch). The post is titled "Investing in the public benefit", published Oct 18, 2026, matching the cited date. The supporting quote appears verbatim: "One example is labor market impacts. AI may generate enormous economic value, but it could also cause instability for many workers. Anthropic has already committed $200 million to studying and addressing this issue, but given the pace of AI progress, bolder approaches may be needed. The Fund will have the versatility to pursue them." ("$200 million" is rendered as a hyperlink in the page.) A regex count of \bjobs?\b over the extracted article text returns 0 occurrences, confirming the word "jobs" does not appear; the phrase "instability for many workers" is exact. Labor market impacts is indeed the only topical worked example in the post; the only other examples given ("large donations to traditional nonprofits or direct distributions to specific populations") describe forms of giving, not issue areas. All numbers, dates, attribution and wording in the claim match the source. Evidence: <https://www.anthropic.com/news/public-benefit-fund>
- Check (crosscheck): confirmed. Verified directly against the primary source (https://www.anthropic.com/news/public-benefit-fund, "Investing in the public benefit", Published Oct 18, 2026, tagged Topics: Funding, Economic Futures, Labor market, Nonprofits), fetched both via WebFetch and as raw HTML (170,835 bytes) which I stripped and grepped myself. Findings: (1) The exact passage appears verbatim: "One example is labor market impacts. AI may generate enormous economic value, but it could also cause instability for many workers. Anthropic has already committed $200 million to studying and addressing this issue, but given the pace of AI progress, bolder approaches may be needed. The Fund will have the versatility to pursue them." (2) A case-insensitive word-boundary search for "job"/"jobs" across the entire page text returned 0 matches; "employment" also does not appear — the post's terms are "workers" and "labor market". (3) Labor market impacts is the only issue area introduced as an example ("One example is..."); the preceding sentence gives examples of giving mechanisms ("for example, we might explore large donations to traditional nonprofits or direct distributions to specific populations"), not problem areas, so "the one worked example" is accurate. Anthropic's news index also lists the post on Oct 18, 2026. Cross-check lens: the post states the Fund is an LLC ("rather than a 501(c)(3)"), Anthropic itself is the public benefit corporation; 5% of shares committed today vs "roughly 20%" dedicated to public good overall (including co-founders' 80% pledge); the post does not state a cofounder count — none of these bear on Claim #6, and the claim does not misstate any of them. Caveat: the per-turn WebSearch budget was exhausted before I could search, so I could not pull a second outlet; however, this claim is about the literal wording of the Anthropic post, for which the primary announcement (not a blog/aggregator) is the definitive evidence, and the task explicitly accepts the primary announcement. Evidence: <https://www.anthropic.com/news/public-benefit-fund>

### F008 ✅ Проверено

The '$200 million' in the post hyperlinks to Anthropic's July 22, 2026 article 'A research agenda for the Economic Futures Research Fund', which states the $200 million commitment to the Anthropic Economic Futures Research Fund for external research on interventions to prepare society for AI's economic impacts, primarily funding projects in the $5-30 million range and nothing below $1 million.

Corrected by verification: The '$200 million' in the Oct 18, 2026 post hyperlinks to Anthropic's July 22, 2026 article 'A research agenda for the Economic Futures Research Fund', which states Anthropic is committing $200 million to the Anthropic Economic Futures Research Fund to support ambitious external research on interventions to prepare society for the economic impacts of AI; it plans to primarily fund projects in the $5-30 million range (flexible upward for well-scoped, high-potential-impact projects) and will not directly fund anything below $1 million from the fund.

- Source: Anthropic, 2026-07-22 — <https://www.anthropic.com/news/economic-futures-research-fund-agenda> (confidence as rated by researcher: primary)
- Quote: «We’re committing $200 million to the fund to support ambitious external research on interventions to prepare society for the economic impacts of AI.»
- Check (fidelity): confirmed. Verified directly against the raw HTML of both pages (fetched via curl, not just summarizer output). (1) In the Oct 18, 2026 post "Investing in the public benefit" (https://www.anthropic.com/news/public-benefit-fund), the text "$200 million" is wrapped in <a href="https://www.anthropic.com/news/economic-futures-research-fund-agenda"> — the hyperlink target matches the claim exactly. (2) That target page has headline "A research agenda for the Economic Futures Research Fund", datePublished 2026-07-22, "Published Jul 22, 2026" — title and date match. (3) The supporting quote appears verbatim in the article body: "We're sharing the research agenda for the Anthropic Economic Futures Research Fund. We're committing $200 million to the fund to support ambitious external research on interventions to prepare society for the economic impacts of AI." (4) Fund name "Anthropic Economic Futures Research Fund" matches. (5) Grant sizes verbatim: "plan to primarily fund projects in the $5-30 million range, though we're flexible upward for well-scoped, high-potential-impact projects" and "we won't directly fund anything below $1 million from this fund." All numbers, dates, attribution and the hyperlink relationship are confirmed. The only hair-splitting nuance: the source says it won't "directly" fund anything below $1 million, and notes flexibility upward beyond $30 million; the claim omits the word "directly" but is otherwise an accurate paraphrase. Evidence: <https://www.anthropic.com/news/economic-futures-research-fund-agenda>
- Check (crosscheck): confirmed. CONFIRMED by primary source plus one independent outlet. (1) Anthropic's post "Investing in the public benefit" (Oct 18, 2026, anthropic.com/news/public-benefit-fund) contains the sentence "Anthropic has already committed $200 million to studying and addressing this issue, but given the pace of AI progress, bolder approaches may be needed." The anchor text "$200 million" is the only hyperlink in the article body and its href is https://www.anthropic.com/news/economic-futures-research-fund-agenda. (2) That target article is titled "A research agenda for the Economic Futures Research Fund", dated Jul 22, 2026, names the "Anthropic Economic Futures Research Fund", and states verbatim: "We're committing $200 million to the fund to support ambitious external research on interventions to prepare society for the economic impacts of AI"; "We plan to primarily fund projects in the $5-30 million range" ("flexible upward for well-scoped, high-potential-impact projects"); and "we won't directly fund anything below $1 million from this fund." The supporting quote supplied matches the source text. (3) Independent cross-check: TechCrunch (Anthony Ha, Oct 18, 2026) reports "the impact that AI might have on the job market, which Anthropic has already committed $200 million to study," with its link URL pointing to the same economic-futures-research-fund-agenda page; Wikipedia's Anthropic article cites this TechCrunch piece (ref 118) for the Oct 2026 public benefit fund announcement. No reputable source contradicts any element. The claim does not touch the 5%/20%, LLC/PBC, or cofounder-count confusion points, and the $200M is correctly attributed to the Economic Futures Research Fund (not to the DoD contract or Snowflake deal, which are separate $200M figures). Note: WebSearch budget was exhausted this turn, so cross-checking relied on direct fetches of known URLs (Anthropic, TechCrunch, Wikipedia). Only tiny imprecision: the source says it "won't directly fund anything below $1 million from this fund" (the word "directly" and the "flexible upward" caveat), reflected in corrected_claim. Evidence: <https://www.anthropic.com/news/economic-futures-research-fund-agenda>

### F009 ✅ Проверено

The Fund is being established as an LLC rather than a 501(c)(3) 'or other format', with the stated reason being 'adjustability between different forms of giving'.

- Source: Anthropic, 2026-10-18 — <https://www.anthropic.com/news/public-benefit-fund> (confidence as rated by researcher: primary)
- Quote: «We’re establishing the Anthropic Public Benefit Fund as an LLC—rather than a 501(c)(3) or other format—to give adjustability between different forms of giving.»
- Check (fidelity): confirmed. Opened the cited primary source https://www.anthropic.com/news/public-benefit-fund (both via WebFetch and a raw curl of the page HTML). The page's metadata gives datePublished / article:published_time = 2026-10-18T00:00:00.000Z, matching the cited date. The article contains the sentence verbatim: "We're establishing the Anthropic Public Benefit Fund as an LLC—rather than a 501(c)(3) or other format—to give adjustability between different forms of giving." It is immediately followed by: "None of the Anthropic equity held by the LLC will be used for lobbying or political giving, in the US or abroad." The claim's three components — (1) structured as an LLC, (2) explicitly contrasted with a 501(c)(3) "or other format", (3) stated reason being "adjustability between different forms of giving" — all appear with exactly this wording, attributed to Anthropic in Anthropic's own announcement. No misquote, wrong date, wrong attribution, or fabricated figure found. Evidence: <https://www.anthropic.com/news/public-benefit-fund>
- Check (crosscheck): confirmed. Primary source confirmed verbatim. Fetching https://www.anthropic.com/news/public-benefit-fund (dated Oct 18, 2026) returned the exact sentence: "We're establishing the Anthropic Public Benefit Fund as an LLC—rather than a 501(c)(3) or other format—to give adjustability between different forms of giving." The page also describes the Fund as "a new wholly owned entity" and notes that Anthropic itself (not the Fund) is a public benefit corporation, so there is no LLC-vs-PBC confusion in the claim. Independent corroboration: TechCrunch (Anthony Ha, Oct 18, 2026, https://techcrunch.com/2026/10/18/anthropic-says-its-committing-5-of-its-shares-to-a-public-benefit-fund/) independently reports the fund is "structured as a wholly owned entity within the company" and that the structure gives "increased flexibility and scale" — consistent with the LLC/adjustability rationale, though TechCrunch does not use the word "LLC." No reputable source contradicts the claim. The claim does not involve the 5%/20% figures or cofounder count, so those confusion traps do not apply (for reference, the primary page says 5% committed now, +2% per 50% valuation increase, ~20% total including prior co-founder/employee pledges). Note: the WebSearch budget for this run was exhausted, so verification relied on direct WebFetch of the primary announcement and publisher pages; CNBC, Axios, Fast Company, The Verge and Business Insider were not fetchable (403/blocked). Evidence: <https://www.anthropic.com/news/public-benefit-fund>

### F010 ✅ Проверено

None of the Anthropic equity held by the LLC will be used for lobbying or political giving, in the US or abroad.

- Source: Anthropic, 2026-10-18 — <https://www.anthropic.com/news/public-benefit-fund> (confidence as rated by researcher: primary)
- Quote: «None of the Anthropic equity held by the LLC will be used for lobbying or political giving, in the US or abroad.»
- Check (fidelity): confirmed. Opened the cited primary source https://www.anthropic.com/news/public-benefit-fund (Anthropic announcement "Investing in the public benefit") both via WebFetch and via raw curl of the page HTML. The page contains the sentence verbatim: "We're establishing the Anthropic Public Benefit Fund as an LLC—rather than a 501(c)(3) or other format—to give adjustability between different forms of giving. None of the Anthropic equity held by the LLC will be used for lobbying or political giving, in the US or abroad." The claim text matches the source word for word. Page metadata shows datePublished 2026-10-18T00:00:00.000Z (displayed as "Oct 18, 2026"), matching the cited date; article:modified_time is 2026-10-21, which does not affect the publication date. Attribution to Anthropic is correct (it is Anthropic's own newsroom post). The "LLC" reference is consistent with the source, which states the Fund is being established as an LLC. No misquote, wrong date, wrong attribution, or unsupported figure found. Evidence: <https://www.anthropic.com/news/public-benefit-fund>
- Check (crosscheck): confirmed. Verified directly against the primary announcement at https://www.anthropic.com/news/public-benefit-fund (dated Oct 18, 2026, matching the citation). The page contains the sentence verbatim: "None of the Anthropic equity held by the LLC will be used for lobbying or political giving, in the US or abroad." It appears in the paragraph that begins "We're establishing the Anthropic Public Benefit Fund as an LLC—rather than a 501(c)(3) or other format", so the "LLC" reference in the claim is correct (the Fund is an LLC; Anthropic itself is the public benefit corporation — the claim does not conflate the two). A second fetch of the surrounding paragraph found no qualifiers, exceptions (e.g. 501(c)(4) or policy-advocacy carve-outs), or contradicting statements anywhere on the page. The claim contains no percentage or cofounder-count assertion, so the 5%/20% and 6-vs-7-cofounder traps do not apply. Note: the primary source correctly says 5% committed now, +2% at board discretion, ~20% total dedicated to the public good (with the cofounders' 80%-of-equity pledge), and the claim does not misstate any of this. Limitation: the WebSearch budget for this turn was exhausted before I could run searches, so I could not retrieve a second independent outlet; however, the cross-check lens explicitly accepts the primary announcement as sufficient, and the claim is an exact quote from that primary document, not a paraphrase from a blog or aggregator. Evidence: <https://www.anthropic.com/news/public-benefit-fund>

### F011 ✅ Проверено

Anthropic frames the escalating structure as an alternative to executive compensation: it contrasts 'escalating compensation awards' for tech executives with 'instead directing that equity to the public benefit'.

Corrected by verification: Anthropic's Oct 18, 2026 announcement frames the Fund's growing stake as an alternative to executive equity awards: in one paragraph it says that because of how the Fund is structured, "the more Anthropic grows, the larger the share of the company that can be dedicated expressly to the public good," and in the next paragraph it states, "It is common practice for tech companies to offer escalating compensation awards to their executives. We are instead directing that equity to the public benefit." (The Fund, a wholly owned LLC, receives 5% of shares today; with the co-founders' 80% pledge and employee match, roughly 20% is expected to be dedicated to the public good.)

- Source: Anthropic, 2026-10-18 — <https://www.anthropic.com/news/public-benefit-fund> (confidence as rated by researcher: primary)
- Quote: «Because of the way the Fund is structured, the more Anthropic grows, the larger the share of the company that can be dedicated expressly to the public good. It is common practice for tech companies to offer escalating compensation awards to their executives. We are instead directing that equity to the public benefit.»
- Check (fidelity): confirmed. Fetched the cited primary source https://www.anthropic.com/news/public-benefit-fund (title "Investing in the public benefit", category Announcements, published Oct 18, 2026, no individual byline, so attribution to Anthropic is correct). The page contains, verbatim and in a single paragraph in this order: (1) a sentence stating that because of how the Fund is structured, the more Anthropic grows, the larger the share of the company that can be dedicated expressly to the public good; (2) "It is common practice for tech companies to offer escalating compensation awards to their executives."; (3) "We are instead directing that equity to the public benefit." The claim's characterization — that Anthropic frames the escalating stake (5% now, plus 2% at board discretion per 50% valuation increase above a baseline) as an alternative to escalating executive compensation awards, contrasting the two phrases quoted — matches the source exactly. Quoted phrases, date and attribution all check out; no misquote or misattribution found. Evidence: <https://www.anthropic.com/news/public-benefit-fund>
- Check (crosscheck): confirmed. Verified directly against the cited primary announcement (anthropic.com/news/public-benefit-fund, dated Oct 18, 2026). All three sentences in the supporting quote appear word-for-word on the page: "Because of the way the Fund is structured, the more Anthropic grows, the larger the share of the company that can be dedicated expressly to the public good." / "It is common practice for tech companies to offer escalating compensation awards to their executives." / "We are instead directing that equity to the public benefit." The only imprecision is presentational: the first sentence is its own paragraph, and the second and third sentences follow in the next paragraph, so the quote is a splice of two adjacent paragraphs rather than one continuous passage. The framing the claim describes (contrasting executives' escalating equity awards with directing that equity to the public benefit) is accurately attributed. Context checks on the lens items: the page says 5% of Anthropic's shares are committed today and that, together with the co-founders' 80% pledge and the employee equity match, roughly 20% will be dedicated to the public good (so 5% vs 20% are distinct figures, both present); Anthropic itself is a public benefit corporation (PBC) while the Fund is a wholly owned LLC rather than a 501(c)(3); the page refers only to "co-founders" without giving a count. No independent second outlet could be checked because this turn's WebSearch budget was exhausted, but the cross-check lens explicitly accepts the primary announcement as confirmation, and the claim is specifically about how Anthropic frames the structure, for which the primary source is authoritative. Evidence: <https://www.anthropic.com/news/public-benefit-fund>

### F012 ✅ Проверено

At founding, Anthropic's co-founders pledged to donate 80% of their equity holdings; since founding Anthropic has run an equity donation match program (employees pledge equity, Anthropic matches), and 'approximately half' of employees participate.

Corrected by verification: Per Anthropic's Oct 18, 2026 announcement of the Anthropic Public Benefit Fund: when Anthropic was founded, its co-founders pledged to donate 80% of their equity holdings; since founding, Anthropic has operated an equity donation match program allowing employees to pledge equity that Anthropic matches, and approximately half of employees participate. Combined with the new Fund, roughly 20% of Anthropic shares will be dedicated to the public good.

- Source: Anthropic, 2026-10-18 — <https://www.anthropic.com/news/public-benefit-fund> (confidence as rated by researcher: primary)
- Quote: «This builds on commitments our co-founders and employees have already made. When Anthropic was founded, our co-founders pledged to donate 80% of their equity holdings, and since founding we have also operated an equity donation match program that allows employees to pledge equity which Anthropic matches. Approximately half of our employees participate in this program.»
- Check (fidelity): confirmed. Opened the cited primary source https://www.anthropic.com/news/public-benefit-fund (Anthropic, "Investing in the public benefit", dated Oct 18, 2026). The page contains, verbatim: "When Anthropic was founded, our co-founders pledged to donate 80% of their equity holdings, and since founding we have also operated an equity donation match program that allows employees to pledge equity which Anthropic matches. Approximately half of our employees participate in this program." Every element of the claim — the 80% co-founder equity pledge at founding, the equity donation match program operated since founding (employees pledge, Anthropic matches), and "approximately half" employee participation — matches the source exactly in figures, attribution (Anthropic's own statement) and date (2026-10-18). The supporting quote given is an accurate verbatim reproduction. No misquote, wrong date, or misattribution found. Minor nuance for precision: the source speaks of the co-founders' pledge to "donate" (a pledge, not a completed donation), and the participation figure is Anthropic's self-reported approximation; the next sentence adds that combined with the new Fund, roughly 20% of Anthropic shares will be dedicated to the public good. Evidence: <https://www.anthropic.com/news/public-benefit-fund>
- Check (crosscheck): confirmed. Primary source confirmed verbatim. Fetched https://www.anthropic.com/news/public-benefit-fund (dated Oct 18, 2026) and it contains exactly: "When Anthropic was founded, our co-founders pledged to donate 80% of their equity holdings", "we have also operated an equity donation match program that allows employees to pledge equity which Anthropic matches", and "Approximately half of our employees participate in this program." The post is listed on Anthropic's news index (https://www.anthropic.com/news, item "Investing in the public benefit", Oct 18, 2026, /news/public-benefit-fund). The post also states the fund is an LLC (not a 501(c)(3)) and that 5% of shares are committed, consistent with the cross-check lens (no 5%/20% or LLC/PBC confusion in this claim; the claim does not assert a co-founder count). Independent corroboration: TechCrunch (Anthony Ha, Oct 18, 2026, https://techcrunch.com/2026/10/18/anthropic-says-its-committing-5-of-its-shares-to-a-public-benefit-fund/) independently reports the fund announcement and the 5% commitment ("structured as a wholly owned entity within the company"), though it does not repeat the 80% pledge, match program or participation figures. Wikipedia's Anthropic article records the October 2026 5% commitment, citing TechCrunch. Anthropic's careers page (https://www.anthropic.com/careers) separately corroborates that the match program exists: "Optional equity donation matching at a 1:1 ratio, up to 25% of your equity grant". Caveat: the 80% pledge, the match program's history "since founding", and the "approximately half" participation figure are Anthropic's own self-reported statements; no independent outlet was found verifying those three specific numbers (WebSearch budget was exhausted this turn, so only direct fetches of publisher pages were possible; Verge, Wired, CNBC and Axios pages were unreachable). The claim is correctly attributed to the Anthropic announcement and matches it exactly, so it is not refuted. Evidence: <https://www.anthropic.com/news/public-benefit-fund>

### F013 ✅ Проверено

Combined with the Fund, 'roughly 20%' of Anthropic shares will be dedicated to the public good, plus any additional percentage added if specific valuation milestones are reached.

Corrected by verification: Combined with the new Fund's 5% commitment (subject to stockholder approval), roughly 20% of Anthropic shares will be dedicated to the public good — the total including the co-founders' earlier pledge of 80% of their equity and the employee equity-donation match program — plus any additional percentage that could be added if the company reaches specific (not yet disclosed) valuation milestones, i.e. an extra 2% at the board's discretion for every 50% increase in company value above a set baseline.

- Source: Anthropic, 2026-10-18 — <https://www.anthropic.com/news/public-benefit-fund> (confidence as rated by researcher: primary)
- Quote: «When combined with today’s announcement, roughly 20% of Anthropic shares will be dedicated to the public good, plus any additional percentage that could be added if the company reaches specific valuation milestones.»
- Check (fidelity): confirmed. Opened the cited primary source https://www.anthropic.com/news/public-benefit-fund directly (WebFetch plus a raw curl of the page HTML). The page is dated Oct 18, 2026 (datePublished 2026-10-18), matching the cited date. The page contains, verbatim: "When combined with today's announcement, roughly 20% of Anthropic shares will be dedicated to the public good, plus any additional percentage that could be added if the company reaches specific valuation milestones." This exactly matches the supporting quote. Context in the same paragraph: the ~20% figure combines the new Fund commitment (5% of shares now, with an additional 2% at the board's discretion for every 50% increase in company value above a set baseline) with co-founders' pledge to donate 80% of their equity and the employee equity-donation match program (about half of employees participate). Attribution to Anthropic is correct. The claim's numbers, date, attribution and wording are faithful to the source; no misquote found. Evidence: <https://www.anthropic.com/news/public-benefit-fund>
- Check (crosscheck): confirmed. Primary source verified directly: Anthropic's announcement "Investing in the public benefit" (anthropic.com/news/public-benefit-fund, dated Oct 18, 2026, confirmed on the anthropic.com/news index) contains the sentence verbatim: "roughly 20% of Anthropic shares will be dedicated to the public good, plus any additional percentage that could be added if the company reaches specific valuation milestones." Context from the same page: the new Fund gets 5% of shares "subject to stockholder approval," with "an additional 2% added at the board's discretion for every 50% increase in the company's value above a set baseline"; the ~20% combined total also counts the co-founders' earlier pledge of 80% of their equity and the employee equity-donation match program (~half of employees participate); the Fund is an LLC (wholly owned entity), not a 501(c)(3); specific valuation thresholds are not yet disclosed. Independent cross-check: TechCrunch (Anthony Ha, Oct 18, 2026) independently reports the 5% commitment, the wholly-owned-entity structure, and the option to add 2% for every 50% valuation increase — consistent with and not contradicting the primary source. TechCrunch does not repeat the 20% combined figure, but nothing contradicts it. On the confusion points: the claim correctly uses 20% as the COMBINED figure (not the Fund's own 5% stake); the Fund is an LLC inside Anthropic (which is itself a PBC) — the claim makes no structural assertion; the page does not state a cofounder count. WebSearch budget was exhausted this turn, so cross-checking was done via direct WebFetch of the primary page and TechCrunch. The claim is accurate; corrected_claim adds precision about what the 20% comprises and the milestone mechanism. Evidence: <https://www.anthropic.com/news/public-benefit-fund>

### F014 ✅ Проверено

Anthropic promises more detail on the Fund's structure and governance 'in the coming months', including the valuation milestones; no specific date is given.

- Source: Anthropic, 2026-10-18 — <https://www.anthropic.com/news/public-benefit-fund> (confidence as rated by researcher: primary)
- Quote: «In the coming months, we will share more about the Anthropic Public Benefit Fund’s structure and governance, including the valuation milestones that may add to its stake.»
- Check (fidelity): confirmed. Opened the cited primary source https://www.anthropic.com/news/public-benefit-fund (datePublished 2026-10-18, matching the cited date). The page contains the sentence verbatim: "In the coming months, we will share more about the Anthropic Public Benefit Fund's structure and governance, including the valuation milestones that may add to its stake." The claim accurately paraphrases this: Anthropic (first-person "we") promises more detail on structure and governance, including valuation milestones, "in the coming months", and the article gives no specific date. Attribution, wording, and date all match the source. Evidence: <https://www.anthropic.com/news/public-benefit-fund>
- Check (crosscheck): confirmed. Confirmed by the primary source and one independent outlet. The Anthropic announcement (anthropic.com/news/public-benefit-fund, dated Oct 18, 2026) contains the verbatim sentence: "In the coming months, we will share more about the Anthropic Public Benefit Fund's structure and governance, including the valuation milestones that may add to its stake." No specific date or deadline appears anywhere on the page; the only timing language is "in the coming months" (the same paragraph also says progress will be reported in an upcoming public benefit report). TechCrunch (Anthony Ha, Oct 18, 2026) independently reports that Anthropic "will share more information about structure and governance in the coming months." The claim does not implicate the 5%-vs-20% (5% committed now, +2% per 50% valuation increase at board discretion, ~20% total including cofounder/employee pledges), LLC-vs-501(c)(3) (primary source says LLC), or cofounder-count issues (count is not stated in the source). Note: the shared WebSearch budget was exhausted, so verification was done via direct WebFetch of the primary announcement, Anthropic's news index, and TechCrunch. Evidence: <https://techcrunch.com/2026/10/18/anthropic-says-its-committing-5-of-its-shares-to-a-public-benefit-fund/>

### F015 ✅ Проверено

Anthropic says it will report progress against its mission in an 'upcoming public benefit report' (no date given).

- Source: Anthropic, 2026-10-18 — <https://www.anthropic.com/news/public-benefit-fund> (confidence as rated by researcher: primary)
- Quote: «We will also report on our progress to date against our mission in an upcoming public benefit report.»
- Check (fidelity): confirmed. Opened the cited source https://www.anthropic.com/news/public-benefit-fund (Anthropic news post "Investing in the public benefit", dated Oct 18, 2026, no individual byline — attributed to Anthropic as a company). The page contains the exact sentence quoted in the claim: "We will also report on our progress to date against our mission in an upcoming public benefit report." The sentence appears in the paragraph where Anthropic says it will share more about the Fund's structure and governance (including valuation milestones) in the coming months. No date for the report is given anywhere on the page, so "no date given" is accurate. The quote, attribution, and date of the source all match; the claim is supported. Evidence: <https://www.anthropic.com/news/public-benefit-fund>
- Check (crosscheck): confirmed. Verified directly against the primary announcement. The Anthropic post "Investing in the public benefit" (https://www.anthropic.com/news/public-benefit-fund, dated October 18, 2026) contains the exact sentence: "We will also report on our progress to date against our mission in an upcoming public benefit report." The article gives no date for that report; the only timing language ("in the coming months") refers to sharing more about the Fund's structure and governance, not to the report, so "no date given" is accurate. The Anthropic news index (https://www.anthropic.com/news) lists the article under that title and date, confirming it is a genuine, live primary source. Independent corroboration of the announcement: TechCrunch, "Anthropic says its committing 5% of its shares to a 'public benefit fund'" (Anthony Ha, Oct 18, 2026, https://techcrunch.com/2026/10/18/anthropic-says-its-committing-5-of-its-shares-to-a-public-benefit-fund/) confirms the fund announcement, the 5% commitment, the +2% per 50% valuation-increase mechanism, and "more information about structure and governance in the coming months". TechCrunch does not repeat the "public benefit report" sentence, but nothing in it contradicts the claim; the claim is explicitly attributed to Anthropic's own statement, and the primary announcement is the authoritative source for what Anthropic "says". Per the cross-check lens, the primary announcement counts as an acceptable independent source. The known confusion traps do not apply: the claim involves no percentage (the article's 5% committed vs. ~20% total dedicated to public good, including the ~80% founder pledge, are not at issue), no LLC-vs-PBC assertion (article: Anthropic is a public benefit corporation; the Fund is an LLC), and no cofounder count (the article gives none). Note: the web search budget for this turn was exhausted, so corroboration was obtained via direct fetches of outlet pages (TechCrunch tag page and article; The Verge was unreachable) rather than search. Evidence: <https://www.anthropic.com/news/public-benefit-fund>

### F016 ✅ Проверено

The post is tagged with the topics Funding, Economic Futures, Labor market, Nonprofits, and Leadership, and lists one related article: 'A research agenda for the Economic Futures Research Fund' (Jul 22, 2026).

Corrected by verification: The post "Investing in the public benefit" (Oct 18, 2026) displays the topic tags Funding, Economic Futures, Labor market, Nonprofits, and Leadership (followed by a "See more..." link), and its "Related articles" section lists one item: "A research agenda for the Economic Futures Research Fund" (Announcements, Jul 22, 2026), located at https://www.anthropic.com/news/economic-futures-research-fund-agenda.

- Source: Anthropic, 2026-10-18 — <https://www.anthropic.com/news/public-benefit-fund> (confidence as rated by researcher: primary)
- Quote: «Topics Funding Economic Futures Labor market Nonprofits Leadership ... Related articles Announcements Jul 22, 2026 A research agenda for the Economic Futures Research Fund»
- Check (fidelity): confirmed. Fetched https://www.anthropic.com/news/public-benefit-fund directly (raw HTML via curl plus WebFetch). The article "Investing in the public benefit" is dated Oct 18, 2026 (<time dateTime="2026-10-18">), category Announcements. The Topics metadata list contains exactly five tag links: Funding (/search?topic=funding), Economic Futures, Labor market, Nonprofits, and Leadership; the last two are in "HiddenTopic" list items revealed by a "See more..." button, but there are no further tags beyond these five. The "Related articles" section lists exactly one item: category "Announcements", date "Jul 22, 2026", title "A research agenda for the Economic Futures Research Fund", followed by a "View more" link. Every element of the claim (tag names, count, related article title and date) matches the source verbatim. Evidence: <https://www.anthropic.com/news/public-benefit-fund>
- Check (crosscheck): confirmed. Verified directly against the primary source. A WebFetch of https://www.anthropic.com/news/public-benefit-fund (title "Investing in the public benefit", dated Oct 18, 2026) shows a "Topics" section listing exactly five tags: Funding, Economic Futures, Labor market, Nonprofits, Leadership (plus a "See more..." link, which is a UI control, not a tag). The "Related articles" section lists exactly one item: "A research agenda for the Economic Futures Research Fund", category "Announcements", dated "Jul 22, 2026", followed by a "View more" link. Independent confirmation of the related article: Anthropic's Economic Futures hub page (https://www.anthropic.com/economic-futures) links the same title, category and date at /news/economic-futures-research-fund-agenda, and fetching that page confirms the title, "Jul 22, 2026" publication date and "Announcements" category. Anthropic's news index also lists "Investing in the public benefit" under Announcements, Oct 18, 2026. This claim concerns only page metadata (tags and related-article listing), so the 5% vs 20%, LLC vs PBC and 6 vs 7 cofounders confusions do not bear on it. Note: a "See more..." link next to the tags suggests the full tag list could be longer than the five visible tags; the claim is accurate as to what the page displays. WebSearch was unavailable this turn (search budget exhausted), so verification relied on WebFetch of Anthropic's own pages, which is the primary announcement and therefore satisfies the cross-check lens. Evidence: <https://www.anthropic.com/news/public-benefit-fund>

### F017 ✅ Проверено

What the post does NOT say: it is 8 paragraphs with a single heading and no subheadings; it names no individuals (no CEO, no Fund governors/trustees/directors; 'Amodei' and 'CEO' appear zero times); the only dollar figure is the $200 million already-committed sum (no valuation of the 5% stake, no fund size); the word 'board' appears once ('the board's discretion'); it does not mention an IPO, a stockholder vote date, the baseline valuation, a jurisdiction for the LLC, or any timeline beyond 'today' and 'in the coming months'.

Corrected by verification: The Oct 18, 2026 Anthropic post "Investing in the public benefit" is 8 paragraphs under a single h1 heading with no subheadings; it names no individuals ("Amodei" and "CEO" appear zero times; no Fund governors, trustees or directors); the only dollar figure is the $200 million already committed to labor-market work (no valuation of the 5% stake, no fund size); "board" appears once ("the board's discretion"); it does not mention an IPO, a stockholder vote date (only "Subject to stockholder approval"), the baseline valuation (only "a set baseline"), or a jurisdiction for the LLC, and gives no dated timeline beyond "today", "in the coming months", and a reference to "an upcoming public benefit report".

- Source: Anthropic, 2026-10-18 — <https://www.anthropic.com/news/public-benefit-fund> (confidence as rated by researcher: primary)
- Quote: «the board’s discretion ... a set baseline ... In the coming months»
- Check (fidelity): confirmed. Fetched https://www.anthropic.com/news/public-benefit-fund directly (Published Oct 18, 2026, Category Announcements). The article body consists of exactly 8 paragraphs under a single h1 ("Investing in the public benefit"); the only other heading tags on the page (h3 "Research", "Policy", "Company", etc.) are site footer navigation, not post subheadings. Term counts within the article: "Amodei" 0, "CEO" 0, no trustee/director/governor names, no individuals named at all. The only dollar figure is "$200 million" (labor-market commitment); no valuation of the 5% stake and no fund size. "board" appears exactly once ("at the board's discretion"). "IPO" 0, no stockholder vote date (only "Subject to stockholder approval"), the baseline is only "a set baseline" with no number, the LLC has no stated jurisdiction (0 hits for Delaware/jurisdiction). Timeline references: "today" (twice), "In the coming months", plus a vague "an upcoming public benefit report" — no dated timeline. Supporting quote fragments ("the board's discretion", "a set baseline", "In the coming months") all appear verbatim. The claim is accurate; the only tiny imprecision is that the post also says "upcoming" for the public benefit report, which is a vague temporal reference rather than a timeline. Evidence: <https://www.anthropic.com/news/public-benefit-fund>
- Check (crosscheck): confirmed. Verified directly against the primary source (https://www.anthropic.com/news/public-benefit-fund, dated Oct 18, 2026) using two independent methods: raw HTML downloaded via curl and parsed programmatically (saved at /tmp/claude-0/-home-user-an-info/b29c76c6-899a-5222-9671-bd3017164403/scratchpad/dl/pbf.html), plus a separate WebFetch rendering. Both agree on every point. Findings from the <article> element: exactly one heading (h1 "Investing in the public benefit"), zero h2/h3/h4 subheadings inside the article (the 11 h3s on the page are footer navigation, outside the body); exactly 8 substantive body paragraphs (the other <p> elements are metadata labels: Published/Oct 18, 2026/Category/Announcements/Topics, and a "Related articles" sidebar card dated Jul 22, 2026 for "A research agenda for the Economic Futures Research Fund"). Keyword counts in body text: 'Amodei' 0, 'CEO' 0, 'trustee' 0, 'director' 0, 'governor' 0, no personal names at all (co-founders and employees referenced only generically); '$' appears once, in "$200 million" (which is a hyperlink to a separate page); 'board' appears once, in "at the board's discretion"; 'IPO' 0; 'stockholder' once, in "Subject to stockholder approval" with no date; 'baseline' once, in "a set baseline" with no figure; 'Delaware' 0 and no jurisdiction given for the LLC (LLC mentioned twice); no valuation of the 5% stake and no fund size stated. Time references: 'today' (2 occurrences: "committed today" and "today's announcement") and "In the coming months"; the only other temporal language is vague ("an upcoming public benefit report", "When Anthropic was founded", "since founding", "already committed") with no dates. The post states 5% committed now, +2% per 50% value increase above a set baseline at the board's discretion, co-founders pledged 80% of their equity, and roughly 20% of shares in total dedicated to public good, which is consistent with the claim and shows no 5%/20% or LLC/PBC confusion (the Fund is an LLC; Anthropic itself is the public benefit corporation). Note: the shared web search budget for this turn was exhausted, so no third-party outlet could be checked; however, this claim is about the text of the announcement itself, for which the primary source is the authoritative evidence and was confirmed by two independent fetches. The claim is accurate; the corrected version adds only minor precision (two 'today' occurrences, the 'upcoming public benefit report' phrase, and the hyperlinked $200 million). Evidence: <https://www.anthropic.com/news/public-benefit-fund>

### F018 ✅ Проверено

Reuters reports that Anthropic also announced the fund in a post on X, and that Elon Musk responded to that X post recommending 'giving the shares directly to the public'; Musk then posted that he would give one SpaceX share to every kid in America next year.

- Source: Reuters (via Virginia Business), 2026-10-19 — <https://virginiabusiness.com/anthropic-commits-5-percent-stake-public-benefit-fund/> (confidence as rated by researcher: major_outlet)
- Quote: «Musk responded to an Anthropic post on X announcing the fund ... "Next year, I will give one of my SpaceX shares to every kid in America. This will be the first of many,"»
- Check (fidelity): confirmed. Opened the cited source (Virginia Business republishing Reuters, dateline "Oct 19 (Reuters)", reporting by Abu Sultan and Anusha Shah in Bengaluru). It states that Anthropic "said on Sunday it will commit 5% of its shares to a new public benefit fund"; that "Musk responded to an Anthropic post on X announcing the fund" by recommending "giving the shares directly to the public"; and that Musk then said in a post: "Next year, I will give one of my SpaceX shares to every kid in America. This will be the first of many." All elements of the claim (Reuters attribution, Anthropic X post announcing the fund, Musk's reply recommending direct distribution to the public, Musk's subsequent pledge of one SpaceX share per kid in America next year) match the source wording and date. The primary Anthropic announcement (anthropic.com/news/public-benefit-fund, dated Oct 18, 2026) does not mention X posts or Musk, which is expected since the Musk exchange is Reuters' reporting, not Anthropic's. Claim confirmed; no correction needed. Evidence: <https://virginiabusiness.com/anthropic-commits-5-percent-stake-public-benefit-fund/>
- Check (crosscheck): confirmed. CONFIRMED by the cited source plus an independent outlet and the primary announcement. (1) Cited source: the Virginia Business page is a verbatim Reuters wire story ("Oct 19 (Reuters)", reporters Abu Sultan and Anusha Shah, Bengaluru). It states that Anthropic announced the fund in a post on X; that Musk responded to that X post recommending "giving the shares directly to the public"; and that "in a post early Monday" (Mon 19 Oct 2026) he wrote: "Next year, I will give one of my SpaceX shares to every kid in America. This will be the first of many." It also notes Musk held ~6.42B SpaceX shares as of June and that SpaceX did not respond. (2) Independent confirmation: Fortune (staff reporter Emma Burleigh, 19 Oct 2026, 10:32 AM ET, not a wire pickup) independently reports Musk replied to Anthropic's announcement on X with "I recommend giving the shares directly to the public," and separately posted "Next year, I will give one of my SpaceX shares to every kid in America," adding "This will be the first of many." Fortune says the giveaway post "followed right after" Anthropic's announcement, consistent with Reuters' sequencing ("Musk then posted"). Fortune gives ~4.8B shares per an August SEC filing (6.4B incl. unvested awards/options) and estimates ~$10.5B for ~72M children at $146.03/share. (3) Primary source: anthropic.com/news/public-benefit-fund (18 Oct 2026) confirms the underlying fund facts: 5% of shares committed (subject to stockholder approval), structured as a wholly owned LLC (explicitly "rather than a 501(c)(3)"), +2% at board discretion per 50% valuation increase, co-founders pledged 80% of equity (number of co-founders not stated), ~20% total dedicated to public good, no lobbying/political giving. TechCrunch (Anthony Ha, 18 Oct) and Wikipedia also corroborate the 5% figure but do not mention the X post or Musk. Cross-check lens: the claim does not confuse 5% vs 20% (Reuters correctly states 5% to the fund, ~20% total), correctly describes the fund as an LLC, and makes no co-founder-count assertion. Could not fetch reuters.com, CNBC, Verge, Guardian, BI, AP, Axios, or x.com (blocked/403), and the WebSearch budget for this turn was exhausted before my first query, so verification relied on direct WebFetch of outlet pages. Minor precision note: Musk's exact words were "I recommend giving the shares directly to the public"; the SpaceX pledge was a separate post early Monday 19 Oct 2026, not necessarily in the same reply thread. Evidence: <https://fortune.com/2026/10/19/billionaire-elon-musk-give-every-kid-in-america-shares-of-spacex-add-up-to-10-billion-in-stock/>

### F019 ✅ Проверено

Reuters describes the escalator baseline as 'yet to be disclosed' and says Anthropic 'is planning one of the biggest IPOs in history as a public benefit corporation'; Anthropic 'said on Sunday' (Oct 18) it will commit 5% of its shares.

Corrected by verification: Reuters (via bdnews24, 19 Oct 2026) reports that Anthropic "said on Sunday" (18 Oct 2026) it will commit 5 percent of its shares to a new public benefit fund, that the fund would receive "an additional 2 percent of Anthropic's shares for every 50 percent increase in the company's value above a baseline yet to be disclosed" (Reuters does not use the word "escalator"), and that "Anthropic is planning one of the biggest IPOs in history as a public benefit corporation."

- Source: Reuters (via bdnews24), 2026-10-19 — <https://bdnews24.com/technology/cy70muyci4> (confidence as rated by researcher: major_outlet)
- Quote: «for every 50 percent increase in the company's value above a baseline yet to be disclosed.»
- Check (fidelity): confirmed. Opened the cited bdnews24 page (Reuters-attributed, headline "Anthropic to commit 5% stake to new 'public benefit fund'", published 19 Oct 2026). It contains all three quoted phrases verbatim: "AI lab Anthropic, the developer of Claude, said on Sunday it will commit 5 percent of its shares to a new public benefit fund"; "receive, at the board's discretion, an additional 2 percent of Anthropic's shares for every 50 percent increase in the company's value above a baseline yet to be disclosed"; and "Anthropic is planning one of the biggest IPOs in history as a public benefit corporation". The Sunday in question is 18 Oct 2026 (verified via `date`: Sunday), matching the primary Anthropic post "Investing in the public benefit" dated Oct 18, 2026, which says "5% of Anthropic's shares will be committed today... with an additional 2% added at the board's discretion for every 50% increase in the company's value above a set baseline." The only imprecision: the word "escalator" is not Reuters' wording (nor Anthropic's) but the claim does not present it as a quote; it is a descriptive label for the 2%-per-50%-increase mechanism. Numbers, date, and attribution all check out. Evidence: <https://bdnews24.com/technology/cy70muyci4>
- Check (crosscheck): confirmed. Verified directly against the cited source and the primary announcement. (1) The bdnews24 page (https://bdnews24.com/technology/cy70muyci4) is bylined "Reuters", headlined "Anthropic to commit 5% stake to new 'public benefit fund'", dated 19 Oct 2026, and contains verbatim: "said on Sunday it will commit 5 percent of its shares to a new public benefit fund"; "for every 50 percent increase in the company's value above a baseline yet to be disclosed"; and "The move comes at a time when Anthropic is planning one of the biggest IPOs in history as a public benefit corporation". It also says the fund "would be established as a wholly owned limited liability company" and that co-founders pledged 80% of their equity, for roughly 20% of shares combined. (2) Independent primary source: Anthropic's own post "Investing in the public benefit" (anthropic.com/news/public-benefit-fund), dated 18 Oct 2026 — which is a Sunday — confirms 5% of shares committed (subject to stockholder approval), the fund as a wholly owned LLC, a board-discretion escalator of +2% per 50% increase in value above a baseline whose amount is not stated (details on valuation milestones promised "in the coming months"), the cofounders' 80% pledge, and ~20% total. Anthropic is described as a public benefit corporation; the LLC is the fund, not Anthropic, so the claim does not confuse the two. The 5% figure is correct (20% is the combined figure including cofounder/employee pledges, which the claim does not conflate). The claim does not assert a cofounder count. Reuters.com itself could not be fetched (blocked for this tool) and the WebSearch budget was exhausted, so Reuters authorship rests on bdnews24's byline, but every substantive fact is confirmed by the primary announcement and nothing contradicts the claim. Evidence: <https://www.anthropic.com/news/public-benefit-fund>

### F020 ✅ Проверено

Reuters (via Virginia Business) reports Anthropic is preparing a market debut that could value it at roughly $2 trillion, with some investors weighing a valuation near $1.5 trillion, which would put the fund's 5% stake between $75 billion and $100 billion. (Figures as summarized from the Reuters text; exact wording beyond the quoted fragment not captured verbatim.)

Corrected by verification: A Reuters wire story dated Oct 19, 2026 (republished by Virginia Business; reporting by Abu Sultan and Anusha Shah) says Anthropic "is preparing for a market debut that could value it at roughly $2 trillion, although Reuters exclusively reported last week that some investors are weighing a lower valuation of around $1.5 trillion. That would value a 5% stake toward the fund in a range of $75 billion to $100 billion." These valuation figures are Reuters' own; Anthropic's Oct 18, 2026 announcement does not mention an IPO or any valuation figure.

- Source: Reuters (via Virginia Business), 2026-10-19 — <https://virginiabusiness.com/anthropic-commits-5-percent-stake-public-benefit-fund/> (confidence as rated by researcher: major_outlet)
- Quote: «Anthropic is preparing for a market debut that could value it at roughly $2 trillion»
- Check (fidelity): confirmed. The cited Virginia Business page is a Reuters wire story dated October 19, 2026 (dateline "Oct 19 (Reuters)", "Reporting by Abu Sultan and Anusha Shah in Bengaluru"). It contains verbatim: "Anthropic is preparing for a market debut that could value it at roughly $2 trillion, although Reuters exclusively reported last week that some investors are weighing a lower valuation of around $1.5 trillion. That would value a 5% stake toward the fund in a range of $75 billion to $100 billion." The supporting quote matches exactly; the $2T, $1.5T, $75B-$100B figures, the Oct 19 date, and the Reuters attribution are all present. Only trivial paraphrase differences: the source says "around $1.5 trillion" (claim says "near") and frames $75B-$100B as Reuters' own derived range for the 5% stake. The Anthropic primary announcement (dated Oct 18, 2026) contains none of these valuation figures, so they are Reuters' numbers, not Anthropic's, which the claim correctly attributes. Evidence: <https://virginiabusiness.com/anthropic-commits-5-percent-stake-public-benefit-fund/>
- Check (crosscheck): confirmed. Verified the cited Virginia Business page directly: it is a Reuters wire story (dateline "Oct 19 (Reuters)", reporting by Abu Sultan and Anusha Shah in Bengaluru, additional reporting by Deborah Sophia) and contains verbatim: "Anthropic is preparing for a market debut that could value it at roughly $2 trillion," "some investors are weighing a lower valuation of around $1.5 trillion," "That would value a 5% stake toward the fund in a range of $75 billion to $100 billion," and "The company is planning one of the biggest IPOs in history as a public benefit corporation." The arithmetic checks (5% x $1.5T = $75B; 5% x $2T = $100B). Independent corroboration: the primary announcement (anthropic.com/news/public-benefit-fund, Oct 18, 2026) confirms the 5% initial share commitment (subject to stockholder approval), with an additional 2% at board discretion per 50% increase in company value, the fund set up as an LLC (Anthropic itself is the public benefit corporation), and "roughly 20%" only as the combined total including earlier cofounder/employee pledges; it gives no valuation figures. TechCrunch (Oct 18, Anthony Ha) independently confirms the 5% commitment; Fortune (Oct 16 and Oct 17, 2026) and TechCrunch (Oct 23, 2026) independently report an IPO "that could reach $2 trillion" / "as much as $2 trillion"; Fortune also cites a longtime investor expecting pricing around $1.8T, below the $2T target, consistent with investors weighing lower valuations. The specific "$1.5 trillion" figure is only sourced to the Reuters story itself (unnamed investors); no second outlet carrying that exact number was found (reuters.com is unreachable from this environment and the web-search budget was exhausted), but Reuters is a reputable primary reporter and the claim correctly attributes it. No 5%-vs-20%, LLC-vs-PBC, or cofounder-count errors in the claim. Claim is accurate; minor precision tweaks given in corrected_claim. Evidence: <https://virginiabusiness.com/anthropic-commits-5-percent-stake-public-benefit-fund/>

### F021 ✅ Проверено

Al Jazeera (John Power, 19 Oct 2026) reports Anthropic is 'expected to list on the US stock market before the end of 2026' with analysts forecasting a valuation 'exceeding $2 trillion'; it quotes the blog post but no executive by name.

Corrected by verification: Al Jazeera (John Power, 19 Oct 2026) reports Anthropic "is preparing for what could be the largest public initial offering in history" and "is expected to list on the US stock market before the end of 2026, with analysts forecasting a valuation exceeding $2 trillion"; the analysts are not named, no Anthropic executive is named or quoted, and the IPO/valuation statements do not appear in Anthropic's own blog post, which the article quotes for the fund details.

- Source: Al Jazeera, 2026-10-19 — <https://www.aljazeera.com/economy/2026/10/19/anthropic-says-it-will-commit-5-of-shares-to-public-benefit-fund> (confidence as rated by researcher: major_outlet)
- Quote: «expected to list on the US stock market before the end of 2026»
- Check (fidelity): confirmed. Opened the cited Al Jazeera URL. Byline: John Power, published 19 October 2026 — matches. The article contains verbatim: "Founded in 2021 by former employees of ChatGPT creator OpenAI, Anthropic is preparing for what could be the largest public initial offering in history. It is expected to list on the US stock market before the end of 2026, with analysts forecasting a valuation exceeding $2 trillion." Both the supporting quote and the "$2 trillion" figure are present exactly as claimed. The article attributes statements to Anthropic and its blog post (quoting e.g. "the more Anthropic grows, the larger the share of the company that can be dedicated expressly to the public good" and "We are instead directing that equity to the public benefit") and names no Anthropic executive in the body — the only personal names are the byline (John Power), a photo credit, and sidebar links. Cross-checked the primary source (anthropic.com/news/public-benefit-fund): it does not mention an IPO, listing date, or any dollar valuation, confirming the IPO/valuation lines are Al Jazeera's own reporting (unsourced "analysts") rather than something from the blog post. Minor nuance: the article's phrase is "public initial offering" (not "initial public offering"), and the "largest ... in history" framing is hedged with "could be"; neither affects the claim's accuracy. Evidence: <https://www.aljazeera.com/economy/2026/10/19/anthropic-says-it-will-commit-5-of-shares-to-public-benefit-fund>
- Check (crosscheck): confirmed. Direct fetch of the cited Al Jazeera article confirms every element of the claim: byline John Power, published 19 Oct 2026; verbatim sentence "It is expected to list on the US stock market before the end of 2026, with analysts forecasting a valuation exceeding $2 trillion" (preceded by "Anthropic is preparing for what could be the largest public initial offering in history"); the article quotes only Anthropic's blog post and names no executive; it names no analysts and contains no inline links, so the IPO timing and $2T figure are unattributed. It correctly states 5 percent of shares committed (with an additional 2 percent at the board's discretion per 50 percent increase in value) and does not conflate this with the "roughly 20%" total public-good figure, nor does it mischaracterize the fund's structure or give a cofounder count.

Independent cross-checks: (1) Primary source, Anthropic's "Investing in the public benefit" post (18 Oct 2026, anthropic.com/news/public-benefit-fund) confirms 5% committed subject to stockholder approval, the fund is a wholly owned LLC (not a 501(c)(3)), "roughly 20%" is the aggregate including cofounders' 80% pledge and employee match, no IPO/listing mention, no named executive quotes. (2) TechCrunch, Anthony Ha, 18 Oct 2026, independently confirms 5% plus the 2%-per-50% mechanism and "wholly owned entity" framing. (3) TechCrunch, Marina Temkin, 23 Oct 2026, independently reports Anthropic's "public listing, which is expected this year" "at a valuation of as much as $2 trillion," with latest private valuation $965B (consistent with Reuters, 28 May 2026, cited on Wikipedia). (4) Wikipedia (citing NYT May 2026, confidential SEC filing announced 1 June 2026, and WSJ Sept 2026 reporting a November 2026 IPO target) corroborates a listing expected before end-2026. Minor framing difference only: TechCrunch says "as much as $2 trillion" where Al Jazeera says "exceeding $2 trillion," but the claim accurately reports Al Jazeera's wording. Note: web search budget was exhausted this turn; verification relied on direct fetches of primary and outlet pages (Reuters, Guardian, CNBC, AP pages were blocked/403). Evidence: <https://www.aljazeera.com/economy/2026/10/19/anthropic-says-it-will-commit-5-of-shares-to-public-benefit-fund>

### F022 ✅ Проверено

TechCrunch (Anthony Ha, Oct 18, 2026, 1:37 PM PDT) reports the announcement was made 'on Sunday', quotes the blog's 'increased flexibility and scale' and 'bolder approaches may be needed' lines, and gives no valuation figure.

Corrected by verification: TechCrunch (Anthony Ha, 1:37 PM PDT, Oct 18, 2026) reports Anthropic "announced on Sunday" it is creating a public benefit fund committing 5% of its shares (plus an optional additional 2% for every 50% increase in Anthropic's value), quotes the blog's "increased flexibility and scale" and "given the pace of AI progress, bolder approaches may be needed. The Fund will have the versatility to pursue them" lines, and gives no dollar valuation for Anthropic (the only dollar figure mentioned is a separate $200 million study commitment); it describes the fund as "a wholly owned entity within the company" without using the terms LLC or PBC and does not mention cofounders.

- Source: TechCrunch, 2026-10-18 — <https://techcrunch.com/2026/10/18/anthropic-says-its-committing-5-of-its-shares-to-a-public-benefit-fund/> (confidence as rated by researcher: major_outlet)
- Quote: «given the pace of AI progress, bolder approaches may be needed. The Fund will have the versatility to pursue them.»
- Check (fidelity): confirmed. Fetched the cited TechCrunch URL directly. It is bylined Anthony Ha with the timestamp "1:37 PM PDT · October 18, 2026" (Oct 18, 2026 is a Sunday, consistent with the day reference). The article opens "Anthropic announced on Sunday that it's creating a 'public benefit fund'". It quotes Anthropic's blog verbatim for "increased flexibility and scale" and for "given the pace of AI progress, bolder approaches may be needed." plus "The Fund will have the versatility to pursue them." — matching the supporting quote supplied. It contains no dollar valuation of Anthropic or of the fund; the only dollar figure is a separate $200 million jobs-impact commitment, and the 5% share commitment / +2% per 50% value increase is given without any dollar amount. The primary Anthropic post (anthropic.com/news/public-benefit-fund, dated Oct 18, 2026) contains the same sentences, confirming the quotes are accurate and not fabricated. All elements of the claim (author, date/time, 'on Sunday', both quotes, no valuation) check out. Evidence: <https://techcrunch.com/2026/10/18/anthropic-says-its-committing-5-of-its-shares-to-a-public-benefit-fund/>
- Check (crosscheck): confirmed. Direct fetch of the cited TechCrunch URL confirms every element: byline Anthony Ha, timestamp "1:37 PM PDT · October 18, 2026"; opening sentence "Anthropic announced on Sunday that it's creating a 'public benefit fund'..."; the article quotes both "increased flexibility and scale" and "given the pace of AI progress, bolder approaches may be needed. The Fund will have the versatility to pursue them." It gives no dollar valuation for Anthropic (the only dollar figure is a separate "$200 million" study commitment, plus the mechanism "an additional 2% for every 50% increase in Anthropic's value"). It states 5% of shares (not 20%), calls the fund "a wholly owned entity within the company" (does not label it LLC or PBC), and does not mention or count cofounders. Oct 18, 2026 was indeed a Sunday (verified with `date`). Independent cross-check: the primary announcement at https://www.anthropic.com/news/public-benefit-fund ("Investing in the public benefit", Oct 18, 2026) contains the identical quoted lines verbatim, states "5% of Anthropic's shares will be committed today", describes the Fund as "a new wholly owned entity" established "as an LLC" (while Anthropic itself is "a public benefit corporation"), gives no valuation figure, and refers only to "our co-founders" pledging 80% of their equity without a count. Note: WebSearch budget was exhausted this turn, so cross-checking relied on fetching the primary source directly; it fully corroborates the TechCrunch reporting. Evidence: <https://www.anthropic.com/news/public-benefit-fund>

### F023 ✅ Проверено

The Associated Press (copy dated Oct 21, 2026 via The Daily Times) says Anthropic is planning a large initial public offering as soon as November, names CEO Dario Amodei, and quotes no spokesperson beyond the blog post.

Corrected by verification: The Associated Press (copy dated Oct 21, 2026 via The Daily Times) says "Anthropic is planning a massive initial public offering as soon as November," names "CEO Dario Amodei and the company's five other cofounders," and quotes no individual or spokesperson — its only quoted language is attributed to what "Anthropic said in a blog post," including the line that the fund "will have increased flexibility and scale, enabling us to pursue our mission in new ways."

- Source: Associated Press (via The Daily Times), 2026-10-21 — <http://www.thedailytimes.com/ap/business/anthropic-commits-5-of-its-stock-to-a-new-public-benefit-fund/article_ec699a60-48e9-5bd3-a5bc-f339d19009c2.html> (confidence as rated by researcher: major_outlet)
- Quote: «will have increased flexibility and scale, enabling us to pursue our mission in new ways»
- Check (fidelity): confirmed. Fetched the cited Daily Times page directly (HTTP 200; datePublished meta = 2026-10-21T23:30:00-04:00, byline "By The Associated Press", AP copyright notice). The article text contains: "Anthropic is planning a massive initial public offering as soon as November." It names "CEO Dario Amodei and the company's five other cofounders." The only quoted language is attributed to "Anthropic said in a blog post" — the exact quote "will have increased flexibility and scale, enabling us to pursue our mission in new ways" appears verbatim, and there is no spokesperson, spokeswoman/spokesman or "declined to comment" line anywhere in the copy. The primary source (anthropic.com/news/public-benefit-fund, dated Oct 18, 2026) contains the identical "increased flexibility and scale" sentence, names no individuals, and does not mention an IPO — so the IPO line is AP's own context, as the claim implies. The only imprecision is "large" vs. the article's actual word "massive"; otherwise every element (date, outlet, attribution, IPO timing, Amodei named, no spokesperson quoted, quote wording) checks out. Note: WebSearch budget was exhausted, but direct fetches of both the cited and primary source were sufficient. Evidence: <https://www.thedailytimes.com/ap/business/anthropic-commits-5-of-its-stock-to-a-new-public-benefit-fund/article_ec699a60-48e9-5bd3-a5bc-f339d19009c2.html>
- Check (crosscheck): confirmed. Directly verified against the cited AP syndication copy (The Daily Times, dated Oct 21, 2026, "By The Associated Press"): the article states Anthropic is planning a "massive" initial public offering "as soon as November"; it names CEO Dario Amodei (as having established Anthropic as a public benefit corporation together with "five other cofounders"); and it quotes no spokesperson or executive — all statements are attributed to and linked from Anthropic's blog post. The supporting quote "will have increased flexibility and scale, enabling us to pursue our mission in new ways" appears verbatim in Anthropic's primary announcement "Investing in the public benefit" (anthropic.com/news/public-benefit-fund, Oct 18, 2026). Independent corroboration: TechCrunch (Oct 18, 2026, Anthony Ha) independently reports the 5% share commitment, names CEO Dario Amodei, quotes no spokesperson, and uses the "increased flexibility and scale" language; Wikipedia's Anthropic article cites the Wall Street Journal (Sept 18, 2026, "Anthropic Shifts Planned IPO to November") for the November 2026 IPO timing, so AP's IPO statement is consistent with prior reputable reporting. Cross-check flags: (a) 5% vs 20% — AP correctly says 5% committed now and roughly 20% combined with earlier pledges, matching the primary source; the claim itself does not cite a percentage. (b) LLC vs PBC — the primary source says the Fund is "a new wholly owned entity" established "as an LLC"; AP calls it "a new entity within the company" and (correctly) describes Anthropic itself as a public benefit corporation; the claim does not assert an entity type. (c) Cofounders — the AP copy says "Dario Amodei and the five other cofounders" (six), whereas Wikipedia's body text says seven founders; this is a likely inaccuracy in the AP copy but is not part of the claim being checked. Only imprecision in the claim: AP's word is "massive," not "large." Note: WebSearch budget was exhausted this turn, so verification relied on direct fetches of the cited article, the primary announcement, TechCrunch, and Wikipedia; apnews.com, Reuters, WSJ and CNBC pages could not be fetched directly. Evidence: <http://www.thedailytimes.com/ap/business/anthropic-commits-5-of-its-stock-to-a-new-public-benefit-fund/article_ec699a60-48e9-5bd3-a5bc-f339d19009c2.html>

### F024 🟠 Вторичный источник

ESG Today (Mark Segal, Oct 19, 2026) quotes the announcement describing the fund as 'dedicated entirely to the public benefit' -- a phrase that does NOT appear in the blog post text (the blog says 'dedicated expressly to the public good'), suggesting it may come from Anthropic's X post.

Corrected by verification: ESG Today (Mark Segal, Oct 19, 2026) describes the Anthropic Public Benefit Fund as "a new entity described by the company as 'dedicated entirely to the public benefit'". That exact phrase does not appear in Anthropic's Oct 18, 2026 blog post (nor in its meta/og/twitter descriptions); the blog instead says the company can be "dedicated expressly to the public good" and that "roughly 20% of Anthropic shares will be dedicated to the public good". ESG Today does not cite an X post, and the origin of its "dedicated entirely to the public benefit" wording could not be verified (Anthropic's X account could not be retrieved).

- Source: ESG Today, 2026-10-19 — <https://www.esgtoday.com/anthropic-commits-5-of-shares-to-a-new-public-benefit-fund/> (confidence as rated by researcher: secondary)
- Quote: «dedicated entirely to the public benefit,»
- Check (fidelity): confirmed. Verified against both sources. (1) ESG Today (Mark Segal, Oct 19, 2026) does contain the phrase, in the first paragraph: 'AI developer Anthropic announced the launch of "Anthropic Public Benefit Fund," a new entity described by the company as "dedicated entirely to the public benefit,"' -- so the quote, author, date and attribution to the company are accurately reported. (2) Anthropic's blog post (https://www.anthropic.com/news/public-benefit-fund, Oct 18, 2026) was fetched raw: the phrase "dedicated entirely to the public benefit" does not appear anywhere in the body, title, meta description, og:description or twitter:description; the word "entirely" appears nowhere on the page. The blog does contain "...the larger the share of the company that can be dedicated expressly to the public good" and "roughly 20% of Anthropic shares will be dedicated to the public good", exactly as the claim states. (3) The only unverified part is the hedged speculation that the phrase comes from Anthropic's X post: the ESG Today article does not mention or cite any X/Twitter post, and I could not retrieve x.com/AnthropicAI (HTTP 402), so the origin of ESG Today's wording remains unconfirmed. Since the core factual assertions are confirmed and the X-post attribution is explicitly framed as a possibility, the claim stands with a precision note. Evidence: <https://www.esgtoday.com/anthropic-commits-5-of-shares-to-a-new-public-benefit-fund/>

### F025 🔴 Не подтверждено

A search-engine summary surfaced wording attributed to Anthropic -- 'a new wholly owned entity dedicated entirely to the public benefit. It will start off with 5% of our shares.' -- which is not in the blog post and could not be located verbatim in any fetched article; it is plausibly the text of the @AnthropicAI X post but is UNVERIFIED.

- Source: Search snippet (unverified), 2026-10-18 — <https://www.anthropic.com/news/public-benefit-fund> (confidence as rated by researcher: speculative)
- Quote: «a new wholly owned entity dedicated entirely to the public benefit. It will start off with 5% of our shares.»
- Check (fidelity): REFUTED. Fetched the cited/primary source https://www.anthropic.com/news/public-benefit-fund (title "Investing in the public benefit", dated Oct 18, 2026) twice. The quoted wording is NOT in it. The article's actual opening sentences are: "Today, we're committing a portion of Anthropic's shares to the Anthropic Public Benefit Fund, a new wholly owned entity with a structure that increases the stake as the company grows." and "Subject to stockholder approval, 5% of Anthropic's shares will be committed today, with an additional 2% added at the board's discretion for every 50% increase in the company's value above a set baseline." The phrases "dedicated entirely to the public benefit" and "It will start off with 5% of our shares" do not appear anywhere in the page. The underlying facts (new wholly owned entity; 5% of shares committed, subject to stockholder approval) are accurate, but the supporting quote is a misquote/paraphrase that the cited source does not contain. I attempted to verify the alternative attribution to the @AnthropicAI X post by fetching x.com/AnthropicAI, which returned HTTP 402 and could not be read; the per-turn web search budget was already exhausted, so no further corroboration was possible. Since the exact wording cannot be confirmed in the cited source or any other fetched source, and the task's source-fidelity rule treats text the source does not contain as a misquote, refuted=true. If the harness wants a quotable version, use the verbatim blog sentences above and drop the search-snippet wording. Evidence: <https://www.anthropic.com/news/public-benefit-fund>

Researcher notes: PRIMARY TEXT: The full announcement (https://www.anthropic.com/news/public-benefit-fund) was retrieved in full via direct HTTP (200, ~170 KB) and the body text extracted; all 'primary' quotes above are verbatim from that extraction. The post is short: 8 paragraphs, ~470 words, one heading ('Investing in the public benefit'), no subheadings, no byline, no images referenced in body. Full body text, in order: P1 lede + 5%/2%/50% sentence; P2 PBC/in-house work; P3 flexibility and scale + two example uses; P4 labor market + $200M; P5 LLC vs 501(c)(3) + no lobbying/political giving; P6 escalator rationale vs executive compensation; P7 cofounders 80% / match program / half of employees / ~20%; P8 coming months + public benefit report.

BASELINE FACTS CHECK: All baseline facts in the task were verified against the primary text and match exactly (5% subject to stockholder approval; +2% at board's discretion per 50% increase above 'a set baseline'; wholly owned entity, LLC chosen over 501(c)(3) 'or other format' for 'adjustability between different forms of giving'; no lobbying/political giving US or abroad; large donations to traditional nonprofits or direct distributions to specific populations; $200M already committed to labor market issue; co-founders pledged 80% of equity holdings at founding; employee equity donation match program, 'approximately half' participate; 'roughly 20%' combined; more on structure/governance and valuation milestones 'in the coming months'; 'upcoming public benefit report'). Nuance: the post says 'wholly owned entity' in P1 and 'LLC' in P5; it never literally says 'wholly owned LLC' in one phrase. The baseline is 'a set baseline' -- the post does not say 'undisclosed'; that characterization comes from Reuters ('yet to be disclosed').

WHAT THE POST DOES NOT SAY: no named people at all (no Amodei, no board members, no Fund governors/managers/trustees); no dollar value of the stake or the fund; no current valuation; no baseline figure; no IPO mention; no date for the stockholder vote, the governance details, or the public benefit report; no LLC jurisdiction; no statement of who controls distributions; the word 'jobs' does not appear ('workers' is used). The page metadata shows dateModified 2026-10-21, i.e. the page was edited three days after publication (content of the edit unknown).

X/TWITTER POST: Could not be retrieved. x.com/AnthropicAI returned HTTP 402; xcancel.com returned HTTP 451; no search result returned a status URL. Reuters confirms an Anthropic X post exists ('Musk responded to an Anthropic post on X announcing the fund'). The phrases 'dedicated entirely to the public benefit' (quoted by ESG Today) and 'It will start off with 5% of our shares' (search snippet) are not in the blog and are likely from the X post, but this is unverified.

SOURCE DISCREPANCIES: bdnews24's Reuters copy describes Musk as running 'Anthropic rival SpaceXSI' (apparently garbled); Taiwan News' Reuters copy says 'xAI'. Al Jazeera does not mention Musk even though search snippets suggested it did. The AP copy (Oct 21) says IPO 'as soon as November'; Al Jazeera says 'before the end of 2026'. Valuation figures ($1.5T-$2T; stake $75B-$100B) appear only in Reuters-derived coverage and were captured by summarization rather than verbatim, so treat exact wording with care. Blocked fetchers: aimagazine.com (403), x.com (402), xcancel.com (451). The 'in the coming months' governance details and the public benefit report had not been published as of 2026-10-24 per the sources found.


## Финансы, оценка и IPO / finance-ipo (45)

### F026 🟢 Первоисточник

Anthropic's announcement 'Investing in the public benefit' (published October 18, 2026) commits 5% of Anthropic's shares to the Anthropic Public Benefit Fund subject to stockholder approval, with the board able to add 2% for every 50% increase in company value above a set baseline; the announcement contains no valuation figure, no dollar value for the stake and no mention of the IPO. The only dollar figure is the $200 million Economic Futures commitment.

- Source: Anthropic, 2026-10-18 — <https://www.anthropic.com/news/public-benefit-fund> (confidence as rated by researcher: primary)
- Quote: «Subject to stockholder approval, 5% of Anthropic's shares will be committed today.»

### F027 🟢 Первоисточник

The Fund is structured as an LLC rather than a 501(c)(3) to allow adjustability between forms of giving; none of its equity may be used for lobbying or political giving in the US or abroad; combined with cofounders' 80% pledge and the employee equity match (about half of employees participate), roughly 20% of Anthropic shares will be dedicated to the public good; more on structure, governance and valuation milestones is promised 'in the coming months', plus an upcoming public benefit report.

- Source: Anthropic, 2026-10-18 — <https://www.anthropic.com/news/public-benefit-fund> (confidence as rated by researcher: primary)
- Quote: «None of the Anthropic equity held by the LLC will be used for lobbying or political giving, in the US or abroad.»

### F028 🟡 Крупное СМИ

Anthropic's latest private round is the $65 billion Series H announced May 28, 2026 at a $965 billion post-money valuation, co-led by Altimeter Capital, Dragoneer, Greenoaks, Sequoia Capital, Capital Group, Coatue and D1 Capital Partners; $15 billion of the round was previously committed hyperscaler money including $5 billion from Amazon announced in April; Anthropic said its revenue run rate 'crossed $47 billion earlier this month'.

- Source: TechCrunch, 2026-05-28 — <https://techcrunch.com/2026/05/28/anthropic-raises-65-billion-nears-1t-valuation-ahead-of-ipo/> (confidence as rated by researcher: major_outlet)
- Quote: «crossed $47 billion earlier this month»

### F029 🟡 Крупное СМИ

Yahoo Finance (Daniel Howley, May 29, 2026) reported Anthropic raised $65 billion at a $965 billion valuation, led by Altimeter Capital, Dragoneer, Greenoaks and Sequoia Capital, above OpenAI's March valuation of $852 billion, with a $47 billion run rate earlier that month, and framed the company as racing to go public before OpenAI.

- Source: Yahoo Finance, 2026-05-29 — <https://finance.yahoo.com/markets/article/anthropic-raises-65-billion-in-latest-funding-round-making-it-more-valuable-than-openai-184115591.html> (confidence as rated by researcher: major_outlet)
- Quote: «Anthropic is in a sprint to go public before archrival OpenAI.»

### F030 🟡 Крупное СМИ

Reuters (Aug 17, 2026) reported Anthropic's annual revenue run rate topped $65 billion by the end of July, up from $47 billion in May and about $9 billion at the end of 2025; Bloomberg first reported the figure. The same Reuters piece restated that Anthropic was valued at $965 billion in May after raising $65 billion in its Series H round, and noted a prior Reuters report that Anthropic projects 2028 revenue of roughly $190-200 billion.

- Source: Reuters (via Yahoo Finance), 2026-08-17 — <https://finance.yahoo.com/technology/ai/articles/anthropic-revenue-run-rate-tops-213602454.html> (confidence as rated by researcher: major_outlet)
- Quote: «Anthropic's annual revenue run rate topped $65 billion by the end of July»

### F031 🟡 Крупное СМИ

Reuters exclusive (Aug 14, 2026, via Investing.com Aug 15) reported Anthropic is projecting annual revenue of roughly $190 billion to $200 billion by 2028, citing people familiar with its finances, and that bankers and investors are applying enterprise value-to-revenue multiples to 2028 forecasts to anchor the IPO valuation; David Merkel of Aleph Investments said the company 'could potentially secure a $2 trillion valuation'.

- Source: Reuters (via Investing.com), 2026-08-15 — <https://www.investing.com/news/stock-market-news/anthropic-ipo-valuation-rests-on-up-to-200-billion-2028-revenue-target--reuters-4861731> (confidence as rated by researcher: major_outlet)
- Quote: «projecting annual revenue of roughly $190 billion to $200 billion by 2028»

### F032 🟡 Крупное СМИ

Reuters (Milana Vinn and Krystal Hu, Oct 14, 2026) reported from Anthropic's pre-IPO investor day in San Francisco that third-quarter revenue rose to $16.8 billion from $11.6 billion in the second quarter (up 45% sequentially), that Anthropic said it was profitable on an adjusted basis in Q3, that analysts estimated the annual run rate could reach $110 billion by year-end, that Anthropic is targeting a valuation of over $2 trillion, and that the debut 'is likely to be pushed until after the November US midterm elections'. The FT first reported the Q3 figure.

- Source: Reuters (via Investing.com), 2026-10-14 — <https://www.investing.com/news/stock-market-news/anthropics-q3-revenue-surges-45-to-nearly-17-billion-4950208> (confidence as rated by researcher: major_outlet)
- Quote: «Third-quarter revenue rose to $16.8 billion from $11.6 billion in the second quarter»

### F033 🟡 Крупное СМИ

Reuters (Milana Vinn and Anirban Sen, Oct 15, 2026) reported that some investors who attended Anthropic's investor day on Wednesday in San Francisco discussed a valuation of around $1.5 trillion for the November share sale, down from the roughly $2 trillion previously expected, after Q3 revenue growth of 45% to $16.8 billion slowed from Q2 (when revenue more than doubled to $11.6 billion); 2025 revenue was nearly $4.6 billion with an operating loss above $8 billion and a $42 billion net loss; Anthropic has committed to spending at least $518 billion over a decade on cloud, compute and infrastructure.

- Source: Reuters (via WTVB), 2026-10-15 — <https://wtvbam.com/2026/10/15/exclusive-investors-temper-anthropic-ipo-valuation-expectations-over-revenue-growth-slowdown-sources-say/> (confidence as rated by researcher: major_outlet)
- Quote: «roughly $2 trillion valuation that investors had previously expected for the November share sale»

### F034 🟡 Крупное СМИ

The Telegraph (via Yahoo Finance, Oct 15, 2026) characterized the Reuters report as investors considering slashing Anthropic's valuation by $500bn, from the $2tn previously expected for the November listing to about $1.5tn, and said Q3 revenue of nearly $17bn was up around 45% from $11.6bn in Q2, versus 146% growth between Q1 and Q2.

- Source: The Telegraph (via Yahoo Finance), 2026-10-15 — <https://finance.yahoo.com/technology/ai/articles/anthropic-valuation-could-slashed-500bn-014243238.html> (confidence as rated by researcher: major_outlet)
- Quote: «Anthropic investors are considering slashing the company's valuation by $500bn (£379bn)»

### F035 🟠 Вторичный источник

FinanceFeeds (Damilola Esebame, Oct 20, 2026) computed that the 5% allocation 'would be worth approximately $48 billion at the company's last reported $965 billion valuation' and 'about $75 billion at the $1.5 trillion valuation investors are reportedly discussing', and said the pledge arrives 'weeks before the AI safety company is expected to launch its initial public offering'; it also said investors are pushing toward roughly $1.5 trillion, below the $2 trillion target initially sought.

- Source: FinanceFeeds, 2026-10-20 — <https://financefeeds.com/anthropic-locks-5-of-equity-into-public-fund/> (confidence as rated by researcher: secondary)
- Quote: «The 5% allocation would be worth approximately $48 billion at the company's last reported $965 billion valuation»

### F036 🟡 Крупное СМИ

CNBC's Kate Rooney (video report dated Oct 19, 2026, as quoted by 24/7 Wall St on Oct 20) said the fund is 'starting with a 5% stake, which could be worth at least $50 billion' and 'Could be closer to $100 billion if the company debuts at a $2 trillion price tag'; she added 'The IPO does come amid public backlash' and that 'Some are questioning why Anthropic would retain control of the money versus just giving it away directly'.

- Source: CNBC (Kate Rooney) via 24/7 Wall St, 2026-10-20 — <https://247wallst.com/investing/2026/10/20/anthropic-sets-aside-5-stake-for-public-benefit-fund-ahead-of-november-ipo/> (confidence as rated by researcher: major_outlet)
- Quote: «starting with a 5% stake, which could be worth at least $50 billion.»

### F037 🟡 Крупное СМИ

CNBC's Oct 18, 2026 story 'Anthropic commits 5% of shares to new public benefit fund that could address AI job disruption' quoted Lise Buyer, partner at IPO advisory firm Class V Group, saying the timing of the announcement is both mandatory to prepare for an IPO and 'beneficial from an image perspective', especially as AI reshapes the jobs market; the CNBC page itself returned HTTP 403 to the fetcher and the wording is confirmed via search snippets and syndications (Slashdot, Breitbart, FinanceFeeds).

- Source: CNBC, 2026-10-18 — <https://www.cnbc.com/2026/10/18/anthropic-ai-public-benefit-fund.html> (confidence as rated by researcher: major_outlet)
- Quote: «beneficial from an image perspective»

### F038 🟠 Вторичный источник

Breitbart (Lucas Nolan, Oct 19, 2026), relaying CNBC, quoted Lise Buyer that the timing ahead of the public offering is 'beneficial from an image perspective' and added her remark: 'Of course, it is also to burnish their reputation at a time when AI is coming under significant scrutiny.' The same piece said the IPO 'could occur as soon as November', cited Q3 revenue of $16.8 billion, and reported Palmer Luckey called the fund 'USAID 2.0'.

- Source: Breitbart (relaying CNBC), 2026-10-19 — <https://www.breitbart.com/tech/2026/10/19/anthropic-will-dedicate-5-of-shares-to-public-benefit-fund-ahead-of-landmark-ai-ipo/> (confidence as rated by researcher: secondary)
- Quote: «Of course, it is also to burnish their reputation at a time when AI is coming under significant scrutiny.»

### F039 🟠 Вторичный источник

Slashdot (Oct 19, 2026), summarizing CNBC, reported that Lise Buyer, a partner at IPO advisory firm Class V Group, said the timing is 'beneficial from an image perspective' and is also needed to prepare for an initial public offering; it also relayed Reuters' note that roughly 20% of shares will be dedicated to public purposes and Elon Musk's X post recommending the shares be given directly to the public.

- Source: Slashdot, 2026-10-19 — <https://it.slashdot.org/story/26/10/19/0252201/anthropic-announces-public-benefit-fund-committing-5-of-its-shares> (confidence as rated by researcher: secondary)
- Quote: «beneficial from an image perspective»

### F040 🟡 Крупное СМИ

Reuters' wire story on the fund (Abu Sultan and Anusha Shah, Oct 18, 2026) said the proposed fund 'would be established as a wholly owned limited liability company', that the fund 'would receive an additional 2% of Anthropic's shares, at the board's discretion' above 'a baseline that has yet to be disclosed', that 'roughly 20% of Anthropic's shares would be dedicated to public purposes', and described Anthropic as 'planning one of the biggest IPOs in history as a public benefit corporation'; it gave no valuation, dollar value, revenue or IPO date.

- Source: Reuters (via Yahoo Finance), 2026-10-18 — <https://finance.yahoo.com/technology/ai/articles/anthropic-commit-5-stake-public-191115841.html> (confidence as rated by researcher: major_outlet)
- Quote: «planning one of the biggest IPOs in history as a public benefit corporation»

### F041 🟠 Вторичный источник

Dealroom (Oct 18, 2026) tied the fund to the Series H valuation, writing 'A $65 billion round in May valued it at $965 billion, meaning the pledged equity could become a substantial sum', and said Anthropic 'prepares what would be the largest IPO for a public benefit corporation'; it cited BBC reporting that a listing 'could value it at more than $1 trillion' and gave no dollar value for the 5%.

- Source: Dealroom, 2026-10-18 — <https://dealroom.co/news/163719-anthropic-pledges-5-of-shares-to-public-benefit-fund-as-it-eyes-record-i/> (confidence as rated by researcher: secondary)
- Quote: «A $65 billion round in May valued it at $965 billion, meaning the pledged equity could become a substantial sum.»

### F042 🟡 Крупное СМИ

On a Yahoo Finance 'Market Hang' panel video (Oct 19, 2026, with Julie Hyman, Mark Malek, Cory Johnson and The Wall Street Skinny co-founders Jen Saarbach and Kristen Kelly), one speaker said 'Taking 5% of the shares is yes, it's 100 billion dollars into a new charity', 'it also takes 5% of the float away from the IPO filing', 'They could price this thing kind of wherever they want if they keep the float low enough, and this does that even further', and 'we think it's Morgan Stanley on the left and Goldman Sachs as well on this deal'; the description says the IPO is 'planned for November'.

- Source: Yahoo Finance, 2026-10-19 — <https://finance.yahoo.com/video/how-anthropics-5-public-benefit-fund-could-reshape-its-ipo-172547871.html> (confidence as rated by researcher: major_outlet)
- Quote: «But it also takes 5% of the float away from the IPO filing, right?»

### F043 ⚪ Оценка или мнение

TradingKey analysis (Block Tao, Oct 19, 2026) called the fund 'the most critical strategic pawn to pave the way for its mega initial public offering', framed it as a governance/compliance step to ease regulatory concerns and attract ESG institutional capital, cited Reuters on investors 'pushing to cut Anthropic's IPO valuation from the original $2 trillion to around $1.5 trillion', and cited pre-IPO OTC data showing the valuation 'fell from $2.1 trillion at the beginning of the month to $1.909 trillion'.

- Source: TradingKey, 2026-10-19 — <https://www.tradingkey.com/analysis/stocks/us-stocks/262223123-stock-anthropic-ipo-tradingkey> (confidence as rated by researcher: speculative)
- Quote: «the most critical strategic pawn to pave the way for its mega initial public offering»

### F044 🟡 Крупное СМИ

TechCrunch's fund story (Anthony Ha, Oct 18, 2026) reported the fund as 'structured as a wholly owned entity within the company' with 'the option to contribute an additional 2% for every 50% increase in Anthropic's value', quoted CEO Dario Amodei calling AI backlash 'fundamentally a crisis of trust', and gave no valuation, dollar value or IPO details.

- Source: TechCrunch, 2026-10-18 — <https://techcrunch.com/2026/10/18/anthropic-says-its-committing-5-of-its-shares-to-a-public-benefit-fund/> (confidence as rated by researcher: major_outlet)
- Quote: «with the option to contribute an additional 2% for every 50% increase in Anthropic's value»

### F045 🟢 Первоисточник

Anthropic announced on June 1, 2026 that it 'confidentially submitted a draft registration statement on Form S-1' to the SEC for a proposed IPO of its common stock, that 'The number of shares to be offered and the price have not yet been set', and that the announcement 'is being published under Rule 135 of the Securities Act of 1933, as amended'.

- Source: Anthropic, 2026-06-01 — <https://www.anthropic.com/news/confidential-draft-s1-sec> (confidence as rated by researcher: primary)
- Quote: «The number of shares to be offered and the price have not yet been set.»

### F046 🟡 Крупное СМИ

TechCrunch (Kirsten Korosec, June 1, 2026) reported Anthropic 'has filed confidentially for an initial public offering, the company said in a blog post Monday', that it 'has yet to list the number of shares or set the price', and that the Series H announced less than a week earlier 'pushed its valuation to $965 billion'.

- Source: TechCrunch, 2026-06-01 — <https://techcrunch.com/2026/06/01/anthropic-files-to-go-public/> (confidence as rated by researcher: major_outlet)
- Quote: «Anthropic has yet to list the number of shares or set the price.»

### F047 🟢 Первоисточник

As of October 23-24, 2026, SEC EDGAR shows no public S-1 from Anthropic: the EDGAR 'current filings' list of S-1 and S-1/A forms filed Oct 22-23, 2026 contains no filer with 'Anthropic' in its name, EDGAR company search for 'anthropic' with form type S-1 returns 'No matching companies', and full-text search for 'Anthropic' in S-1 filings dated 2026-10-15 to 2026-10-24 returns zero hits.

- Source: U.S. SEC EDGAR, 2026-10-24 — <https://www.sec.gov/cgi-bin/browse-edgar?action=getcurrent&type=S-1&count=100> (confidence as rated by researcher: primary)
- Quote: «No matching companies»

### F048 🟡 Крупное СМИ

Yahoo Finance (David Hollerith and Daniel Howley, Oct 21, 2026) reported Anthropic 'is set to publicly file its S-1 investor prospectus as soon as Friday, according to three people familiar with' its plans (Friday = Oct 23); that 'A public filing would clear a key procedural hurdle toward a potential November listing'; that SEC rules require registration materials be public 15 calendar days before a formal roadshow; that 'Wall Street is anticipating that the company could raise as much as $100 billion at a $2 trillion valuation, Reuters previously reported'; that per a Tuesday WSJ report Anthropic 'pulled in $16.3 billion in revenue over the first six months of 2026' and 'reported a net loss of over $80 billion'; and that 'Anthropic did not respond to a request for comment on the timing of its S-1.'

- Source: Yahoo Finance, 2026-10-21 — <https://finance.yahoo.com/markets/article/anthropic-to-publicly-file-for-ipo-as-early-as-friday-sources-say-135343841.html> (confidence as rated by researcher: major_outlet)
- Quote: «Wall Street is anticipating that the company could raise as much as $100 billion at a $2 trillion valuation, Reuters previously reported.»

### F049 🟡 Крупное СМИ

IFR (Amy Or, issue 2655, 17-23 October 2026) reported, citing 'a person familiar with the process', that Anthropic 'plans to file documents publicly on October 26 with the Securities and Exchange Commission', 'plans to launch its public roadshow on November 9' and 'price the deal the following week', 'with the aim of going public in mid-November'; that 'Anthropic is targeting up to US$100bn at a US$2trn valuation'; and that Morgan Stanley and Goldman Sachs 'are joint bookrunners leading an extensive syndicate of banks on the offering'.

- Source: IFR, 2026-10-23 — <https://www.ifre.com/equities/2499407/anthropic-pushes-ahead-with-mid-november-ipo> (confidence as rated by researcher: major_outlet)
- Quote: «Anthropic is targeting up to US$100bn at a US$2trn valuation»

### F050 🟡 Крупное СМИ

PYMNTS (Oct 22, 2026) reported 'The company is set to publicly file its S-1 prospectus as early as Friday' (Oct 23), citing Yahoo Finance's report based on 'three people familiar with the plans'; that 'A public filing would clear the way for a possible November listing'; that 'Wall Street expects the company could raise up to $100 billion at a $2 trillion valuation'; that Anthropic 'brought in $16.3 billion in revenue in the first half of 2026 and posted a net loss of more than $80 billion'; and that Q3 revenue was $16.8 billion, up from $11.5 billion.

- Source: PYMNTS, 2026-10-22 — <https://www.pymnts.com/news/investment-tracker/ipo/2026/anthropic-could-file-ipo-paperwork-as-soon-as-friday/> (confidence as rated by researcher: major_outlet)
- Quote: «Wall Street expects the company could raise up to $100 billion at a $2 trillion valuation.»

### F051 🟡 Крупное СМИ

Reuters (Oct 20, 2026, via Investing.com) relayed the Wall Street Journal's report, citing a draft IPO prospectus, that Anthropic 'recorded a net loss of more than $80 billion in the first half of this year', versus about $13 billion a year earlier, with $72 billion of the loss from 'accounting charges tied to changes in the value of convertible notes'; Anthropic did not immediately respond to a request for comment.

- Source: Reuters (via Investing.com), 2026-10-20 — <https://www.investing.com/news/stock-market-news/anthropic-recorded-net-loss-of-over-80-billion-in-first-half-of-this-year-wsj-reports-4960917> (confidence as rated by researcher: major_outlet)
- Quote: «recorded a net loss of more than $80 billion in the first half of this year»

### F052 🟠 Вторичный источник

Dealroom (Oct 21, 2026, updated Oct 23) summarized the WSJ-reported draft S-1: '$16.3 billion in first-half 2026 revenue against an $80.7 billion net loss', 'About $72 billion of the $80.7 billion loss stems from non-cash accounting charges', nearly $9 billion spent on compute and infrastructure in H1 2026, 'The draft says Anthropic could commit up to $750 billion to compute capacity in the coming years', with Anthropic 'preparing to list as soon as November 2026' at 'a valuation reports have pegged near $2 trillion'.

- Source: Dealroom, 2026-10-21 — <https://dealroom.co/news/164610-anthropics-draft-s-1-reveals-16-3b-revenue-80-7b-loss-and-up-to-750b-com/> (confidence as rated by researcher: secondary)
- Quote: «Anthropic's draft IPO prospectus shows $16.3 billion in first-half 2026 revenue against an $80.7 billion net loss»

### F053 🟡 Крупное СМИ

Reuters exclusive (Echo Wang, Sept 28, 2026, via Yahoo Finance) on Anthropic's IPO prospectus: 'Revenue grew 12-fold in 2025 to nearly $4.6 billion'; 'Anthropic reported a net loss of $42 billion in 2025' with operating losses above $8 billion excluding writedowns and about $34 billion of the net loss a non-cash accounting charge; $7.33 billion spent on compute and infrastructure in 2025; $518 billion planned for cloud, computing and infrastructure obligations; the public sale 'could value it at more than $2 trillion', more than double the $965 billion May valuation; the debut 'is likely to be pushed to after the November US midterm elections, Reuters previously reported, citing sources.'

- Source: Reuters (via Yahoo Finance), 2026-09-28 — <https://finance.yahoo.com/technology/ai/articles/exclusive-anthropics-ipo-prospectus-shows-231722972.html> (confidence as rated by researcher: major_outlet)
- Quote: «Revenue grew 12-fold in 2025 to nearly $4.6 billion»

### F054 🟡 Крупное СМИ

TechCrunch (Connie Loizos, Sept 28, 2026) reported that 'Reuters was first to report on the financial details within the prospectus on Monday', that 2025 revenue 'jumped twelvefold to nearly $4.6 billion', that Anthropic 'recorded an operating loss of more than $8 billion in 2025' with 'total operating expenses to almost $13 billion', and that backers believe it could list 'above $2 trillion, more than double its $965 billion valuation from May'.

- Source: TechCrunch, 2026-09-28 — <https://techcrunch.com/2026/09/28/anthropics-prospectus-details-losses-growth-and-yes-a-warning-that-its-ai-could-end-humanity/> (confidence as rated by researcher: major_outlet)
- Quote: «above $2 trillion, more than double its $965 billion valuation from May»

### F055 🟡 Крупное СМИ

Bloomberg (Oct 1, 2026), as relayed by Quartz the same day, reported Anthropic 'aims to start the formal marketing for its initial public offering as soon as the week of Nov. 9' and plans to 'begin trading before the Thanksgiving holiday, Nov. 26', and that 'Prospective investors believe Anthropic could be valued at between $1.8 trillion and $2 trillion in the IPO'; Quartz also cited the Reuters prospectus report that 2025 revenue was 'nearly $4.6 billion' with an operating loss above $8 billion.

- Source: Quartz (relaying Bloomberg), 2026-10-01 — <https://qz.com/anthropic-ipo-thanksgiving-valuation-100226> (confidence as rated by researcher: major_outlet)
- Quote: «Prospective investors believe Anthropic could be valued at between $1.8 trillion and $2 trillion in the IPO»

### F056 🟡 Крупное СМИ

Yahoo Finance (Michael B. Kelley and Daniel Howley, Oct 1, 2026) reported, citing Bloomberg, that Anthropic is aiming to go public 'as soon as mid-November', 'could begin marketing its initial public offering (IPO) the week of Nov. 9', 'is targeting a valuation of up to $2 trillion', and 'is set to meet with prospective investors on Oct. 14'.

- Source: Yahoo Finance, 2026-10-01 — <https://finance.yahoo.com/technology/article/anthropic-reportedly-looking-to-ipo-as-early-as-mid-november-180315768.html> (confidence as rated by researcher: major_outlet)
- Quote: «could begin marketing its initial public offering (IPO) the week of Nov. 9»

### F057 🟡 Крупное СМИ

Reuters exclusive (Echo Wang, Sept 4, 2026, via Investing.com) reported Anthropic 'is expected to begin marketing its initial public offering in mid-October at the earliest' and 'complete the listing days before the U.S. midterm elections in November'; the public prospectus 'is not expected until late September'; Anthropic is 'looking to finalize a $15 billion revolving credit facility' as part of the IPO process; 'Morgan Stanley, Goldman Sachs, JPMorgan and Citi are among the banks working with Anthropic on the IPO'; and a '$2 trillion listing' was described as suggested by some investors, 'one of the largest IPOs ever attempted'.

- Source: Reuters (via Investing.com), 2026-09-04 — <https://www.investing.com/news/stock-market-news/exclusiveanthropic-ipo-launch-shifts-toward-midoctober-sources-say-4890091> (confidence as rated by researcher: major_outlet)
- Quote: «Morgan Stanley, Goldman Sachs, JPMorgan and Citi are among the banks working with Anthropic on the IPO.»

### F058 🟡 Крупное СМИ

Bloomberg (June 3, 2026), as relayed by Investing.com (Vlad Schepkov), reported Anthropic 'has chosen Morgan Stanley and Goldman Sachs Group Inc. to lead the offering', that 'JPMorgan Chase & Co. will also work on the deal, the report said', that 'Additional banks may join the group', that 'The company is considering going public as soon as October and has filed confidentially for a listing', and that Anthropic 'received a valuation of $965 billion in its most recent funding round'.

- Source: Bloomberg (via Investing.com/Yahoo Finance UK), 2026-06-03 — <https://uk.finance.yahoo.com/news/anthropic-said-pick-morgan-stanley-180010895.html> (confidence as rated by researcher: major_outlet)
- Quote: «has chosen Morgan Stanley and Goldman Sachs Group Inc. to lead the offering.»

### F059 🟡 Крупное СМИ

PYMNTS (June 3, 2026) reported, citing Bloomberg and unnamed sources, that Anthropic 'selected Morgan Stanley and Goldman Sachs to lead its initial public offering' 'with JPMorganChase also involved in the deal', that 'the IPO could be launched as soon as October', and that Anthropic and the three banks declined to comment; it restated the $965 billion post-money Series H valuation.

- Source: PYMNTS, 2026-06-03 — <https://www.pymnts.com/news/ipo/2026/morgan-stanley-and-goldman-sachs-land-anthropic-ipo/> (confidence as rated by researcher: major_outlet)
- Quote: «selected Morgan Stanley and Goldman Sachs to lead its initial public offering»

### F060 🟡 Крупное СМИ

Bloomberg (Bailey Lipschultz, Sept 13, 2026) reported Anthropic PBC has chosen Nasdaq as its listing venue, according to a person familiar with the matter, and that the company is 'seeking to raise as much as or more than SpaceX' in an IPO that could take place as soon as October (preview text only; article paywalled).

- Source: Bloomberg (via Bloomberg Government), 2026-09-13 — <https://news.bgov.com/capital-markets/anthropic-said-to-choose-nasdaq-for-much-anticipated-ipo-listing> (confidence as rated by researcher: major_outlet)
- Quote: «seeking to raise as much as or more than SpaceX»

### F061 🟡 Крупное СМИ

Reuters (Ananya Palyekar, Sept 13, 2026, via The Star Malaysia) reported 'U.S. tech startup Anthropic has selected Nasdaq for its potential initial public offering', as 'Business Insider reported on Sunday, citing a person familiar with the company's plans'; no timing, valuation, raise, banks or company comment were included.

- Source: Reuters (via The Star), 2026-09-13 — <https://www.thestar.com.my/tech/tech-news/2026/09/14/anthropic-selects-nasdaq-for-ipo-business-insider-reports> (confidence as rated by researcher: major_outlet)
- Quote: «U.S. tech startup Anthropic has selected Nasdaq for its potential initial public offering.»

### F062 🟠 Вторичный источник

Quartz (Cris Tolomia, Sept 15, 2026, via Yahoo Finance) reported 'Nasdaq has been selected as the venue for the listing', the IPO 'could value the company at $2 trillion', the company 'could seek to raise as much as $100 billion in its offering', 'Morgan Stanley, Goldman Sachs, and JPMorgan are leading the offering', and 'Nvidia is reportedly weighing a contribution of around $10 billion to the offering', citing Bloomberg, the WSJ and the FT.

- Source: Quartz (via Yahoo Finance), 2026-09-15 — <https://finance.yahoo.com/markets/stocks/articles/anthropic-moving-forward-2-trillion-123756375.html> (confidence as rated by researcher: secondary)
- Quote: «Morgan Stanley, Goldman Sachs, and JPMorgan are leading the offering.»

### F063 🟠 Вторичный источник

The Next Web (Ana-Maria Stanciuc, Sept 13, 2026) reported, citing Business Insider's person familiar with the plans, that 'Anthropic has settled on Nasdaq for a listing it still hopes to complete in October', that estimates 'put it near $2trn', that 'A raise of $100bn would make it the largest flotation ever attempted', and that Anthropic appointed Morgan Stanley and Goldman Sachs to lead the offering.

- Source: The Next Web, 2026-09-13 — <https://thenextweb.com/news/anthropic-ipo-nasdaq-october-listing> (confidence as rated by researcher: secondary)
- Quote: «A raise of $100bn would make it the largest flotation ever attempted.»

### F064 🟠 Вторичный источник

Crypto Briefing (Sept 18, 2026) relayed the Wall Street Journal's report that Anthropic 'is set to launch its initial public offering (IPO) in November, according to the Wall Street Journal', noting pricing/valuation details remained undisclosed and that the IPO had initially been expected to enter marketing by mid-October. Wikipedia's Anthropic article likewise cites WSJ (Driebusch et al., Sept 18, 2026) for the plan to IPO in November 2026.

- Source: Crypto Briefing (relaying WSJ), 2026-09-18 — <https://cryptobriefing.com/anthropic-plans-november-ipo-amid-tech-firm-public-offering-trend-wsj/> (confidence as rated by researcher: secondary)
- Quote: «is set to launch its initial public offering (IPO) in November, according to the Wall Street Journal.»

### F065 🟡 Крупное СМИ

Fortune (Jim Edwards, Aug 13, 2026), relaying the FT, reported 'Anthropic will stage an IPO in October at a predicted valuation of $2 trillion', which would be 'even larger than SpaceX and therefore the largest public offering of stock ever', while 'The IPO is still under discussion, and the valuation has not been formally fixed within the company, sources said.'

- Source: Fortune, 2026-08-13 — <https://fortune.com/2026/08/13/anthropic-ipo-2-trillion-october-largest-ever-spacex/> (confidence as rated by researcher: major_outlet)
- Quote: «The IPO is still under discussion, and the valuation has not been formally fixed within the company, sources said.»

### F066 🟠 Вторичный источник

The Motley Fool (Manali Pradhan, Oct 3, 2026) reported the IPO 'could raise up to $100 billion at roughly a $2 trillion valuation', that 'The terms of the IPO remain under discussion and could change', and that 'it doesn't look like it will happen before the U.S. midterm elections in November.'

- Source: The Motley Fool, 2026-10-03 — <https://www.fool.com/investing/2026/10/03/anthropic-could-raise-up-to-100-billion-in-its-nov/> (confidence as rated by researcher: secondary)
- Quote: «that could raise up to $100 billion at roughly a $2 trillion valuation»

### F067 🟡 Крупное СМИ

Research firm New Constructs published a report titled 'Anthropic Is The Most Ridiculous IPO of 2026' (covered by CNBC on Oct 7, 2026 and The Next Web), calling the planned debut 'an unprecedented test of investor gullibility', putting equity value as low as $144bn against a ~$2 trillion Nasdaq target, and concluding 'We do not believe Anthropic has a viable business model.' The CNBC page returned HTTP 403 to the fetcher.

- Source: CNBC / The Next Web, 2026-10-07 — <https://thenextweb.com/news/anthropic-ipo-valuation-new-constructs-144bn> (confidence as rated by researcher: major_outlet)
- Quote: «an unprecedented test of investor gullibility»

### F068 🟠 Вторичный источник

Crypto Briefing (Sept 12, 2026), citing Reuters, reported Anthropic in early-stage talks with Nvidia to be an anchor investor, with 'Nvidia is reportedly considering an investment of up to $10 billion in the offering', in 'a potential IPO that could raise up to $100 billion' that 'would value Anthropic at roughly $2 trillion', then 'targeting completion before the November 2026 US midterm elections'.

- Source: Crypto Briefing (relaying Reuters), 2026-09-12 — <https://cryptobriefing.com/anthropic-nvidia-record-ipo-talks/> (confidence as rated by researcher: secondary)
- Quote: «Nvidia is reportedly considering an investment of up to $10 billion in the offering.»

### F069 🟠 Вторичный источник

Forge Global's IPO tracker (updated Sept 25, 2026) summarizes: confidential draft registration statement submitted June 2026 (Anthropic, 06/01/2026); Nasdaq selected (Business Insider, 09/13/2026); must publicly file financials at least 15 days before the roadshow; 'the company could seek over $100 billion in capital raised at a $2 trillion valuation' (NYT, 08/21/2026); 'has not finalized a valuation target'; and run rate 'reportedly hit an annualized revenue run rate of $65 billion' (CNBC, 08/17/2026).

- Source: Forge Global, 2026-09-25 — <https://forgeglobal.com/insights/anthropic-upcoming-ipo-news/> (confidence as rated by researcher: secondary)
- Quote: «the company could seek over $100 billion in capital raised at a $2 trillion valuation»

### F070 🟡 Крупное СМИ

Reuters relayed (Sept 28, 2026, via Yahoo) and Reuters' investor-day coverage (Oct 14, 2026) both state that Anthropic's public-market debut is likely to be pushed to after the November US midterm elections; the midterm elections are on November 3, 2026 per Capital.com's relay of Reuters.

- Source: Reuters (via Investing.com), 2026-10-14 — <https://www.investing.com/news/stock-market-news/anthropics-q3-revenue-surges-45-to-nearly-17-billion-4950208> (confidence as rated by researcher: major_outlet)
- Quote: «Its public-market debut is likely to be pushed until after the November US midterm elections»

Researcher notes: SCOPE: Finance/IPO angle only, as of 2026-10-24. All figures are from sources; none computed by me.

KEY STATUS AS OF 2026-10-24: Anthropic's S-1 remains confidential. Anthropic confirmed the confidential draft S-1 on June 1, 2026 (primary). My direct EDGAR checks on Oct 24 (current S-1/S-1A filings for Oct 22-23; company search by name + S-1; full-text search Oct 15-24) show no public Anthropic S-1. Yahoo Finance (Oct 21, three sources) said public filing 'as soon as Friday' Oct 23; IFR (issue dated Oct 17-23) said Oct 26 public filing, Nov 9 roadshow, pricing the following week, mid-November listing. No outlet found confirming a filing on Oct 23. Anthropic has not announced an IPO date, exchange, raise size or valuation.

CONTRADICTIONS / VARIANCE:
- IPO valuation: Bloomberg Oct 1 = $1.8T-$2T (prospective investors); Reuters Oct 15 = ~$1.5T discussed at Oct 14 investor day vs ~$2T previously expected; IFR Oct 17-23 = $2T target; TradingKey cites pre-IPO OTC data $1.909T (low-quality). PYMNTS Oct 22 mentioned some investors weighing ~$1.2T (unverified elsewhere).
- Raise size: up to $100B (IFR; Yahoo Finance citing Reuters; PYMNTS; CNN citing WSJ; Quartz; TNW). A Forkast piece on Yahoo said 'over $20 billion' - low quality, disregard.
- Banks: Bloomberg June 3 = Morgan Stanley + Goldman Sachs lead, JPMorgan 'also' on deal; Reuters Sept 4 = Morgan Stanley, Goldman Sachs, JPMorgan AND Citi 'among the banks'; IFR = MS and GS joint bookrunners with 'extensive syndicate'. Citigroup appears only in Reuters' list.
- Venue: Nasdaq per Business Insider (Sept 13, one source), relayed by Reuters and Bloomberg the same day; not confirmed by Anthropic or Nasdaq.
- Timing drift: June reports 'as soon as October'; Reuters Sept 4 'mid-October marketing, list days before midterms'; WSJ Sept 18 'November'; Reuters Sept 28/Oct 14 'after midterms (Nov 3)'; Bloomberg Oct 1 'roadshow week of Nov 9, trade before Thanksgiving Nov 26'; IFR 'Oct 26 public filing, Nov 9 roadshow, mid-November listing'.
- Dollar value of the 5% stake: all are outlet computations, not Anthropic's. FinanceFeeds: ~$48B at $965B and ~$75B at $1.5T. CNBC's Kate Rooney (via 24/7 Wall St): 'at least $50 billion', 'closer to $100 billion if ... $2 trillion'. Yahoo Finance panel: 'it's 100 billion dollars'. Anthropic gave no figure.
- Revenue: latest official company run-rate is $47B (May, Series H post). $65B end-July run rate is Bloomberg/Reuters-sourced (Aug 17). Reuters Oct 14: Q3 revenue $16.8B (+45% q/q from $11.6B); analysts estimate run rate could reach $110B by year-end. WSJ (Oct 20, via Reuters/PYMNTS/Dealroom): H1 2026 revenue $16.3B, net loss $80.7B ($72B non-cash). Reuters Sept 28: 2025 revenue ~$4.6B, op loss >$8B, net loss $42B (~$34B non-cash). PYMNTS Oct 22 gives Q2 as $11.5B vs Reuters $11.6B. A search snippet attributed 'roughly $10 billion' 2025 revenue to CNBC - conflicts with the prospectus figure and was not verified; disregard.
- Announcement date: a TradingKey page says Aug 18; all other sources and Anthropic say Oct 18, 2026 (Sunday). CNBC/Slashdot dates coverage Oct 18/19.

FETCH FAILURES: CNBC (403 on all three articles incl. the Lise Buyer piece; AMP and r.jina.ai also failed), PYMNTS pre-Thanksgiving piece (403), CNN (451), Qz Sept 14 (403), FinanceFeeds mid-Nov piece (bot check), Bloomberg originals (paywalled; preview via bgov.com). The Lise Buyer 'beneficial from an image perspective' quote is attributed to CNBC in every relay (Slashdot, Breitbart, FinanceFeeds, search snippet of the CNBC text) and she is identified as a partner/founder at IPO advisory firm Class V Group; Breitbart adds her 'burnish their reputation' line. Kate Rooney's figures come via 24/7 Wall St quoting her CNBC video (Oct 19), not from CNBC text directly.

NOT FOUND: Any Anthropic statement giving a dollar value for the fund, any official IPO date/venue/bank confirmation, any Oct 23-24 report confirming the public S-1.


## Сравнения с другими фондами и инициативами / comparisons (52)

### F071 🟢 Первоисточник

Anthropic's announcement 'Investing in the public benefit' (published Oct 18, 2026) commits 5% of Anthropic's shares to the Anthropic Public Benefit Fund, subject to stockholder approval.

- Source: Anthropic, 2026-10-18 — <https://www.anthropic.com/news/public-benefit-fund> (confidence as rated by researcher: primary)
- Quote: «Subject to stockholder approval, 5% of Anthropic's shares will be committed today.»

### F072 🟢 Первоисточник

The board may add 2% of shares to the Fund for every 50% increase in company value above a set (undisclosed) baseline.

- Source: Anthropic, 2026-10-18 — <https://www.anthropic.com/news/public-benefit-fund> (confidence as rated by researcher: primary)
- Quote: «with an additional 2% added at the board's discretion for every 50% increase in the company's value above a set baseline.»

### F073 🟢 Первоисточник

The Fund is structured as an LLC rather than a 501(c)(3), which Anthropic says is to allow flexibility between forms of giving.

- Source: Anthropic, 2026-10-18 — <https://www.anthropic.com/news/public-benefit-fund> (confidence as rated by researcher: primary)
- Quote: «We're establishing the Anthropic Public Benefit Fund as an LLC—rather than a 501(c)(3) or other format ... to give adjustability between different forms of giving.»

### F074 🟢 Первоисточник

Anthropic states none of the equity held by the LLC will be used for lobbying or political giving in the US or abroad.

- Source: Anthropic, 2026-10-18 — <https://www.anthropic.com/news/public-benefit-fund> (confidence as rated by researcher: primary)
- Quote: «None of the Anthropic equity held by the LLC will be used for lobbying or political giving, in the US or abroad.»

### F075 🟢 Первоисточник

Possible uses named by Anthropic: large donations to traditional nonprofits or direct distributions to specific populations; labor-market instability is cited as a motivation, with $200 million already committed to studying it.

- Source: Anthropic, 2026-10-18 — <https://www.anthropic.com/news/public-benefit-fund> (confidence as rated by researcher: primary)
- Quote: «we might explore large donations to traditional nonprofits or direct distributions to specific populations. ... AI may generate enormous economic value, but it could also cause instability for many workers. ... Anthropic has already committed $200 million to studying and addressing this issue.»

### F076 🟢 Первоисточник

Anthropic's co-founders pledged at founding to donate 80% of their equity; an employee equity donation match program (Anthropic matches pledged equity) has roughly half of employees participating; the announcement does NOT state a match ratio.

- Source: Anthropic, 2026-10-18 — <https://www.anthropic.com/news/public-benefit-fund> (confidence as rated by researcher: primary)
- Quote: «When Anthropic was founded, our co-founders pledged to donate 80% of their equity holdings. ... we have also operated an equity donation match program that allows employees to pledge equity ... which Anthropic matches. ... Approximately half of our employees participate in this program.»

### F077 🟢 Первоисточник

Combined with existing pledges, roughly 20% of Anthropic shares will be dedicated to the public good; Anthropic frames the escalator as redirecting equity that tech companies typically give executives as escalating compensation.

- Source: Anthropic, 2026-10-18 — <https://www.anthropic.com/news/public-benefit-fund> (confidence as rated by researcher: primary)
- Quote: «roughly 20% of Anthropic shares will be dedicated to the public good. ... It is common practice for tech companies to offer escalating compensation awards to their executives. ... We are instead directing that equity to the public benefit.»

### F078 🟢 Первоисточник

Anthropic says it will share more on the Fund's structure and governance (including valuation milestones) in the coming months and will report progress in an upcoming public benefit report.

- Source: Anthropic, 2026-10-18 — <https://www.anthropic.com/news/public-benefit-fund> (confidence as rated by researcher: primary)
- Quote: «In the coming months, we will share more about the Anthropic Public Benefit Fund's structure and governance ... We will also report on our progress to date against our mission in an upcoming public benefit report.»

### F079 🟢 Первоисточник

A 20-page PDF titled 'Anthropic 2026 Public Benefit Report: Taking stock of our progress toward our charter' is hosted on Anthropic's CDN (PDF metadata creation date Oct 21, 2026). Daniela Amodei's foreword says the report will be published annually and restates the 5%/80%/~20% figures; the $200 million is described as an 'Economic Futures Research Fund'.

- Source: Anthropic (2026 Public Benefit Report PDF), 2026-10-21 — <https://www-cdn.anthropic.com/a9ceec76a54d28d27affffcdab6faf7c142cd587.pdf> (confidence as rated by researcher: primary)
- Quote: «We announced that, subject to stockholder approval, we are setting aside at least 5% of our shares to fund projects in pursuit of our public benefit charter. Between this set-aside, each of our co-founders' commitment to pledge 80% of their equity to philanthropy, and matched equity-donation pledges from employees, we hope that about 20% of Anthropic shares will be put toward the public good.»

### F080 🟢 Первоисточник

In the report's closing commentary, the Long-Term Benefit Trust (signed by Buddy Shah) describes the fund as a separate entity and says distribution of benefits still lags the company's ambitions.

- Source: Anthropic (2026 Public Benefit Report PDF), 2026-10-21 — <https://www-cdn.anthropic.com/a9ceec76a54d28d27affffcdab6faf7c142cd587.pdf> (confidence as rated by researcher: primary)
- Quote: «If stockholders agree, Anthropic is planning to set aside at least 5% of the company's shares in a separate entity dedicated entirely to the public benefit charter. It is a significant step. But the work of distributing the benefits still lags behind the company's ambitions.»

### F081 🟡 Крупное СМИ

Reuters published a factbox on Oct 20, 2026 (reporting by Pragyan Kalita in Bengaluru, editing by Maju Samuel; syndicated by The Star on Oct 21) comparing Anthropic's fund with nine entities: Anthropic Public Benefit Fund, OpenAI Foundation, Gates Foundation, Warren Buffett's pledge, Elon Musk's pledge, MacKenzie Scott's pledge, Ford Foundation, Lilly Endowment, Novo Nordisk Foundation.

- Source: Reuters (via The Star), 2026-10-20 — <https://www.thestar.com.my/tech/tech-news/2026/10/21/factbox-anthropic039s-public-benefit-fund-and-how-it-compares-with-other-big-philanthropic-efforts> (confidence as rated by researcher: major_outlet)
- Quote: «Anthropic said it would commit 5% of its shares to a new public benefit fund»

### F082 🟡 Крупное СМИ

The Reuters factbox frames Anthropic's pledge as coming months after Senator Bernie Sanders introduced a bill giving the public a 50% stake in the largest US AI companies.

- Source: Reuters (via MarketScreener), 2026-10-20 — <https://www.marketscreener.com/news/anthropic-s-public-benefit-fund-and-how-it-compares-with-other-big-philanthropic-efforts-ce785cd8dd8df122> (confidence as rated by researcher: major_outlet)
- Quote: «The pledge comes amid a broader political debate over who should benefit from AI's gains ... months after US Senator Bernie Sanders introduced a bill that would give the public a 50% stake»

### F083 🟡 Крупное СМИ

Reuters: after OpenAI's October 2025 restructuring, the nonprofit, renamed the OpenAI Foundation, held a 26% stake in the for-profit worth about $130 billion at the time, plus a warrant for additional equity if OpenAI Group's share price rises more than tenfold over 15 years; it plans an initial $25 billion commitment to health/curing diseases and technical solutions to AI resilience, building on a $50 million commitment from July 2025.

- Source: Reuters (via WTAQ), 2026-10-20 — <https://wtaq.com/2026/10/20/factbox-anthropics-public-benefit-fund-and-how-it-compares-with-other-big-philanthropic-efforts/> (confidence as rated by researcher: major_outlet)
- Quote: «with a 26% stake in the for-profit, worth about $130 billion at the time. ... holds a warrant to receive additional equity if OpenAI Group's share price rises more than tenfold over 15 years. ... a $25 billion commitment across two areas: health and curing diseases ... This builds on its $50 million commitment to support nonprofits and mission-focused organizations»

### F084 🟡 Крупное СМИ

TechCrunch (Oct 28, 2025, Russell Brandom) reported at the recapitalization that the OpenAI Foundation would own 26% of the for-profit with a warrant for additional shares if the company continues to grow, would have legal control over OpenAI Group PBC and appoint its board; Microsoft would hold roughly 27% valued at about $135 billion.

- Source: TechCrunch, 2025-10-28 — <https://techcrunch.com/2025/10/28/openai-completes-its-for-profit-recapitalization/> (confidence as rated by researcher: major_outlet)
- Quote: «the OpenAI Foundation will own 26% of the for-profit ... with a warrant for additional shares to be granted if the company continues to grow. ... will have legal control over a public benefit corporation called OpenAI Group ... will appoint its board of directors.»

### F085 🟡 Крупное СМИ

Reuters: Gates Foundation (founded 2000) invested over $102.3 billion in its first 25 years; in May 2025 Gates said it would spend an additional $200 billion over two decades and wind down in December 2045; it plans a record $9 billion payout in 2026 with about 70% of budget on global health.

- Source: Reuters (via WTAQ), 2026-10-20 — <https://wtaq.com/2026/10/20/factbox-anthropics-public-benefit-fund-and-how-it-compares-with-other-big-philanthropic-efforts/> (confidence as rated by researcher: major_outlet)
- Quote: «Gates said the foundation would spend an additional $200 billion over the next two decades ... It plans a record $9 billion payout in 2026, with about 70% of its budget allocated to advancing those first two goals»

### F086 🟡 Крупное СМИ

Reuters: Warren Buffett pledged in 2006 to give nearly all his Berkshire stock to philanthropy; he has donated over half his shares including more than $47 billion to the Gates Foundation and over $17 billion to four family charities; he stopped giving to the Gates Foundation after revelations about Bill Gates' interactions with Jeffrey Epstein; 99.5% of his remaining wealth goes to a charitable trust run by his children with about 10 years to spend it.

- Source: Reuters (via Yahoo Finance UK), 2026-10-20 — <https://uk.finance.yahoo.com/news/factbox-anthropics-public-benefit-fund-184323234.html> (confidence as rated by researcher: major_outlet)
- Quote: «pledged to donate nearly all of his Berkshire stock to philanthropic foundations ... stopped donating to the Gates Foundation following revelations about interactions between Bill Gates»

### F087 🟡 Крупное СМИ

Reuters: MacKenzie Scott received about 4% of Amazon stock (then ~$36 billion) in her 2019 divorce, signed the Giving Pledge, gave $275 million to Planned Parenthood (2022), over $4 billion in pandemic relief, and gave away $7.1 billion in 2025.

- Source: Reuters (via Yahoo Finance UK), 2026-10-20 — <https://uk.finance.yahoo.com/news/factbox-anthropics-public-benefit-fund-184323234.html> (confidence as rated by researcher: major_outlet)
- Quote: «received about 4% of Amazon's stock in her 2019 divorce from the company's founder Jeff Bezos.»

### F088 🟡 Крупное СМИ

Reuters: Ford Foundation was established by Edsel Ford in 1936 with a $25,000 gift, has an endowment of about $18 billion, awarded $768 million through 2,288 grants in 2024, and committed $1 billion in 2015 and another $1 billion in 2021 via BUILD to 350 social justice organizations.

- Source: Reuters (via The Star), 2026-10-20 — <https://www.thestar.com.my/tech/tech-news/2026/10/21/factbox-anthropic039s-public-benefit-fund-and-how-it-compares-with-other-big-philanthropic-efforts> (confidence as rated by researcher: major_outlet)

### F089 🟡 Крупное СМИ

Reuters: Lilly Endowment was established in 1937 by J.K. Lilly and his sons with 17,500 shares of the family drugmaker valued at $262,500; over its first 88 years it disbursed nearly $21.3 billion to 11,651 charities; it paid out $3.85 billion in 2025 while assets rose to nearly $106 billion; focus on education, community development and religion with a particular commitment to Indiana.

- Source: Reuters (via WTAQ / MarketScreener), 2026-10-20 — <https://wtaq.com/2026/10/20/factbox-anthropics-public-benefit-fund-and-how-it-compares-with-other-big-philanthropic-efforts/> (confidence as rated by researcher: major_outlet)
- Quote: «Established in 1937 by J.K. Lilly and his sons through gifts of stock in the family drugmaker ... the Lilly Endowment began with a donation of 17,500 shares valued at $262,500 ... It paid out $3.85 billion in grants in 2025 while its assets rose to nearly $106 billion.»

### F090 🟡 Крупное СМИ

Reuters: the Novo Nordisk Foundation traces its origins to August Krogh, H.C. Hagedorn and August Kongsted; the present foundation took shape in 1989 when the Nordisk and Novo foundations combined; it awarded a record DKK 11.8 billion ($1.77 billion, ~EUR1.6 billion) across 2,206 grants and philanthropic investments in 2025, up from DKK 10.1 billion in 2024; funding focuses on human health, infectious and cardiometabolic diseases, green transition and sustainable agriculture.

- Source: Reuters (via MarketScreener), 2026-10-20 — <https://www.marketscreener.com/news/anthropic-s-public-benefit-fund-and-how-it-compares-with-other-big-philanthropic-efforts-ce785cd8dd8df122> (confidence as rated by researcher: major_outlet)
- Quote: «The present foundation took shape in 1989, when the foundations associated with Nordisk and Novo were combined ... It awarded a record DKK 11.8 billion ($1.77 billion), or about EUR1.6 billion, across 2,206 grants»

### F091 🟢 Первоисточник

Lilly Endowment describes itself as a separate entity from Eli Lilly and Company, with a distinct governing board, staff and location, funded by 1937 gifts of company stock that remain its financial bedrock (structurally the opposite of Anthropic's company-owned LLC).

- Source: Lilly Endowment — <https://lillyendowment.org/about/> (confidence as rated by researcher: primary)
- Quote: «The Endowment was created in 1937 by J.K. Lilly, Sr. and his sons – Eli and J.K. Jr. ... through gifts of stock in their pharmaceutical business, Eli Lilly and Company ... a separate entity from the company ... the gifts of stock remain a financial bedrock of the Endowment»

### F092 🟠 Вторичный источник

The Novo Nordisk Foundation is a Danish enterprise foundation (established 1989) that controls Novo Nordisk and Novonesis through Novo Holdings, holding a minority of share capital but a majority of voting rights; income from these holdings is its primary funding source; Novo Holdings reported about DKK 694 billion (~US$109 billion) in assets under management at year-end 2025. In this model the foundation owns the company, whereas Anthropic's company owns the fund.

- Source: Wikipedia — <https://en.wikipedia.org/wiki/Novo_Nordisk_Foundation> (confidence as rated by researcher: secondary)
- Quote: «The Novo Nordisk Foundation is a Danish enterprise foundation established in 1989. ... It holds a minority of the share capital in Novo and Novonesis but controls a majority of the voting rights. ... Income derived from these holdings constitutes the foundation's primary source of funding.»

### F093 🟡 Крупное СМИ

Axios (Bradley Olson, Oct 19, 2026; URL slug 'silicon-valley-ai-philanthropy-anthropic-fund', headline 'How AI giants will reshape global philanthropy') argues the Anthropic and OpenAI IPOs will create the world's largest charitable organizations and shift philanthropy's center of gravity to Silicon Valley; Anthropic's 5% would be $100 billion at a $2 trillion IPO valuation.

- Source: Axios (via Yahoo Finance), 2026-10-19 — <https://finance.yahoo.com/technology/ai/articles/ai-giants-reshape-global-philanthropy-094006816.html> (confidence as rated by researcher: major_outlet)
- Quote: «the IPOs of AI giants Anthropic and OpenAI will create the world's largest charitable organizations ... shifting its center of gravity to Silicon Valley ... which would amount to $100 billion if it reaches a value of $2 trillion in its IPO.»

### F094 🟡 Крупное СМИ

Axios reports Anthropic's employee donation match is at a 3:1 ratio with roughly half of employees participating, and that the OpenAI Foundation holds a 26% stake worth about $130 billion and has the power to appoint OpenAI's board; it quotes no independent experts and does not mention Gates, Giving Pledge, Google.org, Salesforce, CZI or Buffett.

- Source: Axios (via Yahoo Finance), 2026-10-19 — <https://finance.yahoo.com/technology/ai/articles/ai-giants-reshape-global-philanthropy-094006816.html> (confidence as rated by researcher: major_outlet)
- Quote: «matched donations at a 3:1 ratio ... roughly half its employees participate in donation matching ... holds a 26% equity stake in the company, worth about $130 billion based on the company's current valuation. ... The foundation has the power to appoint OpenAI's board.»

### F095 🟡 Крупное СМИ

Axios notes Anthropic's founders and some employees have close ties to effective altruism, which has drawn criticism from the Trump White House; former White House official Taylor Budowich posted about the 'insane beliefs of those who make up Anthropic', citing a 2010 Dario Amodei blog post that an adult death is 'perhaps 2 or 3 times worse than an infant's death.'

- Source: Axios (via Yahoo Finance), 2026-10-19 — <https://finance.yahoo.com/technology/ai/articles/ai-giants-reshape-global-philanthropy-094006816.html> (confidence as rated by researcher: major_outlet)
- Quote: «Effective altruism has come under sharp criticism from the Trump White House»

### F096 🟡 Крупное СМИ

SF Standard (Rachyl Jones, Oct 20, 2026): the Chan Zuckerberg Initiative popularized the LLC philanthropy structure a decade ago, but CZI was overseen by the couple whereas Anthropic's fund will be part of the company.

- Source: San Francisco Standard, 2026-10-20 — <https://sfstandard.com/2026/10/20/anthropic-musk-philanthropy/> (confidence as rated by researcher: major_outlet)
- Quote: «The Chan Zuckerberg Initiative, led by Mark Zuckerberg and his wife, popularized the structure a decade ago. That organization, however, was overseen by the couple, while Anthropic's will be part of the company.»

### F097 🟡 Крупное СМИ

SF Standard: OpenAI's structure is the inverse of Anthropic's, with the foundation overseeing the for-profit; the OpenAI Foundation has a small separate staff but nearly identical boards; LLC philanthropies may legally spend on lobbying and campaigns though Anthropic said it would not.

- Source: San Francisco Standard, 2026-10-20 — <https://sfstandard.com/2026/10/20/anthropic-musk-philanthropy/> (confidence as rated by researcher: major_outlet)
- Quote: «OpenAI's structure is the inverse of Anthropic's, with the philanthropic foundation overseeing the for-profit arm of the company. The foundation has a small staff separate from the company, but board members for the two entities are nearly identical. ... LLC philanthropies are allowed to use money for lobbying and political campaigns, though Anthropic said it wouldn't use it that way.»

### F098 🟡 Крупное СМИ

Priya Shanker, executive director of Stanford's Center on Philanthropy and Civil Society, said a separate board and governance structure would give Anthropic's fund more legitimacy.

- Source: San Francisco Standard, 2026-10-20 — <https://sfstandard.com/2026/10/20/anthropic-musk-philanthropy/> (confidence as rated by researcher: major_outlet)
- Quote: «It would behoove [Anthropic] to have a separate board and separate governance structure. It would give it a lot more legitimacy.»

### F099 🟡 Крупное СМИ

Jacob Harold, former CEO of GuideStar, said Anthropic is 'giving themselves a whole lot of strategic flexibility' by not saying how it will spend, and characterized Musk's SpaceX-share pledge as 'goodwill-buying' rather than vote-buying.

- Source: San Francisco Standard, 2026-10-20 — <https://sfstandard.com/2026/10/20/anthropic-musk-philanthropy/> (confidence as rated by researcher: major_outlet)
- Quote: «They're kind of doing that preemptively here, and they're giving themselves a whole lot of strategic flexibility, because they're not saying how they're going to spend it. ... where [Musk's donation] is more goodwill-buying»

### F100 🟡 Крупное СМИ

SF Standard tallies recent Trump Account pledges: Michael Dell and his wife $6.25 billion; Gwynne Shotwell and husband shares to 2 million teens from low-income families (estimated $300 million); Micron Technology $250 to up to 1 million children's accounts; Musk one SpaceX share to roughly 72 million children (estimated $10.5 billion); and notes Trump promised every American adult $5,000 if Republicans keep Congress after the midterms.

- Source: San Francisco Standard, 2026-10-20 — <https://sfstandard.com/2026/10/20/anthropic-musk-philanthropy/> (confidence as rated by researcher: major_outlet)
- Quote: «Dell and his wife, through their foundation, pledged $6.25 billion to add to the older children's accounts ... Semiconductor company Micron Technology announced it would give $250 to up to 1 million children's accounts. ... give one share of SpaceX stock to each of the roughly 72 million children in the U.S., ... a donation estimated at $10.5 billion»

### F101 🟡 Крупное СМИ

AP (Oct 20, 2026, via Investment Executive): experts say foundations must distribute at least 5% of endowment value while an LLC is not bound by the same spending rules; Anthropic's pledge triggers no immediate tax write-off; LLCs require less transparency; Katherina Rosqueta (UPenn Center for High Impact Philanthropy) said the LLC gives 'a lot more flexibility and latitude'.

- Source: Associated Press (via Investment Executive), 2026-10-20 — <https://www.investmentexecutive.com/news/markets/ahead-of-massive-ipos-ai-companies-sketch-plans-to-share-their-wealth/> (confidence as rated by researcher: major_outlet)
- Quote: «An LLC is not bound by the same spending rules as a foundation. ... Anthropic's pledge doesn't immediately trigger a tax write-off. ... There's also less transparency required of LLCs. ... They have a lot more flexibility and latitude in how to use the resources they put into the fund»

### F102 🟡 Крупное СМИ

AP: Phil Buchanan (president, Center for Effective Philanthropy), Gary Marcus (NYU professor emeritus) and Brian Mittendorf (Ohio State accounting chair) commented; Mittendorf said LLCs permit 'payouts to individuals that would not be possible through a 501(c)3 charity' and that the pledge 'reflects more of an intention to do things in the future rather than an act now.'

- Source: Associated Press (via Investment Executive), 2026-10-20 — <https://www.investmentexecutive.com/news/markets/ahead-of-massive-ipos-ai-companies-sketch-plans-to-share-their-wealth/> (confidence as rated by researcher: major_outlet)
- Quote: «I guess I'm hopeful, but I'm not going to get too excited until I see some evidence of what's actually happening. ... Anthropic is playing games here. Trying to curry public favour while still holding control and resisting disclosure is annoying.»

### F103 🟡 Крупное СМИ

AP: the OpenAI Foundation pledged $1 billion earlier in 2026 to expand grantmaking; in April 2026 OpenAI proposed a 'Public Wealth Fund' with a stake in AI-driven economic growth across companies; Sam Altman has discussed sharing AI equity with the public with lawmakers of both parties; Gates and Dell set up private foundations during the PC boom while Zuckerberg and other Silicon Valley leaders turned to LLCs.

- Source: Associated Press (via Investment Executive), 2026-10-20 — <https://www.investmentexecutive.com/news/markets/ahead-of-massive-ipos-ai-companies-sketch-plans-to-share-their-wealth/> (confidence as rated by researcher: major_outlet)

### F104 🟡 Крупное СМИ

Marketplace (Samantha Fields, Oct 20, 2026): Steven Dean (Boston University School of Law) said because Anthropic uses an LLC rather than a foundation it is not required to give any money away (foundations must give 5% of assets yearly) and could take the money back; Ray Madoff (Boston College Law) estimated Musk's gift at roughly $10 billion at ~$150/share and said a charitable vehicle could save him about $7 billion in taxes.

- Source: Marketplace, 2026-10-20 — <https://www.marketplace.org/story/2026/10/20/who-will-anthropic-and-elon-musks-philanthropic-plans-benefit> (confidence as rated by researcher: major_outlet)
- Quote: «You've got to read the fine print. ... What's this $150 worth of SpaceX stock going to really do for anybody?»

### F105 🟡 Крупное СМИ

On Oct 19, 2026, one day after Anthropic's announcement, Elon Musk posted on X that he will give one of his SpaceX shares to every kid in America next year; he had replied to Anthropic's post recommending giving shares directly to the public.

- Source: Fox Business, 2026-10-19 — <https://www.foxbusiness.com/fox-news-tech/elon-musk-spacex-shares-american-children-giveaway> (confidence as rated by researcher: major_outlet)
- Quote: «Next year, I will give one of my SpaceX shares to every kid in America. This will be the first of many. ... I recommend giving the shares directly to the public. ... This is what I will be doing»

### F106 🟡 Крупное СМИ

AP (Michelle Chapman, Oct 19, 2026): SpaceX closed at $146.03 on Friday; about 73 million Americans under 18 puts the pledge at roughly $10.66 billion; SpaceX went public in June making Musk the first trillionaire; shares are down 35.3% from their post-IPO peak; Musk has given more than $276 million to midterm campaigns since July; Anthropic's IPO is reportedly planned as soon as November.

- Source: Associated Press (via PBS NewsHour), 2026-10-19 — <https://www.pbs.org/newshour/nation/musk-pledges-to-give-a-share-of-his-spacex-company-to-every-kid-in-america-next-year> (confidence as rated by researcher: major_outlet)
- Quote: «I recommend giving the shares directly to the public.»

### F107 🟡 Крупное СМИ

Reuters factbox quotes Musk's rationale and notes Shotwell's earlier pledge of one SpaceX share each to more than 2 million children under Trump Accounts.

- Source: Reuters (via WTAQ), 2026-10-20 — <https://wtaq.com/2026/10/20/factbox-anthropics-public-benefit-fund-and-how-it-compares-with-other-big-philanthropic-efforts/> (confidence as rated by researcher: major_outlet)
- Quote: «Yes, giving shares, which are stakes in the future economy, directly to the people is the way ... Earlier this year, SpaceX President Gwynne Shotwell and her husband also pledged a share of their SpaceX stock ... to each of more than 2 million children ... under the Trump Accounts investment initiative.»

### F108 🟡 Крупное СМИ

Al Jazeera (Oct 21, 2026): Trump said on Truth Social the Musk shares would go through 'TRUMP ACCOUNTS'; nearly 70 million accounts have been opened; Treasury rules of Sept 30 allow gifting individual company stock, families cannot refuse shares, and shares generally cannot be sold for five years or until the year the child turns 17 if sooner; selling $10.7bn of shares could mean a tax bill of up to about $2.5bn; Musk holds ~4.8bn shares outright and the gift would cut that by ~1.5%.

- Source: Al Jazeera, 2026-10-21 — <https://www.aljazeera.com/news/2026/10/21/musk-pledges-10bn-in-spacex-shares-for-us-children-who-really-gains> (confidence as rated by researcher: major_outlet)

### F109 🟡 Крупное СМИ

CNBC (Oct 20, 2026) reported that under Treasury guidelines families cannot refuse gifted stock in Trump Accounts and generally cannot sell it until the earlier of five years or the end of the calendar year in which the beneficiary turns 17 (page returned 403; claim from search snippet).

- Source: CNBC, 2026-10-20 — <https://www.cnbc.com/2026/10/20/musk-spacex-trump-account-stock-rules.html> (confidence as rated by researcher: major_outlet)

### F110 🟡 Крупное СМИ

Bloomberg Government (Chris Cioffi, Oct 23, 2026): Will McBride (Tax Foundation) estimated Musk would owe about $2.6 billion at the 23.8% capital gains rate if he sold the ~73 million shares (~$10.7 billion at ~$147); temporary regulations require stock distribution through a government or tax-exempt entity; Steven Dean (BU Law) questioned the gift as a substitute for taxation.

- Source: Bloomberg Government, 2026-10-23 — <https://news.bgov.com/bloomberg-government-news/elon-musk-could-skirt-2-billion-tax-bill-with-spacex-stock-gift> (confidence as rated by researcher: major_outlet)
- Quote: «It's certainly a charitable donation ... It just comes with substantial tax benefits. ... Is this a good substitute for other kinds of philanthropy? Maybe ... But is it better than taxing elites? Definitely not.»

### F111 🟠 Вторичный источник

24/7 Wall St (Oct 23, 2026) cites statutory Trump Account rules (26 U.S.C. §530A): before age 18 accounts may hold only low-cost index mutual funds/ETFs so a single stock does not qualify; $5,000 annual contribution cap; 'general funding contributions' exempt from the cap may be made only by governments, tribal governments and 501(c)(3) organizations; it puts Shotwell's commitment at more than $320 million for more than 2 million children.

- Source: 24/7 Wall St., 2026-10-23 — <https://247wallst.com/personal-finance/2026/10/23/elon-musk-wants-to-give-every-kid-in-america-a-spacex-share-the-tax-rules-behind-the-gift-are-more-complicated-than-it-sounds> (confidence as rated by researcher: secondary)

### F112 🟠 Вторичный источник

Gwynne Shotwell (SpaceX President/COO) and her husband announced on July 6, 2026 (the first trading day of Trump Accounts/Invest America, launched July 4, 2026) that they would gift one SpaceX share each to Trump Accounts for more than 2 million children ages 11-17 in lower-income areas with 'a bit more emphasis' on central Texas; Dell pledged $6.25 billion ($250 each to 25 million children); Dalios pledged at least $75 million for 300,000+ Connecticut children.

- Source: Benzinga (via Yahoo Finance), 2026-07-06 — <https://finance.yahoo.com/markets/stocks/articles/spacexs-gwynne-shotwell-pledges-spacex-143104359.html> (confidence as rated by researcher: secondary)
- Quote: «honored and thrilled to participate in the Invest America program»

### F113 🟡 Крупное СМИ

Houston Chronicle (Andrea Leinfelder, July 6, 2026): Shotwell owned nearly 12.7 million SpaceX shares at the IPO per SEC filings, worth roughly $2 billion; the article gives no dollar value for the donated portion.

- Source: Houston Chronicle (via Yahoo Finance), 2026-07-06 — <https://finance.yahoo.com/markets/stocks/articles/spacex-president-pledges-stock-trump-195602754.html> (confidence as rated by researcher: major_outlet)

### F114 🟠 Вторичный источник

24/7 Wall St (Aug 25, 2026) values Shotwell's ~2 million-share gift at roughly $325 million at the July 6 price of $160.42 (attributed to CNBC) and about $276 million at $137.95 later.

- Source: 24/7 Wall St., 2026-08-25 — <https://247wallst.com/investing/2026/08/25/2-million-kids-got-free-spacex-shares-in-their-trump-accounts-so-what-are-they-worth-now/> (confidence as rated by researcher: secondary)

### F115 🟡 Крупное СМИ

Sen. Bernie Sanders (I-Vt.) introduced the 'American AI Sovereign Wealth Fund Act' on Thursday, June 18, 2026: a one-time 50% tax on the stock of the largest AI companies (those generating at least $200 million a year), with the government holding voting shares and equal board representation able to block decisions that hurt the public.

- Source: Bloomberg Government, 2026-06-18 — <https://news.bgov.com/bloomberg-government-news/sanders-to-introduce-bill-giving-americans-stake-in-ai-companies> (confidence as rated by researcher: major_outlet)
- Quote: «cannot be controlled by a handful of the wealthiest people on earth»

### F116 🟠 Вторичный источник

Broadband Breakfast (June 18, 2026, updated Oct 16): the bill applies to companies with $200 million or more in annual gross receipts engaged in AI activities (public stake only in the AI business of mixed companies); Sanders estimated the fund at about $7 trillion with a $1,000 dividend per American; an 'Independent Commission for Democratic AI' of seven commissioners nominated by the president and confirmed by the Senate from a list provided by Congress would ensure an annual dividend of 5% of fund value.

- Source: Broadband Breakfast, 2026-06-18 — <https://broadbandbreakfast.com/sanders-proposes-the-american-ai-sovereign-wealth-fund-act.md> (confidence as rated by researcher: secondary)
- Quote: «The goal here is to make AI work for ordinary people, not just Mr. Musk and some other multibillionaires»

### F117 🟠 Вторичный источник

Hoodline (July 25, 2026) reports the bill is listed as S.4825 (per GovInfo), read and referred to committee; covered activities include AI data centers, computing infrastructure and advanced robotics; annual distributions equal 5% of the fund's average market value; a one-page summary estimates ~$7 trillion at current valuations.

- Source: Hoodline, 2026-07-25 — <https://hoodline.com/2026/07/sanders-wants-half-of-big-ai-promises-1-000-for-every-american-6993186/> (confidence as rated by researcher: secondary)

### F118 🟡 Крупное СМИ

Computerworld (June 19, 2026) compares the Sanders fund to Norway's ~$2 trillion sovereign wealth fund and notes OpenAI's 'Public Wealth Fund' proposal and that Anthropic itself has proposed a sovereign wealth fund; Mashable (June 1, 2026) says Sanders described it as a one-time transfer of 50% of equity (not a profits tax), naming OpenAI, Anthropic and xAI, with Norway and Alaska's Permanent Fund Dividend as models.

- Source: Computerworld, 2026-06-19 — <https://www.computerworld.com/article/4187301/us-should-take-50-stake-in-major-ai-firms-says-bernie-sanders.html> (confidence as rated by researcher: major_outlet)
- Quote: «The foundation of AI is based on the collective knowledge of humanity and the creative work of tens of millions of people.»

### F119 🟠 Вторичный источник

CNBC's Kate Rooney (Oct 19, 2026, as quoted by 24/7 Wall St) said the 5% stake 'could be worth at least $50 billion' and 'closer to $100 billion if the company debuts at a $2 trillion price tag'; Musk and former White House AI czar David Sacks were among those opposing the structure; Anthropic reportedly says retaining control lets it pace donations and the lobbying ban limits self-dealing.

- Source: 24/7 Wall St. (citing CNBC), 2026-10-20 — <https://247wallst.com/investing/2026/10/20/anthropic-sets-aside-5-stake-for-public-benefit-fund-ahead-of-november-ipo/> (confidence as rated by researcher: secondary)
- Quote: «Some are questioning why Anthropic would retain control of the money versus just giving it away directly»

### F120 ⚪ Оценка или мнение

Foreign Policy Journal (David Prior, Oct 20, 2026) calls the pledge 'the largest philanthropic capital commitment in history' based on a rumored $2.2 trillion IPO valuation (~$100 billion), comparing it to the Gates Foundation, Costa Rica's GDP and four years of NASA funding, without citing a source for the ranking.

- Source: Foreign Policy Journal, 2026-10-20 — <https://www.foreignpolicyjournal.com/2026/10/20/anthropic-anth-pvt-pledges-5-equity-to-public-benefit-in-largest-philanthropic-capital-commitment-ever/> (confidence as rated by researcher: speculative)

### F121 🟡 Крупное СМИ

Al Jazeera (John Power, Oct 19, 2026): Anthropic is a Delaware public benefit corporation; analysts forecast a valuation above $2 trillion and a listing before end-2026, possibly the largest IPO in history; Anthropic says 'bolder approaches may be needed' on labor-market disruption.

- Source: Al Jazeera, 2026-10-19 — <https://www.aljazeera.com/economy/2026/10/19/anthropic-says-it-will-commit-5-of-shares-to-public-benefit-fund> (confidence as rated by researcher: major_outlet)
- Quote: «the more Anthropic grows, the larger the share of the company that can be dedicated expressly to the public good»

### F122 🟡 Крупное СМИ

AP's original Oct 18 report (via ABC News) describes the Fund as 'a new entity within the company' that 'will have increased flexibility and scale', notes Anthropic was founded as a public benefit corporation by Dario Amodei and five co-founders, and says the IPO is planned as soon as November.

- Source: Associated Press (via ABC News), 2026-10-18 — <https://abcnews.com/Business/wireStory/anthropic-commits-5-stock-new-public-benefit-fund-137368439> (confidence as rated by researcher: major_outlet)

Researcher notes: CONTRADICTIONS / CAVEATS: (1) Employee match ratio: Axios reports 3:1; Anthropic's announcement states no ratio (only 'which Anthropic matches', ~half of employees). (2) Musk pledge sizing varies by source: 72M (SF Standard, Moneywise, Census 2025) vs 73M children (AP, Al Jazeera, BGov); value $10.36B (at $148), $10.5B (72M x $146), $10.66B/$10.7B (73M x $146.03/$147). (3) Shotwell gift value: $300M (SF Standard), >$320M (24/7 Wall St Oct 23), ~$325M (CNBC per 24/7 Wall St Aug); one outlier of $2.4B found in search snippets, not corroborated. Shotwell's pledge dates from July 6, 2026, not October. (4) Trump Account sale rules are reported inconsistently: CNBC/Al Jazeera 'earlier of five years or end of year child turns 17'; Moneywise 'five years or start of year child turns 18, whichever first'; 24/7 Wall St cites statute §530A allowing only index funds/ETFs before 18, which conflicts with the Sept 30 Treasury temporary regulations allowing individual-stock gifts (BGov notes temporary regs require distribution via a government or tax-exempt entity and an acceptance agreement). BGov headline says $2B tax avoided but body says ~$2.6B; Al Jazeera says up to ~$2.5B; Madoff (Marketplace) says ~$7B could be saved via a charitable vehicle. (5) Sanders bill was introduced June 18, 2026 (not October); Reuters factbox says 'months after'. Threshold of $200M annual gross receipts, 7-member commission, $7T estimate and $1,000 dividend come from secondary outlets (Broadband Breakfast, Hoodline, Center Square) plus BGov; the Senate press release, bill PDF and The Hill returned 403; bill number S.4825 rests on Hoodline citing GovInfo (unverified). (6) OpenAI Foundation: the 26%/$130B figures are 'at the time' of the Oct 28, 2025 recapitalization; the 'tenfold over 15 years' warrant condition comes from Reuters (TechCrunch says only 'if the company continues to grow'); a Wikipedia snapshot shows later ownership of 22.5% (possibly post-dilution). OpenAI's own pages returned 403. (7) Axios headline discrepancy: the axios.com URL (2026/10/19/silicon-valley-ai-philanthropy-anthropic-fund) appears in search results under both 'How AI giants will reshape global philanthropy' and 'Anthropic pledge to usher in new era of AI-infused philanthropy'; the Yahoo syndicated copy uses the former; axios.com itself returned 403. (8) Google.org and Salesforce 1-1-1 were NOT cited by any outlet found in this context; CZI was (SF Standard, AP re Zuckerberg LLCs); Gates/Dell foundations and Benioff mentioned as earlier-era contrast (SF Standard, AP). (9) Novo Nordisk Foundation / Lilly Endowment: only the Reuters factbox places them alongside Anthropic's fund, as scale comparisons; no outlet explicitly says Anthropic's fund 'resembles' them. Structurally they differ: Novo Nordisk Foundation is a Danish enterprise foundation that OWNS/controls the company (majority of votes via Novo Holdings); Lilly Endowment is a separate entity with its own board funded by stock gifts; Anthropic's fund is a wholly owned LLC OWNED BY the company (SF Standard: OpenAI's foundation-over-company is 'the inverse'). (10) Anthropic's 'upcoming public benefit report' appears to exist: a 20-page PDF 'Anthropic 2026 Public Benefit Report' (metadata created Oct 21, 2026) is on www-cdn.anthropic.com, but no anthropic.com announcement page was located (/news/public-benefit-report returned 404), so publication status/date is not confirmed. The report calls the $200M commitment an 'Economic Futures Research Fund' and says the report will be published annually. (11) Anthropic's 'Long-Term Benefit Trust' and public benefit corporation status are separate from the Fund; Al Jazeera clarifies Anthropic itself is not an LLC. (12) Blocked fetches (403/429/402): axios.com, cnbc.com, washingtonpost.com, forbes.com, thehill.com, sanders.senate.gov, openai.com, fastcompany.com, piratewires.com, thestreet.com, usnews.com (503), thecentersquare.com (paywall); claims from those rely on syndicated copies or search snippets as marked.


## Реакции и критика / reactions (45)

### F123 🟢 Первоисточник

Anthropic's announcement 'Investing in the public benefit' states that, subject to stockholder approval, 5% of Anthropic's shares are committed to the Anthropic Public Benefit Fund, with up to 2% more at the board's discretion for every 50% increase in company value above a set baseline.

- Source: Anthropic, 2026-10-18 — <https://www.anthropic.com/news/public-benefit-fund> (confidence as rated by researcher: primary)
- Quote: «Subject to stockholder approval, 5% of Anthropic's shares will be committed today ... with an additional 2% added at the board's discretion for every 50% increase in the company's value above a set baseline.»

### F124 🟢 Первоисточник

Anthropic says none of the equity held by the Fund (an LLC) will be used for lobbying or political giving, that possible uses include large donations to nonprofits or direct distributions to specific populations, that it has already committed $200 million on labor-market impacts, and that roughly 20% of shares will be dedicated to the public good in total; more on structure/governance and an upcoming public benefit report are promised.

- Source: Anthropic, 2026-10-18 — <https://www.anthropic.com/news/public-benefit-fund> (confidence as rated by researcher: primary)
- Quote: «None of the Anthropic equity held by the LLC will be used for lobbying or political giving, in the US or abroad. ... large donations to traditional nonprofits or direct distributions to specific populations ... Anthropic has already committed $200 million to studying and addressing this issue ... roughly 20% of Anthropic shares will be dedicated to the public good»

### F125 🟢 Первоисточник

Anthropic's X announcement was posted Sun Oct 18, 2026 at 18:07:51 UTC; as of Oct 24 it showed 2,318 replies, 21,597 likes and about 7.68 million views. It says the fund 'will start off with 5% of our shares' and that 'roughly 20% of Anthropic's shares are committed to the public good'.

- Source: Anthropic (X post), 2026-10-18 — <https://x.com/AnthropicAI/status/2111881963657412903> (confidence as rated by researcher: primary)
- Quote: «We're committing a portion of Anthropic's shares to the Anthropic Public Benefit Fund, a new wholly owned entity dedicated entirely to the public benefit. It will start off with 5% of our shares. For every 50% increase in the company's value over a set baseline, we can contribute up to an extra 2%, subject to our board's discretion.»

### F126 🟢 Первоисточник

Elon Musk replied to Anthropic's announcement on X on Oct 18, 2026 at 20:16:44 UTC recommending the shares be given directly to the public (verified at original; 42,126 likes, 1,837 reposts at time of check).

- Source: Elon Musk (X post), 2026-10-18 — <https://x.com/elonmusk/status/2111914396490604547> (confidence as rated by researcher: primary)
- Quote: «@AnthropicAI I recommend giving the shares directly to the public»

### F127 🟢 Первоисточник

About four hours later (Oct 19, 2026, 00:39:47 UTC) Musk replied to his own post saying he would do this himself (verified at original; 22,881 likes, ~2.39M views).

- Source: Elon Musk (X post), 2026-10-19 — <https://x.com/elonmusk/status/2111980598084698114> (confidence as rated by researcher: primary)
- Quote: «@AnthropicAI This is what I will be doing»

### F128 🟢 Первоисточник

On Oct 19, 2026 at 07:52:45 UTC Musk pledged one SpaceX share to every child in America next year (verified at original; 624,642 likes, 63,794 reposts, ~36.4M views at time of check).

- Source: Elon Musk (X post), 2026-10-19 — <https://x.com/elonmusk/status/2112089556615123114> (confidence as rated by researcher: primary)
- Quote: «Next year, I will give one of my SpaceX shares to every kid in America.

This will be the first of many.»

### F129 🟢 Первоисточник

On Oct 19, 2026 at 15:58:16 UTC Musk, replying to @Geiger_Capital, reiterated that giving shares directly to people 'is the way' (verified at original).

- Source: Elon Musk (X post), 2026-10-19 — <https://x.com/elonmusk/status/2112211740884975910> (confidence as rated by researcher: primary)
- Quote: «@Geiger_Capital Yes, giving shares, which are stakes in the future economy, directly to the people is the way»

### F130 🟡 Крупное СМИ

Fox Business reported Oct 19, 2026 that Anthropic did not respond to multiple requests for comment on whether it would distribute any fund shares to American children or families after Musk's posts.

- Source: Fox Business, 2026-10-19 — <https://www.foxbusiness.com/technology/anthropic-silent-whether-distribute-shares-americans-following-musk-spacex-pledge> (confidence as rated by researcher: major_outlet)
- Quote: «Anthropic did not respond ... the company did not reply to multiple requests for comment on Monday.»

### F131 🟡 Крупное СМИ

NBC News (Rob Wile, Oct 19, 2026) estimated Musk's SpaceX pledge at about $10.8 billion (roughly 72 million U.S. children under 18 at about $150 per share), less than 2% of his net worth, and quoted Trump thanking Musk on Truth Social.

- Source: NBC News, 2026-10-19 — <https://www.nbcnews.com/tech/tech-news/elon-musk-anthropic-make-promises-give-public-piece-ai-pie-rcna604313> (confidence as rated by researcher: major_outlet)
- Quote: «A BIG THANK YOU to our legendary friend, @ElonMusk, for his incredible generosity in giving SpaceX Stock»

### F132 🟡 Крупное СМИ

In a Reuters wrap (Deborah Mary Sophia and Abu Sultan, Oct 19, 2026), Dakota Wealth Management's Robert Pavlik called Musk's SpaceX share pledge a possible 'publicity stunt' — the remark refers to Musk's pledge, not to Anthropic's fund.

- Source: Reuters (via Investing.com), 2026-10-19 — <https://www.investing.com/news/stock-market-news/anthropic-commits-5-stake-to-new-public-benefit-fund-musk-argues-for-direct-share-donations-to-kids-4958151> (confidence as rated by researcher: major_outlet)
- Quote: «It feels like a publicity stunt ... Will it create positive public sentiment? Perhaps.»

### F133 🟢 Первоисточник

Anthropic co-founder Jack Clark posted on X Oct 18, 2026 at 20:31:54 UTC that roughly 20% of all Anthropic equity will be dedicated to the public good (verified at original; 1,195 likes, 411 replies).

- Source: Jack Clark (X post), 2026-10-18 — <https://x.com/jackclarkSF/status/2111918212946309445> (confidence as rated by researcher: primary)
- Quote: «Between this and our prior commitments, roughly 20% of all Anthropic equity will be dedicated to the public good, and that commitment can grow as Anthropic grows.

We plan to use these funds to ensure more people can share in the benefits of AI, and to increase our ability to provide funding to deal with its risks.»

### F134 🟢 Первоисточник

David Sacks quote-posted Jack Clark's post on X on Oct 18, 2026 at 23:13:06 UTC (verified at original; 5,989 likes, ~287K views). It is a quote-post of Clark, not a reply under Anthropic's post. His X bio reads 'Co-Chair, President's Council of Advisors on Science & Technology', while several outlets call him 'former AI czar'.

- Source: David Sacks (X post), 2026-10-18 — <https://x.com/DavidSacks/status/2111958783396385152> (confidence as rated by researcher: primary)
- Quote: «You've put 20% of your equity in an LLC. Whether it serves the public good remains to be seen.»

### F135 🟢 Первоисточник

Gary Marcus quote-posted Sacks on X on Oct 19, 2026 at 01:26:12 UTC (verified at original; 436 likes). The phrase 'publicity stunt' does NOT appear in this post; his wording is 'playing games' and 'reeks of desperation'.

- Source: Gary Marcus (X post), 2026-10-19 — <https://x.com/GaryMarcus/status/2111992276767691122> (confidence as rated by researcher: primary)
- Quote: «Sacks is right. Anthropic is playing games here.

Trying to curry public favor while still holding control and resisting disclosure is annoying. 

And reeks of desperation.»

### F136 ⚪ Оценка или мнение

The 'publicity stunt' attribution to Gary Marcus appears only in an aggregator (jawlah.co, Oct 19, 2026) as a paraphrase without quotation marks or a link; no original Marcus post or Substack piece with that wording was found (his Substack archive for Oct 17-24 has no Anthropic fund post).

- Source: Jawlah (aggregator), 2026-10-19 — <https://jawlah.co/en/66762> (confidence as rated by researcher: speculative)
- Quote: «Gary Marcus ... criticized the move as mainly promotional and questioned Anthropic's commitment to transparency»

### F137 🟢 Первоисточник

Palmer Luckey replied to Musk's post on X on Oct 18, 2026 at 23:29:54 UTC calling the fund 'USAID 2.0' (verified at original; 6,683 likes, 554 reposts).

- Source: Palmer Luckey (X post), 2026-10-18 — <https://x.com/PalmerLuckey/status/2111963008805290448> (confidence as rated by researcher: primary)
- Quote: «@elonmusk @AnthropicAI The problem is that their definition of "public good" is helping everyone else, not the American public.

If they would commit to helping America and Americans, that would be one thing, but this reeks of USAID 2.0, just another way to funnel billions out of our own economy.»

### F138 🟠 Вторичный источник

Breitbart (Lucas Nolan, Oct 19, 2026) added that Luckey argued Anthropic's Effective Altruist founders prioritize a 'non-western audience' over Americans; this is Breitbart's paraphrase and the words do not appear in Luckey's verified post.

- Source: Breitbart, 2026-10-19 — <https://www.breitbart.com/tech/2026/10/19/anthropic-will-dedicate-5-of-shares-to-public-benefit-fund-ahead-of-landmark-ai-ipo/> (confidence as rated by researcher: secondary)
- Quote: «USAID 2.0»

### F139 🟢 Первоисточник

Patrick Moorhead (Moor Insights & Strategy) quote-posted Anthropic's announcement on X on Oct 18, 2026 at 23:50:22 UTC (verified at original; 73 likes, ~4.8K views).

- Source: Patrick Moorhead (X post), 2026-10-18 — <https://x.com/PatrickMoorhead/status/2111968159649374490> (confidence as rated by researcher: primary)
- Quote: «If it's dedicated entirely the "public benefit" why don't they just give it to the public and citizens where they can directly benefit? Seems like the public would know what to do with the money better than bureaucratic institutions.»

### F140 🟢 Первоисточник

Andrew Curran posted a thread on X on Oct 18, 2026 (root 18:44 UTC) on the fund; a verified post in it (18:54:49 UTC) highlights the lobbying ban. His widely quoted UBI reading is in the same thread but the exact post ID was not retrieved.

- Source: Andrew Curran (X post), 2026-10-18 — <https://x.com/AndrewCurran_/status/2111893782035910759> (confidence as rated by researcher: primary)
- Quote: «None of the Anthropic equity held by the Anthropic Public Benefit Fund 'will be used for lobbying or political giving, in the US or abroad.'»

### F141 🟡 Крупное СМИ

Andrew Curran's UBI remark, as quoted by Business Insider and search snippets of his X thread: he read 'direct distributions to specific populations' as a self-directed global UBI. Original post not fetched directly.

- Source: Business Insider (via Yahoo Finance), 2026-10-18 — <https://finance.yahoo.com/technology/ai/articles/smart-people-saying-anthropics-5-043641796.html> (confidence as rated by researcher: major_outlet)
- Quote: «The most significant line for me is "direct distributions to specific populations." It sounds to me like they are planning their own form of self-directed global UBI.»

### F142 🟡 Крупное СМИ

Business Insider's roundup 'What smart people are saying about Anthropic's 5% public benefit pledge' (Tracy Connor and Tom Carter, Oct 19, 2026, read via Yahoo syndication) quotes Musk, Luckey, Curran, Gerstner, Sam Hogan Heutmaker, Marcus, Moorhead, Sacks, Sarah Polcz, Travis Kalanick, Kevin Roose and Will Brown.

- Source: Business Insider (via Yahoo Finance), 2026-10-19 — <https://finance.yahoo.com/technology/ai/articles/smart-people-saying-anthropics-5-043641796.html> (confidence as rated by researcher: major_outlet)
- Quote: «This will come to be known as 'the reverse OpenAI' ... It's genius.»

### F143 🟡 Крупное СМИ

Fast Company (Grace Snelling, Oct 19, 2026; fastcompany.com headline 'Anthropic stock dedicated to public good? AI-weary skeptics react', syndicated on Yahoo as '...The public is skeptical') says social media reaction was largely skeptical and that Anthropic's 'do-gooder' reputation has soured; section heading 'No more Mr. AI good guy'.

- Source: Fast Company (via Yahoo Finance), 2026-10-19 — <https://finance.yahoo.com/technology/ai/articles/anthropic-says-dedicate-5-shares-191700133.html> (confidence as rated by researcher: major_outlet)
- Quote: «So far, reaction to the news on social media has been largely skeptical. ... Anthropic's reputation as a do-gooder AI company has soured.»

### F144 🟡 Крупное СМИ

Fast Company quotes M&A lawyer Eric Pacifici (SMB Law Group) on the irony of an AI company funding help for people displaced by AI, plus anonymous users calling it a tax write-off.

- Source: Fast Company (via Yahoo Finance), 2026-10-19 — <https://finance.yahoo.com/technology/ai/articles/anthropic-says-dedicate-5-shares-191700133.html> (confidence as rated by researcher: major_outlet)
- Quote: «Your job gets automated. The company that automated it gets more valuable. Its charitable fund gets richer. You apply for assistance.»

### F145 🟠 Вторичный источник

OfficeChai ('Anthropic Criticized For Opaque Nature Of Its Public Benefit Fund', Oct 19, 2026) frames the criticism as being about opacity and control rather than the idea itself, and notes the IPO timing.

- Source: OfficeChai, 2026-10-19 — <https://officechai.com/ai/anthropic-criticized-for-opaque-nature-of-its-public-benefit-fund/> (confidence as rated by researcher: secondary)
- Quote: «nobody outside Anthropic actually knows how the Public Benefit Fund will decide who gets paid. ... The announcement lands just weeks before what is expected to be one of the largest IPOs in history»

### F146 🟠 Вторичный источник

OfficeChai also quotes the X account PoliMath (@politicalmath, Oct 19, 2026) calling the fund a prospective 'NGO slush fund'.

- Source: OfficeChai, 2026-10-19 — <https://officechai.com/ai/anthropic-criticized-for-opaque-nature-of-its-public-benefit-fund/> (confidence as rated by researcher: secondary)
- Quote: «This is going to be an NGO slush fund. This is a bribe to left-wing politicians to get them on board with AI»

### F147 🟢 Первоисточник

Travis Kalanick quote-posted Anthropic's announcement on X on Oct 18, 2026 at 19:10:04 UTC (verified at original; 2,960 likes, ~461K views).

- Source: Travis Kalanick (X post), 2026-10-18 — <https://x.com/travisk/status/2111897619119341913> (confidence as rated by researcher: primary)
- Quote: «Behold, the EA infinite money glitch…»

### F148 🟢 Первоисточник

Jason Calacanis quote-posted Kalanick on X on Oct 18, 2026 at 20:15:57 UTC with a satirical UBI suggestion (verified at original).

- Source: Jason Calacanis (X post), 2026-10-18 — <https://x.com/Jason/status/2111914198632730924> (confidence as rated by researcher: primary)
- Quote: «.@AnthropicAI should start a UBI program that gives $3 to every American every month!

$1b in profits a month gets it done!»

### F149 🟢 Первоисточник

Software investor Vijar Kohli (Golden Door) quote-posted Anthropic on X on Oct 18, 2026 at 19:24:41 UTC arguing the fund dilutes voting rights and is about control (verified at original; 455 likes).

- Source: Vijar Kohli (X post), 2026-10-18 — <https://x.com/VijarKohli/status/2111901300728517038> (confidence as rated by researcher: primary)
- Quote: «This is not a good sign for raising more capital at an IPO. Anthropic is pre-emptively diluting voting rights. ... It gives proxy to whoever runs the Public Benefit Fund. Which will be more about control rather than making money.»

### F150 🟢 Первоисточник

Nathan Calvin (Chief Strategy Officer, Encode AI) posted a ~9,300-character critique on X on Oct 19, 2026 at 21:29:59 UTC, as a reply to Anthropic's @ajcimino about draft legislation. It lists nine Anthropic actions and does NOT mention the Public Benefit Fund; it references a reported $2 trillion IPO target.

- Source: Nathan Calvin (X post), 2026-10-19 — <https://x.com/_NathanCalvin/status/2112295219765137570> (confidence as rated by researcher: primary)
- Quote: «When I look at many notable actions that Anthropic has taken over the past year, that evidence seems most consistent to me with the view that Anthropic is primarily trying to win the race to super intelligence, and that other considerations (including safety) are fundamentally secondary.»

### F151 🟢 Первоисточник

Dario Amodei replied to Calvin with a ~11,400-character quote-post on X at 02:26:30 UTC on Oct 21, 2026 (evening of Oct 20 US Pacific), listing nine actions he says were commercially costly but safety-positive; the Public Benefit Fund is item 9 (verified at original; 4,097 likes, ~1.59M views).

- Source: Dario Amodei (X post), 2026-10-21 — <https://x.com/DarioAmodei/status/2112732230124818891> (confidence as rated by researcher: primary)
- Quote: «Here are some things Anthropic has done, in the same period you've cited (the last year), which were very costly to us commercially while having strong safety benefits: ... 9. Just this week, we announced we were putting 5% (and possibly more over time) of the company into a public benefit fund.

All of these decisions came with very substantial costs to us.»

### F152 🟢 Первоисточник

In the same reply Amodei conceded some of Calvin's examples were mistakes, said items 7, 8 and 9 of Calvin's list could have been handled better, took responsibility as CEO, and said Anthropic is over 5,000 people.

- Source: Dario Amodei (X post), 2026-10-21 — <https://x.com/DarioAmodei/status/2112732230124818891> (confidence as rated by researcher: primary)
- Quote: «I also do agree that some of the examples you cite were mistakes by Anthropic. ... I agree we could have handled your items 7, 8, and 9 better. ... I am of course the CEO, and I take responsibility.»

### F153 🟢 Первоисточник

Kevin Roose posted on X on Oct 19, 2026 at 01:50:06 UTC that the pledge could be the largest philanthropic capital commitment ever (verified at original; 901 likes).

- Source: Kevin Roose (X post), 2026-10-19 — <https://x.com/kevinroose/status/2111998289927454944> (confidence as rated by researcher: primary)
- Quote: «this post announced what could be the largest commitment of philanthropic capital ever made ($200 billion if Anthropic goes public at $1 trillion, which is probably conservative) 

the first reply I saw asked if Anthropic was going to use it for "gay race communism"»

### F154 🟢 Первоисточник

Brad Gerstner (Altimeter) quote-posted Musk on X on Oct 18, 2026 at 21:21:16 UTC, commending Anthropic while voicing concern about foundation wealth concentration (verified at original; 1,527 likes). The jawlah.co wording 'exceptional charitable commitment' is not in the post; the actual phrase is 'extraordinary gift'.

- Source: Brad Gerstner (X post), 2026-10-18 — <https://x.com/altcap/status/2111930638798635348> (confidence as rated by researcher: primary)
- Quote: «I commend Anthropic on their philanthropic commitments in lieu of a founder equity IPO grant.  It is an extraordinary gift - but also understand concerns about foundation wealth concentration.  Like Elon - I hope a meaningful portion of AI's wealth is a direct dividend.»

### F155 🟢 Первоисточник

UC Davis law professor Sarah Polcz (co-author of the AI stock tax framework behind the Sanders bill) posted a qualified welcome on X on Oct 18, 2026 at 21:20:38 UTC (verified at original).

- Source: Sarah Polcz (X post), 2026-10-18 — <https://x.com/SPolcz/status/2111930479725420749> (confidence as rated by researcher: primary)
- Quote: «Of course philanthropy doesn't replace public voice via an AI stock tax, but multiple economic responses to AI can co-exist and very pleased to see the landscape of public benefit evolving. Well done @AnthropicAI»

### F156 🟢 Первоисточник

Anthropic Deputy CISO Jason D. Clinton posted on X on Oct 18, 2026 at 22:18:01 UTC that he and a colleague pledged 50% of their equity and that the match program was a 'costly signal' (verified at original; 2,199 likes).

- Source: Jason D. Clinton (X post), 2026-10-18 — <https://x.com/JasonDClinton/status/2111944917840994774> (confidence as rated by researcher: primary)
- Quote: «Brandon and I pledged 50% of our equity. This was the principal reason that I left Google for Anthropic. The existence of this kind of program was a costly signal that Anthropic wasn't just talk, at a time when Anthropic didn't even have a released model. Fund a bright future!»

### F157 🟡 Крупное СМИ

AP (James Pollard and Wyatte Grantham-Philips, Oct 20, 2026) quoted Phil Buchanan, president of the Center for Effective Philanthropy, as cautiously hopeful.

- Source: Associated Press (via The Business Journal), 2026-10-20 — <https://thebusinessjournal.com/anthropic-openai-share-ai-wealth-public-benefit-funds/> (confidence as rated by researcher: major_outlet)
- Quote: «I guess I'm hopeful ... I'm not going to get too excited until I see some evidence of what's actually happening.»

### F158 🟡 Крупное СМИ

AP also quoted Katherina Rosqueta (UPenn Center for High Impact Philanthropy) on the LLC's flexibility and Brian Mittendorf (Ohio State accounting) calling the arrangement a 'gray area' that reflects intention rather than action now.

- Source: Associated Press (via The Business Journal), 2026-10-20 — <https://thebusinessjournal.com/anthropic-openai-share-ai-wealth-public-benefit-funds/> (confidence as rated by researcher: major_outlet)
- Quote: «They have a lot more flexibility and latitude in how to use the resources they put into the fund. ... reflects more of an intention to do things in the future rather than an act now»

### F159 🟡 Крупное СМИ

The San Francisco Standard (Rachyl Jones, Oct 20, 2026) quoted Priya Shanker, executive director of Stanford's Center on Philanthropy and Civil Society, recommending separate governance for the fund.

- Source: The San Francisco Standard, 2026-10-20 — <https://sfstandard.com/2026/10/20/anthropic-musk-philanthropy/> (confidence as rated by researcher: major_outlet)
- Quote: «It would behoove [Anthropic] to have a separate board and separate governance structure ... It would give it a lot more legitimacy.»

### F160 🟡 Крупное СМИ

The same SF Standard piece quoted Jacob Harold, former CEO of GuideStar, questioning whether the moves count as philanthropy and describing them as pre-emptive.

- Source: The San Francisco Standard, 2026-10-20 — <https://sfstandard.com/2026/10/20/anthropic-musk-philanthropy/> (confidence as rated by researcher: major_outlet)
- Quote: «Does it count as philanthropy? I don't know ... They think their technology will be so impactful that it will fundamentally change the economy ... They're kind of doing that preemptively here»

### F161 🟠 Вторичный источник

IPO adviser Lise Buyer (Class V Group) told CNBC the timing is 'beneficial from an image perspective'; CNBC itself returned 403, so this is relayed via Breitbart's citation of CNBC.

- Source: CNBC via Breitbart, 2026-10-19 — <https://www.breitbart.com/tech/2026/10/19/anthropic-will-dedicate-5-of-shares-to-public-benefit-fund-ahead-of-landmark-ai-ipo/> (confidence as rated by researcher: secondary)
- Quote: «beneficial from an image perspective»

### F162 🟠 Вторичный источник

The Hacker News thread on the announcement had 58 points and 47 comments at time of check and was mostly skeptical; one commenter defended the pledge as genuine.

- Source: Hacker News, 2026-10-18 — <https://news.ycombinator.com/item?id=50143755> (confidence as rated by researcher: secondary)
- Quote: «I feel confident this announcement is genuine, but of course none of us can read minds.»

### F163 🟠 Вторичный источник

HN critics argued the LLC structure imposes no formal constraint and that the 2%-per-50% escalator is too small.

- Source: Hacker News, 2026-10-18 — <https://news.ycombinator.com/item?id=50143755> (confidence as rated by researcher: secondary)
- Quote: «A 2% for every 50% increase is just insulting.»

### F164 🟡 Крупное СМИ

A Reuters factbox (Pragyan Kalita, Oct 20, 2026) compared the fund with other efforts, noting the OpenAI Foundation held a 26% stake worth about $130 billion after OpenAI's October 2025 restructuring and that the Gates Foundation plans to spend an additional $200 billion over two decades.

- Source: Reuters (via The Star), 2026-10-20 — <https://www.thestar.com.my/tech/tech-news/2026/10/21/factbox-anthropic039s-public-benefit-fund-and-how-it-compares-with-other-big-philanthropic-efforts> (confidence as rated by researcher: major_outlet)
- Quote: «would commit 5% of its shares to a new public benefit fund»

### F165 🟡 Крупное СМИ

Forbes (Siladitya Ray, Oct 19, 2026) reported the Musk, Sacks and Luckey reactions and described Sacks as co-chair of President Trump's Council of Advisors on Science and Technology; forbes.com returned 403 and the piece was read via Yahoo syndication.

- Source: Forbes (via Yahoo Finance), 2026-10-19 — <https://finance.yahoo.com/technology/ai/articles/anthropic-pledges-5-shares-public-072152314.html> (confidence as rated by researcher: major_outlet)
- Quote: «You've put 20% of your equity in an LLC. Whether it serves the public good remains to be seen.»

### F166 🟠 Вторичный источник

Stocktwits (Yuvraj Malik, Oct 18, 2026) linked the original Musk, Sacks and Kohli posts and quoted Anthropic's press release.

- Source: Stocktwits, 2026-10-18 — <https://stocktwits.com/news-articles/markets/equity/anthropic-ipo-musk-wants-ai-firm-to-hand-shares-directly-to-public-says-this-is-what-i-will-be-doing/cZx8BTGRBtU> (confidence as rated by researcher: secondary)
- Quote: «Given the pace of AI progress, bolder approaches may be needed. The fund will have the versatility to pursue them.»

### F167 🟠 Вторичный источник

AI FrontPage (Pratima O Pareek, Oct 19, 2026) linked the original Gerstner, Clinton, Luckey and Marcus X posts; those links were used to verify the posts above.

- Source: AI FrontPage, 2026-10-19 — <https://aifront-page.com/anthropic-5-percent-public-benefit-fund-debate/> (confidence as rated by researcher: secondary)
- Quote: «Sacks is right. Anthropic is playing games here.»

Researcher notes: VERIFIED AT ORIGINAL (via fxtwitter API JSON of the X posts, saved under /tmp/claude-0/-home-user-an-info/b29c76c6-899a-5222-9671-bd3017164403/scratchpad/tweets/): Anthropic's X post; Musk x4 (reply, 'This is what I will be doing', SpaceX pledge, 'stakes in the future economy'); Sacks; Marcus; Luckey; Moorhead; Gerstner; Roose; Polcz; Jack Clark; Jason D. Clinton; Kalanick; Calacanis; Kohli; Curran (thread root + lobbying post); Calvin's full post; Amodei's full reply.

COULD NOT VERIFY AT ORIGINAL / FLAGS:
1. Gary Marcus 'publicity stunt': NOT in his X post (2111992276767691122). His actual words: 'Sacks is right. Anthropic is playing games here. Trying to curry public favor while still holding control and resisting disclosure is annoying. And reeks of desperation.' The 'publicity stunt' wording appears only as a paraphrase in the aggregator jawlah.co (no link, no quotation marks) and QuantoSei ('PR gambit'). His Substack archive for Oct 17-24 has no post on the fund. Note the only verified 'publicity stunt' quote is Robert Pavlik (Dakota Wealth, Reuters Oct 19) about MUSK's SpaceX pledge, not Anthropic's fund — possible source of conflation.
2. Gerstner: jawlah's 'exceptional charitable commitment' is not his wording; verified post says 'extraordinary gift'. hyper.ai also attributes 'reeks of desperation' to Marcus correctly but gives no platform.
3. Luckey: Breitbart's claim that he said EA founders prioritize a 'non-western audience' is Breitbart's paraphrase; not in his verified post.
4. Andrew Curran UBI quote ('It sounds to me like they are planning their own form of self-directed global UBI'): quoted by Business Insider and visible in search snippets of his thread, but the exact post ID was not retrieved; only his thread root and lobbying-ban post were fetched.
5. Sam Hogan Heutmaker ('the reverse OpenAI', 'It's genius'): quoted by Business Insider only; original X post not found.
6. Will Brown (Prime Intellect) quote in BI not verified at original.
7. CNBC article (Lise Buyer 'beneficial from an image perspective') returned 403 (also AMP); relayed via Breitbart's citation of CNBC.
8. Inside Philanthropy 'Understanding Anthropic's New Public Benefit Fund Structure' (insidephilanthropy.com/home/copy-2) returned an empty page; could not verify content.
9. No EA Forum or LessWrong posts on the fund surfaced via search; their search pages are JS-rendered and returned no results. No reaction from Holden Karnofsky/Open Philanthropy/Toby Ord found.
10. fastcompany.com, forbes.com, benzinga.com, axios.com, cnbc.com, dealroom.co returned 403; businessinsider.com is blocked for the search tool. Fast Company, Forbes and Business Insider were read via Yahoo Finance syndication (bylines: Grace Snelling; Siladitya Ray; Tracy Connor and Tom Carter). The Fast Company fastcompany.com headline is 'Anthropic stock dedicated to public good? AI-weary skeptics react' (ID 91626042); the Yahoo syndication headline is '...The public is skeptical'.

CONTRADICTIONS BETWEEN SOURCES:
- Sacks's role: outlets say 'former AI czar' / 'former Trump technology adviser'; Forbes says co-chair of PCAST; his X bio says 'Co-Chair, President's Council of Advisors on Science & Technology'.
- Amodei reply date: Business Insider (Aditi Bharade) says Tuesday Oct 20; TNW says Wednesday Oct 21. The post timestamp is Oct 21 02:26:30 UTC = Oct 20 ~7:26pm Pacific, so both are right depending on time zone.
- Sacks's post is a quote-post of Jack Clark's post, not a reply 'under Anthropic's announcement' as OfficeChai describes; Marcus's post is a quote-post of Sacks.
- One search snippet attributed Luckey's 'definition of public good' line to Joe Lonsdale; the verified post is Luckey's.
- Calvin's post is a reply to Anthropic's @ajcimino (named 'Anthony' in the post) about a draft bill; it does not mention the Public Benefit Fund — Amodei introduced the fund as item 9 of his own list.
- Anthropic had not publicly responded to Musk's suggestion as of Oct 19-20 (Fox Business; NBC).

CONTEXT: Reaction split roughly along lines of (a) right-leaning tech figures wanting direct distribution to Americans (Musk, Luckey, Moorhead, Gerstner partially, Kohli), (b) governance/transparency critics (Sacks, Marcus, OfficeChai, HN, Shanker, Mittendorf), (c) EA-skeptic jabs (Kalanick, Calacanis), and (d) qualified positives (Roose, Polcz, Buchanan, Rosqueta, Clinton, tedsanders on HN). Dollar estimates of the 5% stake vary by assumed valuation ($48B at $965B; $100B at $2T; Roose's $200B is for the full ~20% at $1T) — none are from Anthropic.


## Корпоративный контекст Anthropic / anthropic-context (58)

### F168 🟢 Первоисточник

Anthropic's announcement 'Investing in the public benefit' was published October 18, 2026 and commits a portion of Anthropic's shares to a new wholly owned entity, the Anthropic Public Benefit Fund, described as having 'increased flexibility and scale'.

- Source: Anthropic, 2026-10-18 — <https://www.anthropic.com/news/public-benefit-fund> (confidence as rated by researcher: primary)
- Quote: «Today, we're committing a portion of Anthropic's shares to the Anthropic Public Benefit Fund ... The Anthropic Public Benefit Fund will have increased flexibility and scale»

### F169 🟢 Первоисточник

5% of Anthropic's shares are committed to the Fund, subject to stockholder approval, with an additional 2% added at the board's discretion for every 50% increase in company value above a set (undisclosed) baseline.

- Source: Anthropic, 2026-10-18 — <https://www.anthropic.com/news/public-benefit-fund> (confidence as rated by researcher: primary)
- Quote: «Subject to stockholder approval, 5% of Anthropic's shares will be committed today ... with an additional 2% added at the board's discretion for every 50% increase in the company's value above a set baseline»

### F170 🟢 Первоисточник

The Fund is structured as an LLC rather than a 501(c)(3), and none of the Anthropic equity it holds will be used for lobbying or political giving in the US or abroad.

- Source: Anthropic, 2026-10-18 — <https://www.anthropic.com/news/public-benefit-fund> (confidence as rated by researcher: primary)
- Quote: «We're establishing the Anthropic Public Benefit Fund as an LLC—rather than a 501(c)(3) or other format ... None of the Anthropic equity held by the LLC will be used for lobbying or political giving, in the US or abroad.»

### F171 🟢 Первоисточник

Possible uses named by Anthropic are large donations to traditional nonprofits or direct distributions to specific populations; labor-market disruption is the example given, with $200 million already committed and 'bolder approaches' possibly needed.

- Source: Anthropic, 2026-10-18 — <https://www.anthropic.com/news/public-benefit-fund> (confidence as rated by researcher: primary)
- Quote: «we might explore large donations to traditional nonprofits or direct distributions to specific populations ... Anthropic has already committed $200 million to studying and addressing this issue ... given the pace of AI progress, bolder approaches may be needed»

### F172 🟢 Первоисточник

Anthropic frames the Fund as an alternative to escalating executive equity awards: rather than escalating compensation for executives as is common at tech companies, it directs that equity to the public benefit.

- Source: Anthropic, 2026-10-18 — <https://www.anthropic.com/news/public-benefit-fund> (confidence as rated by researcher: primary)
- Quote: «It is common practice for tech companies to offer escalating compensation awards to their executives.»

### F173 🟢 Первоисточник

Anthropic's co-founders pledged to donate 80% of their equity holdings at founding; approximately half of employees participate in an equity donation match program; combined with the Fund, roughly 20% of Anthropic shares will be dedicated to the public good.

- Source: Anthropic, 2026-10-18 — <https://www.anthropic.com/news/public-benefit-fund> (confidence as rated by researcher: primary)
- Quote: «our co-founders pledged to donate 80% of their equity holdings ... Approximately half of our employees participate in this program ... roughly 20% of Anthropic shares will be dedicated to the public good»

### F174 🟢 Первоисточник

The announcement states that as a public benefit corporation most mission work (AI safety and interpretability research, applied biomedical research, Claude discounts for nonprofits and scientific institutions) stays inside the company; it promises more on the Fund's structure and governance, including valuation milestones, 'in the coming months' and an 'upcoming public benefit report'. The announcement does not mention the Long-Term Benefit Trust.

- Source: Anthropic, 2026-10-18 — <https://www.anthropic.com/news/public-benefit-fund> (confidence as rated by researcher: primary)
- Quote: «As a public benefit corporation, most of our work in pursuit of our mission takes place inside the company ... In the coming months, we will share more about the Anthropic Public Benefit Fund's structure and governance ... We will also report on our progress to date against our mission in an upcoming public benefit report»

### F175 🟢 Первоисточник

Anthropic is a Delaware Public Benefit Corporation; Delaware law expressly permits PBC directors to balance stockholders' financial interests with the public benefit purpose, which for Anthropic is 'the responsible development and maintenance of advanced AI for the long-term benefit of humanity'.

- Source: Anthropic, 2023-09-19 — <https://www.anthropic.com/news/the-long-term-benefit-trust> (confidence as rated by researcher: primary)
- Quote: «One governance feature we have already shared is that Anthropic is a Delaware Public Benefit Corporation, or PBC. ... Delaware corporate law expressly permits the directors of a PBC to balance the financial interests of the stockholders ... the responsible development and maintenance of advanced AI for the long-term benefit of humanity»

### F176 🟢 Первоисточник

Under Delaware General Corporation Law § 362(a), a public benefit corporation is a for-profit corporation managed in a manner that balances the stockholders' pecuniary interests, the best interests of those materially affected by the corporation's conduct, and the specific public benefit(s) in its certificate; § 366(b) requires a statement to stockholders on public-benefit progress at least biennially.

- Source: Delaware Code (Title 8, Ch. 1, Subch. XV) — <https://delcode.delaware.gov/title8/c001/sc15/index.html> (confidence as rated by researcher: primary)
- Quote: «balances the stockholders' pecuniary interests ... the best interests of those materially affected by the corporation's conduct ... shall no less than biennially provide its stockholders with a statement»

### F177 🟢 Первоисточник

The 2026 Public Benefit Report describes PBC status as a designation that requires balancing shareholder financial interests with the benefit to the broader public, and says the five charter pillars were set by the Board with input from the co-founders and the Long-Term Benefit Trust.

- Source: Anthropic (2026 Public Benefit Report PDF), 2026-10-21 — <https://www-cdn.anthropic.com/a9ceec76a54d28d27affffcdab6faf7c142cd587.pdf> (confidence as rated by researcher: primary)
- Quote: «Anthropic is a Public Benefit Corporation (PBC), a designation that requires us to balance the financial interests of shareholders with the benefit to the broader public. ... our Board of Directors, with input from Anthropic's co-founders and the Long-Term Benefit Trust, established five charter pillars.»

### F178 🟢 Первоисточник

Anthropic's company page lists its Board of Directors as Dario Amodei, Daniela Amodei, Yasmin Razavi, Reed Hastings, Chris Liddell and Vas Narasimhan, and its LTBT Trustees as Dr. Ben Bernanke, Richard Fontaine, Neil Buddy Shah and Dr. Christopher Stubbs; the board 'is elected by stockholders and our Long-Term Benefit Trust'.

- Source: Anthropic, 2026-10-24 — <https://www.anthropic.com/company> (confidence as rated by researcher: primary)
- Quote: «Anthropic is a Public Benefit Corporation, whose purpose is the responsible development and maintenance of advanced AI for the long-term benefit of humanity.»

### F179 🟢 Первоисточник

The Long-Term Benefit Trust (announced Sept 19, 2023) is a Delaware common-law purpose trust whose five financially disinterested trustees hold Class T stock giving them authority to elect and remove a number of board members that phases in by time- and funding-based milestones, reaching a board majority within 4 years; trustees serve one-year terms and future trustees are elected by the trustees.

- Source: Anthropic, 2023-09-19 — <https://www.anthropic.com/news/the-long-term-benefit-trust> (confidence as rated by researcher: primary)
- Quote: «The Trust is an independent body of five financially disinterested members. ... The Class T stock grants the Trust the authority to elect and remove a number of ... the Trust will elect a majority of the board within 4 years. ... Trustees serve one-year terms. ... Future Trustees will be elected by a vote of the Trustees.»

### F180 🟢 Первоисточник

The LTBT structure contains 'failsafe' provisions allowing stockholders to change the Trust and its powers without trustee consent if sufficiently large supermajorities agree, with required supermajorities increasing as the Trust's power phases in.

- Source: Anthropic, 2023-09-19 — <https://www.anthropic.com/news/the-long-term-benefit-trust> (confidence as rated by researcher: primary)
- Quote: «failsafe ... that allow changes to the Trust and its powers without the consent of the Trustees ... if sufficiently large supermajorities of the stockholders agree»

### F181 🟢 Первоисточник

The LTBT's initial trustees (2023) were Jason Matheny (RAND CEO), Kanika Bahl (Evidence Action CEO), Neil Buddy Shah (Clinton Health Access Initiative CEO, Chair), Paul Christiano (Alignment Research Center founder) and Zach Robinson (Interim CEO, Effective Ventures US), selected by Anthropic's board after a year-long search.

- Source: Anthropic, 2023-09-19 — <https://www.anthropic.com/news/the-long-term-benefit-trust> (confidence as rated by researcher: primary)

### F182 🟢 Первоисточник

Per the LTBT page footnotes: Jason Matheny stepped down December 2023; Paul Christiano stepped down April 2024; Richard Fontaine (CEO, Center for a New American Security) joined May 2025; Kanika Bahl and Zach Robinson stepped down January 2026; Mariano-Florentino (Tino) Cuéllar joined January 2026; Ben Bernanke joined July 2026.

- Source: Anthropic, 2026-10-24 — <https://www.anthropic.com/news/the-long-term-benefit-trust> (confidence as rated by researcher: primary)
- Quote: «Richard Fontaine, CEO of the Center for a New American Security, joined the LTBT in May 2025. ... Mariano-Florentino (Tino) Cuéllar, President of the Carnegie Endowment for International Peace, joined in January 2026. ... former Chair of the Federal Reserve, joined in July 2026.»

### F183 🟠 Вторичный источник

Outside counsel to Anthropic (John Morley of Yale Law School; David Berger and Amy Simmerman of Wilson Sonsini) explained in October 2023 that trustees initially elect one of the company's five directors, rising to two and then three (a board majority) over time or on fundraising milestones; a stockholder supermajority can amend the Trust's powers as 'a kind of failsafe against the actions of the Voting Trustees'.

- Source: Harvard Law School Forum on Corporate Governance, 2023-10-28 — <https://corpgov.law.harvard.edu/2023/10/28/anthropic-long-term-benefit-trust/> (confidence as rated by researcher: secondary)
- Quote: «responsibly develop and maintain advanced AI for the long-term benefit of humanity»

### F184 🟢 Первоисточник

On July 9, 2026 the LTBT named Dr. Ben Bernanke (Fed Chair 2006–2014, 2022 Nobel laureate, Brookings Distinguished Fellow) as a trustee, joining Neil Buddy Shah (Chair), Richard Fontaine and Mariano-Florentino Cuéllar; trustees hold no Anthropic equity, do not share in profits and are compensated only for their time and service.

- Source: Anthropic, 2026-07-09 — <https://www.anthropic.com/news/ben-bernanke> (confidence as rated by researcher: primary)
- Quote: «Anthropic has created a unique governance structure»

### F185 🟢 Первоисточник

In the Bernanke announcement Daniela Amodei said: 'AI may have the most significant economic effects of any technology in modern history', and Neil Buddy Shah said: 'The institutions built around this technology will matter as much as the technology itself.'

- Source: Anthropic, 2026-07-09 — <https://www.anthropic.com/news/ben-bernanke> (confidence as rated by researcher: primary)
- Quote: «AI may have the most significant economic effects of any technology in modern history.»

### F186 🟢 Первоисточник

On January 21, 2026 the LTBT announced Mariano-Florentino (Tino) Cuéllar (former Justice of the Supreme Court of California, Carnegie Endowment president) had joined; Kanika Bahl and Zachary Robinson concluded their terms; the post names Jay Kreps and Reed Hastings as board members the Trust appointed.

- Source: Anthropic, 2026-01-21 — <https://www.anthropic.com/news/mariano-florentino-long-term-benefit-trust> (confidence as rated by researcher: primary)
- Quote: «the need for governance structures that marry private sector dynamism with civic responsibility has never been more urgent.»

### F187 🟢 Первоисточник

On October 21, 2026 Anthropic announced experimental physicist Christopher Stubbs (Samuel C. Moncher Professor of Physics and of Astronomy at Harvard; Harvard Dean of Science 2018–2024; High-Z Supernova Search Team member in 1998 whose work won the Breakthrough Prize in Fundamental Physics; inaugural project scientist of the Vera C. Rubin Observatory; JASON member) joined the LTBT as its first physicist; the Trust 'has the authority to appoint a majority of Anthropic's board'; other trustees named are Neil Buddy Shah (Chair), Richard Fontaine and Ben Bernanke.

- Source: Anthropic, 2026-10-21 — <https://www.anthropic.com/news/christopher-stubbs-joins-long-term-benefit-trust> (confidence as rated by researcher: primary)
- Quote: «I am honored to join Anthropic's Long-Term Benefit Trust and to help the company deliver on its public benefit mission.»

### F188 🟡 Крупное СМИ

Fortune (Jeremy Kahn, Oct 21, 2026) reports Stubbs fills one of two open LTBT seats; one seat remains open since August, when Cuéllar left the Trust to become Anthropic's first chief global affairs officer; the Trust can elect a majority of Anthropic's seven-person board via a special class of stock with no economic value; the Public Benefit Fund 'is separate from the Trust'.

- Source: Fortune, 2026-10-21 — <https://fortune.com/2026/10/21/anthropic-adds-harvard-astrophysicist-to-the-trust-that-controls-its-board> (confidence as rated by researcher: major_outlet)
- Quote: «As a grandfather, I want to help ensure that AI is developed and deployed for the long-term benefit of humanity.»

### F189 🟡 Крупное СМИ

Fortune (Oct 21, 2026) reports Anthropic confidentially filed a draft registration statement with the SEC in June 2026, is widely expected to go public as soon as November 2026, was valued at $965 billion in a May 2026 funding round, reportedly plans super-voting shares for founders, and that critics argue the governance structure plus the Trust would leave public shareholders little say.

- Source: Fortune, 2026-10-21 — <https://fortune.com/2026/10/21/anthropic-adds-harvard-astrophysicist-to-the-trust-that-controls-its-board> (confidence as rated by researcher: major_outlet)

### F190 🟡 Крупное СМИ

Reuters (Oct 21, 2026, Prathik Jayaprakash) describes the LTBT as holding 'the power to appoint a majority of the AI startup's board' and Anthropic's PBC status as a structure that 'formally allows it to balance shareholder interests with broader societal considerations'.

- Source: Reuters (via KFGO), 2026-10-21 — <https://kfgo.com/2026/10/21/anthropic-adds-former-harvard-science-dean-to-oversight-body/> (confidence as rated by researcher: major_outlet)
- Quote: «the power to appoint a majority of the AI startup's board»

### F191 🟡 Крупное СМИ

The Harvard Crimson (Oct 22, 2026) reports Stubbs stepped down as FAS senior adviser on generative AI (announced Oct 1, 2026) less than three weeks before joining the Trust, and that Harvard Corporation member Mariano-Florentino Cuéllar served on Anthropic's trust from January to August 2026 before becoming the company's first global affairs officer.

- Source: The Harvard Crimson, 2026-10-22 — <https://www.thecrimson.com/article/2026/10/22/stubbs-anthropic-trust-harvard/> (confidence as rated by researcher: major_outlet)
- Quote: «I use AI tools in my research every day and see what they make possible.»

### F192 🟢 Первоисточник

In the 2026 Public Benefit Report's closing commentary, the LTBT (signed by Buddy Shah) states it elects a majority of Anthropic's board, has a formal role in safety policies, helped develop the five charter pillars, and explicitly endorses the planned 5% share set-aside as 'a significant step' while saying benefit distribution 'still lags behind the company's ambitions'.

- Source: Anthropic (2026 Public Benefit Report PDF), 2026-10-21 — <https://www-cdn.anthropic.com/a9ceec76a54d28d27affffcdab6faf7c142cd587.pdf> (confidence as rated by researcher: primary)
- Quote: «We elect a majority of Anthropic's board, meet regularly with its leaders, and have a formal role in shaping its safety policies ... If stockholders agree, Anthropic is planning to set aside at least 5% of the company's shares in a separate entity dedicated entirely to the public benefit charter. It is a significant step. But the work of distributing the benefits still lags behind the company's ambitions.»

### F193 🟢 Первоисточник

The LTBT commentary says the report 'largely describes inputs' and that in future reports the Trust will look for outcomes, naming three areas: keeping AI safe, delivering on AI's promise, and meeting shared challenges.

- Source: Anthropic (2026 Public Benefit Report PDF), 2026-10-21 — <https://www-cdn.anthropic.com/a9ceec76a54d28d27affffcdab6faf7c142cd587.pdf> (confidence as rated by researcher: primary)
- Quote: «Right now, it largely describes inputs; in subsequent reports, we will increasingly look for Anthropic to produce outcomes.»

### F194 🟢 Первоисточник

Anthropic's Transparency Hub (updated July 23, 2026) says the LTBT, an independent body of financially disinterested trustees, can elect board members and over time a majority, so that 'our mission is insulated from short-term commercial and shareholder pressures'; Risk Reports published every 3–6 months are shared with the Board and the LTBT.

- Source: Anthropic, 2026-07-23 — <https://www.anthropic.com/transparency/voluntary-commitments> (confidence as rated by researcher: primary)
- Quote: «our mission is insulated from short-term commercial and shareholder pressures»

### F195 🟢 Первоисточник

The 2026 Public Benefit Report PDF (26 pages, titled 'Anthropic 2026 Public Benefit Report: Taking stock of our progress toward our charter') has PDF metadata creation date October 21, 2026; its foreword is by Daniela Amodei, 'Co-Founder and President, Chair of the Board of Directors', who says the report will be published annually.

- Source: Anthropic (2026 Public Benefit Report PDF), 2026-10-21 — <https://www-cdn.anthropic.com/a9ceec76a54d28d27affffcdab6faf7c142cd587.pdf> (confidence as rated by researcher: primary)
- Quote: «This report, which we'll publish annually, lays out how we define success against that charter and the concrete proof of our progress.»

### F196 🟢 Первоисточник

The report's foreword restates the giving commitments: at least 5% of shares set aside subject to stockholder approval, each co-founder's 80% equity pledge to philanthropy, and matched equity-donation pledges from employees, for about 20% of shares toward the public good.

- Source: Anthropic (2026 Public Benefit Report PDF), 2026-10-21 — <https://www-cdn.anthropic.com/a9ceec76a54d28d27affffcdab6faf7c142cd587.pdf> (confidence as rated by researcher: primary)
- Quote: «We announced that, subject to stockholder approval, we are setting aside at least 5% of our shares to fund projects in pursuit of our public benefit charter. Between this set-aside, each of our co-founders' commitment to pledge 80% of their equity to philanthropy, and matched equity-donation pledges from employees, we hope that about 20% of Anthropic shares will be put toward the public good.»

### F197 🟢 Первоисточник

The report's five charter pillars are: (1) The technical problems of AI safety are solved; (2) AI safety is a universal practice backstopped by law; (3) AI strengthens democracy and global stability; (4) AI expands prosperity and human flourishing; (5) AI's benefits are shared by everyone.

- Source: Anthropic (2026 Public Benefit Report PDF), 2026-10-21 — <https://www-cdn.anthropic.com/a9ceec76a54d28d27affffcdab6faf7c142cd587.pdf> (confidence as rated by researcher: primary)
- Quote: «5. AI's benefits are shared by everyone. AI delivers transformative benefits that reach people everywhere, and the opportunities AI creates are distributed.»

### F198 🟢 Первоисточник

Under Pillar 4 the report says Anthropic committed $200 million to an Economic Futures Research Fund, has an Economic Policy Framework and an Economic Advisory Council, and committed an initial $150 million to Claude Corps (with CodePath) to fund 1,000 fellowships at over 400 partnering nonprofits.

- Source: Anthropic (2026 Public Benefit Report PDF), 2026-10-21 — <https://www-cdn.anthropic.com/a9ceec76a54d28d27affffcdab6faf7c142cd587.pdf> (confidence as rated by researcher: primary)
- Quote: «We've committed an initial $150 million to fund 1,000 fellowships for people early in their careers to spend one year working at one of over 400 partnering nonprofits.»

### F199 🟢 Первоисточник

The report concedes its interventions are small relative to AI's impact, that gains may accrue mainly to large businesses including AI companies themselves, that economic gains from AI 'are not yet distributed', and that it lacks evidence its health and education efforts have had their intended effects.

- Source: Anthropic (2026 Public Benefit Report PDF), 2026-10-21 — <https://www-cdn.anthropic.com/a9ceec76a54d28d27affffcdab6faf7c142cd587.pdf> (confidence as rated by researcher: primary)
- Quote: «These early investments have been promising, but they reach thousands, whereas AI's impacts will affect billions. Claude Corps, for example, will support only 1,000 fellows in the first year ... It's possible that the gains from AI will accrue mainly to large businesses, including AI companies themselves»

### F200 🟢 Первоисточник

Other giving/benefit items in the report: MyFriendBen has helped 115,000 households access roughly $150 million in unclaimed benefits using Claude; Claude Team plan for scientists supports over 3,000 institutions in more than 100 countries; AI for Science awarded credits to more than 800 projects at more than 450 institutions; significant discounts to nonprofits in low- and middle-income countries; commitment to keep Claude free of advertising.

- Source: Anthropic (2026 Public Benefit Report PDF), 2026-10-21 — <https://www-cdn.anthropic.com/a9ceec76a54d28d27affffcdab6faf7c142cd587.pdf> (confidence as rated by researcher: primary)
- Quote: «So far, MyFriendBen has helped 115,000 households collectively access roughly $150 million in unclaimed benefits.»

### F201 🟠 Вторичный источник

EdTech Innovation Hub (Oct 23, 2026) reports the 2026 Public Benefit Report was published October 21, 2026 and quotes Daniela Amodei on LinkedIn: 'We'll publish one every year laying out how we define success toward our charter and the concrete proof of our progress.'

- Source: EdTech Innovation Hub, 2026-10-23 — <https://www.edtechinnovationhub.com/news/anthropic-publishes-public-benefit-report-detailing-ai-progress-and-gaps-in-measuring-impact> (confidence as rated by researcher: secondary)
- Quote: «We'll publish one every year laying out how we define success toward our charter and the concrete proof of our progress.»

### F202 🟢 Первоисточник

The Anthropic Economic Futures Program launched June 27, 2025 with three pillars ('Research Grants', 'Evidence-Based Policy', 'Economic Measurement and Data'), rapid grants of up to $50,000 with initial awards in mid-August 2025, API credits for partner institutions, and policy symposia in Washington, DC (September 2025; proposals due July 25, 2025) and London (November 2025; proposals due September 12, 2025).

- Source: Anthropic, 2025-06-27 — <https://www.anthropic.com/news/introducing-the-anthropic-economic-futures-program> (confidence as rated by researcher: primary)
- Quote: «Society's response to AI is not predetermined.»

### F203 🟡 Крупное СМИ

On June 10, 2026 (AP), Anthropic pledged an initial $200 million to an Economic Futures Research Fund for research trials and 'program evaluation' of public policies, plus a separate $150 million national fellowship program for early-career professionals; Dario Amodei's essay the same day said UBI could be funded by taxes on 'relevant companies' or a higher capital gains tax, and Anthropic's framework set responses for 5%, 10% and 'unprecedented' unemployment scenarios.

- Source: Associated Press (via WTOP), 2026-06-10 — <https://wtop.com/national/2026/06/anthropic-pledges-200-million-to-research-ais-economic-impact-as-ceo-suggests-job-loss-solutions/> (confidence as rated by researcher: major_outlet)
- Quote: «The key challenge in such a world won't be incentivizing growth, but finding a way for everyone to share in the benefits.»

### F204 🟢 Первоисточник

Anthropic's 'Policy on the AI Exponential' economic policy framework page describes 'A $200 million commitment to an Economic Futures Research Fund' as 'an evolution to our Economic Futures Program established a year ago', a '$150 million national fellowship program', and for an 'unprecedented' unemployment scenario lists new tax revenue sources, basic income, sovereign wealth models and equity-sharing mechanisms.

- Source: Anthropic — <https://www.anthropic.com/policy-on-the-ai-exponential/epf> (confidence as rated by researcher: primary)
- Quote: «an evolution to our Economic Futures Program established a year ago»

### F205 🟢 Первоисточник

Anthropic's Transparency Hub states: 'In June 2026, Anthropic announced a $200 million commitment' to the Economic Futures Research Fund, and that Claude Corps is 'backed by an initial $150 million commitment' to train 1,000 early-career fellows placed full-time with U.S. nonprofits for a year.

- Source: Anthropic, 2026-07-23 — <https://www.anthropic.com/transparency/voluntary-commitments> (confidence as rated by researcher: primary)
- Quote: «backed by an initial $150 million commitment»

### F206 🟢 Первоисточник

The Economic Futures Research Fund agenda (July 22, 2026) sets five priorities: 'Shaping AI's impact on workers at the firm and workplace level'; 'Equipping people to navigate AI-driven transitions'; 'Modernizing income support for AI-driven displacement'; 'Building worker stakes in AI-driven growth before disruption arrives'; 'Generating new evidence on public investments'. It primarily funds projects of $5–30 million, will not directly fund anything below $1 million, and backs large-scale RCTs, pilots and program evaluations by universities, research institutes and nonprofits.

- Source: Anthropic, 2026-07-22 — <https://www.anthropic.com/news/economic-futures-research-fund-agenda> (confidence as rated by researcher: primary)
- Quote: «We're willing to fund creative and ambitious pilots»

### F207 🟢 Первоисточник

'Introducing Claude Corps' (June 11, 2026): Anthropic commits an initial $150m to teach 1,000 fellows to use Claude and place them with nonprofits (at least 400 nonprofits over 12 months); CodePath is employer of record; Social Finance leads measurement and evaluation; fellows get a full-time $85,000 salary plus benefits; the first cohort of 100 begins October 2026 (applications closed July 17), with further cohorts in March 2027 and August 2027; applicants must be over 18 with under two years of full-time work experience 'regardless of educational background'.

- Source: Anthropic, 2026-06-11 — <https://www.anthropic.com/news/claude-corps> (confidence as rated by researcher: primary)
- Quote: «regardless of educational background»

### F208 🟢 Первоисточник

The Claude Corps FAQ pages state fellows are employed by CodePath at $85,000 per year, host organizations can host up to four fellows and receive a one-time $10,000 grant administered through Social Finance, and the three cohorts start October 19, 2026, March 8, 2027 and August 2027.

- Source: Anthropic (Claude Corps FAQ) — <https://www.anthropic.com/claude-corps/host> (confidence as rated by researcher: primary)

### F209 🟢 Первоисточник

The Anthropic Economic Index launched February 10, 2025 as 'an initiative aimed at understanding AI's effects on labor markets and the economy over time', using Clio on roughly one million Claude.ai Free/Pro conversations; first findings: 37.2% of queries in computer and mathematical tasks, about 36% of occupations used AI for at least a quarter of tasks, about 4% for at least 75%, augmentation 57% vs automation 43%, data shared on Hugging Face.

- Source: Anthropic, 2025-02-10 — <https://www.anthropic.com/news/the-anthropic-economic-index> (confidence as rated by researcher: primary)
- Quote: «37.2% of queries sent to Claude were in this category.»

### F210 🟢 Первоисточник

The Economic Index report 'Cadences' (June 26, 2026) samples Chat and Cowork conversations from April 10 to June 10, 2026 and links them to an Economic Index Survey launched April 2026; 57% of respondents say AI made their skills more valuable, 68% report learning more, 86%/82%/69% report productivity gains in speed/scope/quality, and over a third expect AI to handle 'most or nearly all' of their work tasks next year. The Economic Index landing page shows 'Last updated: June 26, 2026'.

- Source: Anthropic, 2026-06-26 — <https://www.anthropic.com/research/economic-index-june-2026-report> (confidence as rated by researcher: primary)

### F211 🟠 Вторичный источник

The Economic Index January 2026 report ('Economic primitives', November 2025 data) reportedly found augmented conversations rose 5 points to 52% and automated fell 4 points to 45% on Claude.ai (figure taken from a search summary of the Anthropic page, not fetched directly).

- Source: Anthropic (via search summary), 2026-01 — <https://www.anthropic.com/research/anthropic-economic-index-january-2026-report> (confidence as rated by researcher: secondary)

### F212 🟢 Первоисточник

In 'Machines of Loving Grace' (October 2024), section 5 'Work and meaning', Dario Amodei writes that a broader societal conversation about how the economy should be organized will be needed, floats 'a large universal basic income' and 'a capitalist economy of AI systems, which then give out resources', suspects 'some new and stranger thing will be needed', and warns exploitative or dystopian directions must be prevented; the essay does not use the words 'taxation' or 'redistribution'.

- Source: Dario Amodei (darioamodei.com), 2024-10 — <https://www.darioamodei.com/essay/machines-of-loving-grace> (confidence as rated by researcher: primary)
- Quote: «there will be a need for a broader societal conversation about how the economy should be organized ... It could be as simple as a large universal basic income for everyone ... I suspect that some new and stranger thing will be needed»

### F213 🟢 Первоисточник

In 'The Adolescence of Technology' (January 2026), Amodei calls progressive taxation 'the natural policy response to an enormous economic pie coupled with high inequality', says the tax 'could be general or could be targeted against AI companies in particular', and argues extreme inequality justifies 'a more robust tax policy on basic moral grounds'.

- Source: Dario Amodei (darioamodei.com), 2026-01 — <https://www.darioamodei.com/essay/the-adolescence-of-technology> (confidence as rated by researcher: primary)
- Quote: «The natural policy response to an enormous economic pie coupled with high inequality ... The tax could be general or could be targeted against AI companies in particular. ... I think the extreme levels of inequality predicted in this essay justify a more robust tax policy on basic moral grounds.»

### F214 🟢 Первоисточник

The same essay states that all of Anthropic's co-founders have pledged to donate 80% of their wealth, that staff have pledged company shares 'worth billions at current prices', that 'wealthy individuals have an obligation to help solve this problem', and that 'Those who are at the forefront of AI's economic boom should be willing to give away both their wealth and their power.'

- Source: Dario Amodei (darioamodei.com), 2026-01 — <https://www.darioamodei.com/essay/the-adolescence-of-technology> (confidence as rated by researcher: primary)
- Quote: «All of Anthropic's co-founders have pledged to donate 80% of our wealth. ... Fourth, wealthy individuals have an obligation to help solve this problem. ... The thing to worry about is a level of wealth concentration that will break society.»

### F215 🟢 Первоисточник

The essay also proposes real-time data on job displacement, favoring innovation over 'cost savings' layoffs, reassigning employees, and says 'it may be feasible to pay human employees even long after they are no longer providing economic value'; it recalls his 2025 prediction that 'AI could displace half of all entry-level white collar jobs in the next 1–5 years'.

- Source: Dario Amodei (darioamodei.com), 2026-01 — <https://www.darioamodei.com/essay/the-adolescence-of-technology> (confidence as rated by researcher: primary)
- Quote: «it may be feasible to pay human employees even long after they are no longer providing economic value»

### F216 🟡 Крупное СМИ

Fortune (Preston Fore, January 27, 2026) reported that all seven Anthropic cofounders — Dario Amodei, Daniela Amodei, Tom Brown, Jack Clark, Jared Kaplan, Sam McCandlish and Christopher Olah — pledged to donate 80% of their wealth, each estimated by Forbes at about $3.7 billion (before funding talks at a $350 billion valuation, up from $183 billion), with employees also pledging shares worth billions and the company matching; the essay was published the day before (January 26, 2026).

- Source: Fortune, 2026-01-27 — <https://fortune.com/2026/01/27/anthropic-billionaire-cofounders-ceo-dario-amodei-giving-away-80-percent-of-wealth-fighting-inequality-ai-revolution/> (confidence as rated by researcher: major_outlet)
- Quote: «The thing to worry about is a level of wealth concentration that will break society»

### F217 ⚪ Оценка или мнение

Forbes (Richard Nieva, Feb 12, 2026) reportedly estimated that after a $380 billion valuation the seven billionaire cofounders' fortunes nearly doubled to about $7 billion apiece, putting the 80% pledge's total value at up to $39.2 billion (page returned 403; figures from search snippet only).

- Source: Forbes (search snippet), 2026-02-12 — <https://www.forbes.com/sites/richardnieva/2026/02/12/anthropics-seven-billionaire-cofounders-nearly-double-their-fortunes-as-ai-giants-valuation-soars-to-380-billion/> (confidence as rated by researcher: speculative)

### F218 🟡 Крупное СМИ

AP (Oct 18, 2026) reported the fund as 'a new entity within the company', quoted Anthropic's blog that the fund 'will have increased flexibility and scale, enabling us to pursue our mission in new ways', said Anthropic is planning a 'massive' IPO as soon as November, and described Anthropic as a PBC set up by 'CEO Dario Amodei and five other cofounders' (i.e., six, versus seven in Fortune/Forbes).

- Source: Associated Press (via ABC News), 2026-10-18 — <https://abcnews.com/Technology/wireStory/anthropic-commits-5-stock-new-public-benefit-fund-137368440> (confidence as rated by researcher: major_outlet)
- Quote: «will have increased flexibility and scale, enabling us to pursue our mission in new ways»

### F219 🟡 Крупное СМИ

AP (James Pollard and Wyatte Grantham-Philips, Oct 20, 2026): Anthropic was valued at close to $1 trillion earlier in 2026; private foundations must distribute at least 5% of endowment value annually while LLCs are not bound by that rule and can pay individuals (Brian Mittendorf, Ohio State, calls this a 'gray area'); the pledge triggers no immediate tax write-off; Phil Buchanan (Center for Effective Philanthropy): 'I'm not going to get too excited until I see some evidence of what's actually happening.'; Gary Marcus: 'Anthropic is playing games here.'; Jay Ritter says the announcement helps investors 'know what they're buying'.

- Source: Associated Press (via ClickOnDetroit), 2026-10-20 — <https://www.clickondetroit.com/business/2026/10/20/ahead-of-massive-ipos-ai-companies-are-sketching-plans-to-share-their-wealth/> (confidence as rated by researcher: major_outlet)
- Quote: «a lot more flexibility and latitude in how to use the resources they put into the fund»

### F220 🟡 Крупное СМИ

The same AP story says the OpenAI Foundation committed $1 billion earlier in 2026 to grantmaking, OpenAI proposed a 'Public Wealth Fund' in April 2026, and OpenAI plans its own IPO in 2027; Daniela Amodei told AP in May 2026 that success would likely increase philanthropic support for disease research and shared prosperity from AI.

- Source: Associated Press (via ClickOnDetroit), 2026-10-20 — <https://www.clickondetroit.com/business/2026/10/20/ahead-of-massive-ipos-ai-companies-are-sketching-plans-to-share-their-wealth/> (confidence as rated by researcher: major_outlet)

### F221 🟡 Крупное СМИ

Reuters (Oct 18, 2026) reported that none of the fund's equity will be used for lobbying or political giving, that Anthropic's IPO prospectus contains roughly 80 pages of risk factors within a 261-page main body warning AI could pose 'catastrophic or existential risks to humanity', that Elon Musk recommended 'giving the shares directly to the public', and cited IMF chief Kristalina Georgieva's estimate that about 40% of jobs (60% in advanced economies) will be affected by AI.

- Source: Reuters (via Taiwan News), 2026-10-18 — <https://www.taiwannews.com.tw/en/news/6460446> (confidence as rated by researcher: major_outlet)
- Quote: «none of the equity held by its fund would be used for lobbying or political giving in the United States or abroad»

### F222 🟡 Крупное СМИ

Reuters factbox (Oct 20, 2026): the Anthropic fund 'would be a wholly owned limited liability company' receiving an additional 2% of shares at the board's discretion for every 50% increase in value above an undisclosed baseline; it follows Senator Bernie Sanders' bill to give the public a 50% stake in the largest US AI companies; for comparison, OpenAI's October 2025 restructuring left the OpenAI Foundation a 26% stake worth about $130 billion plus a warrant, with an initial $25 billion commitment to health and AI resilience.

- Source: Reuters (via The Star), 2026-10-20 — <https://www.thestar.com.my/tech/tech-news/2026/10/21/factbox-anthropic039s-public-benefit-fund-and-how-it-compares-with-other-big-philanthropic-efforts> (confidence as rated by researcher: major_outlet)
- Quote: «commit 5% of its shares to a new public benefit fund»

### F223 🟡 Крупное СМИ

TechCrunch (Anthony Ha, Oct 18, 2026) described the fund as 'structured as a wholly owned entity within the company', quoted Anthropic that 'The Fund will have the versatility to pursue them', and recalled Dario Amodei describing public backlash against AI as 'fundamentally a crisis of trust'.

- Source: TechCrunch, 2026-10-18 — <https://techcrunch.com/2026/10/18/anthropic-says-its-committing-5-of-its-shares-to-a-public-benefit-fund/> (confidence as rated by researcher: major_outlet)
- Quote: «given the pace of AI progress, bolder approaches may be needed. The Fund will have the versatility to pursue them.»

### F224 ⚪ Оценка или мнение

Third-party estimates of the 5% stake's value: about $48 billion at the $965 billion valuation from a $65 billion May 2026 round; about $75 billion at a discussed ~$1.5 trillion IPO valuation; about $7.2 billion at New Constructs' $144 billion equity estimate; Forbes reportedly estimated about $100 billion at a $2 trillion debut. None of these figures appear in Anthropic's announcement.

- Source: KuCoin News / The Rundown / Forbes (search snippets), 2026-10-19 — <https://www.kucoin.com/news/flash/anthropic-pledges-48-billion-in-stock-to-public-benefit-fund-ahead-of-ipo> (confidence as rated by researcher: speculative)

### F225 🟢 Первоисточник

Anthropic's announcements listing dates the Stubbs post Oct 21, 2026 ('Physicist Christopher Stubbs joins Anthropic's Long-Term Benefit Trust'), the fund post Oct 18, 2026 ('Investing in the public benefit'), and also shows an Oct 2, 2026 post 'Anthropic invests $100 million to train 10,000 engineers' (Claude Frontier Academy); no separate announcement entry exists for the 2026 Public Benefit Report.

- Source: Anthropic, 2026-10-24 — <https://www.anthropic.com/news/announcements> (confidence as rated by researcher: primary)

Researcher notes: CONTRADICTIONS / CAVEATS: (1) Cofounder count: Fortune (Jan 27, 2026) and the Adolescence essay refer to seven cofounders (Dario Amodei, Daniela Amodei, Tom Brown, Jack Clark, Jared Kaplan, Sam McCandlish, Christopher Olah); AP's Oct 18, 2026 wire says 'Dario Amodei and five other cofounders' (six); Fortune Feb 24, 2026 says 'Amodei and Anthropic's six cofounders' (consistent with seven total). (2) Public Benefit Report date: PDF metadata and EdTech Innovation Hub say Oct 21, 2026; a search snippet of Anthropic's homepage showed Oct 7, 2026, which I could not confirm; the report is not listed on anthropic.com/news/announcements. The fund announcement of Oct 18 called the report 'upcoming', consistent with Oct 21. (3) LTBT board-seat count: the 2023 Anthropic post said the Trust would elect a majority 'within 4 years'; outside counsel (Harvard corpgov, 2023) described seats rising 1->2->3 of a five-member board; in 2026 the LTBT's own commentary in the Public Benefit Report says 'We elect a majority of Anthropic's board', Anthropic's Stubbs post says 'authority to appoint a majority', Fortune says a seven-person board, while anthropic.com/company lists six directors (Dario Amodei, Daniela Amodei, Yasmin Razavi, Reed Hastings, Chris Liddell, Vas Narasimhan). Search snippets claimed 'for now, it has the authority to elect three board members' but I could not verify that in a primary source. (4) LTBT composition: Anthropic's company page and Stubbs post list four trustees (Bernanke, Fontaine, Shah, Stubbs); Fortune and the Harvard Crimson say Cuéllar left the Trust in August 2026 to become Anthropic's first chief global affairs officer and one seat remains vacant; the LTBT page footnotes I retrieved did not mention his departure. (5) LTBT role in the Fund: the Oct 18 announcement does not mention the LTBT; Fortune explicitly says the fund 'is separate from the Trust'; the only stated LTBT connection is its endorsement of the 5% set-aside in the Public Benefit Report closing commentary and its statement that it helped develop the five charter pillars. Governance of the Fund itself is still to be published 'in the coming months'. (6) Economic Futures Research Fund timing: AP dates the $200M pledge June 10, 2026 (some aggregators say June 11); the agenda with grant sizes ($5-30M, $1M floor) was published July 22, 2026; Anthropic's Transparency Hub says 'June 2026'. The original Economic Futures Program launched June 27, 2025. (7) Claude Corps: the June 11, 2026 post gives cohort months (Oct 2026, Mar 2027, Aug 2027); the FAQ gives exact dates (Oct 19, 2026; Mar 8, 2027; Aug 2027) and the $10,000 host grant, which the news post does not mention. (8) Economic Index Jan 2026 figures (52%/45%) come only from a search summary, not a direct fetch. (9) Valuation-based dollar figures for the 5% stake ($48B, $75B, $7.2B, ~$100B) and for the cofounders' wealth ($3.7B each; $7B each / $39.2B total) are third-party estimates; Anthropic discloses none of them. (10) Fetch failures: CNBC (Oct 18) and Forbes (Oct 19 and Feb 12) returned 403; US News (Reuters factbox and AP June story) returned 503 and were replaced by The Star and WTOP copies; Inside Philanthropy's page returned no content; Anthropic's economic-index landing page returned only 'Loading data'. (11) 'Machines of Loving Grace' contains no taxation or redistribution language; the taxation argument (progressive taxation, possibly targeted at AI companies) appears in 'The Adolescence of Technology' (Jan 2026) and the June 2026 AP report of Amodei's 'Policy on the AI Exponential' essay (UBI funded by taxes on 'relevant companies' or higher capital gains tax). (12) Delaware §362/§365/§366 quotes were extracted by the fetch tool in fragments; wording is faithful to the statute but the fetch truncated sentences.


## Механизм фонда (5%, 2%, LLC, 20%) / mechanism-deep (49)

### F226 🟢 Первоисточник

Anthropic's announcement states the 5% commitment is conditional on a stockholder vote and uses the word 'committed' (not 'transferred' or 'issued'): 5% 'will be committed today', with a discretionary 2% add-on per 50% valuation increase above a set baseline.

- Source: Anthropic, 2026-10-18 — <https://www.anthropic.com/news/public-benefit-fund> (confidence as rated by researcher: primary)
- Quote: «Subject to stockholder approval, 5% of Anthropic's shares will be committed today, with an additional 2% added at the board's discretion for every 50% increase in the company's value above a set baseline.»

### F227 🟢 Первоисточник

Anthropic describes the Fund as a wholly owned entity whose stake grows with the company; the announcement does not say whether the 5% will be newly issued shares, treasury/existing shares, or how the transfer will be executed, and does not explain why stockholder approval is required.

- Source: Anthropic, 2026-10-18 — <https://www.anthropic.com/news/public-benefit-fund> (confidence as rated by researcher: primary)
- Quote: «Today, we're committing a portion of Anthropic's shares to the Anthropic Public Benefit Fund, a new wholly owned entity with a structure that increases the stake as the company grows.»

### F228 🟢 Первоисточник

In its X post on the announcement, Anthropic phrased the ratchet as 'up to an extra 2%' per 50% increase, subject to board discretion, i.e. 2% is a ceiling per milestone, not an automatic amount.

- Source: Anthropic (X/@AnthropicAI), 2026-10-18 — <https://x.com/AnthropicAI/status/2111881963657412903> (confidence as rated by researcher: primary)
- Quote: «It will start off with 5% of our shares. For every 50% increase in the company's value over a set baseline, we can contribute up to an extra 2%, subject to our board's discretion.»

### F229 🟢 Первоисточник

Anthropic's X post states the combined figure as 'roughly 20%' and attributes it to the Fund plus the co-founders' 80% pledge plus a donation-matching program in which 'around half' of employees participate; no numerical breakdown is given.

- Source: Anthropic (X/@AnthropicAI), 2026-10-18 — <https://x.com/AnthropicAI/status/2111881963657412903> (confidence as rated by researcher: primary)
- Quote: «In total, this means that roughly 20% of Anthropic's shares are committed to the public good. Our co-founders have already pledged to donate 80% of their equity, and around half our employees are donating a portion of their equity as part of a donation matching program we've run since our founding.»

### F230 🟢 Первоисточник

Anthropic frames the valuation-linked additions as equity redirected from what would otherwise be escalating executive compensation awards.

- Source: Anthropic, 2026-10-18 — <https://www.anthropic.com/news/public-benefit-fund> (confidence as rated by researcher: primary)
- Quote: «It is common practice for tech companies to offer escalating compensation awards to their executives. We are instead directing that equity to the public benefit.»

### F231 🟢 Первоисточник

Anthropic's stated reason for choosing an LLC over a 501(c)(3) is 'adjustability between different forms of giving', paired with a pledge that none of the equity held by the LLC will fund lobbying or political giving in the US or abroad.

- Source: Anthropic, 2026-10-18 — <https://www.anthropic.com/news/public-benefit-fund> (confidence as rated by researcher: primary)
- Quote: «We're establishing the Anthropic Public Benefit Fund as an LLC—rather than a 501(c)(3) or other format—to give adjustability between different forms of giving. None of the Anthropic equity held by the LLC will be used for lobbying or political giving, in the US or abroad.»

### F232 🟢 Первоисточник

Anthropic names two possible uses enabled by the LLC's flexibility: large donations to traditional nonprofits, or direct distributions to specific populations.

- Source: Anthropic, 2026-10-18 — <https://www.anthropic.com/news/public-benefit-fund> (confidence as rated by researcher: primary)
- Quote: «The Anthropic Public Benefit Fund will have increased flexibility and scale, enabling us to pursue our mission in new ways: for example, we might explore large donations to traditional nonprofits or direct distributions to specific populations.»

### F233 🟢 Первоисточник

Anthropic's announcement describes the co-founders' 80% pledge and the employee equity-match program and says 'roughly 20%' of shares 'will be dedicated to the public good' when combined with the new 5%; 'approximately half' of employees participate in the match.

- Source: Anthropic, 2026-10-18 — <https://www.anthropic.com/news/public-benefit-fund> (confidence as rated by researcher: primary)
- Quote: «When Anthropic was founded, our co-founders pledged to donate 80% of their equity holdings, and since founding we have also operated an equity donation match program that allows employees to pledge equity which Anthropic matches. Approximately half of our employees participate in this program. When combined with today's announcement, roughly 20% of Anthropic shares will be dedicated to the public good, plus any additional percentage that could be added if the company reaches specific valuation milestones.»

### F234 🟢 Первоисточник

Governance, control and the valuation milestones are explicitly deferred: Anthropic promises details on structure and governance 'in the coming months' and a public benefit report; the announcement says nothing about who manages the LLC or whether/how the Fund's shares vote.

- Source: Anthropic, 2026-10-18 — <https://www.anthropic.com/news/public-benefit-fund> (confidence as rated by researcher: primary)
- Quote: «In the coming months, we will share more about the Anthropic Public Benefit Fund's structure and governance, including the valuation milestones that may add to its stake. We will also report on our progress to date against our mission in an upcoming public benefit report.»

### F235 🟢 Первоисточник

The announcement cites labor-market impacts as an example use and says Anthropic 'has already committed $200 million' to studying and addressing the issue.

- Source: Anthropic, 2026-10-18 — <https://www.anthropic.com/news/public-benefit-fund> (confidence as rated by researcher: primary)
- Quote: «AI may generate enormous economic value, but it could also cause instability for many workers. Anthropic has already committed $200 million to studying and addressing this issue, but given the pace of AI progress, bolder approaches may be needed. The Fund will have the versatility to pursue them.»

### F236 🟢 Первоисточник

The $200 million figure refers to Anthropic's Economic Futures Research Fund, whose research agenda (published July 22, 2026) commits $200 million to external research with priorities including 'Modernizing income support for AI-driven displacement' and 'Building worker stakes in AI-driven growth before disruption arrives'.

- Source: Anthropic, 2026-07-22 — <https://www.anthropic.com/news/economic-futures-research-fund-agenda> (confidence as rated by researcher: primary)
- Quote: «We're committing $200 million to the fund to support ambitious external research»

### F237 🟢 Первоисточник

Anthropic's first Public Benefit Report (PDF metadata creation date Oct 21, 2026) describes the commitment as 'setting aside at least 5%' of shares (note 'at least'), and frames the 20% as a hope ('we hope that about 20%'), signed by Daniela Amodei as Co-Founder, President and Chair of the Board.

- Source: Anthropic (2026 Public Benefit Report, PDF), 2026-10-21 — <https://www-cdn.anthropic.com/a9ceec76a54d28d27affffcdab6faf7c142cd587.pdf> (confidence as rated by researcher: primary)
- Quote: «We announced that, subject to stockholder approval, we are setting aside at least 5% of our shares to fund projects in pursuit of our public benefit charter. Between this set-aside, each of our co-founders' commitment to pledge 80% of their equity to philanthropy, and matched equity-donation pledges from employees, we hope that about 20% of Anthropic shares will be put toward the public good.»

### F238 🟢 Первоисточник

The Long-Term Benefit Trust's closing commentary in the Public Benefit Report (signed by Buddy Shah) describes the Fund as 'a separate entity dedicated entirely to the public benefit charter' and repeats 'at least 5%' and the stockholder condition.

- Source: Anthropic (2026 Public Benefit Report, PDF), 2026-10-21 — <https://www-cdn.anthropic.com/a9ceec76a54d28d27affffcdab6faf7c142cd587.pdf> (confidence as rated by researcher: primary)
- Quote: «If stockholders agree, Anthropic is planning to set aside at least 5% of the company's shares in a separate entity dedicated entirely to the public benefit charter. It is a significant step.»

### F239 🟢 Первоисточник

Anthropic's Oct 21, 2026 post on Christopher Stubbs joining the Long-Term Benefit Trust confirms the Public Benefit Report was published that week, states the LTBT 'has the authority to appoint a majority of Anthropic's board', and repeats that the Fund set-aside is 'Subject to stockholder approval'.

- Source: Anthropic, 2026-10-21 — <https://www.anthropic.com/news/christopher-stubbs-joins-long-term-benefit-trust> (confidence as rated by researcher: primary)
- Quote: «Subject to stockholder approval, we've also committed to setting aside a portion of Anthropic's shares to Anthropic Public Benefit Fund, a new entity with a structure that increases the stake as the company grows.»

### F240 🟡 Крупное СМИ

Reuters (Oct 18, 2026) reported the commitment as conditional on stockholder approval and the fund's stake as potentially increasing with valuation.

- Source: Reuters (via Investing.com), 2026-10-18 — <https://www.investing.com/news/stock-market-news/anthropic-to-commit-5-stake-to-new-public-benefit-fund-4956031> (confidence as rated by researcher: major_outlet)
- Quote: «will commit 5% of its shares to a new public benefit fund, subject to stockholder approval»

### F241 🟡 Крупное СМИ

Reuters (Oct 19, 2026; Deborah Mary Sophia, Abu Sultan) reported the fund 'would be established as a wholly owned limited liability company', that the additional 2% is 'at the board's discretion' above 'a baseline that has yet to be disclosed', and that Anthropic 'would say more soon on the fund's governance, structure and the valuation thresholds'; Reuters' own calculation valued a 5% stake at $75–100 billion using IPO valuation scenarios of ~$1.5–2 trillion.

- Source: Reuters (via Central Oregon Daily), 2026-10-19 — <https://www.centraloregondaily.com/news/consumer/anthropic-to-commit-5-stake-to-new-public-benefit-fund/article_d8ba77f8-ebc7-552b-93c2-7013bef37292.html> (confidence as rated by researcher: major_outlet)
- Quote: «an additional 2% of Anthropic's shares, at the board's discretion»

### F242 🟡 Крупное СМИ

Reuters' factbox (Oct 20, 2026, Pragyan Kalita) compares the Fund with the OpenAI Foundation: OpenAI's October 2025 restructuring left the nonprofit with a 26% stake in the for-profit worth about $130 billion at the time, plus a warrant for additional equity if OpenAI Group's share price rises more than tenfold over 15 years, and an initial $25 billion commitment to health/curing diseases and AI resilience. The factbox does not mention the Chan Zuckerberg Initiative and quotes no outside experts.

- Source: Reuters (via The Star Malaysia), 2026-10-20 — <https://www.thestar.com.my/tech/tech-news/2026/10/21/factbox-anthropic039s-public-benefit-fund-and-how-it-compares-with-other-big-philanthropic-efforts> (confidence as rated by researcher: major_outlet)
- Quote: «wholly owned limited liability company»

### F243 🟡 Крупное СМИ

AP (Oct 20, 2026; James Pollard and Wyatte Grantham-Philips) reports that an LLC is not bound by the private-foundation minimum distribution rule, citing experts: foundations must distribute at least 5% of endowment value annually.

- Source: Associated Press (via The Business Journal), 2026-10-20 — <https://thebusinessjournal.com/anthropic-openai-share-ai-wealth-public-benefit-funds/> (confidence as rated by researcher: major_outlet)
- Quote: «The structure offers more control for its owners, experts say. An LLC is not bound by the same spending rules as a foundation, which is required to distribute at least 5% of the value of its endowment.»

### F244 🟡 Крупное СМИ

Katherina Rosqueta, founding executive director of the University of Pennsylvania's Center for High Impact Philanthropy, told AP the LLC gives Anthropic more latitude over the fund's resources.

- Source: Associated Press (via The Business Journal), 2026-10-20 — <https://thebusinessjournal.com/anthropic-openai-share-ai-wealth-public-benefit-funds/> (confidence as rated by researcher: major_outlet)
- Quote: «They have a lot more flexibility and latitude in how to use the resources they put into the fund,»

### F245 🟡 Крупное СМИ

Brian Mittendorf, chair in accounting at Ohio State University, told AP that LLCs permit activity outside 'traditional philanthropy', such as payouts to individuals not possible through a 501(c)(3) charity, but that non-charitable giving puts companies in a 'gray area' about how the public benefits; he called the announcement a commitment to 'yet-to-be-specified wider goals' that 'reflects more of an intention to do things in the future rather than an act now'.

- Source: Associated Press (via The Business Journal), 2026-10-20 — <https://thebusinessjournal.com/anthropic-openai-share-ai-wealth-public-benefit-funds/> (confidence as rated by researcher: major_outlet)
- Quote: «Brian Mittendorf, the chair in accounting at Ohio State University, said LLCs allow for activity outside "traditional philanthropy," such as payouts to individuals that would not be possible through a 501(c)3 charity.»

### F246 🟡 Крупное СМИ

On tax consequences, AP (citing Rosqueta and Mittendorf) reports that Anthropic's pledge does not immediately trigger a tax write-off and that a deduction can be claimed only once donated shares are moved to a public charity; LLCs also face less transparency requirements.

- Source: Associated Press (via The Business Journal), 2026-10-20 — <https://thebusinessjournal.com/anthropic-openai-share-ai-wealth-public-benefit-funds/> (confidence as rated by researcher: major_outlet)
- Quote: «Anthropic's pledge doesn't immediately trigger a tax write-off, and the company can only claim a deduction once the donated shares are moved to a public charity. There's also less transparency required of LLCs.»

### F247 🟡 Крупное СМИ

Jay R. Ritter, director of the IPO Initiative at the University of Florida's Warrington College of Business, told AP that once public, donations could be made by selling shares or potentially via future cash dividends; specifics of how the Fund will donate are not yet clear, but the pre-IPO disclosure helps investors 'know what they're buying'.

- Source: Associated Press (via The Business Journal), 2026-10-20 — <https://thebusinessjournal.com/anthropic-openai-share-ai-wealth-public-benefit-funds/> (confidence as rated by researcher: major_outlet)
- Quote: «Once a company is public, donations might be made through the selling of future shares, or potentially turning to cash dividends in the future, explained Jay R. Ritter»

### F248 🟡 Крупное СМИ

Phil Buchanan, president of The Center for Effective Philanthropy, welcomed the commitment but said it is 'hard to talk about any of this because it's all so abstract' and warned against the 'arrogance' of earlier tech barons.

- Source: Associated Press (via The Business Journal), 2026-10-20 — <https://thebusinessjournal.com/anthropic-openai-share-ai-wealth-public-benefit-funds/> (confidence as rated by researcher: major_outlet)
- Quote: «"I guess I'm hopeful," Buchanan said, "but I'm not going to get too excited until I see some evidence of what's actually happening."»

### F249 🟡 Крупное СМИ

AP describes the Fund as 'a new entity within the company' whose 5% commitment is 'pending approval from stockholders', and notes Anthropic shared little about recipient organizations.

- Source: Associated Press (via The Business Journal), 2026-10-20 — <https://thebusinessjournal.com/anthropic-openai-share-ai-wealth-public-benefit-funds/> (confidence as rated by researcher: major_outlet)
- Quote: «On Sunday, Anthropic said it would commit 5% of its shares to the Anthropic Public Benefit Fund, a new entity within the company, pending approval from stockholders.»

### F250 🟡 Крупное СМИ

The San Francisco Standard (Rachyl Jones, Oct 20, 2026) reports that, as an LLC, the Fund is not legally required to disclose executive pay, board membership, strategy, goals or decision-making, and that LLC philanthropies may legally fund lobbying and campaigns though Anthropic has said it will not.

- Source: The San Francisco Standard, 2026-10-20 — <https://sfstandard.com/2026/10/20/anthropic-musk-philanthropy/> (confidence as rated by researcher: major_outlet)
- Quote: «Anthropic's fund isn't legally required to disclose how much executives are paid, who sits on the board, its strategy, goals, or how it makes decisions. LLC philanthropies are allowed to use money for lobbying and political campaigns, though Anthropic said it wouldn't use it that way.»

### F251 🟡 Крупное СМИ

SF Standard contrasts the Fund with the Chan Zuckerberg Initiative: CZI popularized the philanthropic-LLC structure a decade ago but was overseen by the couple, whereas Anthropic's LLC 'will be part of the company'.

- Source: The San Francisco Standard, 2026-10-20 — <https://sfstandard.com/2026/10/20/anthropic-musk-philanthropy/> (confidence as rated by researcher: major_outlet)
- Quote: «The Chan Zuckerberg Initiative, led by Mark Zuckerberg and his wife, popularized the structure a decade ago. That organization, however, was overseen by the couple, while Anthropic's will be part of the company.»

### F252 🟡 Крупное СМИ

SF Standard describes OpenAI's structure as the inverse of Anthropic's: the philanthropic foundation oversees the for-profit, with a small separate staff but nearly identical boards.

- Source: The San Francisco Standard, 2026-10-20 — <https://sfstandard.com/2026/10/20/anthropic-musk-philanthropy/> (confidence as rated by researcher: major_outlet)
- Quote: «OpenAI's structure is the inverse of Anthropic's, with the philanthropic foundation overseeing the for-profit arm of the company. The foundation has a small staff separate from the company, but board members for the two entities are nearly identical.»

### F253 🟡 Крупное СМИ

Priya Shanker, executive director of Stanford's Center on Philanthropy and Civil Society, recommended a separate board and governance structure for the Fund for legitimacy; Anthropic has not disclosed how the fund will be governed.

- Source: The San Francisco Standard, 2026-10-20 — <https://sfstandard.com/2026/10/20/anthropic-musk-philanthropy/> (confidence as rated by researcher: major_outlet)
- Quote: «"It would behoove [Anthropic] to have a separate board and separate governance structure," said Priya Shanker, executive director of Stanford University's Center on Philanthropy and Civil Society. "It would give it a lot more legitimacy."»

### F254 🟡 Крупное СМИ

Jacob Harold, former CEO of GuideStar, said Anthropic is giving itself 'a whole lot of strategic flexibility' by not saying how it will spend the money.

- Source: The San Francisco Standard, 2026-10-20 — <https://sfstandard.com/2026/10/20/anthropic-musk-philanthropy/> (confidence as rated by researcher: major_outlet)
- Quote: «"They're kind of doing that preemptively here, and they're giving themselves a whole lot of strategic flexibility, because they're not saying how they're going to spend it."»

### F255 🟠 Вторичный источник

Inside Philanthropy (Mike Scutari, Oct 22, 2026) states that LLCs are not subject to the IRS 5% minimum payout requirement and, unlike private foundations, need not publicly disclose recipients; it also notes that the OpenAI Foundation is a public charity, not a private foundation subject to the 5% payout rule.

- Source: Inside Philanthropy, 2026-10-22 — <https://www.insidephilanthropy.com/home/copy-2> (confidence as rated by researcher: secondary)
- Quote: «For one thing, LLCs are not required to meet the IRS 5% minimum payout requirement.»

### F256 🟠 Вторичный источник

Inside Philanthropy highlights that, as an LLC, the Fund can make cash gifts directly to individuals, and that LLCs let funders combine charitable, political and for-profit activity in one entity (as used by Zuckerberg/Chan, the Arnolds, Melinda French Gates, Laurene Powell Jobs).

- Source: Inside Philanthropy, 2026-10-22 — <https://www.insidephilanthropy.com/home/copy-2> (confidence as rated by researcher: secondary)
- Quote: «the most intriguing element of the Anthropic Public Benefit Fund is how, as an LLC, it can pull a page from the effective altruism playbook and make cash gifts to individuals.»

### F257 🟠 Вторичный источник

Inside Philanthropy raises the governance question of who will oversee the Fund, noting the OpenAI Foundation criticism that its nonprofit and for-profit boards are nearly identical, and asks whether Anthropic's fund will have 'wholly independent leadership'.

- Source: Inside Philanthropy, 2026-10-22 — <https://www.insidephilanthropy.com/home/copy-2> (confidence as rated by researcher: secondary)
- Quote: «One of the big knocks against the OpenAI Foundation is that its governance structure hardwires in conflicts of interest because the OpenAI Foundation nonprofit board and the OpenAI Group PBC for-profit board are nearly identical.»

### F258 🟠 Вторичный источник

Priya Shanker (Stanford PACS) told Inside Philanthropy that staying out of political funding 'is a sensible choice and may give the effort more credibility'; Mike Wang (Building Impact Partners) said transparency 'becomes the donor's choice' under an LLC and urged Anthropic 'to commit to a minimum pace of giving and to public reporting'.

- Source: Inside Philanthropy, 2026-10-22 — <https://www.insidephilanthropy.com/home/copy-2> (confidence as rated by researcher: secondary)
- Quote: «"It's not particularly uncommon for deep-pocketed donors to use a model [LLC] like this, but it becomes the donor's choice to be transparent," Wang said.»

### F259 🟠 Вторичный источник

Inside Philanthropy estimates the Fund's stock could be worth $100 billion if stockholders approve and Anthropic IPOs at a $2 trillion valuation, and recalls the OpenAI Foundation's $130 billion stake; these are the outlet's calculations, not Anthropic figures.

- Source: Inside Philanthropy, 2026-10-22 — <https://www.insidephilanthropy.com/home/copy-2> (confidence as rated by researcher: secondary)
- Quote: «Assuming Anthropic stockholders approve the plan and the company goes public at a $2 trillion valuation, the Anthropic Public Benefit Fund's stock could be worth $100 billion.»

### F260 🟠 Вторичный источник

Inside Philanthropy's explainer on philanthropic LLCs: contributions to an LLC are not tax-deductible and the LLC is not tax-exempt; LLCs have no payout requirements; they need not publish tax returns; they may fund lobbying, campaigns and candidates; and may make non-deductible gifts to individuals.

- Source: Inside Philanthropy, 2025-04-16 — <https://www.insidephilanthropy.com/explainers/what-is-a-philanthropic-llc> (confidence as rated by researcher: secondary)
- Quote: «the money a funder puts into a philanthropic LLC is not tax-deductible, and the LLC is not tax-exempt.»

### F261 🟡 Крупное СМИ

Forbes (Siladitya Ray, Oct 19, 2026) notes the announcement 'didn't include specifics on the fund's full governance structure' and that its ~$100 billion estimate at a $2 trillion IPO 'assumes the fund retains a 5% stake in Anthropic at the time of its IPO' 'without accounting for potential dilution from newly issued shares'; Forbes also says it is 'unclear how the IPO timing would affect the fund's establishment'.

- Source: Forbes (via Yahoo Finance), 2026-10-19 — <https://finance.yahoo.com/technology/ai/articles/anthropic-pledges-5-shares-public-072152314.html> (confidence as rated by researcher: major_outlet)
- Quote: «without accounting for potential dilution from newly issued shares»

### F262 🟠 Вторичный источник

24/7 Wall St (Oct 20, 2026) states Anthropic has not said whether the fund's equity will come from new shares or existing holders, and asserts that 'Anthropic's board still decides where the money goes and how much gets donated' (the outlet's characterization; Anthropic has not published governance).

- Source: 24/7 Wall St (via Yahoo Finance), 2026-10-20 — <https://finance.yahoo.com/markets/stocks/articles/anthropic-sets-aside-5-stake-114524150.html> (confidence as rated by researcher: secondary)
- Quote: «Anthropic has not said whether the added equity will come from new shares or from existing holders»

### F263 🟠 Вторичный источник

Mixed News (Oct 20, 2026) characterizes the 5% as a commitment rather than a transfer until stockholders approve, and notes Anthropic publishes no valuation and no baseline for the 50% steps and does not say whether increments are cumulative.

- Source: Mixed News, 2026-10-20 — <https://mixed-news.com/en/anthropic-public-benefit-fund-5-percent-equity-stockholder-approval/> (confidence as rated by researcher: secondary)
- Quote: «Until stockholders approve it, the 5% is a commitment rather than a transfer.»

### F264 🟡 Крупное СМИ

Business Insider (Yahoo syndication) reports a 5% stake 'is worth about $48 billion, according to the company's most recent valuation in May' and describes the LLC as having the company's stock as its sole asset.

- Source: Business Insider (via Yahoo Finance), 2026-10-18 — <https://finance.yahoo.com/technology/ai/articles/anthropic-commits-billions-public-benefit-184601337.html> (confidence as rated by researcher: major_outlet)
- Quote: «A 5% stake in Anthropic is worth about $48 billion, according to the company's most recent valuation in May.»

### F265 🟡 Крупное СМИ

Business Insider (Tracy Connor, Tom Carter, Oct 19, 2026) compiled reactions: David Sacks (former White House AI czar) replied to Anthropic co-founder Jack Clark's 20% claim: 'You've put 20% of your equity in an LLC. Whether it serves the public good remains to be seen.'; Gary Marcus: 'Trying to curry public favor while still holding control and resisting disclosure is annoying.'; Sam Hogan Heutmaker called it 'the reverse OpenAI'; Will Brown (Prime Intellect) said the entity is 'incentivized to protect the value the stock'.

- Source: Business Insider (via Yahoo Finance), 2026-10-19 — <https://finance.yahoo.com/technology/ai/articles/smart-people-saying-anthropics-5-043641796.html> (confidence as rated by researcher: major_outlet)
- Quote: «You've put 20% of your equity in an LLC. Whether it serves the public good remains to be seen.»

### F266 🟡 Крупное СМИ

Reuters exclusive (Echo Wang, Ross Kerber, Jeffrey Dastin, Sept 28, 2026) on Anthropic's IPO filing: a 'Founder LLC' of the seven co-founders will direct a single Class F share carrying 50.1% of total voting power on key corporate matters; Class F and Class A holders elect three board seats (Dario Amodei, Daniela Amodei, one unnamed) while the Long-Term Benefit Trust elects the remaining four; the co-founders pledged to dedicate 80% of their personal Anthropic equity to charitable causes; Anthropic remains a Delaware PBC. This filing predates the Fund and does not describe it.

- Source: Reuters (via The Star Malaysia), 2026-09-28 — <https://www.thestar.com.my/tech/tech-news/2026/09/29/exclusive-anthropic-leaders-to-control-ai-lab-via-039founder-llc039-to-promote-public-good-over-market-forces> (confidence as rated by researcher: major_outlet)
- Quote: «a single share of Class F stock that amounts to 50.1% of the total voting power over key corporate matters»

### F267 🟡 Крупное СМИ

TechCrunch (Connie Loizos, Sept 25, 2026), citing The Information, reports the co-founders 'reportedly own just 2% of the company apiece, Amodei included', that the LTBT 'would still choose most of the board', and that the co-founders 'have pledged to give away 80% of their wealth'.

- Source: TechCrunch, 2026-09-25 — <https://techcrunch.com/2026/09/25/anthropics-founders-seek-voting-control-ahead-of-ipo/> (confidence as rated by researcher: major_outlet)
- Quote: «reportedly own just 2% of the company apiece, Amodei included.»

### F268 🟠 Вторичный источник

Benzinga (Sept 30, 2026) reports, citing the IPO filing, that CEO Dario Amodei, President Daniela Amodei and the five other co-founders 'have pledged to donate 80% of their personal equity in the company to charitable causes'.

- Source: Benzinga (via Yahoo Finance), 2026-09-30 — <https://finance.yahoo.com/technology/ai/articles/anthropic-founders-reportedly-pledge-away-173019234.html> (confidence as rated by researcher: secondary)
- Quote: «have pledged to donate 80% of their personal equity in the company to charitable causes, according to its IPO filing»

### F269 🟠 Вторичный источник

Forkast News (Lena Park, Sept 29, 2026) reports Anthropic's prospectus 'has not yet appeared on the SEC's EDGAR database' and that the company made a confidential filing on June 1, 2026; an SEC EDGAR full-text search for 'Anthropic Public Benefit Fund' on Oct 24, 2026 returned zero hits (my own check).

- Source: Forkast News (via Yahoo Finance), 2026-09-29 — <https://finance.yahoo.com/technology/ai/articles/anthropic-1-518-billion-commitment-165731037.html> (confidence as rated by researcher: secondary)
- Quote: «has not yet appeared on the SEC's EDGAR database»

### F270 🟡 Крупное СМИ

Chan Zuckerberg Initiative precedent (Fortune, Kia Kokalitcheva, Dec 3, 2015): Zuckerberg explained the LLC lets CZI fund nonprofits, make private investments and participate in policy debates; he and Chan receive no tax benefit from transferring shares to the LLC; the pledge was 99% of their Facebook shares, about $45 billion over time.

- Source: Fortune, 2015-12-03 — <https://fortune.com/2015/12/03/zuckerberg-foundation-llc/> (confidence as rated by researcher: major_outlet)
- Quote: «funding non-profit organizations, making private investments and participating in policy debates»

### F271 🟠 Вторичный источник

Nonprofit Quarterly (Martin Levine, Dec 7, 2015) on the CZI LLC: foundations must spend at least 5% of endowment annually while 'The LLC is under no such obligation' (Jack Blum); LLC records 'are completely private'; the LLC can engage in politics while a regulated nonprofit cannot without limits; the structure offers 'more control'.

- Source: Nonprofit Quarterly, 2015-12-07 — <https://nonprofitquarterly.org/chan-zuckerberg-llc-are-no-tax-breaks-plus-no-accountability-good-for-the-public/> (confidence as rated by researcher: secondary)
- Quote: «The records of an LLC are completely private.»

### F272 🟠 Вторичный источник

OpenAI Foundation comparison (Wikipedia): on October 28, 2025 OpenAI adopted the PBC structure after approval from the California and Delaware attorneys general; the OpenAI Foundation holds about 26% of OpenAI Group PBC and appoints all of its board members, 'which can remove them at any time'.

- Source: Wikipedia, 2026-10-24 — <https://en.wikipedia.org/wiki/OpenAI> (confidence as rated by researcher: secondary)
- Quote: «after receiving approval from the attorneys general of California and Delaware»

### F273 🟡 Крупное СМИ

Al Jazeera (Oct 19, 2026) interpreted 'committed today' as committing 5 percent 'with immediate effect, subject to stockholder approval', and noted Anthropic is registered as a Delaware public benefit corporation.

- Source: Al Jazeera, 2026-10-19 — <https://www.aljazeera.com/economy/2026/10/19/anthropic-says-it-will-commit-5-of-shares-to-public-benefit-fund> (confidence as rated by researcher: major_outlet)
- Quote: «Anthropic said it was committing 5 percent of company shares with immediate effect, subject to stockholder approval, with an additional 2 percent to be added "at the board's discretion" for every 50 percent increase in the company's value.»

### F274 🟡 Крупное СМИ

TechCrunch (Anthony Ha, Oct 18, 2026) notes Anthropic has not said who will decide which public benefits get funded and quotes CEO Dario Amodei's earlier description of AI backlash as 'fundamentally a crisis of trust'.

- Source: TechCrunch, 2026-10-18 — <https://techcrunch.com/2026/10/18/anthropic-says-its-committing-5-of-its-shares-to-a-public-benefit-fund/> (confidence as rated by researcher: major_outlet)
- Quote: «fundamentally a crisis of trust»

Researcher notes: WHAT IS KNOWN VS UNKNOWN, BY ANGLE.

(1) 5%: transfer, issuance, or commitment? Anthropic's wording is 'committed today', 'subject to stockholder approval'; the Public Benefit Report and LTBT commentary use 'setting aside at least 5%' and 'If stockholders agree'. No Anthropic document or press report states whether the shares will be newly issued (dilutive to all holders) or existing/treasury shares, who the counterparty is, or the legal form of the transfer. Forbes and 24/7 Wall St explicitly flag this as undisclosed. No source explains WHY stockholder approval is required (e.g., charter amendment, share issuance authorization, related-party transfer) — this is UNKNOWN; I did not find Delaware-law analysis in any outlet. The stockholder vote's timing and whether it is tied to the IPO are also unknown; Forbes says it is 'unclear how the IPO timing would affect the fund's establishment'. Note a wording drift: announcement says '5%', while the Oct 21 Public Benefit Report and Stubbs post say 'at least 5%'.

(2) Ratchet: Anthropic's X post says 'up to an extra 2%, subject to our board's discretion' per 50% increase 'over a set baseline' — so each step is discretionary and 2% is a ceiling per step, not automatic. The baseline is undisclosed (Reuters: 'a baseline that has yet to be disclosed'); Anthropic says the 'valuation milestones' will be published 'in the coming months'. Whether steps are cumulative/compounding (50% over baseline, then 50% over that, etc.), whether there is a cap, and how 'company's value' is measured (private round vs. public market cap) are NOT stated anywhere. The announcement's plural 'specific valuation milestones' implies multiple steps but nothing more.

(3) LLC vs 501(c)(3): Anthropic's only stated reason is 'adjustability between different forms of giving' plus a voluntary no-lobbying/no-political-giving pledge. Experts quoted in press (AP: Rosqueta/UPenn, Mittendorf/Ohio State, Ritter/UF, Buchanan/CEP; SF Standard: Harold/ex-GuideStar, Shanker/Stanford PACS; Inside Philanthropy: Shanker, Mike Wang/Building Impact Partners) and IP's explainer converge on: no immediate tax deduction (deduction only when shares move to a public charity); no 5% minimum payout; no public Form 990-type disclosure of recipients, pay, board or strategy; legal ability to make direct cash gifts to individuals (not possible via a 501(c)(3)); legal ability to lobby/donate politically (which Anthropic has disclaimed). I found NO coverage in Chronicle of Philanthropy or Nonprofit Quarterly about the Anthropic fund specifically (NQ sources used are 2015 CZI pieces). Comparison: CZI (LLC, Dec 2015, 99% of FB shares ≈ $45B, controlled by the couple) vs Anthropic's LLC which is wholly owned by the company itself — SF Standard and IP stress this is the novel element. OpenAI Foundation is a public charity (not a private foundation; IP) holding ~26% of OpenAI Group PBC (~$130B at Oct 2025) and appointing/removing the PBC board — the 'inverse' of Anthropic where the company owns the charitable vehicle.

(4) Composition of ~20%: Anthropic gives NO breakdown. Components named: 5% Fund; co-founders' pledge of 80% of their personal equity (7 co-founders per Reuters/IPO filing; Forbes says 'six cofounders', AP says 'Dario Amodei and five other cofounders' — the count varies by outlet; Anthropic's post does not number them); employee pledges under the match program (~half of employees) plus Anthropic's match. The Public Benefit Report softens the figure to 'we hope that about 20%'. SPECULATIVE arithmetic (mine, not from any source): if each of 7 co-founders holds ~2% (The Information via TechCrunch, 'reportedly'), 80% of ~14% ≈ 11%; plus 5% Fund ≈ 16%; implying roughly 4% from employee pledges plus company match — but Anthropic has not confirmed any of these inputs, and it is unknown whether the co-founder/employee pledges are routed through the new LLC or given separately (Sacks' '20% of your equity in an LLC' conflates them). Whether the company match shares count toward the 5% or are additional is also unknown.

(5) Control and voting: Anthropic says only that the Fund is 'a new wholly owned entity'/'wholly owned LLC'; it has not named managers, a board, or an independent governance body, and has said nothing about whether the Fund's Anthropic shares carry votes or how they would be voted. No press source answers this; 24/7 Wall St's 'Anthropic's board still decides' is the outlet's inference. Context on company-level control from the IPO filing (Reuters Sept 28): a Founder LLC of the seven co-founders directs a Class F share with 50.1% voting power; LTBT elects 4 of 7 directors (and the Stubbs post confirms LTBT can appoint a board majority). The relationship between the Fund, the Founder LLC, and the LTBT is not described anywhere.

VALUE FIGURES are all third-party calculations: ~$48B (BI, May valuation), $75–100B (Reuters, at $1.5–2T IPO), ~$100B (IP/Forbes, at $2T). Anthropic gave no dollar figure.

ACCESS NOTES: CNBC, Forbes (direct), Axios, Fast Company, Bloomberg and AP-via-US News returned 403/503; I used Yahoo/Investing.com/The Star/Business Journal/Central Oregon Daily syndications. Inside Philanthropy was retrievable only with a Googlebot user-agent. SEC EDGAR full-text search for 'Anthropic Public Benefit Fund' returned 0 hits on Oct 24, 2026, consistent with the S-1 not yet being public.


## Русскоязычное и иноязычное освещение / russian-coverage (46)

### F275 🟢 Первоисточник

Anthropic announced on 2026-10-18 that, subject to stockholder approval, 5% of its shares will be committed to the Anthropic Public Benefit Fund, a new wholly owned entity, with an additional 2% added at the board's discretion for every 50% increase in company value above a set (undisclosed) baseline.

- Source: Anthropic, 2026-10-18 — <https://www.anthropic.com/news/public-benefit-fund> (confidence as rated by researcher: primary)
- Quote: «Subject to stockholder approval, 5% of Anthropic's shares will be committed today, with an additional 2% added at the board's discretion for every 50% increase in the company's value above a set baseline.»

### F276 🟢 Первоисточник

The Fund is being set up as an LLC rather than a 501(c)(3) 'to give adjustability between different forms of giving'; none of the equity held by the LLC will be used for lobbying or political giving in the US or abroad.

- Source: Anthropic, 2026-10-18 — <https://www.anthropic.com/news/public-benefit-fund> (confidence as rated by researcher: primary)
- Quote: «We're establishing the Anthropic Public Benefit Fund as an LLC—rather than a 501(c)(3) or other format—to give adjustability between different forms of giving. None of the Anthropic equity held by the LLC will be used for lobbying or political giving, in the US or abroad.»

### F277 🟢 Первоисточник

Possible uses named by Anthropic are large donations to traditional nonprofits or direct distributions to specific populations; labor-market impacts are given as one example, with $200 million already committed to that issue.

- Source: Anthropic, 2026-10-18 — <https://www.anthropic.com/news/public-benefit-fund> (confidence as rated by researcher: primary)
- Quote: «for example, we might explore large donations to traditional nonprofits or direct distributions to specific populations. [...] Anthropic has already committed $200 million to studying and addressing this issue, but given the pace of AI progress, bolder approaches may be needed.»

### F278 🟢 Первоисточник

Co-founders pledged at founding to donate 80% of their equity holdings; an equity donation match program exists in which approximately half of employees participate; combined with the new Fund roughly 20% of Anthropic shares will be dedicated to the public good, plus any valuation-milestone additions.

- Source: Anthropic, 2026-10-18 — <https://www.anthropic.com/news/public-benefit-fund> (confidence as rated by researcher: primary)
- Quote: «our co-founders pledged to donate 80% of their equity holdings [...] Approximately half of our employees participate in this program. When combined with today's announcement, roughly 20% of Anthropic shares will be dedicated to the public good, plus any additional percentage that could be added if the company reaches specific valuation milestones.»

### F279 🟢 Первоисточник

Anthropic says it will share more about the Fund's structure and governance, including the valuation milestones, 'in the coming months', and will report on mission progress in an upcoming public benefit report.

- Source: Anthropic, 2026-10-18 — <https://www.anthropic.com/news/public-benefit-fund> (confidence as rated by researcher: primary)
- Quote: «In the coming months, we will share more about the Anthropic Public Benefit Fund's structure and governance, including the valuation milestones that may add to its stake. We will also report on our progress to date against our mission in an upcoming public benefit report.»

### F280 🟢 Первоисточник

Anthropic's own English terminology: the company calls itself 'a public benefit corporation' and the new entity 'the Anthropic Public Benefit Fund' / 'the Fund'; it never calls the Fund a charity or foundation.

- Source: Anthropic, 2026-10-18 — <https://www.anthropic.com/news/public-benefit-fund> (confidence as rated by researcher: primary)
- Quote: «As a public benefit corporation, most of our work in pursuit of our mission takes place inside the company»

### F281 🟢 Первоисточник

Anthropic's X post describes the Fund as 'a new wholly owned entity dedicated entirely to the public benefit' starting with 5% of shares.

- Source: Anthropic (X/Twitter), 2026-10-18 — <https://x.com/AnthropicAI/status/2111881963657412903> (confidence as rated by researcher: primary)
- Quote: «We're committing a portion of Anthropic's shares to the Anthropic Public Benefit Fund, a new wholly owned entity dedicated entirely to the public benefit. It will start off with 5% of our shares. For every 50% increase in the company's value over a set baseline, we can contribute…»

### F282 🟢 Первоисточник

Anthropic's canonical description of the Long-Term Benefit Trust (LTBT): an independent body of five financially disinterested members with authority to select and remove a growing portion of the board. No Russian-language outlet surveyed offers a Russian rendering of this name; it is kept in English where mentioned at all.

- Source: Anthropic — <https://www.anthropic.com/news/the-long-term-benefit-trust> (confidence as rated by researcher: primary)
- Quote: «independent body of five financially disinterested members with an authority to select and remove a portion of our Board that will grow over time»

### F283 🟡 Крупное СМИ

The $48 billion figure circulating in Russian and German coverage is a Business Insider calculation: a 5% stake is worth about $48 billion at Anthropic's most recent (May 2026) valuation. Business Insider also calls the LLC 'a charitable organization', a label Anthropic itself avoids.

- Source: Business Insider (via Yahoo Finance), 2026-10-18 — <https://finance.yahoo.com/markets/stocks/articles/anthropic-sets-aside-5-stake-114524150.html> (confidence as rated by researcher: major_outlet)
- Quote: «A 5% stake in Anthropic is worth about $48 billion, according to the company's most recent valuation in May.»

### F284 🟡 Крупное СМИ

Al Jazeera's wording 'with immediate effect, subject to stockholder approval' is the origin of the Russian phrasing in azat.tv that the initiative 'immediately takes effect'; Al Jazeera also notes Anthropic is 'officially registered as a public benefit corporation' in Delaware and that analysts forecast an IPO valuation exceeding $2 trillion.

- Source: Al Jazeera, 2026-10-19 — <https://www.aljazeera.com/economy/2026/10/19/anthropic-says-it-will-commit-5-of-shares-to-public-benefit-fund> (confidence as rated by researcher: major_outlet)
- Quote: «In a blog post, Anthropic said it was committing 5 percent of company shares with immediate effect, subject to stockholder approval, with an additional 2 percent to be added "at the board's discretion" for every 50 percent increase in the company's value.»

### F285 🟡 Крупное СМИ

AP describes the Fund as 'a new entity within the company, pending approval from stockholders' and notes Anthropic 'shared little information' about recipient organizations; AP repeats the ~20% and $200 million figures.

- Source: AP (via The Business Journal), 2026-10-20 — <https://thebusinessjournal.com/anthropic-commits-shares-public-benefit-fund/> (confidence as rated by researcher: major_outlet)
- Quote: «On Sunday, Anthropic said it would commit 5% of its shares to the Anthropic Public Benefit Fund, a new entity within the company, pending approval from stockholders.»

### F286 🟡 Крупное СМИ

Elon Musk's exact reply to Anthropic's post was 'I recommend giving the shares directly to the public'; his follow-up pledge read 'Next year, I will give one of my SpaceX shares to every kid in America. This will be the first of many.' Anthropic did not respond to Fox's requests for comment.

- Source: Fox Business, 2026-10-19 — <https://www.foxbusiness.com/technology/anthropic-silent-whether-distribute-shares-americans-following-musk-spacex-pledge> (confidence as rated by researcher: major_outlet)
- Quote: «"I recommend giving the shares directly to the public," Musk wrote on X. [...] "Next year, I will give one of my SpaceX shares to every kid in America. This will be the first of many," he wrote.»

### F287 🟡 Крупное СМИ

Interfax (19 Oct 2026, 03:59) headline renders the Fund descriptively as 'новый фонд для общественных инициатив' and keeps 'Anthropic Public Benefit Fund' in Latin script; lead calls it 'новый фонд, ориентированный на общественное благо'. Interfax renders 'public benefit corporation' as 'корпорация общественной пользы'.

- Source: Интерфакс, 2026-10-19 — <https://www.interfax.ru/digital/1123345> (confidence as rated by researcher: major_outlet)
- Quote: «Американская компания Anthropic объявила о передаче 5% своих акций в новый фонд, ориентированный на общественное благо,»

### F288 🟡 Крупное СМИ

ERROR in Interfax: it says the founders pledged 80% of their 'состояния' (wealth) to charitable causes, whereas Anthropic says 80% of their equity holdings; Interfax also omits the stockholder-approval condition and the 2%-per-50% mechanism (saying only that an additional stake may be allocated on reaching certain valuation indicators), and interprets the employee match as the company 'doubling' contributions.

- Source: Интерфакс, 2026-10-19 — <https://www.interfax.ru/digital/1123345> (confidence as rated by researcher: major_outlet)
- Quote: «Основатели также обязались направить 80% своего состояния на благотворительные цели. [...] Около половины сотрудников участвуют в программе передачи долей, в рамках которой компания удваивает их вклад. [...] Дополнительная доля может быть выделена при достижении определённых оценочных показателей.»

### F289 🟡 Крупное СМИ

Interfax correctly reports the ~20% combined figure and the $200 million prior commitment (without naming 'Economic Futures').

- Source: Интерфакс, 2026-10-19 — <https://www.interfax.ru/digital/1123345> (confidence as rated by researcher: major_outlet)
- Quote: «С учётом нового решения около 20% акций Anthropic будут направлены на "общественное благо", отмечает компания.»

### F290 🟡 Крупное СМИ

Kommersant (19.10.2026, 12:46, Яна Рождественская) renders the Fund as «Фонд общественного блага» (with 'Public Benefit Fund' in parentheses), headline «Anthropic пообещал направить 5% акций в собственный «Фонд общественного блага»»; it mentions stockholder approval and the 2%-per-50% mechanism, cites only Anthropic's announcement, and omits LLC, lobbying ban, 80%, 20% and $200M.

- Source: Коммерсантъ, 2026-10-19 — <https://www.kommersant.ru/doc/9041934> (confidence as rated by researcher: major_outlet)
- Quote: «направить 5% своих акций в новый собственный «Фонд общественного блага» [...] Теперь решение должны одобрить акционеры компании»

### F291 🟡 Крупное СМИ

DIVERGENCE in Kommersant: it narrows Anthropic's 'direct distributions to specific populations' to donations to 'groups of the population whose jobs were hurt by AI', which the primary source gives only as an example; it adds IMF context that AI will affect ~40% of jobs worldwide.

- Source: Коммерсантъ, 2026-10-19 — <https://www.kommersant.ru/doc/9041934> (confidence as rated by researcher: major_outlet)
- Quote: «пожертвования некоммерческим организациям или группам населения, чьи рабочие места пострадали от ИИ»

### F292 🟡 Крупное СМИ

RBC (19 Oct 2026, 08:48, Евгения Сорокина) headline calls it a 'благотворительный фонд' ('Anthropic сообщила о планах направить 5% акций в благотворительный фонд') but the body keeps 'Anthropic Public Benefit Fund' in Latin script and speaks of 'общественно полезных целей'. RBC is among the most complete Russian reports: LLC vs 501(c)(3), lobbying ban, 80% of shares, ~half of employees, ~20%, $200M, stockholder approval, 2% per 50%.

- Source: РБК, 2026-10-19 — <https://www.rbc.ru/rbcfreenews/6ad5aa5047744c7f7c21cca7> (confidence as rated by researcher: major_outlet)
- Quote: «направить 5% своих акций в новый Anthropic Public Benefit Fund [...] а не организации со статусом 501© (3) [...] не будут использоваться для лоббирования или политических пожертвований»

### F293 🟡 Крупное СМИ

RBC adds valuation context: Anthropic filed for IPO in June; after raising $65 billion its valuation exceeded $900 billion; in September investors reportedly discussed an IPO valuation of up to $2 trillion.

- Source: РБК, 2026-10-19 — <https://www.rbc.ru/rbcfreenews/6ad5aa5047744c7f7c21cca7> (confidence as rated by researcher: major_outlet)

### F294 🟠 Вторичный источник

Expert.ru (19.10.2026, 14:08, Анна Безрукова) uses 'Anthropic Public Benefit Fund (фонд общественного блага)' and headline «Anthropic пообещала направить 5% акций в «фонд общественного блага»»; it cites CNBC's analyst Liz Bayer (Class V Group) calling the move an image-positive step ahead of the IPO, and Bloomberg's report of Q3 2026 revenue of $16.8 billion (+50% q/q). Omits LLC, lobbying ban, 80%, 20%, $200M.

- Source: Эксперт, 2026-10-19 — <https://expert.ru/news/anthropic-poobeschala-napravit-5-aktsiy-v-fond-obschestvennogo-blaga> (confidence as rated by researcher: secondary)
- Quote: «Anthropic Public Benefit Fund (фонд общественного блага)»

### F295 🟠 Вторичный источник

Habr news (19 Oct, Информационная служба Хабра) renders the Fund as «Фонд общественного блага (Anthropic Public Benefit Fund)» and Economic Futures as «Фонд исследований экономического будущего (Anthropic Economic Futures Research)»; it cites the $200 млн figure and Dario Amodei's phrase «кризис доверия».

- Source: Хабр, 2026-10-19 — <https://habr.com/ru/news/1096242/> (confidence as rated by researcher: secondary)
- Quote: «Anthropic объявила о планах создать Фонд общественного блага (Anthropic Public Benefit Fund), который [...] Для этих целей компания создала Фонд исследований экономического будущего (Anthropic Economic Futures Research).»

### F296 🟠 Вторичный источник

IMPRECISION in Habr: the 2% step is described as per '50% роста ценных бумаг компании' (growth of the company's securities) instead of company value above a set baseline, with no mention of board discretion or the baseline; Habr also omits the stockholder-approval condition, the LLC structure, the lobbying ban, the 80% pledge and the ~20% total.

- Source: Хабр, 2026-10-19 — <https://habr.com/ru/news/1096242/> (confidence as rated by researcher: secondary)
- Quote: «Кроме того, Anthropic сможет дополнительно выделять фонду 2% за каждые 50% роста ценных бумаг компании.»

### F297 🟠 Вторичный источник

Inc. Russia renders the Fund as 'новый фонд общественных благ' and PBC as 'корпорации общественной пользы (Public Benefit Corporation)'; it correctly reports the LLC form, 2% per 50% with undisclosed baseline, $200 млн, lobbying ban, 80% of shares, employee co-funding program and ~20%, but never mentions the stockholder-approval condition.

- Source: Inc. Russia, 2026-10-19 — <https://incrussia.ru/news/anthropic-sozdast-fond-dlya-pomoshhi-lyudyam-chi-professii-izmenit-ii/> (confidence as rated by researcher: secondary)
- Quote: «Фонд создадут в форме компании с ограниченной ответственностью, полностью принадлежащей Anthropic. [...] Компания работает в формате корпорации общественной пользы (Public Benefit Corporation)»

### F298 🟠 Вторичный источник

Inc. Russia's rendering of the 80%/20% passage: founders' commitment to give 80% of their shares to charity plus the employee donation co-funding program means about 20% of shares may be tied to public-benefit initiatives, excluding future Fund increases.

- Source: Inc. Russia, 2026-10-19 — <https://incrussia.ru/news/anthropic-sozdast-fond-dlya-pomoshhi-lyudyam-chi-professii-izmenit-ii/> (confidence as rated by researcher: secondary)
- Quote: «С учетом ранее объявленных обязательств сооснователей Anthropic направить на благотворительность 80% принадлежащих им акций, а также программы софинансирования пожертвований сотрудников, около 20% акций компании могут быть связаны с общественно полезными инициативами.»

### F299 🟠 Вторичный источник

dev.by (19.10.2026, 14:04) headline '20% компании на благо общества: Anthropic создала благотворительный фонд в преддверии гигантского IPO' frames the Fund as 'благотворительный' and foregrounds 20%; body keeps 'Public Benefit Fund' in Latin script, renders PBC as «корпорации общественного блага» (Public Benefit Corporation), cites Reuters, and mentions the lobbying ban and Musk.

- Source: dev.by, 2026-10-19 — <https://devby.io/news/anthropic-peredast-5-svoih-aktsii-v-novyi-blagotvoritelnyi-fond> (confidence as rated by researcher: secondary)
- Quote: «Компания выйдет на IPO в особом статусе «корпорации общественного блага» (Public Benefit Corporation) [...] деньги фонда запрещено использовать для лоббирования законов или политических пожертвований»

### F300 🟠 Вторичный источник

ERRORS in dev.by: (1) says the founders pledged 80% of 'личных доходов' (personal income) rather than equity holdings; (2) says 5% is transferred 'сразу' (immediately) with no mention of stockholder approval; (3) says the fund 'будет получать' (will receive) 2% per 50% capitalization growth, dropping board discretion.

- Source: dev.by, 2026-10-19 — <https://devby.io/news/anthropic-peredast-5-svoih-aktsii-v-novyi-blagotvoritelnyi-fond> (confidence as rated by researcher: secondary)
- Quote: «в который сразу передаст 5% своих акций [...] за каждые 50% роста капитализации компании фонд будет получать ещё по 2% бумаг [...] обещанием сооснователей отдавать 80% личных доходов на благотворительность»

### F301 🟠 Вторичный источник

dev.by renders Musk's reply as a jab from the head of competitor xAI suggesting Anthropic 'не плодить фонды, а просто раздать акции напрямую людям'; in its separate Musk piece the rendering is 'лучше бы раздали акции напрямую людям' and the Fund is called 'фонд общественного блага' / 'социальный фонд'.

- Source: dev.by, 2026-10-19 — <https://devby.io/news/shutki-za-700-mlrd-mask-poobeschal-razdat-amerikanskim-detyam-aktsii-spacex> (confidence as rated by researcher: secondary)
- Quote: «Илон Маск, чья xAI конкурирует с Anthropic, уже успел уколоть её в соцсетях [...] не плодить фонды, а просто раздать акции напрямую людям»

### F302 🟠 Вторичный источник

NEWSru.co.il (19 Oct 2026, 12:40) headline 'Anthropic выделит 5% акций на борьбу с ИИ-безработицей' does not name the Fund at all; it describes it as a wholly owned limited-liability structure, reports the lobbying ban, the $200 million commitment, Musk's reaction, and that ~80 of 261 prospectus pages cover risk factors; it omits the 80% pledge, employee match and ~20%.

- Source: NEWSru.co.il, 2026-10-19 — <https://www.newsru.co.il/finance/19oct2026/anthropic308.html> (confidence as rated by researcher: secondary)
- Quote: «полностью принадлежащей компании структуры с ограниченной ответственностью»

### F303 🟠 Вторичный источник

Trashbox.ru (19 Oct 2026, 16:45) keeps the English name, headline 'Anthropic пообещала 5 % акций фонду для помощи сотрудникам, пострадавшим от ИИ'; it correctly states the LLC form, discretionary (not automatic) 2-percentage-point steps, 80%, ~20% and ~half of staff, explicitly notes the 20% is neither the fund's starting stake nor a cap, and that recipients, amounts and timing are unnamed; omits lobbying ban, 501(c)(3) and $200M.

- Source: Trashbox.ru, 2026-10-19 — <https://trashbox.ru/link/2026-10-19-anthropic-poobeschala-5-akciy-fondu-dlya-resheniya-obschestvennyh-problem> (confidence as rated by researcher: secondary)

### F304 🟠 Вторичный источник

Overclockers.ru user blog (Nacvark, 19 Oct) headline 'Anthropic пожертвует 5% своих акций в фонд для поддержки людей, пострадавших от развития ИИ'; based on Reuters; names 'Anthropic Public Benefit Fund'; reports LLC, stockholder approval, 2% per 50% above undisclosed baseline, lobbying ban, $200 million; omits 80%/20%/match.

- Source: Overclockers.ru (блог), 2026-10-19 — <https://overclockers.ru/blog/Nacvark/show/266497/Anthropic-pozhertvuet-5-svoih-akcij-v-fond-dlya-podderzhki-ljudej-postradavshih-ot-razvitiya-II> (confidence as rated by researcher: secondary)

### F305 🟠 Вторичный источник

Forbes.ru's piece (seen via Prospect reprint credited to forbes.ru, 19 Oct 2026, 11:50) is headlined 'Anthropic пообещала отдать 5% акций в новый фонд для помощи теряющим работу из-за ИИ', uses 'фонд общественной пользы Anthropic Public Benefit Fund', says experts called the step a 'выгодный ход' ahead of the IPO, and that the IPO is reportedly being prepared for October (other outlets say November).

- Source: Forbes.ru (reprint on prospect.com.ru), 2026-10-19 — <https://prospect.com.ru/news/7105883/anthropic-poobeschala-otdat-5-aktsij-v-novyj-fond-dlya-pomoschi-teryayuschim-rabotu-izza-ii.html> (confidence as rated by researcher: secondary)

### F306 🟠 Вторичный источник

3DNews (via Prospect reprint credited to 3dnews.ru, 19 Oct 2026, 16:10) headline 'Anthropic направит до 20 % акций на благотворительность — в том числе для борьбы с безработицей из-за ИИ' — DIVERGENCE: it recasts the combined ~20% (which includes founders' and employees' pledges) as something Anthropic 'is ready to give' as capitalization grows, uses 'до 20 %' in the headline vs 'около 20 %' in the body, and calls it 'благотворительность'. A teaser on the same page uses 'Anthropic Public Benefit Fund (фонд общественной пользы)'.

- Source: 3DNews (reprint on prospect.com.ru), 2026-10-19 — <https://prospect.com.ru/news/7106302/anthropic-napravit-do-20-aktsij-na-blagotvoritelnost-v-tom-chisle-dlya-borby-s-bezrabotitsej-izza-ii.html> (confidence as rated by researcher: secondary)
- Quote: «По мере роста своей капитализации Anthropic готова отдать около 20 % своих акций на нужды благотворительности.»

### F307 🟠 Вторичный источник

iXBT (via Prospect reprint credited to ixbt.com, 19 Oct 2026, 16:50) headline 'Anthropic передаст общественному фонду 5% своих акций — доля будет расти вместе с компанией' keeps the English name, uses 'общественный фонд', and correctly frames the increase as 2 percentage points per 50% with board approval.

- Source: iXBT (reprint on prospect.com.ru), 2026-10-19 — <https://prospect.com.ru/news/7106378/anthropic-peredast-obschestvennomu-fondu-5-svoih-aktsij-dolya-budet-rasti-vmeste-s-kompaniej.html> (confidence as rated by researcher: secondary)
- Quote: «Изначально фонду выделят 5% акций [...] с одобрения совета директоров его долю смогут увеличивать ещё на 2 процентных пункта»

### F308 🟠 Вторичный источник

azat.tv (19/10/2026, 21:00) uses 'фонд общественного блага', headline 'Фонд общественного блага получит 5% акций Anthropic перед выходом компании на биржу'; DIVERGENCES: it says the initiative 'немедленно вступает в силу в операционной структуре компании' (a garbled echo of Al Jazeera's 'with immediate effect, subject to stockholder approval') and attributes the lobbying ban to the fund's 'charter' (no charter has been published). It cites The Guardian, Livemint and KuCoin and gives $965 billion May valuation after a $65 billion round and $16.8 billion Q3 revenue.

- Source: azat.tv, 2026-10-19 — <https://azat.tv/ru/anthropic-pledges-5-percent-shares-public-benefit-fund-ipo/> (confidence as rated by researcher: secondary)
- Quote: «немедленно вступает в силу в операционной структуре компании»

### F309 🟠 Вторичный источник

KuCoin's machine-translated Russian blog (2026-10-22) uses three different names for the Fund — 'Фонд общественной пользы', 'Публичный благотворительный фонд Anthropic' and 'Anthropic Public Benefit Fund' — and reports LLC, stockholder approval, lobbying ban, 80%, ~half of employees, ~20%, $200 million, a $965 billion valuation and IPO talk of $1.5–2 trillion.

- Source: KuCoin Blog (RU, machine translation), 2026-10-22 — <https://www.kucoin.com/ru/blog/ru-anthropic-pledges-5-of-its-equity-to-public-benefit-fund-as-musk-promises-spacex-shares-to-us-children> (confidence as rated by researcher: secondary)
- Quote: «Никакая доля в фонде не может использоваться для лоббирования или политических пожертвований в США или где-либо еще. [...] примерно 20% акций Anthropic сейчас направлены на цели общественной пользы»

### F310 ⚪ Оценка или мнение

Unite.AI's Russian version (18 Oct 2026, AI-generated, labelled as such) keeps 'Anthropic Public Benefit Fund' and 'Economic Futures' in Latin script, renders LLC as 'ООО' and PBC as 'общественно полезной корпорации'; it adds a claim that the fund will mainly back projects of $5–30 million and not fund projects under $1 million — this is NOT in Anthropic's announcement and should not be used.

- Source: Unite.AI (RU, AI-generated), 2026-10-18 — <https://www.unite.ai/ru/anthropic-commits-5-of-its-shares-to-new-public-benefit-fund/> (confidence as rated by researcher: speculative)

### F311 🟡 Крупное СМИ

The Moscow Times (Russian edition, 19.10.2026) uses «фонд общественного блага», values the 5% at 'порядка $100 млрд' based on a WSJ-reported possible $2 trillion post-IPO capitalization in November, and renders Musk's pledge as «В следующем году я подарю по одной своей акции SpaceX каждому ребенку в Америке. Она будет первой из многих».

- Source: The Moscow Times (RU), 2026-10-19 — <https://ru.themoscowtimes.com/2026/10/19/mask-poobeschal-po-aktsii-spacex-kazhdomu-rebenku-v-ssha-posle-togo-kak-anthropic-videlila-5-na-obschestvennoe-blago-a208990> (confidence as rated by researcher: major_outlet)
- Quote: «В следующем году я подарю по одной своей акции SpaceX каждому ребенку в Америке. Она будет первой из многих»

### F312 🟠 Вторичный источник

The Insider (19 Oct 2026, 13:16) uses «Фонд общественного блага», says Anthropic will direct 'at least 5%' of shares (about $48 billion), paraphrases Musk as saying shares should go directly to people, and renders his pledge as «В следующем году я отдам по одной своей акции SpaceX каждому ребенку в Америке. Это будет первая раздача из многих»; cites CNN and Reuters.

- Source: The Insider, 2026-10-19 — <https://theins.ru/news/298460> (confidence as rated by researcher: secondary)
- Quote: «В следующем году я отдам по одной своей акции SpaceX каждому ребенку в Америке. Это будет первая раздача из многих»

### F313 🟠 Вторичный источник

Russian Wikipedia's Anthropic infobox renders 'public benefit corporation' as 'корпорация общественного блага' (red link); it does not mention the Long-Term Benefit Trust or the Public Benefit Fund.

- Source: Русская Википедия — <https://ru.wikipedia.org/wiki/Anthropic> (confidence as rated by researcher: secondary)
- Quote: «бизнес, технологическая компания и корпорация общественного блага»

### F314 🟡 Крупное СМИ

Handelsblatt (19.10.2026, 03:37; Reuters-based, datelined New York) headline 'KI: Anthropic will fünf Prozent seiner Aktien in Gemeinwohl-Fonds stecken'; keeps 'Anthropic Public Benefit Fund' and 'Public Benefit Corporation' (glossed as 'US-Rechtsform'); reports lobbying ban, ~20% and pending shareholder approval; no LLC, 80%, match or $200M.

- Source: Handelsblatt, 2026-10-19 — <https://www.handelsblatt.com/technik/ki/ki-anthropic-will-fuenf-prozent-seiner-aktien-in-gemeinwohl-fonds-stecken/100263117.html> (confidence as rated by researcher: major_outlet)
- Quote: «dürften weder im In- noch im Ausland für Lobbyarbeit oder politische Spenden verwendet werden [...] rund 20 Prozent der Anthropic-Aktien für öffentliche Zwecke vorgesehen [...] Die Aktionäre müssen den Plänen noch zustimmen.»

### F315 🟡 Крупное СМИ

Reuters' German wire (via cash.ch, 18.10.2026, 21:27) calls the Fund a 'hundertprozentige Tochtergesellschaft' (wholly owned subsidiary) rather than naming the LLC form, uses the generic 'Gemeinwohl-Fonds', keeps «Anthropic Public Benefit Fund» and «Public Benefit Corporation» in English, and reports the lobbying ban, ~20% and shareholder-approval condition.

- Source: Reuters (via cash.ch), 2026-10-18 — <https://www.cash.ch/news/top-news/anthropic-will-funf-prozent-seiner-aktien-in-gemeinwohl-fonds-stecken-977559> (confidence as rated by researcher: major_outlet)
- Quote: «Der Fonds soll als hundertprozentige Tochtergesellschaft gegründet werden. [...] Voraussetzung für das Vorhaben sei aber die Zustimmung der Aktionäre.»

### F316 🟡 Крупное СМИ

Golem.de headline: 'KI: Anthropic will 5 Prozent seiner Aktien dem Gemeinwohl widmen' (article body behind a cookie-consent wall; not verified).

- Source: Golem.de, 2026-10-19 — <https://www.golem.de/news/ki-anthropic-will-5-prozent-seiner-aktien-dem-gemeinwohl-widmen-2610-214243.html> (confidence as rated by researcher: major_outlet)

### F317 🟠 Вторичный источник

Trending Topics (AT, 19.10.2026, Jakob Steinschaden, 'co-produced by AI') keeps 'Public Benefit Fund' in English, states the LLC form, lobbying ban, 80% founders' pledge, employee match, ~20% and $200 million, and computes a hypothetical ~$100 billion (≈€89 billion) value at a >$2 trillion IPO valuation.

- Source: Trending Topics, 2026-10-19 — <https://www.trendingtopics.eu/anthropic-public-benefit-fund-sicherheitsgesetz/> (confidence as rated by researcher: secondary)
- Quote: «Der Fonds wird als eigene Gesellschaft (LLC) aufgesetzt, die vollständig Anthropic gehört. [...] wären 5 Prozent rund 100 Milliarden Dollar (rund 89 Milliarden Euro) wert»

### F318 🟠 Вторичный источник

Dr. Web (DE, 19 Oct 2026, updated 22 Oct, Michael Dobler) renders the Fund as 'Fonds für das Gemeinwohl' / 'Gemeinwohlfonds' and explicitly not a 'Stiftung'; describes the LLC as 'vergleichbar einer GmbH'; computes €42 billion for 5% at the May valuation ($965 billion at 0.87 €/$); notes shareholders must approve because each step dilutes holders; cites Bloomberg for a November IPO.

- Source: Dr. Web, 2026-10-19 — <https://www.drweb.de/anthropic-aktien-gemeinwohlfonds/> (confidence as rated by researcher: secondary)
- Quote: «Anthropic will 5 Prozent seiner Aktien in einen eigenen Fonds für das Gemeinwohl einbringen [...] darf der Verwaltungsrat weitere 2 Prozent nachlegen [...] Die Aktionäre müssen noch zustimmen»

### F319 🟠 Вторичный источник

News.at (Austria, updated 19.10.2026) uses 'Gemeinwohlfonds' in the headline and 'Fonds für das Gemeinwohl' in the body, keeps the English fund name and 'Public Benefit Corporation', glosses 'Board' as 'Leitungsgremium', and reports LLC, lobbying ban, employee match ('verdoppelt'), 80% of founders' shares, ~20%, $200 million and shareholder approval; notes Anthropic gives no dollar value for the fund.

- Source: News.at, 2026-10-19 — <https://www.news.at/wirtschaft/anthropic-public-benefit-fund-5-prozent-aktien-gemeinwohl-ki-arbeitsmarkt> (confidence as rated by researcher: secondary)
- Quote: «Rechtlich ist der Fonds eine hundertprozentige Tochtergesellschaft in Form einer LLC [...] Für Beschäftigte gibt es ein Programm, das Aktienspenden verdoppelt [...] Wie hoch dieser Ausgangswert ist und welchen Wert der Fonds in Dollar hat, nennt Anthropic nicht.»

### F320 🟡 Крупное СМИ

Ben Bernanke was appointed to Anthropic's Long-Term Benefit Trust on 2026-07-09 (relevant background for LTBT terminology; no Russian-language coverage of this appointment surfaced in searches).

- Source: Bloomberg, 2026-07-09 — <https://www.bloomberg.com/news/articles/2026-07-09/former-fed-chairman-ben-bernanke-joins-anthropic-oversight-trust> (confidence as rated by researcher: major_outlet)

Researcher notes: TERMINOLOGY (for a Russian-language article)
1) Fund name — attested Russian renderings, by frequency: «Фонд общественного блага» (Коммерсантъ, Хабр, Эксперт gloss, The Moscow Times, The Insider, azat.tv, dev.by body, devby Musk piece) is the dominant form; «фонд общественной пользы» (Forbes.ru via Prospect, 3DNews teaser, KuCoin, Prospect teasers; this matches the user's own wording); «фонд общественных благ» (Inc.); descriptive «фонд для общественных инициатив» (Interfax headline), «фонд, ориентированный на общественное благо» (Interfax lead); «общественный фонд» (iXBT headline, KuCoin headline); «социальный фонд» (dev.by); «благотворительный фонд» (RBC headline, dev.by headline, 3DNews 'благотворительность'); machine-translation oddity «Публичный благотворительный фонд Anthropic» (KuCoin). Interfax, RBC, Trashbox, Overclockers, iXBT, Unite.AI keep "Anthropic Public Benefit Fund" in Latin script. Recommended: keep the English name on first mention with gloss «Фонд общественного блага» (or «общественной пользы»); avoid «благотворительный фонд» — Anthropic deliberately chose an LLC rather than a 501(c)(3)/charity, and Business Insider's "a charitable organization" label is an outlet's gloss, not Anthropic's.
2) "Public benefit corporation": «корпорация общественной пользы» (Interfax; Inc. with English in parentheses) and «корпорация общественного блага» (dev.by; Russian Wikipedia infobox) are the two established renderings; «общественно полезная корпорация» appears only in AI-generated Unite.AI. German outlets (Handelsblatt, Reuters/cash.ch, News.at) keep "Public Benefit Corporation" in English and gloss it as a "US-Rechtsform". Anthropic is registered as a PBC in Delaware (Al Jazeera, Reuters explainer).
3) "Long-Term Benefit Trust": NO Russian rendering found in any Russian outlet (Habr, vc.ru, 3DNews, Forbes.ru, Коммерсантъ, РБК, Russian Wikipedia all checked via search; none render it). The English name is universally kept. Anthropic's own description: "independent body of five financially disinterested members with an authority to select and remove a portion of our Board that will grow over time"; trustees hold Class T stock. If a gloss is needed, «Траст долгосрочной выгоды» or «траст долгосрочных интересов (человечества)» are reasonable but unattested — mark as translator's gloss, keep the English name.
4) Note the two distinct Anthropic entities: the PBC (the company), the LTBT (governance trust, 2023), and now the Public Benefit Fund (LLC, 2026). Habr renders "Economic Futures Research" as «Фонд исследований экономического будущего».

ERRORS / DIVERGENCES FOUND IN NON-ENGLISH COVERAGE
- 80% pledge misreported: Interfax says 80% of founders' «состояния» (wealth); dev.by says 80% of «личных доходов» (personal income). Primary: 80% of equity holdings. Correct: RBC («80% своих акций»), Inc. («80% принадлежащих им акций»), News.at («80 Prozent ihrer Anteile»).
- 5% vs 20% confusion: 3DNews headline «Anthropic направит до 20 % акций на благотворительность» and dev.by headline «20% компании на благо общества» present the combined ~20% (Fund + founders + employees) as the company's giving; the Fund itself starts at 5%. Trashbox explicitly and correctly notes the 20% is neither the Fund's starting stake nor a cap.
- Stockholder approval omitted: Interfax, Habr, Inc., dev.by («сразу передаст 5%»). Correct: Коммерсантъ, РБК, Trashbox, Overclockers, Handelsblatt, Reuters/cash.ch, Dr. Web, News.at.
- Board discretion dropped (automatic ratchet implied): dev.by («фонд будет получать»), Habr («за каждые 50% роста ценных бумаг» — also wrong trigger). Correct: РБК, Inc., iXBT («с одобрения совета директоров»), Trashbox.
- "Immediately takes effect": azat.tv's «немедленно вступает в силу в операционной структуре компании» is a distortion of Al Jazeera's "with immediate effect, subject to stockholder approval". azat.tv also attributes the lobbying ban to the fund's "charter" — no charter has been published.
- Employee match: Interfax/News.at say the company "doubles" («удваивает»/"verdoppelt") donations; primary says only that Anthropic "matches" pledged equity — ratio not specified.
- Kommersant narrows "direct distributions to specific populations" to groups whose jobs were hurt by AI.
- Unite.AI (AI-generated) adds project-size figures ($5–30M, nothing under $1M) absent from the primary source — do not use.
- IPO timing: Forbes.ru/Prospect says October; Bloomberg/WSJ/FT (via Dr. Web, Moscow Times, TNW) say November. Not stated by Anthropic.
- Dollar values are all outlet calculations, not Anthropic's: ~$48bn (Business Insider; 5% of the $965bn May valuation; repeated by The Insider, Golem, KuCoin) vs ~$100bn (Moscow Times, Trending Topics, Decrypt; 5% of a hypothetical $2tn IPO valuation); Dr. Web gives €42bn. News.at correctly notes Anthropic gives no dollar value.
- Musk's exact reply: "I recommend giving the shares directly to the public" (Fox Business). Russian renderings: dev.by «лучше бы раздали акции напрямую людям» / «не плодить фонды, а просто раздать акции напрямую людям»; NEWSru.co.il/The Insider paraphrase similarly. His pledge "Next year, I will give one of my SpaceX shares to every kid in America. This will be the first of many" is rendered «подарю ... Она будет первой из многих» (Moscow Times) vs «отдам ... Это будет первая раздача из многих» (The Insider) vs «передам» (dev.by).

COVERAGE GAPS / ACCESS
- No coverage found from Ведомости, ТАСС, РИА Новости, Lenta.ru (searched). Forbes.ru and 3DNews originals could not be located directly (3dnews.ru tag page and forbes.ru search returned errors); both are cited via Prospect reprints that credit them. Golem.de body blocked by cookie wall; techora.ru anti-bot; pasqualepillitteri.it (RU) 502; kurs.com.ua (UA, headline «Розробник Claude створює фонд для фінансування суспільних проєктів») 403. dev.by also has a Belarusian version (slug: «20% кампаніі на карысць грамадства: Anthropic стварыла дабрачынны фонд напярэдадні гіганцкага IPO»). German coverage is Reuters-driven (Handelsblatt, cash.ch, onvista, TradingView) plus Golem, Trending Topics, Dr. Web, News.at, itreseller.ch, mind-verse.de; no heise/t3n/FAZ/Spiegel/NZZ pieces surfaced. German outlets consistently use "Fonds"/"Gemeinwohlfonds"/"Gemeinwohl-Fonds", never "Stiftung" (Dr. Web explicitly contrasts with Stiftung). Habr shows 2 comments but their text was not retrievable.
- Local scratch copies used for parsing: /tmp/claude-0/-home-user-an-info/b29c76c6-899a-5222-9671-bd3017164403/scratchpad/dl/inc.html (Inc. Russia), /tmp/claude-0/-home-user-an-info/b29c76c6-899a-5222-9671-bd3017164403/scratchpad/dl/pbf.html (Anthropic announcement).

