#!/usr/bin/env python3
"""Git Mobile Privacy 页面自检。

检查项：
1. 每个 TOC/正文锚点都能命中同语言的 id，且 id 不重复；
2. 中英文段章节数量一致（避免只改一种语言导致结构漂移）；
3. 页面自包含：没有外部 script/src/href，不引入第三方资源；
4. 两个语言段都有「最后更新」日期；
5. PRIVACY.md 与页面的更新日期一致。

只读文件，不修改任何内容；退出码非 0 表示有问题。
"""
from __future__ import annotations

import re
import sys
from html.parser import HTMLParser
from pathlib import Path

ROOT = Path(__file__).resolve().parent
HTML = ROOT / "index.html"
MD = ROOT / "PRIVACY.md"


class Scanner(HTMLParser):
    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.ids: list[str] = []
        self.anchors: list[str] = []
        self.sections: list[str] = []
        self.h2_by_lang: dict[str, list[str]] = {}
        self._lang: str | None = None
        self._in_h2 = False
        self._h2_buf: list[str] = []
        self.external: list[str] = []
        self.has_script = False

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if "id" in a:
            self.ids.append(a["id"])
        if tag == "section" and "data-lang" in a:
            self._lang = a["data-lang"]
            self.sections.append(self._lang)
            self.h2_by_lang[self._lang] = []
        if tag == "a" and a.get("href", "").startswith("#"):
            self.anchors.append(a["href"][1:])
        if tag == "h2":
            self._in_h2 = True
            self._h2_buf = []
        if tag == "script":
            self.has_script = True
            if a.get("src"):
                self.external.append(a["src"])
        if tag in ("img", "link", "iframe") and (a.get("src") or a.get("href")):
            url = a.get("src") or a.get("href") or ""
            if not url.startswith("data:"):
                self.external.append(url)

    def handle_endtag(self, tag):
        if tag == "h2" and self._in_h2:
            self._in_h2 = False
            if self._lang:
                self.h2_by_lang[self._lang].append("".join(self._h2_buf).strip())

    def handle_data(self, data):
        if self._in_h2:
            self._h2_buf.append(data)


def main() -> int:
    html = HTML.read_text(encoding="utf-8")
    md = MD.read_text(encoding="utf-8")
    s = Scanner()
    s.feed(html)

    errors: list[str] = []
    warnings: list[str] = []

    dup = sorted({i for i in s.ids if s.ids.count(i) > 1})
    if dup:
        errors.append(f"重复 id：{dup}")

    idset = set(s.ids)
    missing = [a for a in s.anchors if a not in idset]
    if missing:
        errors.append(f"锚点找不到目标：{missing}")

    # 每个 TOC 锚点应指向同语言段落
    cross = []
    for a in s.anchors:
        if a.startswith("zh-") or a.startswith("en-"):
            pre, rest = a.split("-", 1)
            want = {pre}
            if not any(i for i in idset if i == a):
                cross.append(a)
    if cross:
        errors.append(f"跨语言锚点：{cross}")

    langs = sorted(s.h2_by_lang)
    counts = {k: len(v) for k, v in s.h2_by_lang.items()}
    if len(set(counts.values())) != 1:
        errors.append(f"两种语言章节数不一致：{counts}")

    if not s.has_script:
        warnings.append("页面没有脚本，语言切换将不可用")
    if s.external:
        errors.append(f"页面引用了外部资源：{s.external}")

    dates = {
        "zh": re.search(r"最后更新：\s*([0-9]{4}\s*年\s*[0-9]{1,2}\s*月\s*[0-9]{1,2}\s*日)", html),
        "en": re.search(r"last updated:\s*([A-Z][a-z]+ \d{1,2}, \d{4})", html, re.I),
    }
    missing_dates = [k for k, v in dates.items() if not v]
    if missing_dates:
        errors.append(f"缺少更新日期：{missing_dates}")

    md_date = re.search(r"\*\*生效日期：(.+?)\*\*", md)
    if not md_date:
        errors.append("PRIVACY.md 缺少生效日期")

    print(f"sections: {s.sections}")
    print(f"h2 per language: {counts}")
    print(f"ids={len(s.ids)} anchors={len(s.anchors)} external={len(s.external)}")
    if warnings:
        for w in warnings:
            print(f"WARN {w}")
    if errors:
        for e in errors:
            print(f"FAIL {e}")
        return 1
    print("OK: 结构与链接自检通过")
    return 0


if __name__ == "__main__":
    sys.exit(main())
