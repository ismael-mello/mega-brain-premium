#!/usr/bin/env python3
"""
Append 10x Secrets (10XS) elements to Russell Brunson's DNA.yaml.
120 new elements: 25 PHI + 20 MM + 30 HEUR + 25 FW + 20 MET
"""

import pathlib
import sys
import re

DNA_PATH = pathlib.Path("C:/Users/ISMAEL_MELLO/Downloads/mega-brain-premium/knowledge/external/dna/persons/russell-brunson/DNA.yaml")

# ---------------------------------------------------------------------------
# NEW ELEMENTS
# ---------------------------------------------------------------------------

L1_NEW = """\
    - id: "PHI-RB-201"
      statement: "Teaching is NOT what gets people to buy. What gets people to buy is understanding their belief patterns, and then structuring the content around their belief pattern, finding a belief pattern, breaking it and rebuilding it into the actual truth."
      context: "10x Secrets -- 10XS 01-Course. Perfect Webinar philosophy: content delivery alone does not sell; belief architecture does."
      module_sources:
      - 10XS
    - id: "PHI-RB-202"
      statement: "Selling to the masses is a dead art and the most powerful skill. I'm actually a really bad salesperson one-to-one, but really good at selling to the masses. It's a skill that when you understand it, it's the most powerful thing in the world."
      context: "10x Secrets -- 10XS 01-Course. Stage selling philosophy contrasted with one-to-one sales."
      module_sources:
      - 10XS
    - id: "PHI-RB-203"
      statement: "No one cares about making a million bucks. Nobody does. They want a feeling. The real reason people buy is the internal transformation, not the external result."
      context: "10x Secrets -- 10XS 01-Course + Story Selling FHL. Internal desire drives purchase, not external metrics."
      module_sources:
      - 10XS
    - id: "PHI-RB-204"
      statement: "Everything is choreographed. Why did I point this direction instead of that? Why was I walking? Everything in a $3M presentation is designed down to every gesture."
      context: "10x Secrets -- 10XS 01-Course. Event selling mastery: every physical action on stage has intent."
      module_sources:
      - 10XS
    - id: "PHI-RB-205"
      statement: "The framework is perfect. Don't mess with it. It might shrink -- from 90 min to 30 min to 5 min -- but the structure never changes."
      context: "10x Secrets -- 10XS 01-Course. Perfect Webinar immutability: compress the vehicle, preserve the structure."
      module_sources:
      - 10XS
    - id: "PHI-RB-206"
      statement: "If you leave the backstory before you have connection, you're in trouble. If people died in a movie and you don't care, it's because they didn't spend time in the backstory."
      context: "10x Secrets -- 10XS 01-Course. Story-first selling: rapport requires backstory time investment before advancing."
      module_sources:
      - 10XS
    - id: "PHI-RB-207"
      statement: "Vulnerability creates connection, not authority posturing. The attractive character connects through vulnerability -- 'this is why I'm just like you' -- not bragging."
      context: "10x Secrets -- 10XS 01-Course. Attractive character mechanics: vulnerability over credentials."
      module_sources:
      - 10XS
    - id: "PHI-RB-208"
      statement: "True growth comes from contribution to others. You cannot keep progressing past a certain point until you help somebody else. The only way to grow is by leaping from student to expert."
      context: "10x Secrets -- 10XS FHAT Day 1. Expert identity requires the leap from consuming to contributing."
      module_sources:
      - 10XS
    - id: "PHI-RB-209"
      statement: "First off, no matter what you try in the beginning, it's going to suck. Because you suck. But you'll suck less. And eventually you'll suck so little that you'll actually be good. (Garrett White, adopted by Russell)"
      context: "10x Secrets -- 10XS FHAT Day 1. Iterative mastery philosophy: embrace early failure as the path."
      module_sources:
      - 10XS
    - id: "PHI-RB-210"
      statement: "Copy and persuasion can get cold people in. But if you don't have the foundational movement stuff, everything falls apart. You can sell someone once, but you can't keep selling them unless you build something."
      context: "10x Secrets -- 10XS FHAT Day 1. Movement foundation is required for sustainable selling."
      module_sources:
      - 10XS
    - id: "PHI-RB-211"
      statement: "Self-confidence is for children. Certainty is for men. Whoever comes into a situation the most certain will always win. (Setema, adopted by Russell)"
      context: "10x Secrets -- 10XS FHAT Day 1. Certainty as the dominant persuasion energy on stage."
      module_sources:
      - 10XS
    - id: "PHI-RB-212"
      statement: "Don't sell broke people. Rule number one. The bait you create determines the customers you attract."
      context: "10x Secrets -- 10XS FHAT Day 1. Bait quality determines customer quality; attract the right buyer."
      module_sources:
      - 10XS
    - id: "PHI-RB-213"
      statement: "Stories are the way we create belief now. Sales used to be about copy. Today it's story -- emotional story told the right way. You can lie through copy easily. It's hard to lie through story on camera."
      context: "10x Secrets -- 10XS FHAT Day 2. Video/live era shifts primary belief-creation tool from copy to story."
      module_sources:
      - 10XS
    - id: "PHI-RB-214"
      statement: "People don't really care about achievement. They care about transformation. In every great movie, the real journey we care about is the character's transformation, not whether they hit their goal."
      context: "10x Secrets -- 10XS FHAT Day 2 + Story Selling. Transformation > achievement in emotional resonance."
      module_sources:
      - 10XS
    - id: "PHI-RB-215"
      statement: "Without a vision, the people perish. If they don't have a vision of what's possible, they're gonna fall away. You're gonna lose your people."
      context: "10x Secrets -- 10XS FHAT Day 1. Leader responsibility to paint vivid future possibility for their movement."
      module_sources:
      - 10XS
    - id: "PHI-RB-216"
      statement: "Status is the #1 thing people care about. People will buy anything that increases their perceived status. They will NOT buy anything that decreases their status -- even if it's logically better."
      context: "10x Secrets -- 10XS FHAT Day 1. Status as primary human motivator overriding logic."
      module_sources:
      - 10XS
    - id: "PHI-RB-217"
      statement: "If you know the stories, you should be able to pull them out and just deliver. You should be able to walk in the morning and say I want to sell something and then put it together and boom, go do it."
      context: "10x Secrets -- 10XS FHAT Pitches. Mastery = on-demand story inventory deployment."
      module_sources:
      - 10XS
    - id: "PHI-RB-218"
      statement: "The power to influence others is an awesome power. If you use it for good, you are going to be a wonderful human being and you will change a lot of lives. (John Childers)"
      context: "10x Secrets -- 10XS Childers Chunks. Ethical framing of stage selling power."
      module_sources:
      - 10XS
    - id: "PHI-RB-219"
      statement: "I can sell things I don't believe in because I have learned a system, a method, a way to present words that moves an audience. (John Childers)"
      context: "10x Secrets -- 10XS Childers Chunks. Selling as learnable system independent of product belief."
      module_sources:
      - 10XS
    - id: "PHI-RB-220"
      statement: "Knowledge is the answer to everything. (John Childers -- knowledge overcomes all three walls: lack of knowledge, confidence, and money)"
      context: "10x Secrets -- 10XS Childers Chunks. Three Walls framework resolved by knowledge acquisition."
      module_sources:
      - 10XS
    - id: "PHI-RB-221"
      statement: "Selling is not talking people into buying things they don't want. Selling is uncovering the value of what we have so well that people are happy to exchange the money. (Myron Golden)"
      context: "10x Secrets -- 10XS Masterclass. Value revelation model replaces persuasion model."
      module_sources:
      - 10XS
    - id: "PHI-RB-222"
      statement: "Work with human nature instead of working against it. People love a deal -- why would I not create a deal so it makes it easier for them to say yes? (Myron Golden)"
      context: "10x Secrets -- 10XS Masterclass. Align offer mechanics with innate human psychology."
      module_sources:
      - 10XS
    - id: "PHI-RB-223"
      statement: "If the bonus doesn't have an overwhelming, compelling, oh my God factor, it will actually hurt the sale, not help the sale. (Jason Fladlien)"
      context: "10x Secrets -- 10XS Masterclass. Bonus quality threshold: mediocre bonuses reduce conversion."
      module_sources:
      - 10XS
    - id: "PHI-RB-224"
      statement: "The audience has to love you. They're not buying zip if they don't. It's never the audience's fault -- ever. It's your fault. You didn't talk to them. (Ted Thomas)"
      context: "10x Secrets -- 10XS Masterclass. Speaker takes 100% responsibility for audience connection."
      module_sources:
      - 10XS
    - id: "PHI-RB-225"
      statement: "You never have to sell to sell if you're a pro. The testimonial IS your sale. (Ted Thomas)"
      context: "10x Secrets -- 10XS Masterclass. Proof-first selling: powerful testimonials remove the need for hard selling."
      module_sources:
      - 10XS
"""

L2_NEW = """\
    - id: "MM-RB-181"
      name: Broadway Play Model
      description: "Entrepreneurs put on a Broadway play, it's a smashing success on opening night, and the next day close it and start writing a new play. What you need to do is take that play on the road. (Mary Ellen Tripp)"
      context: "10x Secrets -- 10XS 01-Course. Stop rebuilding; replicate and scale what already works."
      module_sources:
      - 10XS
    - id: "MM-RB-182"
      name: Prolific Index
      description: "On a spectrum from Boring/Mainstream to Crazy, the money is in the middle -- the Prolific Zone. If you can learn it in school, it's mainstream (no money). If it's too crazy, no one buys. The sweet spot is just crazy enough to be interesting but not insane."
      context: "10x Secrets -- 10XS FHAT Day 1. Market positioning framework for niche selection."
      module_sources:
      - 10XS
    - id: "MM-RB-183"
      name: Trading Scale
      description: "All sales is: does this person think that this thing is worth more than their dollar? If they think this offer is worth more than their money, they will trade you."
      context: "10x Secrets -- 10XS 01-Course. Fundamental value exchange model underlying all selling."
      module_sources:
      - 10XS
    - id: "MM-RB-184"
      name: Introduction and Release of Constraints
      description: "Creating urgency through constraints (limited spots, limited time) then releasing them. That's what gets people to jump over tables and fight to get to your thing."
      context: "10x Secrets -- 10XS 01-Course. Stack teaching: tension-release mechanics drive physical action."
      module_sources:
      - 10XS
    - id: "MM-RB-185"
      name: Throwing Rocks at the Red Ocean
      description: "When you create your blue ocean, look backwards and throw rocks at the sub-market. 'How many of you think hiring salespeople will 10X your business? Not gonna happen.' Make all other vehicles irrelevant."
      context: "10x Secrets -- 10XS 01-Course. Blue ocean creation requires active demolition of existing alternatives."
      module_sources:
      - 10XS
    - id: "MM-RB-186"
      name: Identity vs Logic
      description: "There's an identity shift when they feel connected to you. If you connect and they feel part of something, they'll follow you. They don't actually care about the logic."
      context: "10x Secrets -- 10XS Story Selling FHL. Identity-level connection supersedes logical argument."
      module_sources:
      - 10XS
    - id: "MM-RB-187"
      name: Negative Customer Acquisition Cost
      description: "We spend $15 to sell a book, make $33 through the funnel. So customers PAY US $18, then we introduce them to ClickFunnels. VCs couldn't understand it."
      context: "10x Secrets -- 10XS FHAT Day 1. Value ladder funnel mechanics creating negative CAC."
      module_sources:
      - 10XS
    - id: "MM-RB-188"
      name: Bait Determines Customer
      description: "The bait you create attracts the quality of customer you get. Sell 'get rich on internet' -- get broke dreamers. Sell '108 Split Tests' -- get real marketers."
      context: "10x Secrets -- 10XS FHAT Day 1. Intentional bait design as customer quality filter."
      module_sources:
      - 10XS
    - id: "MM-RB-189"
      name: Campaign Slogans Model
      description: "Every winning presidential candidate had a future-based slogan. Losers had present/self-focused slogans. Applied to building your movement's future-based cause."
      context: "10x Secrets -- 10XS FHAT Day 1. Future-pacing as the rhetorical structure of winning movements."
      module_sources:
      - 10XS
    - id: "MM-RB-190"
      name: Expert Plus Business Equals Fuel
      description: "An expert personality wrapped around a business is like a shot of adrenaline. Tony Robbins + financial company = $6 billion raised in 6 months."
      context: "10x Secrets -- 10XS FHAT Day 1. Expert personal brand as business accelerant."
      module_sources:
      - 10XS
    - id: "MM-RB-191"
      name: Four-Minute Mile
      description: "Roger Bannister broke the 4-minute mile in 1954, then everyone started doing it. Create your own '4-minute mile' moment -- show people it's possible."
      context: "10x Secrets -- 10XS FHAT Day 1. Community belief cascade triggered by visible proof of possibility."
      module_sources:
      - 10XS
    - id: "MM-RB-192"
      name: Kryptonite Effect
      description: "Superman is the most boring character until they introduce kryptonite. Sharing your flaws and vulnerabilities is what makes people care. Nobody cares until there's a weakness."
      context: "10x Secrets -- 10XS FHAT Day 1. Vulnerability as the mechanism of character engagement."
      module_sources:
      - 10XS
    - id: "MM-RB-193"
      name: Story Inventory Model
      description: "Every objection needs a pre-built story to counter it. Build an inventory of stories for every single objection. They'll pop out when needed -- but only if practiced hundreds of times. (Dan Kennedy concept)"
      context: "10x Secrets -- 10XS FHAT Day 2. Pre-built story-to-objection mapping as sales infrastructure."
      module_sources:
      - 10XS
    - id: "MM-RB-194"
      name: Comedian Model
      description: "Great comedians don't go straight to Jimmy Fallon. They test in dive bars, keep the 2 jokes that land, throw away 8. Same with webinars -- do them live repeatedly before automating."
      context: "10x Secrets -- 10XS Masterclass. Live-first iteration before automation as quality control."
      module_sources:
      - 10XS
    - id: "MM-RB-195"
      name: Price Marinade
      description: "Give audience a high anchor price at the beginning. Let it soak in while you deliver value. When you reveal the actual (lower) price, it feels like a relief. (Myron Golden)"
      context: "10x Secrets -- 10XS Masterclass. Price anchoring through temporal separation of reveal."
      module_sources:
      - 10XS
    - id: "MM-RB-196"
      name: Four Types of Buyers
      description: "Freeple (want everything free), Cheapo (want cheapest), Fee-ple (willing to pay), Premium (willing to pay premium). You attract the type you ARE. (Myron Golden)"
      context: "10x Secrets -- 10XS Masterclass. Buyer segmentation and self-selection through seller identity."
      module_sources:
      - 10XS
    - id: "MM-RB-197"
      name: Six Audience Segments
      description: "In mass selling, there are always about six groups with different primary buying triggers: risk-averse, reward-driven, trust-based, embarrassment-avoidant, etc. Cycle through all six in your close. (Jason Fladlien)"
      context: "10x Secrets -- 10XS Masterclass. Comprehensive close architecture covering all buyer psychology types."
      module_sources:
      - 10XS
    - id: "MM-RB-198"
      name: Selection Close
      description: "Instead of selling a high-ticket program, make prospects write an essay to be selected. They end up begging you to accept them. Reverses the dynamic from selling to qualifying. (Myron Golden)"
      context: "10x Secrets -- 10XS Masterclass. Role reversal creates desire through exclusivity and application process."
      module_sources:
      - 10XS
    - id: "MM-RB-199"
      name: Three Walls Model
      description: "Every person faces three obstacles -- Lack of Knowledge, Lack of Confidence (Fear), Lack of Money. Knowledge overcomes ALL three. (John Childers)"
      context: "10x Secrets -- 10XS Childers Chunks. Universal objection framework reduced to single root cause."
      module_sources:
      - 10XS
    - id: "MM-RB-200"
      name: IDEAL Investment Formula
      description: "I=Income, D=Deductions, E=Equity, A=Appreciation, L=Leverage. Any investment must pass all five tests. (John Childers)"
      context: "10x Secrets -- 10XS Childers Chunks. Five-filter investment evaluation framework."
      module_sources:
      - 10XS
"""

L3_NEW = """\
    - id: "HEUR-RB-306"
      rule: "1,000 people registered for this webinar every single week = 7-figure webinar model."
      threshold: "1,000 registrants/week minimum for 7-figure outcome"
      context: "10x Secrets -- 10XS 01-Course. Baseline registration volume for profitable automated webinar."
      module_sources:
      - 10XS
    - id: "HEUR-RB-307"
      rule: "25% show-up rate on live webinars. 1,000 register, ~250 show up."
      threshold: "25% show-up rate benchmark"
      context: "10x Secrets -- 10XS 01-Course. Standard live webinar attendance expectation."
      module_sources:
      - 10XS
    - id: "HEUR-RB-308"
      rule: "10% close rate when following the Perfect Webinar script properly."
      threshold: "10% close rate on attended webinar"
      context: "10x Secrets -- 10XS 01-Course. Expected conversion when script is executed correctly."
      module_sources:
      - 10XS
    - id: "HEUR-RB-309"
      rule: "Follow-up sequence (Fri-Sun) doubles live webinar sales."
      threshold: "2x sales multiplier from 3-day follow-up"
      context: "10x Secrets -- 10XS 01-Course. Replay and urgency follow-up sequence impact on total revenue."
      module_sources:
      - 10XS
    - id: "HEUR-RB-310"
      rule: "Facebook ad cost: $3-5 per webinar registrant."
      threshold: "$3-5 cost per registrant benchmark"
      context: "10x Secrets -- 10XS 01-Course. Baseline acquisition cost for webinar funnel viability."
      module_sources:
      - 10XS
    - id: "HEUR-RB-311"
      rule: "Do the webinar live at least 30-40 times before automating (Russell says 75 in FHAT)."
      threshold: "30-75 live runs before automation"
      context: "10x Secrets -- 10XS 01-Course + FHAT. Repetition requirement before evergreen deployment."
      module_sources:
      - 10XS
    - id: "HEUR-RB-312"
      rule: "90% of sales come AFTER the initial price reveal -- The Stack, If/All, QVC closing. Russell threw away 90% of his sales for 5 years."
      threshold: "90% of revenue from post-reveal close mechanics"
      context: "10x Secrets -- 10XS 01-Course. The Stack and post-close sequence is the primary revenue generator."
      module_sources:
      - 10XS
    - id: "HEUR-RB-313"
      rule: "20 seconds MAX on credentials, then back to rapport. Don't keep talking about how great you are."
      threshold: "20-second credential window maximum"
      context: "10x Secrets -- 10XS 01-Course. Rapid credentialing to avoid authority-over-rapport imbalance."
      module_sources:
      - 10XS
    - id: "HEUR-RB-314"
      rule: "If/All close: get 3 yeses before price. 'If all this did was [X], would it be worth it?' Three times."
      threshold: "3 conditional yeses before price reveal"
      context: "10x Secrets -- 10XS 01-Course. Pre-commitment technique compounding before price anchor."
      module_sources:
      - 10XS
    - id: "HEUR-RB-315"
      rule: "Export questions after every live webinar. Identify gaps, add 2-3 slides. Went from $30K to $120K in one iteration."
      threshold: "4x revenue increase from single iteration using Q&A feedback"
      context: "10x Secrets -- 10XS 01-Course. Q&A mining as highest-leverage webinar optimization tool."
      module_sources:
      - 10XS
    - id: "HEUR-RB-316"
      rule: "$2,739/day = $1M/year. Break the goal into daily amounts to make it achievable."
      threshold: "$2,739/day = $1M annual target"
      context: "10x Secrets -- 10XS 01-Course. Daily revenue target decomposition for goal clarity."
      module_sources:
      - 10XS
    - id: "HEUR-RB-317"
      rule: "Improvement offers close 1-2% of audience. New opportunity closes 10-50%+."
      threshold: "New opportunity: 5-50x higher close rate vs improvement offer"
      context: "10x Secrets -- 10XS 01-Course. New opportunity framing superiority in mass conversion."
      module_sources:
      - 10XS
    - id: "HEUR-RB-318"
      rule: "Only 2-3% of population has ambition. Everyone has desire. New opportunities target desire (mass market)."
      threshold: "2-3% ambition-driven; 97%+ desire-driven"
      context: "10x Secrets -- 10XS 01-Course. Mass market psychology favors desire over ambition messaging."
      module_sources:
      - 10XS
    - id: "HEUR-RB-319"
      rule: "Average woman does 8 weight loss plans a year -- proof people are already in vehicles. Your job is to switch them. (Kaelin Poulin data)"
      threshold: "8 vehicle switches/year = high switching readiness"
      context: "10x Secrets -- 10XS 01-Course. Market already in motion; compete for vehicle switches not new buyers."
      module_sources:
      - 10XS
    - id: "HEUR-RB-320"
      rule: "60%+ close rate with constraint introduction and release mechanics (table rush example at 10X)."
      threshold: "60%+ room close rate with table rush mechanics"
      context: "10x Secrets -- 10XS 01-Course. Physical urgency mechanics in live events driving majority close."
      module_sources:
      - 10XS
    - id: "HEUR-RB-321"
      rule: "Price Marinade: get audience to commit to price in first 5-6 minutes. '$11,552 -- will you give me that?'"
      threshold: "Price anchor within first 5-6 minutes of presentation"
      context: "10x Secrets -- 10XS 01-Course. Early anchoring window before value delivery begins."
      module_sources:
      - 10XS
    - id: "HEUR-RB-322"
      rule: "Don't start webinar ads until Monday. Sunday registrants forget by Thursday."
      threshold: "Monday-Wednesday ad window only; no Sunday ads"
      context: "10x Secrets -- 10XS 01-Course. Timing window optimization for Thursday live webinar."
      module_sources:
      - 10XS
    - id: "HEUR-RB-323"
      rule: "35-105 trial closes per 90-minute presentation. Target: 100+ yes's before asking for money. (Ted Thomas)"
      threshold: "35-105 trial closes; target 100+ micro-commitments"
      context: "10x Secrets -- 10XS Masterclass. Micro-commitment density as primary conversion lever."
      module_sources:
      - 10XS
    - id: "HEUR-RB-324"
      rule: "Adding just 7 trial closes to automated webinar increased $/registrant from $9.45 to $16.50 -- 75% increase."
      threshold: "7 trial closes = 75% revenue-per-registrant increase"
      context: "10x Secrets -- 10XS Masterclass. High ROI micro-commitment insertion into existing presentation."
      module_sources:
      - 10XS
    - id: "HEUR-RB-325"
      rule: "Myron Golden repitch: $3.5 million in 30 minutes from the same audience that already bought $4M from Russell."
      threshold: "$3.5M repitch revenue = 87% of initial close on same audience"
      context: "10x Secrets -- 10XS Masterclass. Repitch potential from same audience is near-equal to initial close."
      module_sources:
      - 10XS
    - id: "HEUR-RB-326"
      rule: "Jason Fladlien: $25 million through webinars for someone else's product as affiliate."
      threshold: "$25M affiliate webinar revenue benchmark"
      context: "10x Secrets -- 10XS Masterclass. Webinar mastery applied to affiliate model at scale."
      module_sources:
      - 10XS
    - id: "HEUR-RB-327"
      rule: "Jaime Cross: $120K/summer at farmers markets -- Two Comma Club in 12 months using 5-min Perfect Webinar for $30 soap."
      threshold: "5-min webinar for $30 product = Two Comma Club in 12 months"
      context: "10x Secrets -- 10XS Masterclass. Perfect Webinar framework compressed for low-ticket physical product."
      module_sources:
      - 10XS
    - id: "HEUR-RB-328"
      rule: "Kaelin did 38-40 live webinars in one year. First FB Live (memorized from 40+ live) did $1M+ in 30 days."
      threshold: "40 live runs -- transition to FB Live -- $1M/30 days"
      context: "10x Secrets -- 10XS Masterclass. Repetition to memorization to scaling without slides."
      module_sources:
      - 10XS
    - id: "HEUR-RB-329"
      rule: "If bonus can't create 'oh my God' factor in 5 seconds or less, it hurts the sale. (Jason Fladlien at-a-glance test)"
      threshold: "5-second oh-my-God test for every bonus"
      context: "10x Secrets -- 10XS Masterclass. Bonus quality threshold: instant comprehension + instant desire."
      module_sources:
      - 10XS
    - id: "HEUR-RB-330"
      rule: "First time using The Stack: went from never breaking six figures to $180K in sales in 90 minutes. (Armand Morin taught Russell)"
      threshold: "$180K/90-min first Stack use"
      context: "10x Secrets -- 10XS Masterclass. Documented Russell's first Stack deployment result."
      module_sources:
      - 10XS
    - id: "HEUR-RB-331"
      rule: "One person asks a question = at least 10 people have it. Answer all questions in repitch. (Myron Golden)"
      threshold: "1 question = 10 silent objectors holding same concern"
      context: "10x Secrets -- 10XS Masterclass. Q&A volume multiplier for repitch targeting."
      module_sources:
      - 10XS
    - id: "HEUR-RB-332"
      rule: "High-ticket ($50K+): about 8-10% of room max with Selection Close. (Myron Golden)"
      threshold: "8-10% close rate for $50K+ offers with Selection Close"
      context: "10x Secrets -- 10XS Masterclass. Realistic ceiling for ultra-premium closing in group settings."
      module_sources:
      - 10XS
    - id: "HEUR-RB-333"
      rule: "90% of business is curiosity. If people think they can figure it out on their own, they won't show up."
      threshold: "90% of attendance driven by curiosity gap"
      context: "10x Secrets -- 10XS FHAT Day 2. Curiosity as the dominant lever for engagement and show-up rate."
      module_sources:
      - 10XS
    - id: "HEUR-RB-334"
      rule: "Deleting 700 negative comments on Facebook Live replay cut acquisition cost from $90 to $50 -- literally in half."
      threshold: "Negative comment removal = 44% CAC reduction"
      context: "10x Secrets -- 10XS FHAT Day 3. Social proof hygiene as acquisition cost lever."
      module_sources:
      - 10XS
    - id: "HEUR-RB-335"
      rule: "$165/month for 25 years at 20% yield = $1.4 million. The only variable is what yield you LEARN to get. (John Childers)"
      threshold: "$165/month + 20% yield + 25 years = $1.4M"
      context: "10x Secrets -- 10XS Childers Chunks. Compounding investment formula illustrating knowledge-yield relationship."
      module_sources:
      - 10XS
"""

L4_NEW = """\
    - id: "FW-RB-181"
      name: Event Choreography Framework
      description: "Pre-event hooks -- Audience energy management -- Intro video with social proof -- Origin story with vulnerability -- Three secrets with stories -- Price marinade early -- Stack with visual slides -- Constraint introduction -- Table rush mechanics -- Post-close second-day offer."
      context: "10x Secrets -- 10XS 01-Course. Complete event selling architecture from pre-event to post-close."
      module_sources:
      - 10XS
    - id: "FW-RB-182"
      name: Weekly Webinar Model
      description: "Monday-Wednesday drive registrations (ads, email, JVs) -- Thursday live webinar -- Friday-Saturday-Sunday follow-up/replay -- Sunday midnight offer expires -- Monday restart."
      context: "10x Secrets -- 10XS 01-Course. 7-day weekly rhythm for sustainable webinar revenue engine."
      module_sources:
      - 10XS
    - id: "FW-RB-183"
      name: Five Rapport-Building Tactics
      description: "(1) Justify their failures, (2) Allow their fears, (3) Throw rocks at their enemies, (4) Confirm their suspicions, (5) Encourage their dreams. (Blair Warren's One Sentence Persuasion)"
      context: "10x Secrets -- 10XS 01-Course + FHAT. Five-point rapport architecture using Blair Warren's framework."
      module_sources:
      - 10XS
    - id: "FW-RB-184"
      name: Transition Question Framework
      description: "'A lot of you have learned this stuff. You now believe [vehicle] is right. But how many are overwhelmed and not sure how? You'd love my help? Cool. Let me show you.'"
      context: "10x Secrets -- 10XS 01-Course. Bridge from content delivery to offer introduction using audience agreement."
      module_sources:
      - 10XS
    - id: "FW-RB-185"
      name: Two Choices Close
      description: "Choice 1: Go cheap, can't guarantee success. Choice 2: Costs more, I can devote resources to help guarantee success. Then: What would the result be worth? When I went through this, here's what I paid."
      context: "10x Secrets -- 10XS 01-Course. Binary choice framing forcing value comparison over price comparison."
      module_sources:
      - 10XS
    - id: "FW-RB-186"
      name: QVC Closing (30 min)
      description: "Preload 30 most common questions. Say question, answer, close with URL. Repeat. Weave in 'you're probably thinking this, right?' Resolve concern. Close again. For 30 straight minutes."
      context: "10x Secrets -- 10XS 01-Course. Extended objection marathon turning Q&A into closing engine."
      module_sources:
      - 10XS
    - id: "FW-RB-187"
      name: Include/Exclude Slide
      description: "'How many have a business? Cool, this is for you. Startup phase? Even better -- means you haven't screwed up.' Make everyone feel they belong."
      context: "10x Secrets -- 10XS 01-Course. Audience universalization slide eliminating self-exclusion objections."
      module_sources:
      - 10XS
    - id: "FW-RB-188"
      name: Pain-Cost / Ease-Speed Contrast
      description: "For each stack bonus: introduce it -- show the pain/cost YOU went through -- make it EASY and FAST for THEM. Contrast your pain with their ease."
      context: "10x Secrets -- 10XS 01-Course. Stack bonus framing formula maximizing perceived value through contrast."
      module_sources:
      - 10XS
    - id: "FW-RB-189"
      name: Hero's Two Journeys Story Selling
      description: "(1) Create Rapport (backstory), (2) Introduce Conflict, (3) Show Turning Point, (4) External Achievement + Internal Transformation running parallel, (5) Audience bonds with TRANSFORMATION, not achievement."
      context: "10x Secrets -- 10XS 01-Course (FHL 2017). Dual-journey story architecture for maximum emotional resonance."
      module_sources:
      - 10XS
    - id: "FW-RB-190"
      name: Culture Building Toolkit
      description: "(1) Self-identification label ('funnel hacker'), (2) T-shirt/wearable, (3) Mini Manifesto (phone screensaver), (4) Full Manifesto, (5) Title of Liberty, (6) Four-Minute Mile Marker (Two Comma Club)."
      context: "10x Secrets -- 10XS FHAT Day 1. Six-component toolkit for creating identifiable, self-sustaining movement."
      module_sources:
      - 10XS
    - id: "FW-RB-191"
      name: FHAT Pitch Construction Framework
      description: "Phase 1: Interview/Discovery -- Phase 2: Whiteboard Brainstorm -- Phase 3: Short Break (organize notes) -- Phase 4: Deliver Live in Character -- Phase 5: Debrief (record + transcribe = script)."
      context: "10x Secrets -- 10XS FHAT Pitches. Five-phase rapid pitch assembly for any product in under 30 minutes."
      module_sources:
      - 10XS
    - id: "FW-RB-192"
      name: Secret Title Formula
      description: "'[Desirable outcome] even if [biggest objection/fear]' -- e.g. 'How to have more energy when pregnant than before, even if you have morning sickness.'"
      context: "10x Secrets -- 10XS FHAT Pitches. Title formula preempting primary objection while promising outcome."
      module_sources:
      - 10XS
    - id: "FW-RB-193"
      name: Offer Stack Construction by Layer
      description: "Layer 1: Core System -- Layer 2: Tool per module -- Layer 3: Community/Accountability -- Layer 4: Exclusive access -- Layer 5: Done-for-you element -- Layer 6: Urgency bonus."
      context: "10x Secrets -- 10XS FHAT Pitches. Six-layer offer architecture for maximum perceived value stacking."
      module_sources:
      - 10XS
    - id: "FW-RB-194"
      name: Story Stacking
      description: "When handling objection, don't tell ONE story. Stack 2-3 stories. First tips the domino, second and third knock out remaining excuses."
      context: "10x Secrets -- 10XS FHAT Day 2. Multiple story layering for compound objection demolition."
      module_sources:
      - 10XS
    - id: "FW-RB-195"
      name: Childers Presentation Shell (12 Chunks)
      description: "American Dream -- Working Hard Doesn't Work -- Inflation/Taxes -- Debt Leverage -- IDEAL Formula -- Wealth Formula -- Three Walls -- Minefield -- Method of Learning -- Testimonial -- Your Story -- GROWTH Close. (John Childers)"
      context: "10x Secrets -- 10XS Childers Chunks. Complete 12-segment seminar presentation architecture."
      module_sources:
      - 10XS
    - id: "FW-RB-196"
      name: GROWTH Close
      description: "G=Greater Power, R=Relationships, O=Outlook, W=Wealth, T=Time, H=Health. Emotionally prepares for the offer by transcending money. (John Childers)"
      context: "10x Secrets -- 10XS Childers Chunks. Six-dimension life vision close elevating conversation above price."
      module_sources:
      - 10XS
    - id: "FW-RB-197"
      name: Three-Part Testimonial
      description: "(1) Likeable person, (2) Problem similar to audience's, (3) Overcame with YOUR specific product. Most speakers butcher by not connecting solution to their product. (John Childers)"
      context: "10x Secrets -- 10XS Childers Chunks. Testimonial architecture requiring product-specific resolution."
      module_sources:
      - 10XS
    - id: "FW-RB-198"
      name: Product Pricing Ladder
      description: "$25 Book < $500 Audio/Home Study < $1,000 Video < $5,000+ Live Training with Mentor. Same information, different method of learning = different effectiveness. (John Childers)"
      context: "10x Secrets -- 10XS Childers Chunks. Delivery method determines price ceiling independent of information."
      module_sources:
      - 10XS
    - id: "FW-RB-199"
      name: Trial Close Implementation System
      description: "Write list of questions -- Place keyword reminders -- After every testimonial drop 4-5 trial closes -- After every teaching point 1-2 trial closes -- Never repeat same one -- Practice until natural. (Ted Thomas)"
      context: "10x Secrets -- 10XS Masterclass. Systematic trial close integration across full presentation arc."
      module_sources:
      - 10XS
    - id: "FW-RB-200"
      name: Price Marinade Framework
      description: "(1) Reveal high anchor at beginning, (2) Get commitment, (3) Deliver value while price soaks, (4) Reveal actual lower price, (5) Audience feels relief, (6) Close. (Myron Golden)"
      context: "10x Secrets -- 10XS Masterclass. Six-step price anchoring and relief architecture."
      module_sources:
      - 10XS
    - id: "FW-RB-201"
      name: Repitch Framework
      description: "Phase 1 (Initial) = Emotional sell. Phase 2 (Repitch next day) = Logical sell. Phase 3 (Final push) = Urgency + Scarcity. (Myron Golden)"
      context: "10x Secrets -- 10XS Masterclass. Three-phase emotional-logical-urgency repitch sequence."
      module_sources:
      - 10XS
    - id: "FW-RB-202"
      name: Affiliate Bonus Architecture
      description: "(1) Study vendor's product, (2) Create EXCLUSIVE bonuses that can't be purchased, (3) Pay experts as bonuses, (4) Show proof of investment, (5) 95% of pitch on bonuses, (6) Recruit sub-affiliates. (Jason Fladlien)"
      context: "10x Secrets -- 10XS Masterclass. Six-component affiliate offer construction maximizing bonus dominance."
      module_sources:
      - 10XS
    - id: "FW-RB-203"
      name: You're Probably Thinking Close
      description: "After main close, say 'You're probably thinking [objection]' -- Address thoroughly -- Repeat for EVERY objection -- Continue 60-90+ minutes -- Each addressed triggers new sales wave. (Jason Fladlien)"
      context: "10x Secrets -- 10XS Masterclass. Extended post-close objection marathon structure."
      module_sources:
      - 10XS
    - id: "FW-RB-204"
      name: Kaelin FB Live Webinar
      description: "Hook -- Social proof (live comments) -- Secret 1-2-3 with trial closes -- Urgency strips -- Stack on whiteboard -- Scarcity (100 spots) -- Testimonial visuals -- Push to URL with countdown."
      context: "10x Secrets -- 10XS Masterclass. Slide-free FB Live webinar structure for $30 physical product."
      module_sources:
      - 10XS
    - id: "FW-RB-205"
      name: Perfect Webinar for Physical Products
      description: "Find big domino -- 3 secrets -- Test at 30 min -- Compress until sweet spot (5 min for $30 product) -- Replace stack with urgency/scarcity -- Run as FB ad -- funnel. (Jaime Cross)"
      context: "10x Secrets -- 10XS Masterclass. Perfect Webinar compression methodology for low-ticket physical goods."
      module_sources:
      - 10XS
"""

L5_NEW = """\
    - id: "MET-RB-111"
      name: How to Perfect Your Webinar Through Live Iteration
      steps: "Create first version -- Do it live every Thursday -- Export Q&A after each -- Identify confusion points -- Add 2-3 slides -- Repeat 30-75 times -- When you know every question before they ask, THEN automate."
      context: "10x Secrets -- 10XS 01-Course. Iteration protocol: live testing as prerequisite to automation."
      module_sources:
      - 10XS
    - id: "MET-RB-112"
      name: How to Create Origin Story Earnings Disclaimer
      steps: "State result -- Immediately disclaim -- Slip into backstory -- Make relatable (bills) -- Reveal achievable goal ($2,739/day) -- Ask them to set their goal. Turns legal requirement into rapport-building."
      context: "10x Secrets -- 10XS 01-Course. Compliance-to-connection transformation technique."
      module_sources:
      - 10XS
    - id: "MET-RB-113"
      name: FB Live Perfect Webinar (Kaelin method)
      steps: "Write 3 secrets on paper -- Write stack on whiteboard -- Go live -- Hold up paper 1, tell story -- Paper 2 -- Paper 3 -- Turn to whiteboard, present stack -- Close. 30 min, no slides."
      context: "10x Secrets -- 10XS 01-Course. Minimal-equipment live webinar execution for physical product."
      module_sources:
      - 10XS
    - id: "MET-RB-114"
      name: How to Build Stack Slide
      steps: "Start with core product -- Each bonus addresses a false belief -- Present each with Pain-Cost/Ease-Speed -- Cumulative Stack Slide after each -- 3 If/All statements -- Two Choices -- Price drop -- Guarantee -- Re-stack -- Urgency -- CTA."
      context: "10x Secrets -- 10XS 01-Course. Complete Stack Slide construction and delivery sequence."
      module_sources:
      - 10XS
    - id: "MET-RB-115"
      name: How to Offer Hack
      steps: "Go to ClickBank, competitor sites -- Watch videos, study offer structure -- Note core product, bonuses, stack, pricing -- Study 20-30 offers -- Identify patterns -- Build your stack from best elements."
      context: "10x Secrets -- 10XS 01-Course. Competitive intelligence method for offer architecture research."
      module_sources:
      - 10XS
    - id: "MET-RB-116"
      name: How to Create a Table Rush
      steps: "Introduce constraints throughout close -- Build pressure with energy/speed/urgency -- At critical moment RELEASE constraint ('I'm opening it NOW -- first 50') -- Order forms at tables -- Direct: 'Stand up RIGHT NOW' -- Keep closing from stage."
      context: "10x Secrets -- 10XS 01-Course. Physical urgency mechanics for live event table rush."
      module_sources:
      - 10XS
    - id: "MET-RB-117"
      name: FHAT Pitch Method for Other People's Products
      steps: "Interview subject deeply -- Whiteboard brainstorm -- 5-min break to organize -- Deliver in first person (become them) -- Record -- Transcribe = script. Russell assembled and delivered Alison Prince's pitch in under 25 minutes."
      context: "10x Secrets -- 10XS FHAT Pitches. Rapid pitch assembly for any product in under 30 minutes."
      module_sources:
      - 10XS
    - id: "MET-RB-118"
      name: Build Your Story Inventory
      steps: "List every objection -- Write Epiphany Bridge story for each -- Categorize into Vehicle/Internal/External -- Identify #1 belief per category -- Create curiosity titles (= your 3 Secrets) -- Practice until natural -- Every new objection = new story."
      context: "10x Secrets -- 10XS FHAT Day 2. Systematic story bank construction mapped to belief architecture."
      module_sources:
      - 10XS
    - id: "MET-RB-119"
      name: Create Your New Opportunity
      steps: "Identify core market (Wealth/Health/Relationships) -- Identify sub-market -- Map ecosystem (list competitors) -- CREATE your unique niche -- Test if sub-market is excited -- Verify willing AND able to buy."
      context: "10x Secrets -- 10XS FHAT Day 1. Six-step new opportunity creation and validation process."
      module_sources:
      - 10XS
    - id: "MET-RB-120"
      name: Manifesto Creation
      steps: "Record 30-min rant about what your people stand for -- Pull best parts -- Write rallying cry -- Create phone screensaver version -- Create sticker version (free+shipping) -- Share in community -- Social proof cascade."
      context: "10x Secrets -- 10XS FHAT Day 1. Community manifesto creation and distribution sequence."
      module_sources:
      - 10XS
    - id: "MET-RB-121"
      name: Reverse Engineer Selling Skills
      steps: "Watch best pitchmen on webinars -- Send to rev.com for transcription -- Read transcription 10-15 times -- Identify hooks, closes, transitions -- Practice incorporating -- Test on next webinar -- Iterate."
      context: "10x Secrets -- 10XS FHAT Day 2. Skill acquisition through competitor deconstruction and deliberate practice."
      module_sources:
      - 10XS
    - id: "MET-RB-122"
      name: Kaelin's Weekly Webinar Refinement
      steps: "Every Thursday same time -- Print every comment/question -- Identify unique objections -- Make slides addressing them -- Insert 'you're probably thinking' between stack items -- After 38-40 iterations, transition to FB Live (memorized)."
      context: "10x Secrets -- 10XS Masterclass. 38-40 iteration refinement protocol to memorized delivery."
      module_sources:
      - 10XS
    - id: "MET-RB-123"
      name: Jaime Cross Farmers Market to Funnel
      steps: "Spend years testing pitches face-to-face -- Note what phrases make people buy -- Put exact phrases in funnel copy -- Apply Perfect Webinar framework -- Compress to match price point -- Change from bundle to hero product with upsells."
      context: "10x Secrets -- 10XS Masterclass. Offline testing to online funnel transfer methodology."
      module_sources:
      - 10XS
    - id: "MET-RB-124"
      name: Trial Close Implementation (Beginner)
      steps: "Aim for 5-10 first -- Write keywords on sticky notes -- Place where only you see them -- After testimonials drop 4-5 -- Use gentle questions -- Review video, find 5 more spots -- Build to 25+ -- Goal: 100+. (Ted Thomas)"
      context: "10x Secrets -- 10XS Masterclass. Progressive trial close integration for new practitioners."
      module_sources:
      - 10XS
    - id: "MET-RB-125"
      name: Myron Golden Selection Close (High-Ticket $50K+)
      steps: "Day 1 announce program + marinated price -- Tell success stories -- 'Write me an essay on why I should select you' (1 page, today only) -- Next day call people up -- 'Scale 1-10 how coachable?' -- 'You're being considered' -- They beg to be accepted."
      context: "10x Secrets -- 10XS Masterclass. Role-reversal selection close for ultra-premium offers."
      module_sources:
      - 10XS
    - id: "MET-RB-126"
      name: Repitch Q&A Method (Myron Golden)
      steps: "Collect all questions -- Email: 'I'm going live to answer questions' -- Go live on DIFFERENT platform -- Answer each with a story that disempowers disempowering belief -- Each answer = repitch opportunity -- Close with urgency."
      context: "10x Secrets -- 10XS Masterclass. Question-to-story-to-close repitch sequence on separate platform."
      module_sources:
      - 10XS
    - id: "MET-RB-127"
      name: Jason Fladlien Objection Closing Marathon
      steps: "Flag all questions in real-time -- Transform content questions into objection reframes -- Prioritize questions from potential buyers -- Ask 'What would make this 10/10 for you?' -- Get progressively more aggressive -- Stay 60-90+ min after main close."
      context: "10x Secrets -- 10XS Masterclass. Extended post-close marathon converting remaining objectors."
      module_sources:
      - 10XS
    - id: "MET-RB-128"
      name: Socratic Selling (John Childers)
      steps: "Make a point -- Ask audience for implications -- Let THEM provide ALL answers -- Repeat what they say -- They can never argue because THEY said it -- Result: 'In 20 years, no one ever asked me that question because I didn't teach them anything -- they told me.'"
      context: "10x Secrets -- 10XS Childers Chunks. Audience-generated conclusion technique eliminating all resistance."
      module_sources:
      - 10XS
    - id: "MET-RB-129"
      name: Audience Control in 6 Seconds (Childers)
      steps: "Walk on stage -- Say 'Good morning' with LOW energy -- Audience responds weakly -- Smile: 'Let's try that again' -- 'Good morning!' HIGH energy -- Audience mirrors -- You've taken control."
      context: "10x Secrets -- 10XS Childers Chunks. Six-second stage opening for immediate energy ownership."
      module_sources:
      - 10XS
    - id: "MET-RB-130"
      name: Two Comma Club Milestone Creation
      steps: "Define your community's '4-minute mile' -- Create TANGIBLE marker (trophy) -- Award publicly -- Display prominently -- Make it the visible goal -- As more achieve it, belief cascades through community."
      context: "10x Secrets -- 10XS FHAT Day 1. Visible milestone creation as belief cascade trigger for community."
      module_sources:
      - 10XS
"""

# ---------------------------------------------------------------------------
# MAIN INSERTION LOGIC
# ---------------------------------------------------------------------------

def find_insertion_point(lines, next_layer_pattern):
    """Return the 0-based index just before the next layer header line."""
    for i, line in enumerate(lines):
        if re.match(next_layer_pattern, line):
            return i
    return None

def update_count_line(lines, layer_pattern, delta):
    """Find the count: line inside the given layer and increment it."""
    in_layer = False
    for i, line in enumerate(lines):
        if re.match(layer_pattern, line):
            in_layer = True
            continue
        if in_layer and line.strip().startswith('count:'):
            m = re.match(r'^(\s*count:\s*)(\d+)', line)
            if m:
                new_count = int(m.group(2)) + delta
                lines[i] = m.group(1) + str(new_count)
                return new_count
        # Stop when we hit the next top-level layer or statistics
        if in_layer and (re.match(r'  L[2-5]_', line) or line.startswith('statistics:')):
            break
    return None

def main():
    content = DNA_PATH.read_text(encoding='utf-8')
    lines = content.split('\n')
    print(f"[INFO] Read {len(lines)} lines from DNA.yaml")

    # -----------------------------------------------------------------------
    # INSERT L5 first (to avoid line-number shifts affecting earlier layers)
    # We insert before 'statistics:' line
    # -----------------------------------------------------------------------
    stats_idx = None
    for i, line in enumerate(lines):
        if line.startswith('statistics:'):
            stats_idx = i
            break
    if stats_idx is None:
        print("[ERROR] Could not find 'statistics:' line")
        sys.exit(1)

    l5_items = L5_NEW.rstrip('\n').split('\n')
    lines = lines[:stats_idx] + l5_items + [''] + lines[stats_idx:]
    print(f"[INFO] Inserted {len(l5_items)} L5 lines before statistics: (was line {stats_idx+1})")

    # -----------------------------------------------------------------------
    # INSERT L4 before L5_METHODOLOGIES
    # -----------------------------------------------------------------------
    l5_idx = None
    for i, line in enumerate(lines):
        if re.match(r'  L5_METHODOLOGIES:', line):
            l5_idx = i
            break
    if l5_idx is None:
        print("[ERROR] Could not find L5_METHODOLOGIES")
        sys.exit(1)

    l4_items = L4_NEW.rstrip('\n').split('\n')
    lines = lines[:l5_idx] + l4_items + [''] + lines[l5_idx:]
    print(f"[INFO] Inserted {len(l4_items)} L4 lines before L5 (was line {l5_idx+1})")

    # -----------------------------------------------------------------------
    # INSERT L3 before L4_FRAMEWORKS
    # -----------------------------------------------------------------------
    l4_idx = None
    for i, line in enumerate(lines):
        if re.match(r'  L4_FRAMEWORKS:', line):
            l4_idx = i
            break
    if l4_idx is None:
        print("[ERROR] Could not find L4_FRAMEWORKS")
        sys.exit(1)

    l3_items = L3_NEW.rstrip('\n').split('\n')
    lines = lines[:l4_idx] + l3_items + [''] + lines[l4_idx:]
    print(f"[INFO] Inserted {len(l3_items)} L3 lines before L4 (was line {l4_idx+1})")

    # -----------------------------------------------------------------------
    # INSERT L2 before L3_HEURISTICS
    # -----------------------------------------------------------------------
    l3_idx = None
    for i, line in enumerate(lines):
        if re.match(r'  L3_HEURISTICS:', line):
            l3_idx = i
            break
    if l3_idx is None:
        print("[ERROR] Could not find L3_HEURISTICS")
        sys.exit(1)

    l2_items = L2_NEW.rstrip('\n').split('\n')
    lines = lines[:l3_idx] + l2_items + [''] + lines[l3_idx:]
    print(f"[INFO] Inserted {len(l2_items)} L2 lines before L3 (was line {l3_idx+1})")

    # -----------------------------------------------------------------------
    # INSERT L1 before L2_MENTAL_MODELS
    # -----------------------------------------------------------------------
    l2_idx = None
    for i, line in enumerate(lines):
        if re.match(r'  L2_MENTAL_MODELS:', line):
            l2_idx = i
            break
    if l2_idx is None:
        print("[ERROR] Could not find L2_MENTAL_MODELS")
        sys.exit(1)

    l1_items = L1_NEW.rstrip('\n').split('\n')
    lines = lines[:l2_idx] + l1_items + [''] + lines[l2_idx:]
    print(f"[INFO] Inserted {len(l1_items)} L1 lines before L2 (was line {l2_idx+1})")

    # -----------------------------------------------------------------------
    # UPDATE COUNTS in each layer header
    # -----------------------------------------------------------------------
    additions = {
        r'  L1_PHILOSOPHIES:': 25,
        r'  L2_MENTAL_MODELS:': 20,
        r'  L3_HEURISTICS:': 30,
        r'  L4_FRAMEWORKS:': 25,
        r'  L5_METHODOLOGIES:': 20,
    }

    for pattern, delta in additions.items():
        new_count = update_count_line(lines, pattern, delta)
        layer_name = pattern.strip().rstrip(':')
        print(f"[INFO] Updated {layer_name} count +{delta} -> new count: {new_count}")

    # -----------------------------------------------------------------------
    # UPDATE HEADER: source, modules_processed, total_transcriptions
    # -----------------------------------------------------------------------
    for i, line in enumerate(lines):
        if line.strip().startswith('source:') and 'Two Comma Club' in line:
            lines[i] = '  source: Two Comma Club Coaching - Secrets Masterclass ($4,997) + 10x Secrets'
            print(f"[INFO] Updated source line")
            break

    for i, line in enumerate(lines):
        if line.strip().startswith('modules_processed:'):
            lines[i] = '  modules_processed: 10'
            print(f"[INFO] Updated modules_processed -> 10")
            break

    for i, line in enumerate(lines):
        if line.strip().startswith('total_transcriptions:'):
            lines[i] = '  total_transcriptions: 174'
            print(f"[INFO] Updated total_transcriptions -> 174 (118 + 56)")
            break

    # -----------------------------------------------------------------------
    # UPDATE statistics total_unique_elements and by_layer counts
    # -----------------------------------------------------------------------
    total_new = 120  # 25+20+30+25+20
    for i, line in enumerate(lines):
        if line.strip().startswith('total_unique_elements:'):
            m = re.match(r'^(\s*total_unique_elements:\s*)(\d+)', line)
            if m:
                new_total = int(m.group(2)) + total_new
                lines[i] = m.group(1) + str(new_total)
                print(f"[INFO] Updated total_unique_elements -> {new_total}")
            break

    by_layer_deltas = {
        'philosophies:': 25,
        'mental_models:': 20,
        'heuristics:': 30,
        'frameworks:': 25,
        'methodologies:': 20,
    }

    in_by_layer = False
    for i, line in enumerate(lines):
        if line.strip() == 'by_layer:':
            in_by_layer = True
            continue
        if in_by_layer:
            for key, delta in by_layer_deltas.items():
                if line.strip().startswith(key):
                    m = re.match(r'^(\s*' + key + r'\s*)(\d+)', line)
                    if m:
                        new_val = int(m.group(2)) + delta
                        lines[i] = m.group(1) + str(new_val)
                        print(f"[INFO] Updated by_layer.{key} +{delta} -> {new_val}")
            # Stop after the 5 by_layer entries
            if line.strip() and not any(line.strip().startswith(k) for k in by_layer_deltas):
                if in_by_layer and i > 0 and not lines[i-1].strip() == 'by_layer:':
                    pass  # continue scanning

    # -----------------------------------------------------------------------
    # WRITE BACK
    # -----------------------------------------------------------------------
    output = '\n'.join(lines)
    DNA_PATH.write_text(output, encoding='utf-8')
    print(f"\n[SUCCESS] Written {len(lines)} lines ({len(output):,} bytes) to DNA.yaml")

    # -----------------------------------------------------------------------
    # VERIFY
    # -----------------------------------------------------------------------
    print("\n[VERIFY] Checking new element IDs...")
    verify_ids = [
        'PHI-RB-201', 'PHI-RB-225',
        'MM-RB-181', 'MM-RB-200',
        'HEUR-RB-306', 'HEUR-RB-335',
        'FW-RB-181', 'FW-RB-205',
        'MET-RB-111', 'MET-RB-130',
    ]
    final_content = DNA_PATH.read_text(encoding='utf-8')
    for vid in verify_ids:
        found = vid in final_content
        status = "OK" if found else "MISSING"
        print(f"  [{status}] {vid}")

    print("\n[VERIFY] Checking counts...")
    import yaml
    try:
        data = yaml.safe_load(final_content)
        layers = data['layers']
        for lname in ['L1_PHILOSOPHIES', 'L2_MENTAL_MODELS', 'L3_HEURISTICS', 'L4_FRAMEWORKS', 'L5_METHODOLOGIES']:
            declared = layers[lname]['count']
            actual = len(layers[lname]['items'])
            match = "OK" if declared == actual else "MISMATCH"
            print(f"  [{match}] {lname}: count={declared}, items={actual}")
    except Exception as e:
        print(f"  [WARN] YAML parse check failed: {e}")

if __name__ == '__main__':
    main()
