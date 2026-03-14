"""
Insert Funnel University 2016 DNA elements into Russell Brunson DNA.yaml
40 elements: 10 PHI + 7 MM + 12 HEUR + 6 FW + 5 MET
"""

with open('C:/Users/ISMAEL_MELLO/Downloads/mega-brain-premium/knowledge/external/dna/persons/russell-brunson/DNA.yaml', 'r', encoding='utf-8') as f:
    content = f.read()

fu_phi = """
      # --- Funnel University 2016 Philosophies ---
      - id: "PHI-RB-120"
        statement: "Content marketing should self-liquidate. The goal is not to make profit from your content -- it's to break even. If you spend a dollar to get someone to listen, read, or watch your content, and you make a dollar back immediately, your entire audience growth becomes free. That's the power of a Self-Liquidating Offer (SLO)."
        context: "FU Issue 1 / Self-Liquidating Content - Mike Dillard Self Made Man case study. Russell's core thesis on content monetization."
        tags: ["content-marketing", "slo", "fu2016", "self-liquidating"]
        confidence: 0.95
        module_sources: [FU2016]
        raw_source: "knowledge/external/sources/russell-brunson/raw/17._Funnel_University_2016/"

      - id: "PHI-RB-121"
        statement: "There are only two reasons to publish content: (1) to find your voice -- even if nobody shows up, you're becoming better; (2) to discover what your audience responds to -- the topics that get engagement tell you what to do more of. Publishing is a feedback loop, not just a broadcast."
        context: "FU Issue 1 / Self-Liquidating Content. Russell's philosophy on content creation as discovery mechanism."
        tags: ["content-marketing", "publishing", "fu2016"]
        confidence: 0.92
        module_sources: [FU2016]
        raw_source: "knowledge/external/sources/russell-brunson/raw/17._Funnel_University_2016/"

      - id: "PHI-RB-122"
        statement: "Cold traffic requires a bridge -- you cannot sell directly from cold interest to your offer. Someone who just voted to impeach Obama won't sign up for ClickFunnels. There's nothing connecting those two things. You must build a bridge that takes them from where they are emotionally to where you need them to be."
        context: "FU Issue 1 / Political Bridge. The fundamental insight about cold traffic conversion."
        tags: ["cold-traffic", "bridge", "fu2016"]
        confidence: 0.95
        module_sources: [FU2016]
        raw_source: "knowledge/external/sources/russell-brunson/raw/17._Funnel_University_2016/"

      - id: "PHI-RB-123"
        statement: "The best funnels push people AWAY. Don't try to appeal to everyone -- create a funnel that filters for your dream client. If some people are offended, if some people self-select out, that's working AS DESIGNED. The goal is the core few who are exactly right, not the masses who are sort of right."
        context: "FU Issue 2 / Warrior Week case study (Garrett White). The polarization-as-filter philosophy."
        tags: ["filtering", "positioning", "high-ticket", "fu2016"]
        confidence: 0.95
        module_sources: [FU2016]
        raw_source: "knowledge/external/sources/russell-brunson/raw/17._Funnel_University_2016/"

      - id: "PHI-RB-124"
        statement: "You must sell the desire at every single step. Don't just say give me your email and send you a documentary. Pitch it. Create desire for why they NEED to watch it. If there's no desire, they won't give the email, and they certainly won't watch 2 hours. Every page is a sales page."
        context: "FU Issue 2 / Warrior Week funnel analysis. Garrett White model -- every step must sell the next step."
        tags: ["desire", "high-ticket", "documentary-funnel", "fu2016"]
        confidence: 0.95
        module_sources: [FU2016]
        raw_source: "knowledge/external/sources/russell-brunson/raw/17._Funnel_University_2016/"

      - id: "PHI-RB-125"
        statement: "When you have a buyer at a certain price point, you MUST sell them the next thing. A $5,000 buyer has more money to spend. A $10,000 Warrior Week attendee will buy a $50,000 program. If you don't have a next offer, you're leaving massive money on the table. The moment of highest conversion is immediately after an amazing experience."
        context: "FU Issue 2 / High Ticket Funnel (Warrior Week). Russell's reflection on backend offer stacking."
        tags: ["backend", "offer-stack", "high-ticket", "fu2016"]
        confidence: 0.95
        module_sources: [FU2016]
        raw_source: "knowledge/external/sources/russell-brunson/raw/17._Funnel_University_2016/"

      - id: "PHI-RB-126"
        statement: "Sell one specific thing from your library, not the whole library. Nobody wants to pay for a library card -- they want the ONE book they need right now. Pull out individual pieces of your membership/content and sell each as its own front-end offer. Different pieces attract different market segments."
        context: "FU Issue 3 / Digital Marketer Continuity Funnel. Ryan Deiss model that took DM from hundreds to tens of thousands of continuity members."
        tags: ["continuity", "splinter-offer", "membership", "fu2016"]
        confidence: 0.95
        module_sources: [FU2016]
        raw_source: "knowledge/external/sources/russell-brunson/raw/17._Funnel_University_2016/"

      - id: "PHI-RB-127"
        statement: "Indoctrination before the sale is the key to high-ticket. Don't sell on the first touch. Build culture, community, belonging FIRST. Let them watch hours of content, fill out applications, go through a process -- by the time they talk to sales, they're already sold. The sale is just the formality."
        context: "FU Issue 2 / Warrior Week funnel. Average person watches 2-hour documentary 4x before applying = 8+ hours before purchase."
        tags: ["indoctrination", "high-ticket", "pre-selling", "fu2016"]
        confidence: 0.95
        module_sources: [FU2016]
        raw_source: "knowledge/external/sources/russell-brunson/raw/17._Funnel_University_2016/"

      - id: "PHI-RB-128"
        statement: "People don't just want to BUY your thing -- they want to BELONG to something. The most powerful funnels create a movement, a tribe, an identity. When they join Warrior Week, they're not buying training -- they're becoming a Warrior. Build your funnel around belonging, not just benefit."
        context: "FU Issue 2 / Warrior Week. The experiential funnel philosophy -- belonging over benefit."
        tags: ["belonging", "tribe", "community", "fu2016"]
        confidence: 0.95
        module_sources: [FU2016]
        raw_source: "knowledge/external/sources/russell-brunson/raw/17._Funnel_University_2016/"

      - id: "PHI-RB-129"
        statement: "The goal of a continuity self-liquidating offer is to cover ad costs with the backend upsell, not the recurring billing. Build in a $300-400 high-ticket upsell right after the $1 trial. The trial builds the membership. The high ticket pays for the ads. Any continuity revenue is pure profit on top."
        context: "FU Issue 3 / Digital Marketer Continuity Funnel analysis. Russell's insight on continuity funnel economics."
        tags: ["continuity", "slo", "fu2016", "economics"]
        confidence: 0.95
        module_sources: [FU2016]
        raw_source: "knowledge/external/sources/russell-brunson/raw/17._Funnel_University_2016/"
"""

fu_mm = """
      # --- Funnel University 2016 Mental Models ---
      - id: "MM-RB-103"
        name: "Splinter Content Model"
        description: "Your membership/library is the POOL. Each individual piece of content is a BUCKET from that pool. You sell each bucket separately to attract a specific market segment, then offer the whole pool as the upsell. Every bucket has the same backend ($1 trial to high-ticket). New bucket = new front-end funnel = new market segment."
        tags: ["continuity", "membership", "splinter", "fu2016"]
        confidence: 0.95
        module_sources: [FU2016]
        raw_source: "knowledge/external/sources/russell-brunson/raw/17._Funnel_University_2016/"

      - id: "MM-RB-104"
        name: "Food Court Test (Cold Traffic)"
        description: "Imagine 500 people in a mall food court. Stand up and pitch your offer. If most would raise their hands = cold traffic ready. If only your niche would raise their hands = warm traffic offer only. To pass the food court test, you need something universally desirable (free money-making website) not niche-specific (learn to build a funnel)."
        tags: ["cold-traffic", "offer-design", "fu2016"]
        confidence: 0.95
        module_sources: [FU2016]
        raw_source: "knowledge/external/sources/russell-brunson/raw/17._Funnel_University_2016/"

      - id: "MM-RB-105"
        name: "Documentary Funnel Model"
        description: "For high-ticket offers, replace the short-form squeeze page with an experiential documentary. The documentary does 3 things: builds desire, creates belonging, and pre-sells the high-ticket. People watch a 2-hour doc 4 times before applying. That's 8 hours of brand immersion before you ever talk to them."
        tags: ["documentary-funnel", "high-ticket", "fu2016"]
        confidence: 0.95
        module_sources: [FU2016]
        raw_source: "knowledge/external/sources/russell-brunson/raw/17._Funnel_University_2016/"

      - id: "MM-RB-106"
        name: "Self-Liquidating Content Loop"
        description: "You pay money to show content. Content builds audience. SLO at end of content breaks even. Audience is now free. Bigger audience = easier to launch next product. The content IS the ad. The SLO makes it free. The audience is the asset."
        tags: ["content-marketing", "slo", "flywheel", "fu2016"]
        confidence: 0.95
        module_sources: [FU2016]
        raw_source: "knowledge/external/sources/russell-brunson/raw/17._Funnel_University_2016/"

      - id: "MM-RB-107"
        name: "Dream 100 as Content Distribution"
        description: "When you interview someone from your Dream 100, you're not just getting content -- you're getting access to THEIR audience. They'll share the interview with their followers. Each interview is a new front-end bait targeted at a new audience pool. The interviewee's audience becomes YOUR list."
        tags: ["dream-100", "content-distribution", "fu2016"]
        confidence: 0.95
        module_sources: [FU2016]
        raw_source: "knowledge/external/sources/russell-brunson/raw/17._Funnel_University_2016/"

      - id: "MM-RB-108"
        name: "Controversial Optin Model"
        description: "Controversial/polarizing survey questions get higher optins and double opt-in confirmation than neutral offers because emotional engagement drives action. Should Obama be impeached? generates 2M+ free optins because nobody is neutral -- they HAVE to vote. Find the polarizing angle in your market."
        tags: ["optin", "survey", "cold-traffic", "fu2016"]
        confidence: 0.92
        module_sources: [FU2016]
        raw_source: "knowledge/external/sources/russell-brunson/raw/17._Funnel_University_2016/"

      - id: "MM-RB-109"
        name: "Positioning by Exclusion"
        description: "High-ticket funnels should EXCLUDE wrong prospects as explicitly as they include right ones. Are you a man or woman? removes women. Are you a married businessman? filters immediately. The act of exclusion increases perceived exclusivity and desire in those who qualify."
        tags: ["positioning", "exclusion", "high-ticket", "fu2016"]
        confidence: 0.95
        module_sources: [FU2016]
        raw_source: "knowledge/external/sources/russell-brunson/raw/17._Funnel_University_2016/"
"""

fu_heur = """
      # --- Funnel University 2016 Heuristics ---
      - id: "HEUR-RB-162"
        rule: "Invisible Funnel prepay rate: 70-80% of registrants will choose to prepay (at $20 discount) over the pay-only-if-you-love-it option. Despite the funnel being positioned as free, the majority choose to pay upfront when given a small savings incentive."
        tags: ["invisible-funnel", "prepay", "benchmarks", "fu2016"]
        confidence: 0.92
        module_sources: [FU2016]
        raw_source: "knowledge/external/sources/russell-brunson/raw/17._Funnel_University_2016/"

      - id: "HEUR-RB-163"
        rule: "Invisible Funnel upsell conversion: ~18% of Invisible Funnel buyers will take an upsell offer immediately after registering. Even on a free/pay-if-you-love-it offer, 18% upsell conversion is achievable."
        tags: ["invisible-funnel", "upsell", "benchmarks", "fu2016"]
        confidence: 0.90
        module_sources: [FU2016]
        raw_source: "knowledge/external/sources/russell-brunson/raw/17._Funnel_University_2016/"

      - id: "HEUR-RB-164"
        rule: "Invisible Funnel show-up rate: 85-90% vs ~30% for standard free webinars. The credit card on file creates accountability. People show up because they feel committed even if they haven't paid yet."
        tags: ["invisible-funnel", "show-rate", "webinar", "fu2016"]
        confidence: 0.92
        module_sources: [FU2016]
        raw_source: "knowledge/external/sources/russell-brunson/raw/17._Funnel_University_2016/"

      - id: "HEUR-RB-165"
        rule: "Documentary pre-purchase consumption: Average Warrior Week prospect watches 2-hour documentary 4 times before applying = 8-10+ hours of content consumption before becoming a lead. High-ticket buyers self-qualify through consumption, not forms."
        tags: ["documentary-funnel", "high-ticket", "consumption", "fu2016"]
        confidence: 0.90
        module_sources: [FU2016]
        raw_source: "knowledge/external/sources/russell-brunson/raw/17._Funnel_University_2016/"

      - id: "HEUR-RB-166"
        rule: "High-ticket event close rate: 6 out of 8 Warrior Week attendees (~75%) bought a $50,000 backend program at the end of the 4-day event. Experiential events create extraordinary close rates compared to any other format."
        tags: ["high-ticket", "close-rate", "event", "fu2016"]
        confidence: 0.90
        module_sources: [FU2016]
        raw_source: "knowledge/external/sources/russell-brunson/raw/17._Funnel_University_2016/"

      - id: "HEUR-RB-167"
        rule: "Political quiz funnels: 2M+ optins per year at near-zero cost. Controversial/polarizing surveys with mandatory double opt-in to confirm your vote can generate massive volume because the emotional hook drives confirmation behavior."
        tags: ["survey-funnel", "cold-traffic", "optins", "fu2016"]
        confidence: 0.90
        module_sources: [FU2016]
        raw_source: "knowledge/external/sources/russell-brunson/raw/17._Funnel_University_2016/"

      - id: "HEUR-RB-168"
        rule: "Continuity front-end adoption: Less than 10% of continuity members come through the core membership sales page. 90%+ are acquired through splinter front-end offers ($7-10) that pull out one specific piece of the library. This is how Digital Marketer went from hundreds to tens of thousands of members."
        tags: ["continuity", "splinter", "membership", "fu2016"]
        confidence: 0.93
        module_sources: [FU2016]
        raw_source: "knowledge/external/sources/russell-brunson/raw/17._Funnel_University_2016/"

      - id: "HEUR-RB-169"
        rule: "DCSLabs Two Tiny Words: Adding I Agree checkbox to order confirmation forms increased Dollars Per Lead (DPL) by 74.61%. Getting micro-commitments from buyers before they complete purchase dramatically increases completion rates and LTV."
        tags: ["conversion-optimization", "micro-commitment", "split-test", "fu2016"]
        confidence: 0.95
        module_sources: [FU2016]
        raw_source: "knowledge/external/sources/russell-brunson/raw/17._Funnel_University_2016/"

      - id: "HEUR-RB-170"
        rule: "Downsell payment plan insight: When you offer a payment plan downsell (e.g. 3x$67 vs $197 pay-in-full), a significant percentage of no-buyers choose to pay IN FULL on the downsell page. They just needed one more push. Don't assume the payment plan is what people want -- the full-pay option on a downsell page converts well."
        tags: ["downsell", "payment-plan", "conversion", "fu2016"]
        confidence: 0.88
        module_sources: [FU2016]
        raw_source: "knowledge/external/sources/russell-brunson/raw/17._Funnel_University_2016/"

      - id: "HEUR-RB-171"
        rule: "Cold traffic advertorial strategy: Drive freezing cold traffic to advertorial (pre-sell article) then they click to VSL. Drive warm traffic (Facebook, JV) directly to squeeze page then optin then VSL. Same VSL, two entry points, each optimized for traffic temperature."
        tags: ["cold-traffic", "advertorial", "funnel-structure", "fu2016"]
        confidence: 0.92
        module_sources: [FU2016]
        raw_source: "knowledge/external/sources/russell-brunson/raw/17._Funnel_University_2016/"

      - id: "HEUR-RB-172"
        rule: "Invisible Funnel option pricing: Offer both (1) pay nothing now, pay $X in 5 days if you loved it, and (2) prepay and save $20. Between 70-80% choose prepay. The pay-nothing option acts as a risk-reversal headline, but buyers self-select into prepay at high rates."
        tags: ["invisible-funnel", "pricing", "prepay", "fu2016"]
        confidence: 0.92
        module_sources: [FU2016]
        raw_source: "knowledge/external/sources/russell-brunson/raw/17._Funnel_University_2016/"

      - id: "HEUR-RB-173"
        rule: "$10 DM splinter offer + $1 trial upsell + $395 self-liquidating backend: This 3-step continuity acquisition funnel is designed so the $395 backend covers ad costs (self-liquidates), the $1 trial converts members, and the $38/mo continuity is pure profit. Front-end ($7-10) is designed to break even or lose money -- it's only a lead magnet for the continuity."
        tags: ["continuity", "economics", "splinter", "fu2016"]
        confidence: 0.93
        module_sources: [FU2016]
        raw_source: "knowledge/external/sources/russell-brunson/raw/17._Funnel_University_2016/"
"""

fu_fw = """
      # --- Funnel University 2016 Frameworks ---
      - id: "FW-RB-104"
        name: "Self-Liquidating Content Funnel (SLO Funnel)"
        components: "1) Content Channel (podcast/video/blog) 2) Dream 100 Interviews - each = new audience pool 3) Blog/Subscribe page 4) Thank-you > SLO Video (story + soft pitch) 5) Simple product offer ($47-97) - goal: BREAK EVEN not profit"
        purpose: "Make content marketing cost-free by breaking even on subscriber acquisition"
        tags: ["content-marketing", "slo", "dream-100", "fu2016"]
        confidence: 0.95
        module_sources: [FU2016]
        raw_source: "knowledge/external/sources/russell-brunson/raw/17._Funnel_University_2016/"

      - id: "FW-RB-105"
        name: "Political Bridge (Cold Traffic Survey) Funnel"
        components: "1) Controversial Ad (polarizing question) 2) Survey Page - emotional response, name/email/zip 3) Thank-you: Confirm your vote > forced double opt-in 4) Survey Results Page 5) Bridge Page - mini article transitioning topic to offer 6) VSL or Sales Page"
        purpose: "Generate massive cold optins from political/emotional topics then bridge to offer"
        notes: "NewsMax model got 2M+ optins/year at near-zero cost"
        tags: ["cold-traffic", "survey", "bridge-funnel", "fu2016"]
        confidence: 0.92
        module_sources: [FU2016]
        raw_source: "knowledge/external/sources/russell-brunson/raw/17._Funnel_University_2016/"

      - id: "FW-RB-106"
        name: "High-Ticket Documentary Funnel (Warrior Week Model)"
        components: "1) Squeeze Page - sells the documentary (3-4 min video pitching WHY to watch) 2) Documentary Page (60-120+ min) with Video Spoiler Box 3) Apply Button > Application Page (exclusion questions) 4) Indoctrination Page - videos + schedule call + private content 5) Sales Call 6) High-Ticket Event ($10k) 7) Backend Offer ($50k) pitched at event"
        close_rates: "~75% of event attendees buy $50k backend"
        tags: ["documentary-funnel", "high-ticket", "warrior-week", "fu2016"]
        confidence: 0.95
        module_sources: [FU2016]
        raw_source: "knowledge/external/sources/russell-brunson/raw/17._Funnel_University_2016/"

      - id: "FW-RB-107"
        name: "Digital Marketer Continuity Splinter Funnel"
        components: "1) Pull individual pieces from membership library 2) Create sales page for EACH piece - $7-10 targeting specific segment 3) Universal Upsell (same for ALL front-ends): $1 trial > $38/mo membership 4) Self-Liquidating Backend: certification/advanced course $395 5) Repeat: every new piece = new front-end, same backend"
        key_insight: "<10% buy through main membership page; 90%+ through splinters"
        tags: ["continuity", "splinter", "membership", "fu2016"]
        confidence: 0.95
        module_sources: [FU2016]
        raw_source: "knowledge/external/sources/russell-brunson/raw/17._Funnel_University_2016/"

      - id: "FW-RB-108"
        name: "REO Rockstar VSL Funnel (Cold Traffic Optimized)"
        components: "1A) Pre-Sale Advertorial (cold traffic) - 5-paragraph article 1B) Squeeze Page with audio whisper (warm traffic) 1C) Exit Pop - text version of VSL offer 2) Video Sales Letter - $37 front-end 3) Upsell 1: $197 course (if no > Downsell: 3x$67 OR pay-in-full) 4) Upsell 2: $97/mo continuity (if no > 30-day free trial)"
        tags: ["vsl-funnel", "cold-traffic", "advertorial", "fu2016"]
        confidence: 0.92
        module_sources: [FU2016]
        raw_source: "knowledge/external/sources/russell-brunson/raw/17._Funnel_University_2016/"

      - id: "FW-RB-109"
        name: "Invisible Funnel (Pay Only If You Love It)"
        components: "1) Sales Page - Attend free, pay $X only if you double your result + prepay option at discount (70-80% take this) 2) Upsell Page - bundle of related products ($197) 3) Members Area - webinar delivery + replay 4) Live Webinar - 3-4 hours, deliver tangible result 5) At End - pitch high-ticket program"
        show_up_rate: "85-90%"
        prepay_rate: "70-80%"
        upsell_cvr: "~18%"
        best_use: "Internal list (warm audience), not cold traffic"
        tags: ["invisible-funnel", "webinar", "fu2016"]
        confidence: 0.95
        module_sources: [FU2016]
        raw_source: "knowledge/external/sources/russell-brunson/raw/17._Funnel_University_2016/"
"""

fu_met = """
      # --- Funnel University 2016 Methodologies ---
      - id: "MET-RB-062"
        name: "How to Launch a Self-Liquidating Content Funnel"
        steps: "1) Choose ONE content channel (podcast, video, blog) - stick to it 2) Build Dream 100 list of people with audiences in your market 3) Interview Dream 100 members - each interview = new audience pool 4) Create dedicated page per interview 5) Drive their audience to their interview page > blog subscribe 6) Blog subscribe > SLO video (use popup order form) 7) Sell $47-97 product - goal: break even on acquisition cost 8) Add upsells later once core funnel converts"
        key_metric: "Cost to acquire subscriber = Revenue from SLO, target 1:1 ratio"
        tags: ["content-marketing", "slo", "dream-100", "fu2016"]
        confidence: 0.95
        module_sources: [FU2016]
        raw_source: "knowledge/external/sources/russell-brunson/raw/17._Funnel_University_2016/"

      - id: "MET-RB-063"
        name: "Political Bridge Funnel Build Process"
        steps: "1) Identify hot/controversial topic in audience's life 2) Create polarizing question (no middle ground - forces emotional response) 3) Build survey page collecting email + vote 4) Redirect to confirm your vote > double opt-in (high confirm rate due to passion) 5) Show results page > bridge page 6) Bridge page: mini article OR video transitioning from topic to offer 7) From bridge > VSL or direct offer 8) Monetize list additionally by selling ad space to complementary offers"
        food_court_test: "Before building, test: Would masses at a mall food court raise their hand for my bridge offer?"
        tags: ["survey-funnel", "cold-traffic", "bridge", "fu2016"]
        confidence: 0.92
        module_sources: [FU2016]
        raw_source: "knowledge/external/sources/russell-brunson/raw/17._Funnel_University_2016/"

      - id: "MET-RB-064"
        name: "Invisible Funnel Launch Sequence"
        steps: "1) Identify deliverable result achievable in ONE live session 2) Build sales page: headline = the result + or you don't pay 3) Write out 3-step rules clearly (credit card reserve > attend > pay if loved) 4) Add prepay option at $20 discount (70-80% take it) 5) Build upsell: bundle related products, 18% conversion expected 6) Build members area: handouts pre-loaded, webinar link, replay after 7) Promote to warm list (NOT cold traffic) 8) Live webinar: deliver result in 3-4 hours 9) At end: if you have high-ticket offer, pitch it HERE 10) 5 days after: bill those who loved it, honor cancellations"
        tags: ["invisible-funnel", "webinar", "fu2016"]
        confidence: 0.95
        module_sources: [FU2016]
        raw_source: "knowledge/external/sources/russell-brunson/raw/17._Funnel_University_2016/"

      - id: "MET-RB-065"
        name: "Digital Marketer Continuity Machine - Ongoing Operation"
        steps: "1) Build/have core membership site with library of content 2) Identify 10-20 individual pieces from library 3) For each piece: build dedicated sales page targeting specific market segment ($7-10) 4) All front-ends lead to SAME upsell: $1 trial to get everything 5) After trial upsell: self-liquidating backend ($300-400 certification/advanced) 6) Launch new front-end each week (just swap piece, keep same backend) 7) Track which front-ends attract which segments, double down on winners"
        key_note: "Two upsell pages NEVER CHANGE. Only front-end changes per launch."
        tags: ["continuity", "membership", "splinter", "fu2016"]
        confidence: 0.95
        module_sources: [FU2016]
        raw_source: "knowledge/external/sources/russell-brunson/raw/17._Funnel_University_2016/"

      - id: "MET-RB-066"
        name: "Documentary Funnel Build Process (for High-Ticket)"
        steps: "1) Film 60-120 min documentary (experiential footage, emotion, story - testimonials, transformation stories, behind-the-scenes) 2) Create squeeze page: 3-4 min video SELLING why they need to watch documentary 3) Documentary page: video + video spoiler box (chapter breakdown) 4) Application flow: personal video + qualifying form with exclusion questions 5) Indoctrination page: videos + book call + private content access 6) Sales call: by this point buyer is pre-sold (consumed 8+ hours of content) 7) Event/experience: deliver amazing result 8) Backend pitch: at end of experience, pitch higher-tier program"
        note: "Works best when you have experiential component (event, mastermind, week-long training)"
        tags: ["documentary-funnel", "high-ticket", "fu2016"]
        confidence: 0.95
        module_sources: [FU2016]
        raw_source: "knowledge/external/sources/russell-brunson/raw/17._Funnel_University_2016/"
"""

# Markers to find insertion points
markers = [
    (
        'transcription_6.txt"\n\n      # --- ITH MENTAL MODELS ---',
        'transcription_6.txt"\n' + fu_phi + '\n      # --- ITH MENTAL MODELS ---',
        "PHI insertion"
    ),
    (
        'transcription_12.txt"\n\n      # --- ITH HEURISTICS',
        'transcription_12.txt"\n' + fu_mm + '\n      # --- ITH HEURISTICS',
        "MM insertion"
    ),
    (
        "        module_sources: [ITH]\n\n      # --- ITH FRAMEWORKS ---",
        "        module_sources: [ITH]\n" + fu_heur + "\n      # --- ITH FRAMEWORKS ---",
        "HEUR insertion"
    ),
    (
        "        module_sources: [ITH]\n\n      # --- ITH METHODOLOGIES ---",
        "        module_sources: [ITH]\n" + fu_fw + "\n      # --- ITH METHODOLOGIES ---",
        "FW insertion"
    ),
    (
        "        module_sources: [ITH]\n\n      # --- Fast Product Development (FPD) Methodologies ---",
        "        module_sources: [ITH]\n" + fu_met + "\n      # --- Fast Product Development (FPD) Methodologies ---",
        "MET insertion"
    ),
]

for old, new, label in markers:
    count = content.count(old)
    if count == 0:
        print(f"ERROR: {label} marker not found!")
    elif count > 1:
        print(f"WARNING: {label} marker found {count} times, replacing first only")
        content = content.replace(old, new, 1)
    else:
        print(f"OK: {label} marker found, replacing")
        content = content.replace(old, new, 1)

# Verify all IDs present
checks = ['PHI-RB-120', 'PHI-RB-129', 'MM-RB-103', 'MM-RB-109', 'HEUR-RB-162', 'HEUR-RB-173', 'FW-RB-104', 'FW-RB-109', 'MET-RB-062', 'MET-RB-066']
print("\nVerification:")
all_ok = True
for c in checks:
    found = c in content
    print(f'  {c}: {"OK" if found else "MISSING"}')
    if not found:
        all_ok = False

if all_ok:
    with open('C:/Users/ISMAEL_MELLO/Downloads/mega-brain-premium/knowledge/external/dna/persons/russell-brunson/DNA.yaml', 'w', encoding='utf-8') as f:
        f.write(content)
    print(f'\nFile written successfully! Lines: {content.count(chr(10))}')
else:
    print('\nERROR: Not all elements found. File NOT written.')
