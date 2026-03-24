/**
 * MEGA BRAIN VIDEO RENDERER
 *
 * Renders videos programmatically from JSON input.
 * Used by the /video skill to generate videos from agent outputs.
 *
 * Usage:
 *   node render.mjs --input scene-data.json --composition VSL --output output/my-video.mp4
 *   node render.mjs --input scene-data.json --composition Creative
 *   node render.mjs --input scene-data.json --composition Presentation
 */

import { bundle } from "@remotion/bundler";
import { renderMedia, selectComposition } from "@remotion/renderer";
import { readFileSync, existsSync, mkdirSync } from "fs";
import { join, dirname, resolve } from "path";
import { fileURLToPath } from "url";

const __filename = fileURLToPath(import.meta.url);
const __dirname = dirname(__filename);

// --- Parse CLI args ---
function parseArgs() {
  const args = process.argv.slice(2);
  const parsed = {
    input: null,
    composition: "VSL",
    output: null,
    codec: "h264",
  };

  for (let i = 0; i < args.length; i++) {
    switch (args[i]) {
      case "--input":
      case "-i":
        parsed.input = args[++i];
        break;
      case "--composition":
      case "-c":
        parsed.composition = args[++i];
        break;
      case "--output":
      case "-o":
        parsed.output = args[++i];
        break;
      case "--codec":
        parsed.codec = args[++i];
        break;
    }
  }

  if (!parsed.input) {
    console.error("Error: --input is required");
    console.error("Usage: node render.mjs --input data.json --composition VSL --output output.mp4");
    process.exit(1);
  }

  if (!parsed.output) {
    const timestamp = new Date().toISOString().replace(/[:.]/g, "-").slice(0, 19);
    parsed.output = join(__dirname, "output", `${parsed.composition}-${timestamp}.mp4`);
  }

  return parsed;
}

// --- Main render function ---
async function main() {
  const args = parseArgs();
  const inputPath = resolve(args.input);

  if (!existsSync(inputPath)) {
    console.error(`Error: Input file not found: ${inputPath}`);
    process.exit(1);
  }

  // Read input data
  const inputData = JSON.parse(readFileSync(inputPath, "utf-8"));
  console.log(`\n  MEGA BRAIN VIDEO RENDERER`);
  console.log(`  Composition: ${args.composition}`);
  console.log(`  Input: ${inputPath}`);
  console.log(`  Output: ${args.output}\n`);

  // Ensure output directory exists
  const outputDir = dirname(args.output);
  if (!existsSync(outputDir)) {
    mkdirSync(outputDir, { recursive: true });
  }

  // Step 1: Bundle
  console.log("  [1/3] Bundling Remotion project...");
  const bundleLocation = await bundle({
    entryPoint: join(__dirname, "src", "index.ts"),
    webpackOverride: (config) => config,
  });

  // Step 2: Select composition
  console.log("  [2/3] Selecting composition...");

  // Calculate total duration from scenes/slides
  let totalDuration = 900; // default 30s
  if (args.composition === "VSL" && inputData.scenes) {
    totalDuration = inputData.scenes.reduce((sum, s) => sum + (s.duration || 120), 0);
  } else if (args.composition === "Presentation" && inputData.slides) {
    totalDuration = 120 + inputData.slides.reduce((sum, s) => sum + (s.duration || 150), 0);
    if (inputData.closingText) totalDuration += 90;
  } else if (args.composition === "Creative") {
    totalDuration = 450; // 15s
  }

  const composition = await selectComposition({
    serveUrl: bundleLocation,
    id: args.composition,
    inputProps: inputData,
  });

  // Override duration
  composition.durationInFrames = totalDuration;

  // Step 3: Render
  console.log(`  [3/3] Rendering ${totalDuration} frames (${(totalDuration / 30).toFixed(1)}s)...`);

  let lastProgress = 0;
  await renderMedia({
    composition,
    serveUrl: bundleLocation,
    codec: args.codec,
    outputLocation: args.output,
    inputProps: inputData,
    onProgress: ({ progress }) => {
      const percent = Math.round(progress * 100);
      if (percent >= lastProgress + 10) {
        const bar = "█".repeat(Math.round(percent / 5)) + "░".repeat(20 - Math.round(percent / 5));
        console.log(`  [${bar}] ${percent}%`);
        lastProgress = percent;
      }
    },
  });

  console.log(`\n  Video rendered successfully!`);
  console.log(`  Output: ${args.output}`);
  console.log(`  Duration: ${(totalDuration / 30).toFixed(1)} seconds`);
  console.log(`  Frames: ${totalDuration}\n`);
}

main().catch((err) => {
  console.error("Render failed:", err);
  process.exit(1);
});
