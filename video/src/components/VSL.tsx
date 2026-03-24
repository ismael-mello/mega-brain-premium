import React from "react";
import {
  AbsoluteFill,
  Sequence,
  useCurrentFrame,
  useVideoConfig,
  interpolate,
  spring,
  Easing,
} from "remotion";
import { z } from "zod";

// --- Schema ---

const sceneSchema = z.object({
  type: z.enum(["hook", "problem", "agitate", "solution", "proof", "offer", "cta", "custom"]),
  text: z.string(),
  subtext: z.string().optional(),
  duration: z.number().min(30).default(120), // frames
  imageUrl: z.string().optional(),
});

export const vslSchema = z.object({
  headline: z.string(),
  subheadline: z.string().optional(),
  scenes: z.array(sceneSchema).min(1),
  brandColor: z.string().default("#FF6B00"),
  backgroundColor: z.string().default("#0A0A0A"),
  fontFamily: z.string().default("Inter"),
  logoUrl: z.string().optional(),
});

type VSLProps = z.infer<typeof vslSchema>;
type Scene = z.infer<typeof sceneSchema>;

// --- Scene Component ---

const SceneBlock: React.FC<{
  scene: Scene;
  brandColor: string;
  backgroundColor: string;
  fontFamily: string;
}> = ({ scene, brandColor, backgroundColor, fontFamily }) => {
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();

  const fadeIn = interpolate(frame, [0, 15], [0, 1], {
    extrapolateRight: "clamp",
  });

  const slideUp = spring({
    frame,
    fps,
    config: { damping: 12, stiffness: 100 },
  });

  const sceneLabels: Record<string, string> = {
    hook: "HOOK",
    problem: "THE PROBLEM",
    agitate: "BUT IT GETS WORSE",
    solution: "THE SOLUTION",
    proof: "PROOF",
    offer: "THE OFFER",
    cta: "TAKE ACTION NOW",
    custom: "",
  };

  const accentColors: Record<string, string> = {
    hook: brandColor,
    problem: "#FF3333",
    agitate: "#FF5555",
    solution: "#33CC66",
    proof: "#3399FF",
    offer: brandColor,
    cta: "#FFD700",
    custom: brandColor,
  };

  const accent = accentColors[scene.type] || brandColor;
  const label = sceneLabels[scene.type] || "";

  return (
    <AbsoluteFill
      style={{
        backgroundColor,
        display: "flex",
        flexDirection: "column",
        justifyContent: "center",
        alignItems: "center",
        padding: "80px 120px",
        opacity: fadeIn,
      }}
    >
      {/* Scene label */}
      {label && (
        <div
          style={{
            fontSize: 24,
            fontFamily,
            fontWeight: 700,
            color: accent,
            letterSpacing: "4px",
            marginBottom: 40,
            opacity: fadeIn,
            textTransform: "uppercase",
          }}
        >
          {label}
        </div>
      )}

      {/* Main text */}
      <div
        style={{
          fontSize: scene.type === "cta" ? 72 : 56,
          fontFamily,
          fontWeight: 800,
          color: "#FFFFFF",
          textAlign: "center",
          lineHeight: 1.3,
          transform: `translateY(${interpolate(slideUp, [0, 1], [40, 0])}px)`,
          maxWidth: "80%",
        }}
      >
        {scene.text}
      </div>

      {/* Subtext */}
      {scene.subtext && (
        <div
          style={{
            fontSize: 32,
            fontFamily,
            fontWeight: 400,
            color: "#CCCCCC",
            textAlign: "center",
            marginTop: 30,
            opacity: interpolate(frame, [20, 35], [0, 1], {
              extrapolateRight: "clamp",
            }),
          }}
        >
          {scene.subtext}
        </div>
      )}

      {/* Bottom accent line */}
      <div
        style={{
          position: "absolute",
          bottom: 60,
          width: interpolate(frame, [0, 30], [0, 200], {
            extrapolateRight: "clamp",
            easing: Easing.out(Easing.cubic),
          }),
          height: 4,
          backgroundColor: accent,
          borderRadius: 2,
        }}
      />
    </AbsoluteFill>
  );
};

// --- Main VSL Component ---

export const VSL: React.FC<VSLProps> = ({
  headline,
  subheadline,
  scenes,
  brandColor,
  backgroundColor,
  fontFamily,
  logoUrl,
}) => {
  const totalDuration = scenes.reduce((sum, s) => sum + s.duration, 0);

  let currentFrame = 0;

  return (
    <AbsoluteFill style={{ backgroundColor }}>
      {scenes.map((scene, index) => {
        const from = currentFrame;
        currentFrame += scene.duration;

        return (
          <Sequence
            key={index}
            from={from}
            durationInFrames={scene.duration}
            name={`Scene: ${scene.type}`}
          >
            <SceneBlock
              scene={scene}
              brandColor={brandColor}
              backgroundColor={backgroundColor}
              fontFamily={fontFamily}
            />
          </Sequence>
        );
      })}
    </AbsoluteFill>
  );
};
