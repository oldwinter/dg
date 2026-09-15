import assert from "node:assert/strict";
import { readFileSync } from "node:fs";
import { dirname, join } from "node:path";
import { describe, it } from "node:test";
import { fileURLToPath } from "node:url";

const root = join(dirname(fileURLToPath(import.meta.url)), "..");
const layout = readFileSync(join(root, "_layouts/default.html"), "utf8");
const config = readFileSync(join(root, "_config.yml"), "utf8");
const notFound = readFileSync(join(root, "404.html"), "utf8");
const lockfile = readFileSync(join(root, "Gemfile.lock"), "utf8");
const netlify = readFileSync(join(root, "netlify.toml"), "utf8");

describe("garden layout language", () => {
  it("declares zh-CN on the root html element", () => {
    assert.match(layout, /<html\s+lang="zh-CN">/);
    assert.doesNotMatch(layout, /<html\s+lang="en">/);
  });

  it("keeps the layout contract test out of the published garden", () => {
    assert.match(config, /['"]tests['"]/);
  });

  it("locks linux gems so Netlify can bundle install", () => {
    assert.match(lockfile, /^  x86_64-linux/m);
    assert.match(lockfile, /nokogiri \(1\.\d+\.\d+-x86_64-linux/);
  });

  it("asks Netlify for a supported Node for deploy plugins", () => {
    assert.match(netlify, /NODE_VERSION\s*=\s*"22"/);
    assert.doesNotMatch(netlify, /NODE_VERSION\s*=\s*"18"/);
    assert.match(netlify, /bundle exec jekyll build --trace/);
  });

  it("does not rewrite the 404 copy", () => {
    assert.match(notFound, /你到达了一个不存在的界面，施主/);
    assert.match(notFound, /请回/);
  });
});
