import assert from "node:assert/strict";
import { readFileSync } from "node:fs";
import { dirname, join } from "node:path";
import { describe, it } from "node:test";
import { fileURLToPath } from "node:url";

const root = join(dirname(fileURLToPath(import.meta.url)), "..");
const notFound = readFileSync(join(root, "404.html"), "utf8");
const config = readFileSync(join(root, "_config.yml"), "utf8");
const gardenGuide = readFileSync(
  join(root, "_notes/🍀 花园导览/🍀 花园导览.md"),
  "utf8",
);

describe("404 garden next step", () => {
  it("keeps a home link", () => {
    assert.match(notFound, /href="\{\{\s*site\.baseurl\s*\}\}\/"/);
    assert.match(notFound, /请回/);
  });

  it("says this path has no matching note", () => {
    assert.match(notFound, /这条路径没有对应笔记/);
  });

  it("offers 🍀 花园导览 as the map, not only the homepage", () => {
    assert.match(notFound, /where:\s*"title",\s*"🍀 花园导览"/);
    assert.match(
      notFound,
      /href="\{\{\s*site\.baseurl\s*\}\}\{\{\s*garden_guide_url\s*\}\}"/,
    );
    assert.match(notFound, />🍀 花园导览<\/a>/);
  });

  it("falls back to the published garden-guide permalink", () => {
    assert.match(gardenGuide, /^title:\s*🍀 花园导览$/m);
    assert.match(gardenGuide, /^permalink:\s*\/🍀 花园导览\/🍀 花园导览\.md$/m);
    assert.match(notFound, /default:\s*"\/🍀 花园导览\/🍀 花园导览\.md"/);
  });

  it("does not rewrite garden-guide note body", () => {
    assert.match(gardenGuide, /这里我尽量将已经成熟的花草展示给您/);
    assert.doesNotMatch(notFound, /这里我尽量将已经成熟的花草展示给您/);
  });

  it("keeps the 404 contract test out of the published garden", () => {
    assert.match(config, /['"]tests['"]/);
  });
});
