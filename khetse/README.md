# खेत से · KhetSe

**A Hindi-first, voice-first marketplace that connects farmers directly with restaurants, grocers and housing societies, without pretending middlemen do nothing.**

> “एक किसान 100 किलो टमाटर ₹8 प्रति किलो में बेचता है। वही टमाटर शहर में ₹40 में बिकता है। बीच में 3 बिचौलिए हैं।”
>
> A farmer sells 100 kg of tomatoes at ₹8/kg. The same tomatoes sell for ₹40/kg in the city. There are three middlemen in between.

Built for **Problem Statement 4: The Farm-to-Fork Gap (Agritech)**.

- **Live prototype:** https://claude.ai/artifact/JWuUeMXnVwWuyXipGPXN57
- **Product requirements (PRD):** [`docs/PRD.md`](docs/PRD.md)

---

## The idea

The obvious answer is “an app that cuts out all three middlemen.” It fails, because middlemen carry real costs: transport, storage, credit and spoilage risk. KhetSe keeps the services and removes one layer of margin:

| Today’s layer | KhetSe decision | How |
| --- | --- | --- |
| Village aggregator | **Partner** | Becomes the paid *KhetSe Saathi* (₹1.5/kg): weighs, grades, crates, helps first-time farmers |
| Mandi agent / wholesaler | **Replace** | Pre-orders plus one shared truck per village cluster on fixed days; no warehouse |
| City shop | **Bypass for B2B** | Restaurants and grocers order directly; households order as a society group |

**Who earns what on 100 kg of tomatoes sold to a restaurant at ₹24/kg** (illustrative pilot assumptions):

| Farmer | Truck | Spoilage reserve | KhetSe | Saathi | City hub | Payments | **Buyer pays** |
| --- | --- | --- | --- | --- | --- | --- | --- |
| ₹1,400 (was ₹800) | ₹300 | ₹200 | ₹200 | ₹150 | ₹100 | ₹50 | **₹2,400** (vs ~₹3,000) |

Credit is replaced by UPI payment within an hour of pickup plus NBFC/FPO input loans. Storage is designed out by selling before harvest. Anything unsold goes to the local mandi the same day, so the farmer is never worse off than today.

## What the prototype does

**Farmer’s phone (Hindi-first, voice-first)**
- Say the whole listing in one sentence, for example “100 किलो टमाटर, 14 रुपये किलो, लासलगांव, परसों”, and all five fields fill in: crop, quantity, price, village and pickup date.
- Understands Hindi number words (सौ, पचास, चौदह), Devanagari digits, quintals and relative days (आज, कल, परसों). Typed Hindi works too.
- Crop picture tiles, big ₹ digits, today’s mandi rate and a suggested fair price.
- Reads the listing back aloud in Hindi; nothing is published until the farmer confirms.

**Buyer page**
- Browse listings with grade, kg left, pickup date and the farmer’s share of every rupee.
- Order as a restaurant, grocer or housing society, under your own name.

**Confirmation to the farmer**
- A Hindi message, spoken aloud, says who ordered, from where, what and how much: *“राम राम रमेश जी। ईशान जी ने आपको नया ऑर्डर दिया है…”*

**Pitch website around it:** a scroll-driven tomato journey (₹8 → ₹40), the steelman case for middlemen, a “Break it” moment that attacks the first solution, the refined model, an earnings calculator, and music generated live in the browser that builds as you scroll.

## Hindi voice

The farmer must be able to use KhetSe without reading, so the voice is the core of the product. It works through a fallback chain:

1. **KhetSe built-in voice (default):** a bold male Hindi voice that runs entirely inside the page using eSpeak-NG compiled to WebAssembly. It needs no internet, no install and no installed device voice. A custom voice profile (`tools/khetse.voice`) removes breath, roughness and pitch flutter to stop crackle, and the audio is levelled, EQ’d, compressed and limited so it is loud without clipping.
2. **Sarvam AI Bulbul API (optional):** a natural Indian male voice (“Abhilash”) when you paste your own API key.
3. **Google Hindi TTS API:** a natural female voice, used when the page is hosted where outside requests are allowed.
4. **The device’s own Hindi voice:** the last fallback, via the Web Speech API.

All numbers are converted to Hindi words before speaking (₹1,400 → “एक हज़ार चार सौ रुपये”).

## Run it

It is one self-contained `index.html` file with no build step.

```bash
git clone https://github.com/<your-username>/khetse.git
cd khetse
python3 -m http.server 8000
# open http://localhost:8000
```

Use Chrome or Edge for Hindi voice input. On localhost, the cloud TTS APIs are reachable as well.

### Deploy on GitHub Pages

Settings → Pages → Deploy from branch → `main` / root. The site will be live at `https://<your-username>.github.io/khetse/`.

## Project structure

```
khetse/
├── index.html            # the whole app: pitch site, prototype, voice engine
├── docs/PRD.md           # product requirements, steelman, unit economics
├── tools/
│   ├── khetse.voice      # custom male Hindi voice profile for eSpeak-NG
│   └── build_voice.py    # rebuilds the Hindi-only voice data embedded in index.html
├── LICENSE               # GPL-3.0
└── README.md
```

## Tech

Plain HTML, CSS and JavaScript, with no framework. Web Speech API for Hindi speech recognition. eSpeak-NG (WebAssembly, Hindi data only, ~0.75 MB) for the built-in voice. Web Audio API for voice processing and the live-generated music. Optional Google Translate TTS and Sarvam AI Bulbul APIs. Fonts: Yatra One and Mukta (Google Fonts). Built with Claude (Anthropic).

## What is mocked or simplified

- Listings, farmers, buyers and mandi prices are sample data; all rupee figures are illustrative pilot assumptions.
- No backend: listings and orders are saved in the browser (localStorage).
- The farmer’s phone and WhatsApp-style messages are simulated on the page; no SMS or WhatsApp is sent.
- The Hindi parser understands a fixed set of crops, villages and number words.
- Payments, NBFC credit, truck routing, grading photos and the Saathi app are designed in the PRD but not built.
- In production, API keys would live on a backend, not in the browser.

## Roadmap

1. **Hackathon:** voice listing, buyer page, Hindi confirmation (this prototype).
2. **Pilot (3 months):** one village cluster near Nashik, one city hub in Pune, tomato and onion.
3. **Phase 2:** NBFC input credit, restaurant supply plans, Marathi and Bhojpuri voice.
4. **Phase 3:** cold chain for longer routes, more clusters.

## License

GPL-3.0, because KhetSe embeds [eSpeak-NG](https://github.com/espeak-ng/espeak-ng) (GPL-3.0) via the [Echogarden Emscripten port](https://github.com/echogarden-project/espeak-ng-emscripten). See [`LICENSE`](LICENSE).
