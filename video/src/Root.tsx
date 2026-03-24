import React from "react";
import { Composition } from "remotion";
import { VSL, vslSchema } from "./components/VSL";
import { Creative, creativeSchema } from "./components/Creative";
import { Presentation, presentationSchema } from "./components/Presentation";

export const RemotionRoot: React.FC = () => {
  return (
    <>
      {/* VSL - Video Sales Letter */}
      <Composition
        id="VSL"
        component={VSL}
        schema={vslSchema}
        durationInFrames={900} // 30s at 30fps (overridden by props)
        fps={30}
        width={1920}
        height={1080}
        defaultProps={{
          headline: "Your Headline Here",
          subheadline: "Your subheadline",
          scenes: [
            {
              type: "hook",
              text: "What if you could...",
              duration: 90,
            },
            {
              type: "problem",
              text: "The problem is...",
              duration: 120,
            },
            {
              type: "solution",
              text: "Here's the solution...",
              duration: 120,
            },
            {
              type: "cta",
              text: "Click the button below",
              duration: 90,
            },
          ],
          brandColor: "#FF6B00",
          backgroundColor: "#0A0A0A",
          fontFamily: "Inter",
          logoUrl: "",
        }}
      />

      {/* Creative - Social Media Ad */}
      <Composition
        id="Creative"
        component={Creative}
        schema={creativeSchema}
        durationInFrames={450} // 15s at 30fps
        fps={30}
        width={1080}
        height={1080}
        defaultProps={{
          headline: "Your Ad Headline",
          body: "Your ad body text",
          ctaText: "Learn More",
          brandColor: "#FF6B00",
          backgroundColor: "#0A0A0A",
          imageUrl: "",
          style: "bold" as const,
        }}
      />

      {/* Presentation - Knowledge Summary */}
      <Composition
        id="Presentation"
        component={Presentation}
        schema={presentationSchema}
        durationInFrames={1800} // 60s at 30fps
        fps={30}
        width={1920}
        height={1080}
        defaultProps={{
          title: "Presentation Title",
          subtitle: "By Expert Name",
          slides: [
            {
              title: "Slide 1",
              bullets: ["Point 1", "Point 2", "Point 3"],
              duration: 150,
            },
          ],
          brandColor: "#FF6B00",
          backgroundColor: "#0A0A0A",
          fontFamily: "Inter",
        }}
      />
    </>
  );
};
