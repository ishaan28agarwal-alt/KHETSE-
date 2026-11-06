# KhetSe (खेत से) — PRD: The Farm-to-Fork Gap

Nov 6, 2026 · @Team4

## 1. Problem understanding

The real problem is not that three middlemen exist; it is that the farmer has no second option, so he takes ₹8/kg for tomatoes that sell for ₹40/kg in the city.

> “एक किसान 100 kg टमाटर ₹8 प्रति किलो में बेचता है। वही टमाटर शहर में ₹40 में बिकता है। बीच में 3 बिचौलिए हैं।”

| Fact from the brief | What it means for the product |
| --- | --- |
| 100 kg at ₹8/kg = ₹800 to the farmer | The farmer’s share of the consumer rupee is 20% |
| City price ₹40/kg | The ₹32/kg gap is the pool everyone argues over |
| 3 middlemen in between | Typically a village aggregator, a mandi commission agent / wholesaler, and a city retailer |
| Farmer uses a smartphone but cannot read English | The interface must work with voice, pictures and Hindi numbers, not English text |
| Buyers: restaurant, grocer, household | Three very different order sizes: 20–50 kg/day, 50–200 kg/day, 1–3 kg/week |

**The catch.** Middlemen provide transport, storage and credit. Any plan that removes them without replacing those services fails on day one.

**Users.**

- **Ramesh, 42, tomato farmer, Nashik district.** Android phone, uses WhatsApp voice notes and YouTube; reads Hindi slowly, cannot read English. Owes the local aggregator ₹15,000 for seed and fertiliser taken on credit.
- **Fatima, 35, runs a 40-seat dhaba in Pune.** Buys 25 kg tomatoes daily from a wholesaler at about ₹30/kg; cares about steady supply and grade more than the last rupee.
- **Kiran, grocer.** Buys 80–150 kg/day; needs predictable quality and credit terms.
- **Household.** Wants 2 kg, cares about freshness; impossible to serve individually from a farm 150 km away.

All prices in this PRD are illustrative assumptions for the pitch, not sourced market data.

## 2. Steelman: the case for the middlemen

Made as strongly as their defenders would make it, most of the ₹32 gap pays for real costs and real risk, not pure profit.

| Middleman | Service | Estimated cost it carries (₹/kg) |
| --- | --- | --- |
| Village aggregator | Collects small lots, crates, loads, gives the farmer **credit** for seed and fertiliser, pays cash same day | 1.5–2.5 |
| Mandi agent / wholesaler | **Transport** to the city, **storage**, price discovery, finds buyers, absorbs unsold stock, mandi fees and commission | 6–9 |
| City retailer | Shop rent, breaking 100 kg into 1 kg lots, last-mile, keeps stock on display | 6–8 |
| Everyone | **Spoilage**: tomatoes are soft; 20–30% can be lost between farm and plate in loose transport | 6–9 |
| Margin | What is left as profit across all three | roughly 5–8 |

The strongest arguments a defender makes:

1. **Credit is the real chain.** The farmer sells to the aggregator because he owes him. An app that pays ₹4 more but no advance will not win him.
2. **Risk transfer.** The farmer gets cash today; the middleman carries the price crash and the rot.
3. **Aggregation is efficient.** One truck carrying 10 farmers’ lots is cheaper per kg than 10 trips.
4. **Trust and grading.** Buyers trust a wholesaler they know; they do not trust a stranger’s photo.
5. **Households are expensive to serve.** Splitting 100 kg into fifty 2 kg orders is the most costly step in the whole chain.

**What survives the steelman.** The farmer’s weak spot is not the existence of services; it is that he has one buyer, no price information and no bargaining power. The opportunity is to keep the services, cut the spoilage and remove one layer of margin, then hand most of the saving to the farmer.

## 3. Solution v1, and how it breaks

The obvious answer, “a Hindi voice app that connects farmers directly to city buyers and cuts all three middlemen”, fails on six counts.

**v1 in one line:** farmer speaks a listing, any buyer orders, a courier picks it up, the platform takes 10%.

| # | Attack (steelman critique) | Why v1 breaks | Fix carried into v2 |
| --- | --- | --- | --- |
| 1 | “Who gives him the ₹15,000 advance?” | Farmer is tied by debt; extra ₹4/kg does not repay it | Instant payment on pickup + input credit through an NBFC/FPO partner, recovered from sales |
| 2 | “100 kg to 50 households?” | Last-mile per kg costs more than the margin saved | B2B first (restaurants, grocers); households only as society/RWA group orders with a 25 kg minimum |
| 3 | “Who carries it and who eats the rot?” | Couriers do not handle 100 kg of produce; loose transport loses 20–30% | Scheduled shared truck per village cluster, plastic crates, sell-before-harvest so stock moves within 24 h |
| 4 | “Why would a buyer trust a stranger?” | No grading, no recourse | Grade (A/B) set at the collection point, photo at pickup, replace-or-refund promise |
| 5 | “What if nobody orders?” | Ripe tomatoes rot on the farm | Floor promise: unsold stock goes to the local mandi via the partner, so the farmer never earns less than today |
| 6 | “The aggregator will fight you” | Local power, social pressure on farmers | Recruit him: the aggregator becomes the paid KhetSe Saathi, not the enemy |

Two smaller breaks: voice recognition fails on dialects and farm noise (fix: read-back confirmation plus picture and number-pad fallback), and a farmer may underprice (fix: show today’s mandi rate and a suggested fair price).

## 4. Solution v2: KhetSe (खेत से)

KhetSe **partners** with the first middleman, **replaces** the second with a scheduled route, and **sells around** the third by serving restaurants, grocers and housing societies directly.

**Decision on middlemen: partner, replace, bypass.**

| Today’s layer | KhetSe decision | How |
| --- | --- | --- |
| Village aggregator | **Partner** → KhetSe Saathi | Runs the collection point: weighs, grades, crates, helps first-time farmers. Paid a fixed ₹1.5/kg, no price-setting power |
| Mandi agent / wholesaler | **Replace** | Pre-orders + one shared truck per cluster on fixed days (Mon/Wed/Fri). No warehouse; stock is sold before it is picked |
| City retailer | **Bypass for B2B, keep for some households** | Restaurants and grocers order directly; households order as a society group with one drop point |

**How produce gets from farm to buyer.**

1. Farmer speaks the listing in Hindi: crop, quantity, price, village, pickup date.
2. KhetSe reads it back in Hindi; farmer says “हाँ” to publish.
3. Buyers order against the listing before harvest; the listing shows grade and pickup date.
4. On pickup day the farmer brings crates to the Saathi collection point (within 5 km); weight and grade are recorded with a photo.
5. Farmer is paid by UPI at the collection point the same hour; a Hindi voice message confirms the amount.
6. The cluster truck reaches the city hub by morning; orders go out in crates to restaurants, grocers and society drop points.
7. Anything not ordered is sold by the Saathi at the local mandi that day (the floor promise).

**Credit, storage, transport — what replaces each service.**

- **Credit:** same-day payment removes the farmer’s need to wait; seasonal input credit (seed, fertiliser) comes from a partner NBFC or FPO, repaid as a small deduction from each sale. KhetSe uses its sales history as the farmer’s credit record.
- **Storage:** designed out by selling before harvest; the city hub holds stock for under 12 hours. Cold storage only in phase 3.
- **Transport:** a contracted truck per cluster of 15–25 villages, paid per trip, filled by pooled orders.

**Why it is defensible.** The Saathi network and the sales-based credit record are hard to copy, and buyers get steady graded supply, which they value above a lower price.

## 5. Who earns what from one sale

On the same 100 kg of tomatoes, the farmer earns ₹1,400 instead of ₹800 (+75%), and a restaurant pays ₹2,400 instead of about ₹3,000.

| Who | ₹/kg | ₹ on 100 kg | What it pays for |
| --- | --- | --- | --- |
| Farmer | 14.0 | 1,400 | The produce (was ₹8/kg) |
| Transport (cluster truck) | 3.0 | 300 | \~150 km, shared across 10–15 farmers’ lots |
| Spoilage reserve | 2.0 | 200 | Crates + under-24 h transit cut loss from \~25% to \~8% |
| KhetSe platform fee | 2.0 | 200 | Platform revenue (\~8% of order value) |
| KhetSe Saathi (partner) | 1.5 | 150 | Weighing, grading, crating, helping farmers |
| City hub + delivery | 1.0 | 100 | Sorting and drop to restaurant / grocer |
| Payment + credit cost | 0.5 | 50 | UPI, same-day payout float, NBFC partner fee |
| **Buyer pays (B2B)** | **24.0** | **2,400** | vs \~₹30/kg from a city wholesaler today |

**Households** pay ₹28/kg via a society group order (vs ₹40 at a shop): the extra ₹4 covers society drop-off (₹3) and ₹1 more to the platform.

**How the ₹32 gap is shared.** Of the old ₹32 between ₹8 and ₹40, the farmer gains ₹6, the household buyer saves ₹12, and the remaining ₹14 still pays for real services — now visible line by line.

**Platform revenue.**

1. Transaction fee: ₹2/kg on every order (core).
2. Buyer plans: a monthly fee for guaranteed daily supply for restaurants (phase 2).
3. Credit referral fee from the NBFC partner on input loans (phase 2).

At 1 cluster × 3 trucks/week × 3 tonnes, the fee yields about ₹18,000/week of revenue per cluster. Assumptions to validate in the pilot: truck cost per km, real spoilage rate in crates, and restaurant willingness to switch.

## 6. Product requirements (minimum working prototype)

The prototype must do three things end to end: a Hindi voice listing, a buyer order, and a Hindi confirmation back to the farmer.

**Farmer listing flow (Hindi-first, voice-first)**

| ID | Requirement | Priority |
| --- | --- | --- |
| F1 | One-shot voice: farmer says “100 किलो टमाटर, 14 रुपये किलो, नासिक, परसों” and all five fields fill | Must |
| F2 | Step-by-step fallback, one question per screen: crop → quantity → price → location → pickup date | Must |
| F3 | Crop picked by picture tiles (🍅 टमाटर, 🧅 प्याज, 🥔 आलू…) as well as voice | Must |
| F4 | Hindi number words understood (“सौ”, “पचास”, “चौदह”) and digits | Must |
| F5 | Read-back: app speaks the listing in Hindi and waits for “हाँ” / ✅ before publishing | Must |
| F6 | Price hint: shows today’s mandi rate and suggested fair price in big digits | Should |
| F7 | Pickup date by relative words (“आज”, “कल”, “परसों”) or a 7-day picture calendar | Should |
| F8 | Works on typed Hindi when voice is not available | Must |

**Buyer page**

| ID | Requirement | Priority |
| --- | --- | --- |
| B1 | Browse live listings with crop, grade, kg left, price, village, pickup date | Must |
| B2 | Filter by crop; see the farmer’s share of every rupee on each listing | Must |
| B3 | Order a quantity (minimum 10 kg) and see the total and delivery day | Must |
| B4 | Bilingual (English + Hindi) labels | Should |

**Confirmation to farmer**

| ID | Requirement | Priority |
| --- | --- | --- |
| C1 | On order, farmer gets a Hindi message: buyer type, kg, amount, pickup date and point | Must |
| C2 | Message is also spoken aloud (text-to-speech) | Must |
| C3 | Production: WhatsApp + SMS + missed-call IVR fallback | Later |

**Non-functional:** works on a ₹7,000 Android phone on 3G; listing screen under 300 KB; every farmer screen usable without reading (icons + voice); all farmer-facing text in Hindi, with Marathi and Bhojpuri next.

## 7. Can a farmer really use this without help?

Honest answer: the first listing is done with the Saathi beside him; from the second listing on, the target is alone in under 90 seconds.

**Design rules for the farmer side**

- **Speak, don’t type.** One big mic button on every screen; the app talks first (“कौन सी फसल बेचनी है?”).
- **Pictures for nouns, big digits for numbers.** Crops are photos/emoji tiles; prices and kg are shown in large ₹ digits, which most farmers read even without reading Hindi words fluently.
- **One question per screen**, with a progress bar of 5 dots.
- **Read-back before anything happens.** The app speaks the full listing; nothing publishes without “हाँ”.
- **Undo is always one tap**; nothing a farmer does can lose money.
- **The same voice everywhere.** Order alerts and payment confirmations arrive as Hindi voice notes, like the WhatsApp voice notes he already uses.

**Usability test for the pilot (pass/fail)**

| Measure | Target |
| --- | --- |
| Second listing completed alone | 8 of 10 farmers |
| Time to complete a listing | under 90 seconds |
| Voice fields corrected by the farmer | under 1 per listing |
| Farmer can say what he will be paid after hearing the confirmation | 9 of 10 farmers |

## 8. Metrics, risks, roadmap and pitch answers

**North-star metric:** farmer’s share of the buyer’s rupee — from 20% today to 58% on B2B orders (₹14 of ₹24).

| Metric | Pilot target (90 days, 1 cluster) |
| --- | --- |
| Active farmers | 150 |
| Repeat B2B buyers | 40 restaurants/grocers |
| Listings sold before pickup | 70% |
| Spoilage farm → buyer | under 10% |
| Farmer paid within 1 hour of pickup | 95% |

**Top risks and responses**

| Risk | Response |
| --- | --- |
| Buyers don’t commit before harvest | Floor promise via local mandi; start with 10 anchor restaurants on weekly standing orders |
| Saathi favours some farmers | Weights and grades logged with photos; farmer hears his own weight read out |
| Truck runs half empty | Pickup days fixed; minimum load before dispatch; combine crops |
| Price crash season | Show mandi rate honestly; no guaranteed price beyond the floor |
| State mandi rules | Pilot in a state that allows direct private trade; Saathi uses existing licences |

**Roadmap**

1. **Hackathon:** voice listing, buyer page, Hindi confirmation (this prototype).
2. **Pilot (3 months):** one cluster near Nashik, one city hub in Pune, tomato + onion.
3. **Phase 2:** NBFC input credit, restaurant supply plans, Marathi and Bhojpuri voice.
4. **Phase 3:** cold-chain for longer routes, more clusters.

**The three pitch answers**

- **Who earns what?** Farmer ₹14/kg (was ₹8), Saathi ₹1.5, truck ₹3, spoilage ₹2, KhetSe ₹2, hub ₹1, payments ₹0.5; restaurant pays ₹24 instead of \~₹30.
- **What happens to middlemen’s services?** Transport becomes a scheduled shared truck; storage is designed out by pre-orders; credit becomes same-day UPI plus NBFC input loans; the aggregator becomes a paid partner.
- **Can a farmer use it alone?** After one assisted listing, yes: voice in, pictures, big digits, Hindi read-back, and a test target of 8 in 10 farmers listing alone.
