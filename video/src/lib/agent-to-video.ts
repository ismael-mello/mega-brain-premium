/**
 * AGENT-TO-VIDEO CONVERTER
 *
 * Transforms agent output (conclave, cargo, person) into
 * structured data that Remotion components can render.
 *
 * This is the bridge between Mega Brain agents and video generation.
 */

import { z } from "zod";

// --- Input: What agents produce ---

export const agentOutputSchema = z.object({
  type: z.enum(["vsl", "creative", "presentation", "summary"]),
  expert: z.string().optional(), // e.g., "Alex Hormozi", "Cole Gordon"
  topic: z.string(),
  content: z.object({
    hook: z.string().optional(),
    problem: z.string().optional(),
    agitate: z.string().optional(),
    solution: z.string().optional(),
    proof: z.string().optional(),
    offer: z.string().optional(),
    cta: z.string().optional(),
    bullets: z.array(z.string()).optional(),
    headline: z.string().optional(),
    body: z.string().optional(),
    slides: z
      .array(
        z.object({
          title: z.string(),
          points: z.array(z.string()),
        })
      )
      .optional(),
  }),
  branding: z
    .object({
      color: z.string().optional(),
      backgroundColor: z.string().optional(),
      logoUrl: z.string().optional(),
    })
    .optional(),
});

export type AgentOutput = z.infer<typeof agentOutputSchema>;

// --- Output: What Remotion needs ---

/**
 * Converts a VSL agent output into Remotion VSL props
 */
export function agentToVSL(input: AgentOutput) {
  const scenes = [];
  const content = input.content;

  if (content.hook) {
    scenes.push({ type: "hook" as const, text: content.hook, duration: 120 });
  }
  if (content.problem) {
    scenes.push({ type: "problem" as const, text: content.problem, duration: 150 });
  }
  if (content.agitate) {
    scenes.push({ type: "agitate" as const, text: content.agitate, duration: 120 });
  }
  if (content.solution) {
    scenes.push({ type: "solution" as const, text: content.solution, duration: 150 });
  }
  if (content.proof) {
    scenes.push({ type: "proof" as const, text: content.proof, duration: 120 });
  }
  if (content.offer) {
    scenes.push({ type: "offer" as const, text: content.offer, duration: 150 });
  }
  if (content.cta) {
    scenes.push({ type: "cta" as const, text: content.cta, duration: 90 });
  }

  return {
    headline: content.headline || input.topic,
    subheadline: input.expert ? `Based on ${input.expert}'s methodology` : undefined,
    scenes,
    brandColor: input.branding?.color || "#FF6B00",
    backgroundColor: input.branding?.backgroundColor || "#0A0A0A",
    fontFamily: "Inter",
    logoUrl: input.branding?.logoUrl,
  };
}

/**
 * Converts a Creative agent output into Remotion Creative props
 */
export function agentToCreative(input: AgentOutput) {
  return {
    headline: input.content.headline || input.content.hook || input.topic,
    body: input.content.body || input.content.solution || "",
    ctaText: input.content.cta || "Saiba Mais",
    brandColor: input.branding?.color || "#FF6B00",
    backgroundColor: input.branding?.backgroundColor || "#0A0A0A",
    imageUrl: input.branding?.logoUrl,
    style: "bold" as const,
  };
}

/**
 * Converts a Presentation agent output into Remotion Presentation props
 */
export function agentToPresentation(input: AgentOutput) {
  const slides =
    input.content.slides?.map((s) => ({
      title: s.title,
      bullets: s.points,
      duration: 150,
    })) || [];

  // If no slides but has bullets, create a single slide
  if (slides.length === 0 && input.content.bullets) {
    slides.push({
      title: input.topic,
      bullets: input.content.bullets,
      duration: 180,
    });
  }

  return {
    title: input.content.headline || input.topic,
    subtitle: input.expert || undefined,
    slides,
    brandColor: input.branding?.color || "#FF6B00",
    backgroundColor: input.branding?.backgroundColor || "#0A0A0A",
    fontFamily: "Inter",
    closingText: input.content.cta,
  };
}

/**
 * Auto-detect and convert based on type
 */
export function convertAgentOutput(input: AgentOutput) {
  switch (input.type) {
    case "vsl":
      return { composition: "VSL", props: agentToVSL(input) };
    case "creative":
      return { composition: "Creative", props: agentToCreative(input) };
    case "presentation":
    case "summary":
      return { composition: "Presentation", props: agentToPresentation(input) };
    default:
      return { composition: "VSL", props: agentToVSL(input) };
  }
}
