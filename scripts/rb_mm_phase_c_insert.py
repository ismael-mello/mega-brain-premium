#!/usr/bin/env python3
"""
RB-MM Phase C: Welcome (MM-08) insertion
Source: inbox/Dan Kennedy & Russell Brunson - Magnetic Marketing/transcription_mp4_00-Welcome_.txt
RB-unique elements only (DK content excluded - already in DK DNA)
Next IDs: PHI-RB-198, MM-RB-178, HEUR-RB-301, FW-RB-179, MET-RB-110
"""
import yaml
import sys
import shutil
from pathlib import Path

DNA_PATH = Path("knowledge/external/dna/persons/russell-brunson/DNA.yaml")
BACKUP_PATH = DNA_PATH.with_suffix(".yaml.bak_phase_c")

# ============================================================
# MM-08: WELCOME (RB-unique elements from DK interview)
# ============================================================

PHASE_C_ELEMENTS = {
    "L1_PHILOSOPHIES": [
        {
            "id": "PHI-RB-198",
            "statement": "Build your business on a solid foundation of strategies, not fly-by-night tactics. The reason I've been in business for over two decades is because my business was not built on these fly-by-night tactics. Tactics are things that work today but are gone tomorrow -- the fleeting things. Strategies are the principles from the best marketers in the world that last forever.",
            "context": "MM Welcome video -- RB's opening address announcing ClickFunnels acquisition of Magnetic Marketing. Core philosophy explaining WHY he acquired DK's company: to give the next generation strategies, not tactics.",
            "module_sources": ["MM-08-Welcome"],
        },
        {
            "id": "PHI-RB-199",
            "statement": "When you find your mentor's work and it changes your life, you have an obligation to pass it on to the next generation. I was 20 years old when I ran into Dan Kennedy's stuff and it changed my life forever. I want to bring that to the next generation of entrepreneurs.",
            "context": "MM Welcome -- RB explaining the personal mission behind acquiring Magnetic Marketing. Mentorship legacy as moral obligation (parallels PHI-RB-001 moral obligation to sell).",
            "module_sources": ["MM-08-Welcome"],
        },
        {
            "id": "PHI-RB-200",
            "statement": "You don't run an internet business. You run a business and you happen to use the internet as a channel. The medium is just the delivery mechanism -- the underlying marketing principles are what matter.",
            "context": "MM Welcome -- RB recounting one of the first lessons he learned from DK. Reframing from 'internet marketer' to 'marketer who uses internet'. Fundamental shift in identity and approach.",
            "module_sources": ["MM-08-Welcome"],
        },
    ],
    "L2_MENTAL_MODELS": [
        {
            "id": "MM-RB-178",
            "name": "Five Fatal Flaws of Funnels",
            "description": "Framework for diagnosing funnel failures through 5 core principles learned from Dan Kennedy. Designed to help funnel hackers look at their funnels and business differently using foundational marketing principles rather than internet-only tactics.",
            "context": "MM Welcome -- RB's structured interview framework with DK. The 5 flaws represent gaps between internet marketing tactics and foundational direct response principles.",
            "module_sources": ["MM-08-Welcome"],
        },
        {
            "id": "MM-RB-179",
            "name": "Strategies vs Tactics Mental Model",
            "description": "Two-tier evaluation of any marketing approach: (1) Is this a STRATEGY (timeless principle that works across media and eras) or a TACTIC (platform-specific trick that expires)? Build your foundation on strategies, use tactics for execution. When tactics stop working, strategies remain.",
            "context": "MM Welcome -- RB's core thesis for acquiring Magnetic Marketing. All internet marketing training teaches tactics; DK's material teaches strategies. The combination creates sustainable businesses.",
            "module_sources": ["MM-08-Welcome"],
        },
        {
            "id": "MM-RB-180",
            "name": "Webinar Mastery Through Repetition",
            "description": "When you find a presentation that works, do it 100+ times back to back until the AV crew can set their watch by when you say each sentence. Every joke, water break, and transition becomes muscle memory. Inspired by Kavett Robert's principle (via DK): 'It's infinitely easier to get a new qualified audience than it is to get a new speech that works.'",
            "context": "MM Welcome -- RB describing his ClickFunnels launch webinar experience. Did the same 75-minute presentation 100+ times. AV crew knew his timing to the second. Direct application of DK's 'ride the winner' principle.",
            "module_sources": ["MM-08-Welcome"],
        },
    ],
    "L3_HEURISTICS": [
        {
            "id": "HEUR-RB-301",
            "rule": "When you bomb at speak-to-sell, the problem is almost never your teaching -- it's your pitch. You can blow minds with content and still sell zero if you don't have a structured close. Teaching alone does not convert to sales.",
            "context": "MM Welcome -- RB recounting bombing at speaking events early in career. Thought teaching great content = sales. Learned from DK that platform selling requires specific pitch mechanics separate from content delivery.",
            "module_sources": ["MM-08-Welcome"],
        },
        {
            "id": "HEUR-RB-302",
            "rule": "When you find a working webinar/presentation, deploy it in every media channel you can that at least breaks even (if you have a back end). A winning message should be converted to direct mail, video ads, email, stage -- every possible deployment. Don't create new content when your winner hasn't been fully deployed.",
            "context": "MM Welcome -- DK's multi-media deployment principle as applied by RB. ClickFunnels webinar went from live to automated to multiple media. Same message, maximum distribution.",
            "module_sources": ["MM-08-Welcome"],
        },
        {
            "id": "HEUR-RB-303",
            "rule": "The difference between a standing ovation and getting credit cards is massive. Getting applause is easy -- getting people to buy requires a completely different skill set. Never confuse audience engagement with conversion ability.",
            "context": "MM Welcome -- DK teaching RB about platform selling. Standing ovation vs credit cards distinction. Joan Rivers example: amazing entertainer, sold 2 units first attempt because she skipped the 16-minute pitch.",
            "module_sources": ["MM-08-Welcome"],
        },
        {
            "id": "HEUR-RB-304",
            "rule": "Fatal Flaw #1 of Funnels: Focusing only on funnel mechanics without understanding the marketing fundamentals underneath. A funnel is just a delivery mechanism for a marketing message -- if the message sucks, the funnel fails regardless of design.",
            "context": "MM Welcome -- First of RB's Five Fatal Flaws framework. The realization that waking up one day and questioning whether money was coming from the funnel or from good marketing was the first shift.",
            "module_sources": ["MM-08-Welcome"],
        },
        {
            "id": "HEUR-RB-305",
            "rule": "As acquisition costs rise (and they always do), whoever figures out how to spend the most for their lead and their sale wins. They buy speed, scale, discouragement of competition, and sustainability. You must figure this out without going bankrupt -- you need a shorter runway than Uber's 12 years.",
            "context": "MM Welcome -- DK's 'whoever can spend the most to acquire a customer wins' applied to modern context. RB connecting DK's principle to Facebook/Apple privacy wars driving costs up. Mathematical gravity of direct marketing.",
            "module_sources": ["MM-08-Welcome"],
        },
    ],
    "L4_FRAMEWORKS": [
        {
            "id": "FW-RB-179",
            "name": "Annoying Pest to Most Welcome Guest Framework",
            "description": "The transformation from pest to guest happens through RIGHT MESSAGE + RIGHT TIME alignment. Example: solicitor is annoying pest until your house is on fire and he says 'you call the fire department, I'll work the hose.' Only thing that changed was message-timing alignment. Applied to email: sending 8 emails/day doesn't fix the pest problem -- you need to become the welcome guest with relevant, timely value.",
            "context": "MM Welcome -- DK's parable about door-to-door solicitors, taught during Five Fatal Flaws discussion. RB identifies this as a core principle missing from internet marketing: most marketers optimize for frequency (more emails, more ads) when they should optimize for relevance.",
            "module_sources": ["MM-08-Welcome"],
        },
        {
            "id": "FW-RB-180",
            "name": "Equity in Customers Framework",
            "description": "Three things everyone wants: freedom, wealth, and security. NONE come from what you do (skills/work); all three come from what you OWN. The most controllable asset is yourself (personality, knowledge, skill). The second hardest to lose is equity in your customers. When DK got divorced, he took the customer list (illiquid) and rebuilt in 18 months. 'Send the invoice to the herd' -- with strong customer equity, you can recover from any setback.",
            "context": "MM Welcome -- DK's wealth philosophy as captured by RB. Customer equity > cash. List > Lamborghini. This directly informs RB's obsession with building email lists and customer relationships over one-time transactions.",
            "module_sources": ["MM-08-Welcome"],
        },
    ],
    "L5_METHODOLOGIES": [
        {
            "id": "MET-RB-110",
            "name": "Speak-to-Sell Recovery Method",
            "description": "Step 1: Accept you bombed (teaching != selling). Step 2: Study the specific pitch mechanics (not content). Step 3: Create a timed, scripted close separate from your teaching content. Step 4: Practice the pitch until it's flawless. Step 5: Deploy 100+ times to different audiences. Joan Rivers proof: admitted failure to audience, re-did the 16-minute pitch properly, killed it. Next night, killed it from the start.",
            "context": "MM Welcome -- RB synthesizing his own speak-to-sell failure + DK's Joan Rivers case study into a recovery methodology. The key insight: your pitch is a separate skill from your teaching. Practice them independently.",
            "module_sources": ["MM-08-Welcome"],
        },
    ],
}

def main():
    print("=" * 60)
    print("RB-MM PHASE C: WELCOME (MM-08)")
    print("=" * 60)

    # Backup
    shutil.copy2(DNA_PATH, BACKUP_PATH)
    print(f"Backup: {BACKUP_PATH}")

    # Load DNA
    with open(DNA_PATH, "r", encoding="utf-8") as f:
        data = yaml.safe_load(f)

    layers = data.get("layers", {})

    # Count before
    total_before = sum(len(layers.get(k, {}).get("items", [])) for k in layers)
    print(f"DNA before: {total_before} elements")

    total_inserted = 0
    for layer_key, elements in PHASE_C_ELEMENTS.items():
        if layer_key not in layers:
            print(f"  WARNING: {layer_key} not found in DNA, skipping")
            continue
        items = layers[layer_key].get("items", [])
        for elem in elements:
            items.append(elem)
        layers[layer_key]["items"] = items
        total_inserted += len(elements)
        print(f"  {layer_key}: +{len(elements)} elements inserted")

    # Count after
    total_after = sum(len(layers.get(k, {}).get("items", [])) for k in layers)
    print(f"\nDNA after: {total_after} elements (+{total_after - total_before})")

    # Write
    with open(DNA_PATH, "w", encoding="utf-8") as f:
        yaml.dump(data, f, default_flow_style=False, allow_unicode=True, sort_keys=False, width=200)

    # Validate
    print("\nValidating YAML...")
    try:
        with open(DNA_PATH, "r", encoding="utf-8") as f:
            test = yaml.safe_load(f)
        test_total = sum(len(test["layers"].get(k, {}).get("items", [])) for k in test["layers"])
        print(f"YAML VALID - {test_total} elements verified")
    except Exception as e:
        print(f"YAML ERROR: {e}")
        print("Restoring backup...")
        shutil.copy2(BACKUP_PATH, DNA_PATH)
        print("Backup restored.")
        sys.exit(1)

    print(f"\n{'=' * 60}")
    print(f"PHASE C COMPLETE: +{total_inserted} elements ({total_before} -> {total_after})")
    print(f"{'=' * 60}")


if __name__ == "__main__":
    main()
