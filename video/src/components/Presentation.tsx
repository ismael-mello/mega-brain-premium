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

const slideSchema = z.object({
  title: z.string(),
  bullets: z.array(z.string()).min(1),
  duration: z.number().min(60).default(150), // frames
  highlight: z.string().optional(), // word to highlight in title
});

export const presentationSchema = z.object({
  title: z.string(),
  subtitle: z.string().optional(),
  slides: z.array(slideSchema).min(1),
  brandColor: z.string().default("#FF6B00"),
  backgroundColor: z.string().default("#0A0A0A"),
  fontFamily: z.string().default("Inter"),
  closingText: z.string().optional(),
});

type PresentationProps = z.infer<typeof presentationSchema>;
type Slide = z.infer<typeof slideSchema>;

// --- Title Slide ---

const TitleSlide: React.FC<{
  title: string;
  subtitle?: string;
  brandColor: string;
  backgroundColor: string;
  fontFamily: string;
}> = ({ title, subtitle, brandColor, backgroundColor, fontFamily }) => {
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();

  const titleSpring = spring({ frame, fps, config: { damping: 12 } });
  const subtitleFade = interpolate(frame, [20, 40], [0, 1], {
    extrapolateRight: "clamp",
  });

  return (
    <AbsoluteFill
      style={{
        backgroundColor,
        display: "flex",
        flexDirection: "column",
        justifyContent: "center",
        alignItems: "center",
        padding: "80px",
      }}
    >
      <div
        style={{
          fontSize: 80,
          fontFamily,
          fontWeight: 900,
          color: "#FFFFFF",
          textAlign: "center",
          transform: `translateY(${interpolate(titleSpring, [0, 1], [50, 0])}px)`,
          opacity: interpolate(titleSpring, [0, 1], [0, 1]),
        }}
      >
        {title}
      </div>

      {subtitle && (
        <div
          style={{
            fontSize: 36,
            fontFamily,
            fontWeight: 400,
            color: brandColor,
            textAlign: "center",
            marginTop: 30,
            opacity: subtitleFade,
            letterSpacing: "2px",
          }}
        >
          {subtitle}
        </div>
      )}

      {/* Bottom bar */}
      <div
        style={{
          position: "absolute",
          bottom: 80,
          width: interpolate(frame, [0, 40], [0, 400], {
            extrapolateRight: "clamp",
            easing: Easing.out(Easing.cubic),
          }),
          height: 4,
          backgroundColor: brandColor,
          borderRadius: 2,
        }}
      />
    </AbsoluteFill>
  );
};

// --- Content Slide ---

const ContentSlide: React.FC<{
  slide: Slide;
  slideNumber: number;
  totalSlides: number;
  brandColor: string;
  backgroundColor: string;
  fontFamily: string;
}> = ({ slide, slideNumber, totalSlides, brandColor, backgroundColor, fontFamily }) => {
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();

  const titleSpring = spring({ frame, fps, config: { damping: 15 } });

  return (
    <AbsoluteFill
      style={{
        backgroundColor,
        display: "flex",
        flexDirection: "column",
        padding: "80px 120px",
      }}
    >
      {/* Slide number */}
      <div
        style={{
          fontSize: 18,
          fontFamily,
          fontWeight: 600,
          color: brandColor,
          letterSpacing: "3px",
          marginBottom: 20,
          opacity: interpolate(frame, [0, 10], [0, 1], {
            extrapolateRight: "clamp",
          }),
        }}
      >
        {String(slideNumber).padStart(2, "0")} / {String(totalSlides).padStart(2, "0")}
      </div>

      {/* Title */}
      <div
        style={{
          fontSize: 52,
          fontFamily,
          fontWeight: 800,
          color: "#FFFFFF",
          marginBottom: 50,
          transform: `translateX(${interpolate(titleSpring, [0, 1], [-30, 0])}px)`,
          opacity: interpolate(titleSpring, [0, 1], [0, 1]),
          borderLeft: `4px solid ${brandColor}`,
          paddingLeft: 24,
        }}
      >
        {slide.title}
      </div>

      {/* Bullets */}
      <div style={{ display: "flex", flexDirection: "column", gap: 24 }}>
        {slide.bullets.map((bullet, i) => {
          const bulletDelay = 15 + i * 12;
          const bulletSpring = spring({
            frame: frame - bulletDelay,
            fps,
            config: { damping: 12 },
          });

          return (
            <div
              key={i}
              style={{
                display: "flex",
                alignItems: "flex-start",
                gap: 20,
                opacity: interpolate(bulletSpring, [0, 1], [0, 1]),
                transform: `translateX(${interpolate(bulletSpring, [0, 1], [20, 0])}px)`,
              }}
            >
              <div
                style={{
                  width: 12,
                  height: 12,
                  borderRadius: "50%",
                  backgroundColor: brandColor,
                  marginTop: 12,
                  flexShrink: 0,
                }}
              />
              <div
                style={{
                  fontSize: 32,
                  fontFamily,
                  fontWeight: 400,
                  color: "#E0E0E0",
                  lineHeight: 1.4,
                }}
              >
                {bullet}
              </div>
            </div>
          );
        })}
      </div>

      {/* Progress bar */}
      <div
        style={{
          position: "absolute",
          bottom: 40,
          left: 120,
          right: 120,
          height: 3,
          backgroundColor: "#333333",
          borderRadius: 2,
        }}
      >
        <div
          style={{
            width: `${(slideNumber / totalSlides) * 100}%`,
            height: "100%",
            backgroundColor: brandColor,
            borderRadius: 2,
          }}
        />
      </div>
    </AbsoluteFill>
  );
};

// --- Main Presentation Component ---

export const Presentation: React.FC<PresentationProps> = ({
  title,
  subtitle,
  slides,
  brandColor,
  backgroundColor,
  fontFamily,
  closingText,
}) => {
  const titleDuration = 120; // 4 seconds
  let currentFrame = 0;

  return (
    <AbsoluteFill style={{ backgroundColor }}>
      {/* Title slide */}
      <Sequence from={0} durationInFrames={titleDuration} name="Title">
        <TitleSlide
          title={title}
          subtitle={subtitle}
          brandColor={brandColor}
          backgroundColor={backgroundColor}
          fontFamily={fontFamily}
        />
      </Sequence>

      {/* Content slides */}
      {(() => {
        currentFrame = titleDuration;
        return slides.map((slide, index) => {
          const from = currentFrame;
          currentFrame += slide.duration;

          return (
            <Sequence
              key={index}
              from={from}
              durationInFrames={slide.duration}
              name={`Slide ${index + 1}: ${slide.title}`}
            >
              <ContentSlide
                slide={slide}
                slideNumber={index + 1}
                totalSlides={slides.length}
                brandColor={brandColor}
                backgroundColor={backgroundColor}
                fontFamily={fontFamily}
              />
            </Sequence>
          );
        });
      })()}

      {/* Closing slide */}
      {closingText && (
        <Sequence
          from={currentFrame}
          durationInFrames={90}
          name="Closing"
        >
          <TitleSlide
            title={closingText}
            brandColor={brandColor}
            backgroundColor={backgroundColor}
            fontFamily={fontFamily}
          />
        </Sequence>
      )}
    </AbsoluteFill>
  );
};
