import React from "react";
import {
  AbsoluteFill,
  useCurrentFrame,
  useVideoConfig,
  interpolate,
  spring,
  Easing,
  Img,
} from "remotion";
import { z } from "zod";

// --- Schema ---

export const creativeSchema = z.object({
  headline: z.string(),
  body: z.string(),
  ctaText: z.string().default("Learn More"),
  brandColor: z.string().default("#FF6B00"),
  backgroundColor: z.string().default("#0A0A0A"),
  imageUrl: z.string().optional(),
  style: z.enum(["bold", "minimal", "gradient"]).default("bold"),
});

type CreativeProps = z.infer<typeof creativeSchema>;

// --- Main Creative Component ---

export const Creative: React.FC<CreativeProps> = ({
  headline,
  body,
  ctaText,
  brandColor,
  backgroundColor,
  imageUrl,
  style,
}) => {
  const frame = useCurrentFrame();
  const { fps, durationInFrames } = useVideoConfig();

  const fadeIn = interpolate(frame, [0, 15], [0, 1], {
    extrapolateRight: "clamp",
  });

  const slideUp = spring({
    frame,
    fps,
    config: { damping: 15, stiffness: 120 },
  });

  const ctaSpring = spring({
    frame: frame - 30,
    fps,
    config: { damping: 10, stiffness: 80 },
  });

  const pulse = interpolate(
    frame % 60,
    [0, 30, 60],
    [1, 1.05, 1],
    { extrapolateRight: "clamp" }
  );

  const bgStyle: React.CSSProperties =
    style === "gradient"
      ? {
          background: `linear-gradient(135deg, ${backgroundColor} 0%, ${brandColor}33 100%)`,
        }
      : { backgroundColor };

  return (
    <AbsoluteFill
      style={{
        ...bgStyle,
        display: "flex",
        flexDirection: "column",
        justifyContent: "center",
        alignItems: "center",
        padding: "60px",
        opacity: fadeIn,
      }}
    >
      {/* Image (if provided) */}
      {imageUrl && (
        <div
          style={{
            width: 300,
            height: 300,
            borderRadius: "50%",
            overflow: "hidden",
            marginBottom: 40,
            border: `4px solid ${brandColor}`,
            transform: `scale(${interpolate(slideUp, [0, 1], [0.8, 1])})`,
          }}
        >
          <Img
            src={imageUrl}
            style={{ width: "100%", height: "100%", objectFit: "cover" }}
          />
        </div>
      )}

      {/* Headline */}
      <div
        style={{
          fontSize: style === "bold" ? 64 : 48,
          fontFamily: "Inter, sans-serif",
          fontWeight: 900,
          color: "#FFFFFF",
          textAlign: "center",
          lineHeight: 1.2,
          transform: `translateY(${interpolate(slideUp, [0, 1], [30, 0])}px)`,
          maxWidth: "90%",
          textShadow: style === "bold" ? `0 2px 20px ${brandColor}44` : "none",
        }}
      >
        {headline}
      </div>

      {/* Body */}
      <div
        style={{
          fontSize: 28,
          fontFamily: "Inter, sans-serif",
          fontWeight: 400,
          color: "#CCCCCC",
          textAlign: "center",
          marginTop: 24,
          maxWidth: "80%",
          opacity: interpolate(frame, [15, 30], [0, 1], {
            extrapolateRight: "clamp",
          }),
        }}
      >
        {body}
      </div>

      {/* CTA Button */}
      <div
        style={{
          marginTop: 50,
          padding: "20px 60px",
          backgroundColor: brandColor,
          borderRadius: 12,
          transform: `scale(${interpolate(ctaSpring, [0, 1], [0, 1]) * pulse})`,
          opacity: interpolate(ctaSpring, [0, 1], [0, 1]),
        }}
      >
        <div
          style={{
            fontSize: 28,
            fontFamily: "Inter, sans-serif",
            fontWeight: 700,
            color: "#FFFFFF",
            textTransform: "uppercase",
            letterSpacing: "2px",
          }}
        >
          {ctaText}
        </div>
      </div>

      {/* Decorative accent */}
      <div
        style={{
          position: "absolute",
          top: 0,
          left: 0,
          width: interpolate(frame, [0, 45], [0, 1080], {
            extrapolateRight: "clamp",
            easing: Easing.out(Easing.cubic),
          }),
          height: 6,
          backgroundColor: brandColor,
        }}
      />
    </AbsoluteFill>
  );
};
