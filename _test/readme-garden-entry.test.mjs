import assert from "node:assert/strict";
import { existsSync, readFileSync } from "node:fs";
import { dirname, join } from "node:path";
import { describe, it } from "node:test";
import { fileURLToPath } from "node:url";

const root = join(dirname(fileURLToPath(import.meta.url)), "..");
const readme = readFileSync(join(root, "README.md"), "utf8");
const home = readFileSync(join(root, "_pages/index.md"), "utf8");
const notFound = readFileSync(join(root, "404.html"), "utf8");
const about = readFileSync(join(root, "_pages/about.md"), "utf8");
const layout = readFileSync(join(root, "_layouts/default.html"), "utf8");
const gardenGuide = join(root, "_notes/🍀 花园导览/🍀 花园导览.md");

describe("repo entry next step", () => {
  it("names this fork, not the upstream template title", () => {
    assert.match(readme, /^# oldwinter 的公开数字花园/m);
    assert.doesNotMatch(readme, /Digital garden Jekyll template/);
    assert.match(readme, /oldwinter\/dg/);
  });

  it("gives a copyable local preview command", () => {
    assert.match(readme, /bundle exec jekyll serve/);
    assert.match(readme, /\[README-new\.md\]\(README-new\.md\)/);
    assert.ok(existsSync(join(root, "README-new.md")));
  });

  it("points at notes, sync, and the garden guide file", () => {
    assert.match(readme, /_notes\//);
    assert.match(readme, /\[SYNC_README\.md\]\(SYNC_README\.md\)/);
    assert.match(readme, /python sync_notes\.py/);
    assert.match(readme, /_notes\/🍀%20花园导览\/🍀%20花园导览\.md/);
    assert.ok(existsSync(gardenGuide));
    assert.ok(existsSync(join(root, "SYNC_README.md")));
  });

  it("does not send first-time readers to the template preview as this garden", () => {
    const beforeThanks = readme.slice(0, readme.indexOf("## 模板致谢"));
    assert.doesNotMatch(beforeThanks, /digital-garden-jekyll-template\.netlify\.app/);
    assert.doesNotMatch(beforeThanks, /Setting up your own digital garden with Jekyll/);
    assert.doesNotMatch(
      beforeThanks,
      /api\.netlify\.com\/api\/v1\/badges\/8cfa8785-8df8-4aad-ad35-8f1c790b8baf/,
    );
  });

  it("keeps template credit after local preview, notes, and sync", () => {
    const preview = readme.indexOf("## 本地预览");
    const notes = readme.indexOf("## 笔记在哪");
    const sync = readme.indexOf("## 怎么同步");
    const thanks = readme.indexOf("## 模板致谢");
    assert.ok(preview >= 0 && notes > preview && sync > notes && thanks > sync);
    assert.match(readme.slice(thanks), /maximevaillancourt\/digital-garden-jekyll-template/);
    assert.match(readme, /\[MIT\]\(LICENSE\)/);
    assert.ok(existsSync(join(root, "LICENSE")));
  });

  it("puts 🍀 花园导览 on the homepage before the timelines", () => {
    assert.match(
      home,
      /href="\{\{\s*site\.baseurl\s*\}\}\/🍀 花园导览\/🍀 花园导览\.md"/,
    );
    assert.match(home, />🍀 花园导览<\/a>/);
    const guide = home.indexOf("🍀 花园导览");
    const created = home.indexOf("最近创建");
    const updated = home.indexOf("最近更新");
    assert.ok(guide >= 0 && created > guide && updated > created);
  });

  it("does not restack 404, about, or html lang", () => {
    assert.match(notFound, /施主<a href="\/">请回<\/a>/);
    assert.doesNotMatch(notFound, /🍀 花园导览/);
    assert.match(about, /This is an about page/);
    assert.match(layout, /<html lang="en">/);
  });
});
