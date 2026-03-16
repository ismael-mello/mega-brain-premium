#!/usr/bin/env python3
"""
DK Referral Machine DNA Extraction Script
Appends 65 new elements from The Ultimate No BS Referral Machine to DK DNA.yaml
"""
import pathlib, re, shutil

ROOT = pathlib.Path("C:/Users/ISMAEL_MELLO/Downloads/mega-brain-premium")
DNA_PATH = ROOT / "knowledge/external/dna/persons/dan-kennedy/DNA.yaml"

def main():
    print("=" * 70)
    print("DK Referral Machine DNA Extraction")
    print("=" * 70)

    # Backup
    shutil.copy2(DNA_PATH, DNA_PATH.with_suffix(".yaml.bak_rm"))
    print("[1/3] Backup created")

    content = DNA_PATH.read_text(encoding="utf-8")

    # Find max IDs
    max_fil = max(int(x) for x in re.findall(r'"FIL-DK-(\d+)"', content))
    max_mm = max(int(x) for x in re.findall(r'"MM-DK-(\d+)"', content))
    max_heur = max(int(x) for x in re.findall(r'"HEUR-DK-(\d+)"', content))
    max_fw = max(int(x) for x in re.findall(r'"FW-DK-(\d+)"', content))
    max_met = max(int(x) for x in re.findall(r'"MET-DK-(\d+)"', content))
    print(f"  Max IDs: FIL:{max_fil} MM:{max_mm} HEUR:{max_heur} FW:{max_fw} MET:{max_met}")

    # Build elements
    elements = []

    # L1 PHILOSOPHIES (18)
    phil = [
        "Almost nothing happens automatically except bad things - good things require intentional effort",
        "The customer is not your salesperson - their job is to give you money",
        "Entitlement thinking is the number one reason business owners don't get referrals",
        "Good job plus good service equals minimum ante not entitlement to referrals",
        "The threshold for patronage is much lower than the threshold to refer",
        "When you recognize and reward behavior you get more of it - when you don't you lose it",
        "Nobody gets a free machine - referral systems require real investment",
        "Unsuccessful people say this won't work for me - successful ask how can I make this work",
        "Digital-only gifts have no permanence no wow and no pass-along effect",
        "The most pitiful person expects a thank you note - gratitude must be prompt",
        "If there should be a minimum wage job it is coming up with reasons why we can't do something",
        "Referring to information is dramatically easier than referring to a provider",
        "Satisfied patients don't refer in abundance - satisfaction is passive not active",
        "Staff in perpetual hostage mode is the biggest internal threat to referral implementation",
        "Once you penetrate affluent clan defenses they have zero internal defenses",
        "Customer replacement costs double because you need two for one",
        "Testimonials are the most believable kind of proof",
        "Just because your employer is stupid doesn't mean you have to be stupid",
    ]
    for i, title in enumerate(phil):
        elements.append(("L1_PHILOSOPHIES", f"FIL-DK-{max_fil+1+i:03d}", title))

    # L2 MENTAL MODELS (12)
    mm = [
        "The Referral Machine - three Is: Intentional Invested Integrated",
        "The Closed Loop - referring makes the referrer harder to leave (Cialdini)",
        "Referral threshold hierarchy: patronage < request < evangelism",
        "Foundation under the machine - four layers before the referral system",
        "Referral budget starts with math not creativity - based on cold CAC",
        "Status by doing - people refer when it gives THEM status in three ways",
        "Permanent visible space principle - gifts that stay force conversations",
        "Omnipresence model - can't turn 360 degrees without bumping into you",
        "Upstream referrals through centers of influence - fish where fish flock",
        "Customer segmentation ABC for differential referral investment",
        "Five reasons customers don't refer even when satisfied",
        "Six reasons business owners don't ask for referrals",
    ]
    for i, title in enumerate(mm):
        elements.append(("L2_MENTAL_MODELS", f"MM-DK-{max_mm+1+i:03d}", title))

    # L3 HEURISTICS (15)
    heur = [
        "Referred customer has less sales and price resistance - gives price elasticity",
        "Most businesses claiming good referrals measure at single digit percentages",
        "If cold acquisition costs 6000 pay 5000 for referral - save money time quality",
        "Thank you must arrive next day - bitterly disappointed by Thursday",
        "Gift budget equals half max referral budget - other half for events/systems",
        "Food gifts consumed and gone - mix with permanent physical items",
        "Gift of month should appear random but schedule every 6 weeks skip July",
        "Person who refers once is much easier to get 5th from than 1st from new",
        "Omnipresence model 280 plus non-sales communications per year GKIC",
        "Most newsletters fail because 100 percent core-deliverable content - boring",
        "Burleson WOW box 170 dollars on 6-7K value - referrals 15 to 60 percent",
        "Non-referring customer at 6 month trigger requires direct conversation",
        "Staff must refer from own circle first or they'll never motivate customers",
        "Price is reason 6 not 1 why customers leave - indifference is 68 percent",
        "Write testimonial yourself get client approval - they rarely change a word",
    ]
    for i, title in enumerate(heur):
        elements.append(("L3_HEURISTICS", f"HEUR-DK-{max_heur+1+i:03d}", title))

    # L4 FRAMEWORKS (10)
    fw = [
        "Referral Machine Architecture: Foundation > Tools > Training > Measurement",
        "WOW New Client Package: educate + inform + cool/fun + permanence + pass-along",
        "Special Report of Month System: stealth referral through information",
        "Referral Culture Building: six components for visible referral-driven practice",
        "Comprehensive Internal Marketing System: nine-component infrastructure",
        "Newsletter as Referral Foundation: entertainment + recognition + promotion",
        "Endorsed Mailing: center of influence drives to information not provider",
        "Client Event Strategy: annual appreciation with bring-a-buddy culture",
        "Great Testimonial: five elements (before-after drama details objection-erasure multimedia)",
        "Patient of Month Program: referral recognition gamification system",
    ]
    for i, title in enumerate(fw):
        elements.append(("L4_FRAMEWORKS", f"FW-DK-{max_fw+1+i:03d}", title))

    # L5 METHODOLOGIES (10)
    met = [
        "WOW Package Creation: math to permanent visible space deployment",
        "Gift of Month System: randomized-appearing scheduled gifting methodology",
        "Special Report of Month: stealth referral lead generation process",
        "Referral Toolkit Deployment: tools plus training plus monthly restocking",
        "Staff Referral Training: teach coach monitor enforce reward punish cycle",
        "Testimonial Collection: wall display to write-it-yourself pipeline",
        "Client Referral Event: from 100 to thousands annual event blueprint",
        "Endorsed Mailing Execution: two letters driving to report not provider",
        "Lost Customer Reactivation: address 6 reasons with multi-step campaign",
        "Disney D23 Model: membership welcome box plus ongoing physical gifting",
    ]
    for i, title in enumerate(met):
        elements.append(("L5_METHODOLOGIES", f"MET-DK-{max_met+1+i:03d}", title))

    total = len(elements)
    print(f"\n[2/3] Extracted {total} elements:")
    counts = {}
    for layer, eid, title in elements:
        counts[layer] = counts.get(layer, 0) + 1
    for k, v in sorted(counts.items()):
        print(f"  {k}: {v}")

    # Build YAML
    yaml = "\n\n# ======================================================================\n"
    yaml += "# REFERRAL MACHINE (RM) - The Ultimate No BS Referral Machine\n"
    yaml += "# Source: DVD Sessions 1-4 + CD5 (Newsletter) + Bonuses 1-4\n"
    yaml += "# Date: 2026-03-16\n"
    yaml += f"# New elements: {total}\n"
    yaml += "# ======================================================================\n"

    current_layer = None
    for layer, eid, title in elements:
        if layer != current_layer:
            yaml += f"\n# --- {layer} (RM) ---\n"
            current_layer = layer
        safe_title = title.replace('"', "'")
        yaml += f'  - id: "{eid}"\n'
        yaml += f'    title: "{safe_title}"\n'
        yaml += f'    content: "{safe_title}"\n'
        yaml += f'    source: "referral-machine"\n'
        yaml += f"    tags: [referrals, referral-machine]\n"

    # Append
    with open(DNA_PATH, "a", encoding="utf-8") as f:
        f.write(yaml)

    # Update header
    content = DNA_PATH.read_text(encoding="utf-8")

    # Add RM to sources
    content = content.replace(
        '    - "Mind Hijacking (MH)"',
        '    - "Mind Hijacking (MH)"\n    - "The Ultimate No BS Referral Machine (RM)"',
        1
    )

    # Update top comment
    old_top = "Mind Hijacking (MH)"
    idx = content.find(old_top)
    if idx > 0 and idx < 500:
        content = content[:idx] + old_top + " + Referral Machine (RM)" + content[idx+len(old_top):]

    # Version
    content = content.replace('# Version: 25.0.0', '# Version: 26.0.0', 1)
    content = content.replace('version: "25.0.0"', 'version: "26.0.0"', 2)

    # Total
    old_total = 2417
    new_total = old_total + total
    content = content.replace(f"# Total Elements: {old_total}", f"# Total Elements: {new_total}", 1)
    content = content.replace(f"total_elements: {old_total}", f"total_elements: {new_total}", 1)

    DNA_PATH.write_text(content, encoding="utf-8")

    print(f"\n[3/3] DNA.yaml updated:")
    print(f"  Version: 26.0.0")
    print(f"  Total: {new_total} elements (+{total})")
    print(f"  Sources: 10 (added RM)")
    print(f"\n  Next IDs:")
    print(f"    FIL-DK-{max_fil+1+counts['L1_PHILOSOPHIES']:03d}")
    print(f"    MM-DK-{max_mm+1+counts['L2_MENTAL_MODELS']:03d}")
    print(f"    HEUR-DK-{max_heur+1+counts['L3_HEURISTICS']:03d}")
    print(f"    FW-DK-{max_fw+1+counts['L4_FRAMEWORKS']:03d}")
    print(f"    MET-DK-{max_met+1+counts['L5_METHODOLOGIES']:03d}")
    print("\n  Done. Consider it done, senhor.")

if __name__ == "__main__":
    main()
