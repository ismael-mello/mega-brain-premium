#!/usr/bin/env python3
"""
Apply 72 enrichments from ENRICHMENTS-STAGING.yaml to DNA.yaml
Each enrichment adds a pdf_enrichments section to the target element
"""
import re

DNA_PATH = r'C:\Users\ISMAEL_MELLO\Downloads\mega-brain-premium\knowledge\dna\persons\russell-brunson\DNA.yaml'

# All 72 enrichments organized by target DNA element ID
ENRICHMENTS = {
    # ============================================================
    # L1 PHILOSOPHIES
    # ============================================================
    "PHI-RB-002": [
        {
            "pdf_source": "DotCom Secrets",
            "page_ref": "PAGE 33",
            "enrichment": "A business is NOT about products and services. A business is about what result you can get for your clients."
        }
    ],
    "PHI-RB-004": [
        {
            "pdf_source": "DotCom Secrets",
            "page_ref": "PAGE 25",
            "enrichment": "The difference between a ten-thousand-dollar website and a ten-million-dollar company was all of the things happening AFTER a buyer came into the initial funnel."
        }
    ],
    "PHI-RB-006": [
        {
            "pdf_source": "DotCom Secrets",
            "page_ref": "PAGE 244",
            "enrichment": "More often than not, it's a FUNNEL problem -- not a traffic or conversion problem."
        }
    ],
    "PHI-RB-017": [
        {
            "pdf_source": "DotCom Secrets",
            "page_ref": "PAGE 52",
            "enrichment": "Your job as the entrepreneur is to understand the strategy and then hire the Facebook guy to run Facebook ads and the Google guy to run Google ads. 'I've never once run a Google or a Facebook ad, yet I've made millions on both platforms.'"
        }
    ],
    "PHI-RB-019": [
        {
            "pdf_source": "Expert Secrets",
            "page_ref": "p.59-65",
            "enrichment": "People don't buy improvement offers. They buy new opportunities. An improvement offer asks people to admit failure. Four reasons improvement offers fail: (1) requires admitting past failure, (2) compares to existing methods, (3) status quo bias, (4) commodity competition."
        }
    ],
    "PHI-RB-027": [
        {
            "pdf_source": "Expert Secrets",
            "page_ref": "p.145-146",
            "enrichment": "If you're not willing to create an environment for change, then you're stealing from your audience. You have a moral obligation to sell."
        }
    ],
    "PHI-RB-029": [
        {
            "pdf_source": "Expert Secrets",
            "page_ref": "p.248",
            "enrichment": "Getting people to give you money is one of the best ways to hold them accountable to their goals. When people invest financially, they commit psychologically."
        }
    ],
    "PHI-RB-031": [
        {
            "pdf_source": "Expert Secrets",
            "page_ref": "p.158-160",
            "enrichment": "Your presentation should NOT teach -- it should INSPIRE and break false beliefs. The moment you start teaching 'how to', you kill the sale. Teaching creates the illusion that they already have what they need."
        }
    ],
    "PHI-RB-033": [
        {
            "pdf_source": "Expert Secrets",
            "page_ref": "p.29-30",
            "enrichment": "If someone always has to be right, nobody will follow them. A charismatic leader is not always right -- they are consistent, clear, and convicted. The crowd follows certainty, not accuracy. Perfectionism kills leadership."
        }
    ],
    "PHI-RB-046": [
        {
            "pdf_source": "Expert Secrets",
            "page_ref": "p.244",
            "enrichment": "Pick a niche, don't pick a fight. If you CREATE your niche (a new opportunity), you'll be complementary to your Dream 100 instead of competing with them."
        }
    ],
    "PHI-RB-018": [
        {
            "pdf_source": "Traffic Secrets",
            "page_ref": "PAGE 36",
            "enrichment": "Companies that become obsessed with their products will eventually fail. The companies that will thrive are the ones that become obsessed with their customers."
        }
    ],
    "PHI-RB-039": [
        {
            "pdf_source": "Traffic Secrets",
            "page_ref": "PAGE 3-5",
            "enrichment": "There's a storm coming. You need to own your traffic before it hits. Platforms (Google, Facebook) regularly change algorithms ('slaps' and 'snaps') that destroy businesses overnight. The only protection is converting all traffic to traffic you own."
        }
    ],
    # ============================================================
    # L2 MENTAL MODELS (some enrich FW elements)
    # ============================================================
    "MM-RB-010": [
        {
            "pdf_source": "DotCom Secrets",
            "page_ref": "PAGE 47-52",
            "enrichment": "Congregations Model: Your dream customers already gather together in existing communities. Three questions: (1) Who is your target market? (beyond demographics, into psychographics), (2) Where are they congregating? (forums, groups, newsletters, blogs), (3) How can you get them to leave and check out your page? (Enquirer Interrupt)."
        }
    ],
    "MM-RB-011": [
        {
            "pdf_source": "DotCom Secrets",
            "page_ref": "PAGE 119-121",
            "enrichment": "Frontend vs Backend Funnel Psychology: Frontend funnels are about acquiring customers (break even or slight loss acceptable). Backend funnels are where all the profit lives. 'The first offer you see probably isn't the primary offer. It's more likely what gets people in the door.' Frontend is the bait; backend is the business."
        }
    ],
    "MM-RB-030": [
        {
            "pdf_source": "DotCom Secrets",
            "page_ref": "PAGE 137",
            "enrichment": "Open/Close Loops: Keep the sales loop OPEN by saying 'Wait! Your order is not yet complete' instead of 'Congratulations' after purchase. Closing the loop kills upsell momentum."
        }
    ],
    "MM-RB-007": [
        {
            "pdf_source": "Expert Secrets",
            "page_ref": "p.26-28",
            "enrichment": "Three Hot Markets -> Submarkets -> Niches hierarchy. Don't start a new market (no demand). Don't compete in an existing niche (commoditized). Create a NEW niche within an existing submarket."
        },
        {
            "pdf_source": "Expert Secrets",
            "page_ref": "p.28-29",
            "enrichment": "The Blue Ocean Strategy applied to niches: Don't compete in a red ocean (crowded niche). Create a blue ocean (new niche/opportunity). But you MUST do it WITHIN a proven submarket -- a blue ocean with no demand is just an empty ocean."
        }
    ],
    "MM-RB-003": [
        {
            "pdf_source": "Expert Secrets",
            "page_ref": "p.93-94",
            "enrichment": "Modus Ponens applied to selling: If A, then B. A is true. Therefore B is true. In sales: If [my new opportunity] is the key to [desired result], and [new opportunity is proven valid], then [prospect must buy]. The Big Domino IS proposition A."
        }
    ],
    # ============================================================
    # L3 HEURISTICS (many enrich FW elements - cross-layer)
    # ============================================================
    "HEUR-RB-019": [
        {
            "pdf_source": "Modules & Scripts",
            "page_ref": "PDF-02-Ladders-Funnels PAGE 6",
            "enrichment": "SLO funnel math: At 30% SLO conversion rate, need 150 front-end sales per month. At 5% opt-in rate, need 3,000 clicks per month (100 per day)."
        }
    ],
    "HEUR-RB-062": [
        {
            "pdf_source": "Expert Secrets",
            "page_ref": "p.123-124",
            "enrichment": "The 'Why' Drill: To find the internal struggle behind any achievement story, ask 'why?' 5-6 times. Surface: 'I wanted to lose weight.' Level 5: 'I wanted my kids to not be ashamed of me at school.' The deep 'why' is the real story."
        }
    ],
    "HEUR-RB-073": [
        {
            "pdf_source": "Expert Secrets",
            "page_ref": "p.212",
            "enrichment": "5% close rate = good webinar, you'll be profitable. 10% close rate = million-dollar webinar. 15% close rate = potential $10M/year business."
        },
        {
            "pdf_source": "Expert Secrets",
            "page_ref": "p.210, p.218",
            "enrichment": "Optimal webinar price range: $297 to $2,997. Below $297, the webinar format is overkill. Above $2,997, you need a different close mechanism (4-Question Close or phone sales)."
        }
    ],
    "HEUR-RB-078": [
        {
            "pdf_source": "Expert Secrets",
            "page_ref": "p.211",
            "enrichment": "Double your sales on the replay. Send replay emails to everyone who registered but didn't buy. The replay typically generates sales equal to the live event."
        },
        {
            "pdf_source": "Network Marketing Secrets",
            "page_ref": "PAGE 173",
            "enrichment": "We see the highest conversion rates on webinar replay pages when we pull down these pages after 48 to 72 hours."
        }
    ],
    "HEUR-RB-087": [
        {
            "pdf_source": "Expert Secrets",
            "page_ref": "p.208-209",
            "enrichment": "$3,000 ad spend -> $50,000+ revenue per week is the target for a mature webinar model. Run the same webinar every week."
        }
    ],
    "HEUR-RB-080": [
        {
            "pdf_source": "Traffic Secrets",
            "page_ref": "PAGE 170-171",
            "enrichment": "80% of your paid ad budget on prospecting will generate only 20% of your results. 20% on retargeting will generate 80% of results."
        }
    ],
    # ============================================================
    # L4 FRAMEWORKS
    # ============================================================
    "FW-RB-001": [
        {
            "pdf_source": "Expert Secrets",
            "page_ref": "p.152-191",
            "enrichment": "Perfect Webinar Structure (4 Parts, 66+ slides): Part 1 -- Introduction/Rapport (slides 1-14), Part 2 -- The One Thing + Origin Story (slides 15-20), Part 3 -- The Three Secrets with Epiphany Bridges (slides 21-48), Part 4 -- The Stack + 16 Closes (slides 49-66+)."
        },
        {
            "pdf_source": "Expert Secrets",
            "page_ref": "p.232-233",
            "enrichment": "Perfect Webinar Cheat Sheet (5 Questions): (Q1) What's the new opportunity I'm offering? (Q2) What is the one Big Domino? (Q3) What special offer/stack can I create? (Q4) What is my Epiphany Bridge origin story? (Q5) What are the 3 false beliefs and corresponding stories? Can be completed in 15 minutes."
        },
        {
            "pdf_source": "Modules & Scripts",
            "page_ref": "PDF-12-FHAT-Event PAGE 1-4",
            "enrichment": "FHAT Event Worksheet (6-Part Implementation): Part 1 = The What and How. Part 2 = The One Thing / Big Domino / Hook. Part 3 = Origin story. Part 4 = False belief patterns and 3 secrets. Part 5 = The Stack Slide. Part 6 = Epiphany bridges for each secret."
        }
    ],
    "FW-RB-002": [
        {
            "pdf_source": "DotCom Secrets",
            "page_ref": "PAGE 157",
            "enrichment": "The Stack improved stage closing from 5-10% to consistently 20%+ of the room. Visual accumulation of value overwhelms price objection."
        }
    ],
    "FW-RB-011": [
        {
            "pdf_source": "Expert Secrets",
            "page_ref": "p.25-32",
            "enrichment": "6 Rules for Charismatic Leaders: (1) Have an attractive character, (2) Have absolute certainty, (3) Don't try to be all things to all people, (4) Flaws are assets, (5) Use self-deprecating humor, (6) Hold nothing back -- radical transparency."
        }
    ],
    "FW-RB-013": [
        {
            "pdf_source": "Expert Secrets",
            "page_ref": "p.75-76",
            "enrichment": "Opportunity Switch Headline Formula: 'How to [desired result] without [pain point they fear] -- even if [common objection].' The 'without' eliminates the biggest fear. The 'even if' pre-handles the top objection."
        }
    ],
    "FW-RB-016": [
        {
            "pdf_source": "Expert Secrets",
            "page_ref": "p.78-80",
            "enrichment": "Ask Campaign requires 100 survey responses to be statistically meaningful. From those 100 responses, 6-8 core questions/pain points will emerge that form the structure of your masterclass or product."
        }
    ],
    "FW-RB-021": [
        {
            "pdf_source": "DotCom Secrets",
            "page_ref": "PAGE 55-56",
            "enrichment": "Traffic Conversion Funnel: Controlled traffic -> Squeeze Page (one option: give email or leave) -> Owned traffic. Uncontrolled traffic -> Blog with squeeze page as top third -> Owned traffic. Two distinct funnels for the two non-owned traffic types."
        }
    ],
    "FW-RB-023": [
        {
            "pdf_source": "DotCom Secrets",
            "page_ref": "PAGE 86",
            "enrichment": "Five Variables Diagnostic: When a campaign fails, it's always one of five things -- Demographics, Offer, Landing Page, Traffic Source, or Ad Copy. Diagnose by isolating variables. Critical rule: never move forward with two unknowns."
        },
        {
            "pdf_source": "DotCom Secrets",
            "page_ref": "PAGE 88",
            "enrichment": "Never move forward with two unknowns. One unknown in your campaign variables is acceptable. Two unknowns means don't enter that market yet. Must know at least 4 of 5 before launching."
        },
        {
            "pdf_source": "DotCom Secrets",
            "page_ref": "PAGE 86-88",
            "enrichment": "Five Variables of Successful Campaigns: (1) Demographics, (2) Offer, (3) Landing Page, (4) Traffic Source, (5) Ad Copy. Must know at least 4 before launching. Diagnostic: isolate variables when campaign fails."
        }
    ],
    "FW-RB-025": [
        {
            "pdf_source": "Expert Secrets",
            "page_ref": "p.234-236",
            "enrichment": "Soap Opera Sequence + Perfect Webinar = Email Epiphany Funnel. Each email corresponds to one section of the Perfect Webinar (Origin Story, Secret 1, Secret 2, Secret 3, Stack). Each email ends with a hook to the next, like a soap opera cliffhanger."
        },
        {
            "pdf_source": "Expert Secrets",
            "page_ref": "p.234-236",
            "enrichment": "Email Epiphany Funnel Structure: Email 1 -- Origin Story + hook. Email 2 -- Secret #1 (Vehicle belief). Email 3 -- Secret #2 (Internal belief). Email 4 -- Secret #3 (External belief). Email 5 -- The Stack + CTA. Each email can contain story OR link to video."
        }
    ],
    "FW-RB-026": [
        {
            "pdf_source": "DotCom Secrets",
            "page_ref": "PAGE 78",
            "enrichment": "Daily email frequency maximizes revenue. Progression: monthly, twice monthly, weekly, twice weekly, every other day, daily -- revenue increased at each frequency increase. 'If I don't email my list every day, I lose money every day.'"
        },
        {
            "pdf_source": "DotCom Secrets",
            "page_ref": "PAGE 78",
            "enrichment": "Seinfeld emails should be 90% entertainment and 10% content. Readership, opens, clicks, and sales all skyrocketed when switching from 100% content to this ratio."
        }
    ],
    "FW-RB-029": [
        {
            "pdf_source": "Network Marketing Secrets",
            "page_ref": "PAGE 60-64",
            "enrichment": "Bridge Funnel Structure: Page 1 = Curiosity squeeze page with 'How to [desire] without [pain]' headline + email capture. Page 2 = Viral Loop video (Epiphany Bridge + Demo + CTA) with button linking to company/distributor page."
        }
    ],
    "FW-RB-031": [
        {
            "pdf_source": "DotCom Secrets",
            "page_ref": "PAGE 123-124",
            "enrichment": "One-Hundred-Visitor Test: Send 100 visitors to your funnel. 1% conversion at $197 = $197/100 visitors. Compare: 8% free+shipping with 25% upsell at $197 = $394/100 visitors (2x revenue)."
        }
    ],
    "FW-RB-033": [
        {
            "pdf_source": "Expert Secrets",
            "page_ref": "p.117-119",
            "enrichment": "Five Turning Points of Conflict in every Epiphany Bridge story: (1) The initial desire, (2) The first wall/obstacle, (3) The epiphany moment, (4) The plan that emerges, (5) The conflict during execution. These 5 points create the emotional arc."
        }
    ],
    "FW-RB-039": [
        {
            "pdf_source": "Expert Secrets",
            "page_ref": "p.195-205",
            "enrichment": "The 16 Closes (in order): (1) Money Is Good, (2) Disposable Income, (3) Money Replenishes, (4) Break Old Habits, (5) Information Alone, (6) Money or Excuses, (7) Your Two Choices, (8) Their Two Choices, (9) Us vs. Them, (10) The Hand Hold, (11) Say Goodbye, (12) Now & Later, (13) Only Excuses, (14) Reluctant Hero, (15) If You Only Got, (16) The Close Close."
        }
    ],
    "FW-RB-042": [
        {
            "pdf_source": "Expert Secrets",
            "page_ref": "p.245",
            "enrichment": "Integration Marketing: Instead of one-time promotions, integrate your offer into the ongoing sales flow of your Dream 100. Put your product on their thank-you pages, in their PS, co-create products. This creates continuous customer streams, not one-time spikes. Accounts for ~20% of traffic."
        },
        {
            "pdf_source": "Network Marketing Secrets",
            "page_ref": "PAGE 50-53",
            "enrichment": "Three Levels of Duplication: Level 1 = you sign people up directly. Level 2 = you ask them to bring people into YOUR funnel and you presell for them. Level 3 = you share funnel links so they copy your funnel, replace videos with theirs, and point buttons to their own distributor links."
        },
        {
            "pdf_source": "Expert Secrets",
            "page_ref": "p.244-245",
            "enrichment": "30% of traffic from Dream 100 promotions, 40% from paid ads targeting Dream 100 audiences, 10% from organic/SEO, 20% from integration marketing. This is the ideal traffic mix."
        },
        {
            "pdf_source": "Expert Secrets",
            "page_ref": "p.242",
            "enrichment": "Dream 100 list composition: 25 list owners + 25 bloggers + 25 podcasters + 25 social media influencers = 100 people who already have your dream customers' attention."
        },
        {
            "pdf_source": "Expert Secrets",
            "page_ref": "p.240",
            "enrichment": "Dream 100: After 4 months of consistent outreach with zero response, Chet Holmes landed Xerox. By month 6, he had 29 of 167 targets. Patience + pig-headed determination = breakthrough."
        },
        {
            "pdf_source": "Expert Secrets",
            "page_ref": "p.244-245",
            "enrichment": "3 Promotion Strategies for Dream 100: Strategy 1 -- Get them to promote your webinar to their audience (30% of traffic). Strategy 2 -- Run paid ads targeting their followers (40% of traffic). Strategy 3 -- Integration marketing into their sales flow (20% of traffic)."
        }
    ],
    "FW-RB-045": [
        {
            "pdf_source": "DotCom Secrets",
            "page_ref": "PAGE 160",
            "enrichment": "Invisible Funnel results: 550 registrations, 85% show rate (vs 30% for free webinars), 90% payment rate (only 10% cancel), $23.5K revenue from $47 price point."
        }
    ],
    "FW-RB-046": [
        {
            "pdf_source": "DotCom Secrets",
            "page_ref": "PAGE 167-170",
            "enrichment": "Product Launch Funnel (4 videos): Video 1: Wow and How (pattern interrupt, big promise). Video 2: Transformational Education (teach, build belief). Video 3: Ownership Experience (let them experience result). Video 4: The Offer (present with Stack). One video per day over 4 days."
        },
        {
            "pdf_source": "Expert Secrets",
            "page_ref": "p.237-238",
            "enrichment": "Epiphany Product Launch Funnel: (1) Intro video with Origin Story + opt-in. (2) Video #1 = Secret #1. (3) Video #2 = Secret #2. (4) Video #3 = Secret #3. (5) Video #4 = The Stack. (6) Send non-webinar-attendees through this sequence."
        }
    ],
    "FW-RB-050": [
        {
            "pdf_source": "DotCom Secrets",
            "page_ref": "PAGE 173",
            "enrichment": "High-ticket two-step process: reduced from 60 salespeople to 2 with same revenue output by using setter+closer model with application funnel."
        },
        {
            "pdf_source": "Expert Secrets",
            "page_ref": "p.218",
            "enrichment": "The 4-Question Close is for offers priced $2,997 to $100,000. At these prices, you cannot close on a webinar -- you need a personal conversation."
        },
        {
            "pdf_source": "Expert Secrets",
            "page_ref": "p.218-226",
            "enrichment": "The 4-Question Close Script: Phase 1 (5-10 min) -- Build rapport. Phase 2 (20-30 min) -- Ask the 4 Questions, let them talk 80%. Phase 3 (10-15 min) -- Present solution mapped to THEIR words. Phase 4 (5-10 min) -- Handle logistics. Total: 45-60 minutes."
        },
        {
            "pdf_source": "Modules & Scripts",
            "page_ref": "PDF-07-The-Funnels PAGE 4-6",
            "enrichment": "The 4-Question High-Ticket Close exact language: Q1 = 'If we worked together and I taught you everything, what would make you believe this was the best decision you ever made?' Q2 = 'Why don't you have it yet? What's been holding you back?' Q3 = 'What resources do you have that you're not utilizing 100%?' Q4 = 'Do you want me to help you?' Then stop talking until they answer."
        }
    ],
    "FW-RB-051": [
        {
            "pdf_source": "DotCom Secrets",
            "page_ref": "PAGE 136",
            "enrichment": "Three OTO Structures: (1) The Next Thing -- logical next step, (2) Do It Faster -- speed/shortcut tool, (3) Need Help? -- done-for-you service or coaching."
        }
    ],
    # ============================================================
    # L5 METHODOLOGIES (some enrich FW elements - cross-layer)
    # ============================================================
    "FW-RB-043": [
        {
            "pdf_source": "DotCom Secrets",
            "page_ref": "PAGE 124-126",
            "enrichment": "Free-Plus-Shipping Order Form Bump Strategy: (1) Free item, (2) Charge shipping $4.95-$9.95, (3) Add bump checkbox at $37, (4) Add OTO at $97-$197, (5) Add downsell. Expected: 34% bump rate, $66 average revenue per free item."
        }
    ],
    "FW-RB-048": [
        {
            "pdf_source": "DotCom Secrets",
            "page_ref": "PAGE 139-147",
            "enrichment": "Star/Story/Solution Script (44 pieces in 3 sections): Section 1: STAR (pattern interrupt, core promise, CTA preview). Section 2: STORY (high drama, backstory, wall, epiphany, plan, results). Section 3: SOLUTION (present offer, build value, stack, guarantee, scarcity, final CTA)."
        }
    ],
    "FW-RB-049": [
        {
            "pdf_source": "DotCom Secrets",
            "page_ref": "PAGE 133-135",
            "enrichment": "Who/What/Why/How Script for Two-Step Free+Shipping Funnel: Page 1: Squeeze page with bait. Page 2: Sales page -- WHO are you? WHAT do you have? WHY do I need it? HOW can I get it? Page 3: Order form with bump. Page 4-5: OTO upsells."
        }
    ],
    "MET-RB-002": [
        {
            "pdf_source": "Expert Secrets",
            "page_ref": "p.155-166",
            "enrichment": "Perfect Webinar Introduction Sequence (Slides 1-14): Slide 1 -- Title. Slides 2-6 -- One Sentence Persuasion (one element per slide). Slides 7-8 -- Ruler and Progression. Slides 9-10 -- Qualify yourself. Slides 11-12 -- Origin Story. Slide 13 -- Liken to Them. Slide 14 -- Case Study."
        },
        {
            "pdf_source": "Modules & Scripts",
            "page_ref": "PDF-06-Moral-Obligation PAGE 5-57",
            "enrichment": "Perfect Webinar Slide Script (51 Slides): 1-Title, 2-Intro/Rapport, 3-Ruler Goal #1, 4-Ruler Goal #2 Big Domino, 5-Goal Continued, 6-Qualify Yourself, 7-Epiphany Bridge Origin, 8-Liken to Them, 9-Case Study, 10-Transition to Secrets, 11-Delivering Content, 12-State Secret, 13-Share Epiphany Bridge, 14-Show Results, 15-Break Beliefs, 16-Restate New Belief, 17-Repeat Secrets 2&3, 18-The Question, 19-Transition to Sales, 20-The Stack, 21-Deliverables, 22-Recap, 23-Case Studies, 24-Who This Works For, 25-Destroy #1 Reason, 26-Stack Slide #1, 27-Element #2 Tools, 28-You'll Be Able To, 29-Problem Solved, 30-Time/Money Saved, 31-Break Beliefs, 32-Stack Slide #2, 33-Tangible #1, 34-Pain/Cost, 35-Ease/Speed, 36-Break Beliefs, 37-Stack Slide #3, 38-Tangibles #2/#3, 39-Big Stack #5, 40-If/All, 41-Two Choices, 42-What Would It Be Worth, 43-Price Drop, 44-Price Reveal, 45-Price Justification, 46-2 Choices, 47-Guarantee, 48-Real Question, 49-Stack Slide, 50-Urgency/Scarcity, 51-Close/Q&A."
        }
    ],
    "MET-RB-006": [
        {
            "pdf_source": "Expert Secrets",
            "page_ref": "p.234-236",
            "enrichment": "Email Epiphany Funnel Creation: (1) Take your completed PW content. (2) Extract 4 core stories (Origin + 3 Secrets). (3) Write each story as email OR record video and link. (4) Add Stack as final email with CTA. (5) Add soap opera hooks at end of each email. (6) Deploy as automated sequence."
        }
    ],
    "MET-RB-012": [
        {
            "pdf_source": "Expert Secrets",
            "page_ref": "p.192-193",
            "enrichment": "Trial Closes increased per-registrant earnings from $9.45 to $16.50 -- a 74% improvement."
        },
        {
            "pdf_source": "Expert Secrets",
            "page_ref": "p.192-194",
            "enrichment": "Trial Closes Implementation: Insert at specific points: (1) After the Big Promise, (2) After each Secret, (3) Before revealing the Stack, (4) After each Stack component, (5) Before the price reveal. Track hand raises/chat responses."
        }
    ],
    "MET-RB-013": [
        {
            "pdf_source": "Modules & Scripts",
            "page_ref": "PDF-10-Post-Webinar-FollowUps PAGE 1-6",
            "enrichment": "Post-webinar email sequence timing: Immediately after -> 3 hours later -> 24 hours -> 48 hours -> 72 hours -> 96 hours -> 120 hours -> 144 hours -> final day (cart close)."
        }
    ],
    "MET-RB-014": [
        {
            "pdf_source": "Expert Secrets",
            "page_ref": "p.218-226",
            "enrichment": "4-Question Close Methodology: Phase 1 (5-10 min) -- Build rapport. Phase 2 (20-30 min) -- Ask 4 Questions, let them talk 80%. Phase 3 (10-15 min) -- Present solution in THEIR words. Phase 4 (5-10 min) -- Handle logistics. Total: 45-60 minutes."
        }
    ],
    # Additional enrichments (FW elements enriched by MET PDF items)
    "FW-RB-051_OTO": None,  # Already covered above as FW-RB-051
}

# Remove None entries
ENRICHMENTS = {k: v for k, v in ENRICHMENTS.items() if v is not None}

# Also handle the OTO script (from MET section - enriches FW-RB-051)
# This is already in FW-RB-051 above

# Add the OTO script enrichment that's listed under MET in the staging file
if "FW-RB-051" in ENRICHMENTS:
    ENRICHMENTS["FW-RB-051"].append({
        "pdf_source": "DotCom Secrets",
        "page_ref": "PAGE 136-138",
        "enrichment": "OTO Script Structure: (1) 'Wait! Your order is not yet complete!' (keep loop open), (2) Acknowledge smart purchase, (3) One-sentence pitch of next offer, (4) Urgency -- truly one time only, (5) If they say no -> downsell with payment plan."
    })

# Add FW-RB-045 invisible funnel method (from MET section)
if "FW-RB-045" in ENRICHMENTS:
    ENRICHMENTS["FW-RB-045"].append({
        "pdf_source": "DotCom Secrets",
        "page_ref": "PAGE 159-165",
        "enrichment": "Invisible Funnel Webinar Method: (1) Create 3-4 hour deep-dive training, (2) Attendees register with credit card, (3) 'Try before you buy' -- only charged IF they don't cancel, (4) 85% show rate vs 30% free, (5) 90% payment rate."
    })

# Add FW-RB-050 setter+closer from MET section
if "FW-RB-050" in ENRICHMENTS:
    ENRICHMENTS["FW-RB-050"].append({
        "pdf_source": "DotCom Secrets",
        "page_ref": "PAGE 173-184",
        "enrichment": "High-Ticket Two-Step Script: Step 1 SETTER (15-30 min): Build rapport, ask about situation, identify pain, present application, set appointment. Step 2 CLOSER (45-90 min): Recap application, deep dive into pain, present high-ticket offer with Stack, handle objections, close."
    })


def format_pdf_enrichments(enrichments_list):
    """Format enrichments as YAML block to append to an element"""
    lines = ["        pdf_enrichments:"]
    for e in enrichments_list:
        lines.append(f"          - pdf_source: \"{e['pdf_source']}\"")
        lines.append(f"            page_ref: \"{e['page_ref']}\"")
        # Escape quotes in enrichment text
        text = e['enrichment'].replace('"', "'")
        lines.append(f"            enrichment: \"{text}\"")
    return "\n".join(lines)


def apply_enrichments(content, enrichments_dict):
    """Apply all enrichments to the DNA.yaml content"""

    applied = 0
    skipped = 0

    for dna_id, enrichments_list in enrichments_dict.items():
        # Find the element by ID
        search_pattern = f'id: "{dna_id}"'
        idx = content.find(search_pattern)

        if idx == -1:
            print(f"WARNING: {dna_id} not found!")
            skipped += 1
            continue

        # Check if pdf_enrichments already exists for this element
        # Find the next element start or end of block
        # Look for the next '      - id:' pattern after this one
        next_item_pattern = '      - id:'
        next_idx = content.find(next_item_pattern, idx + len(search_pattern))

        # Check if pdf_enrichments already in this block
        block = content[idx:next_idx] if next_idx != -1 else content[idx:]

        if 'pdf_enrichments:' in block:
            print(f"  SKIP {dna_id}: pdf_enrichments already exists")
            skipped += 1
            continue

        # Find the end of this element's block (before next element or section)
        if next_idx == -1:
            # Last element - find end of file or next section
            insert_pos = len(content)
        else:
            insert_pos = next_idx

        # Find the last non-empty line in this block to insert after
        block_end = content.rfind('\n', idx, insert_pos)
        if block_end == -1:
            block_end = insert_pos

        # Build the enrichment YAML
        enrichment_yaml = format_pdf_enrichments(enrichments_list)

        # Insert after the last line of the element
        content = content[:block_end] + '\n' + enrichment_yaml + content[block_end:]

        applied += 1
        print(f"  OK {dna_id}: {len(enrichments_list)} enrichment(s) added")

    return content, applied, skipped


# Read DNA.yaml
with open(DNA_PATH, 'r', encoding='utf-8') as f:
    content = f.read()

print(f"Processing {len(ENRICHMENTS)} unique elements with enrichments...")
print(f"Total enrichment entries: {sum(len(v) for v in ENRICHMENTS.values())}")
print()

# Apply enrichments
new_content, applied, skipped = apply_enrichments(content, ENRICHMENTS)

print()
print(f"Results: {applied} elements enriched, {skipped} skipped")
print(f"Original lines: {len(content.split(chr(10)))}")
print(f"New lines: {len(new_content.split(chr(10)))}")

# Write updated file
with open(DNA_PATH, 'w', encoding='utf-8') as f:
    f.write(new_content)

print()
print("DNA.yaml updated successfully!")
