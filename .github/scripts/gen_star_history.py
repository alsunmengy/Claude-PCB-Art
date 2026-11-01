#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Claude-PCB-Art · Star History 生成器
背景：assets/star-history-bg.jpg（横版插画，橙发少女 + 灯笼暖光）
主题色：从背景取色 —— 橙发高光 #ecb37a / 中调 #a15232 / 灯笼暖光 #ecb37a
输出：assets/star-history.png
"""
import json
import os
import subprocess
import urllib.request
from datetime import datetime, timezone, timedelta
from PIL import Image, ImageDraw, ImageFilter, ImageFont, ImageChops

REPO = "alsunmengy/Claude-PCB-Art"
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", ".."))
BG = os.path.join(ROOT, "assets", "star-history-bg.jpg")
OUT = os.path.join(ROOT, "assets", "star-history.png")

def pick_font(env_name, candidates, default):
    p = os.environ.get(env_name)
    if p and os.path.exists(p):
        return p
    for c in candidates:
        if os.path.exists(c):
            return c
    return default


FONT_CN = pick_font("FONT_CN", [
    "/usr/share/fonts/truetype/lxgw/LXGWWenKai-Medium.ttf",
    "/home/sever/.local/share/fonts/LXGWWenKai-Medium.ttf",
    "/usr/share/fonts/truetype/wqy/wqy-microhei.ttc",
    "/usr/share/fonts/opentype/noto/NotoSansCJK-Regular.ttc",
], "/usr/share/fonts/truetype/lxgw/LXGWWenKai-Medium.ttf")
FONT_MONO = pick_font("FONT_MONO", [
    "/usr/share/fonts/truetype/lxgw/LXGWWenKaiMono-Medium.ttf",
    "/home/sever/.local/share/fonts/LXGWWenKaiMono-Medium.ttf",
    "/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf",
], "/usr/share/fonts/truetype/lxgw/LXGWWenKaiMono-Medium.ttf")

ACCENT      = (245, 154, 87)
ACCENT_HI   = (255, 208, 146)
INK         = (248, 236, 222)
INK_DIM     = (219, 187, 162)
PANEL       = (26, 15, 9)

W, H = 1672, 941
S = 2


def font(path, size):
    return ImageFont.truetype(path, int(size * S))


def alpha_layer():
    return Image.new("RGBA", (W * S, H * S), (0, 0, 0, 0))


def vgrad(size, top, bottom):
    w, h = size
    g = Image.new("RGBA", (1, h))
    d = ImageDraw.Draw(g)
    for y in range(h):
        t = y / max(1, h - 1)
        d.point((0, y), tuple(int(top[i] + (bottom[i] - top[i]) * t) for i in range(4)))
    return g.resize((w, h))


def radial_mask(w, h, cx, cy, r):
    m = Image.new("L", (w, h), 0)
    d = ImageDraw.Draw(m)
    steps = 90
    for i in range(steps):
        t = i / steps
        rad = r * t
        d.ellipse([cx - rad, cy - rad, cx + rad, cy + rad], fill=int(255 * (1 - t) ** 1.4))
    return m.filter(ImageFilter.GaussianBlur(r * 0.18))


def spaced(draw, xy, text, fnt, fill, tracking=0):
    x, y = xy
    for ch in text:
        draw.text((x, y), ch, font=fnt, fill=fill)
        bbox = draw.textbbox((0, 0), ch, font=fnt)
        x += (bbox[2] - bbox[0]) + tracking


def rrect_mask(size, radius):
    m = Image.new("L", size, 0)
    ImageDraw.Draw(m).rounded_rectangle([0, 0, size[0] - 1, size[1] - 1], radius=radius, fill=255)
    return m


# ---------------- 数据 ----------------
def gh_api(path):
    token = os.environ.get("GITHUB_TOKEN")
    if not token:
        try:
            token = subprocess.run(["gh", "auth", "token"], capture_output=True, text=True).stdout.strip()
        except Exception:
            token = ""
    req = urllib.request.Request("https://api.github.com" + path)
    req.add_header("Accept", "application/vnd.github.star+json")
    req.add_header("User-Agent", "star-history-gen")
    if token:
        req.add_header("Authorization", "Bearer " + token)
    opener = urllib.request.build_opener(urllib.request.ProxyHandler({}))
    with opener.open(req, timeout=30) as r:
        return json.load(r)


def fetch():
    repo = gh_api(f"/repos/{REPO}")
    stars = gh_api(f"/repos/{REPO}/stargazers?per_page=100")
    try:
        views = gh_api(f"/repos/{REPO}/traffic/views")
    except Exception:
        views = {"count": 0, "uniques": 0, "views": []}
    return repo, stars, views


def build(repo, stars, views):
    created = datetime.fromisoformat(repo["created_at"].replace("Z", "+00:00"))
    now = datetime.now(timezone.utc)
    total_stars = repo["stargazers_count"]

    day0 = created.replace(hour=0, minute=0, second=0, microsecond=0)
    days, d = [], day0
    while d.date() <= now.date():
        days.append(d)
        d += timedelta(days=1)
    idx = {dd.date(): i for i, dd in enumerate(days)}
    n = len(days)

    new_stars = [0] * n
    for s in stars:
        t = datetime.fromisoformat(s["starred_at"].replace("Z", "+00:00")).date()
        if t in idx:
            new_stars[idx[t]] += 1
    cum, run = [], 0
    for v in new_stars:
        run += v
        cum.append(run)

    vmap = {}
    for v in views.get("views", []):
        vmap[datetime.fromisoformat(v["timestamp"].replace("Z", "+00:00")).date()] = v["count"]
    vmax = max(list(vmap.values()) + [1])

    # ---------------- 画布 ----------------
    bg1x = Image.open(BG).convert("RGB").resize((W, H), Image.LANCZOS)
    bg = bg1x.resize((W * S, H * S), Image.LANCZOS)
    canvas = bg.convert("RGBA")
    canvas = Image.alpha_composite(canvas, vgrad((W * S, H * S), (10, 5, 3, 118), (14, 8, 4, 196)))

    corner = Image.new("RGBA", (W * S, H * S), (12, 6, 4, 255))
    cm = radial_mask(W * S, H * S, int(0.10 * W * S), int(0.10 * H * S), int(0.46 * W * S))
    corner.putalpha(cm.point(lambda v: int(v * 0.62)))
    canvas = Image.alpha_composite(canvas, corner)

    # ---------------- 毛玻璃面板 ----------------
    px0, py0, px1, py1 = 56, 512, W - 56, H - 40
    pw, ph = px1 - px0, py1 - py0
    box = (px0 * S, py0 * S, px1 * S, py1 * S)

    glow = alpha_layer()
    ImageDraw.Draw(glow).rounded_rectangle(
        [box[0] - 5 * S, box[1] - 5 * S, box[2] + 5 * S, box[3] + 5 * S],
        radius=34 * S, fill=ACCENT + (46,))
    canvas = Image.alpha_composite(canvas, glow.filter(ImageFilter.GaussianBlur(30 * S)))

    region = bg1x.crop((px0, py0, px1, py1)).resize((pw * S, ph * S), Image.LANCZOS)
    region = region.filter(ImageFilter.GaussianBlur(10 * S))
    region = Image.blend(region, Image.new("RGB", region.size, PANEL), 0.60)
    region = region.point(lambda v: int(v * 0.70)).convert("RGBA")
    canvas.paste(region, box[:2], rrect_mask((pw * S, ph * S), 30 * S))

    edge = alpha_layer()
    ImageDraw.Draw(edge).rounded_rectangle(box, radius=30 * S, outline=ACCENT + (105,), width=max(1, int(1.4 * S)))
    canvas = Image.alpha_composite(canvas, edge)
    d = ImageDraw.Draw(canvas)

    # ---------------- 左上标题 ----------------
    f_eyebrow = font(FONT_MONO, 20)
    f_title = font(FONT_MONO, 54)
    f_sub = font(FONT_CN, 24)
    spaced(d, (80 * S, 66 * S), "STAR HISTORY", f_eyebrow, ACCENT + (255,), tracking=7 * S)
    d.text((80 * S, 100 * S), "Claude PCB Art", font=f_title, fill=INK + (255,))
    d.text((84 * S, 172 * S), "宪法 AI 的拟人纪念卡 · 星标增长记录", font=f_sub, fill=INK_DIM + (235,))
    for (sx, sy, r, a) in [(70, 74, 3.2, 210), (70, 178, 2.0, 150)]:
        d.ellipse([(sx - r) * S, (sy - r) * S, (sx + r) * S, (sy + r) * S], fill=ACCENT_HI + (a,))

    # ---------------- 图表区 ----------------
    cx0, cy0, cx1, cy1 = px0 + 74, py0 + 96, 1100, py1 - 72
    f_leg = font(FONT_CN, 19)
    f_axis = font(FONT_MONO, 16)

    lx = cx0 - 30
    d.ellipse([lx * S, (py0 + 42) * S, (lx + 8) * S, (py0 + 50) * S], fill=ACCENT_HI + (255,))
    d.text(((lx + 16) * S, (py0 + 34) * S), "累计 Star", font=f_leg, fill=INK_DIM + (255,))
    lx2 = lx + 136
    d.rounded_rectangle([lx2 * S, (py0 + 41) * S, (lx2 + 10) * S, (py0 + 51) * S], radius=2 * S, fill=ACCENT + (90,))
    d.text(((lx2 + 18) * S, (py0 + 34) * S), "每日浏览", font=f_leg, fill=INK_DIM + (255,))
    d.text((1100 * S, (py0 + 34) * S), f"近 {len(vmap)} 天有浏览数据", font=f_leg, fill=INK_DIM + (130,), anchor="ra")

    ymax = max(2, total_stars + 1)
    for i in range(3):
        y = cy1 - (cy1 - cy0) * (i / 2)
        d.line([cx0 * S, y * S, cx1 * S, y * S], fill=(255, 255, 255, 30), width=max(1, int(0.9 * S)))
        d.text(((cx0 - 22) * S, (y - 10) * S), str(int(ymax * i / 2)), font=f_axis, fill=INK_DIM + (160,), anchor="ra")

    def px_of(i):
        return cx0 + (cx1 - cx0) * (i / max(1, n - 1))

    def py_of(v):
        return cy1 - (cy1 - cy0) * (v / ymax)

    step_w = (cx1 - cx0) / max(1, n - 1)

    for i, day in enumerate(days):
        v = vmap.get(day.date(), 0)
        if not v:
            continue
        hh = (cy1 - cy0) * (v / vmax) * 0.80
        half = min(step_w * 0.22, 34)
        x = px_of(i)
        left, right = max(cx0, x - half), min(cx1, x + half)
        d.rounded_rectangle([left * S, (cy1 - hh) * S, right * S, cy1 * S], radius=3 * S, fill=(238, 214, 190, 42))
        d.text((x * S, (cy1 - hh - 22) * S), str(v), font=font(FONT_MONO, 14), fill=INK_DIM + (130,), anchor="ma")

    pts = [(px_of(i), py_of(cum[i])) for i in range(n)]

    area = Image.new("L", (W * S, H * S), 0)
    ad = ImageDraw.Draw(area)
    poly = [(px_of(0), cy1)] + pts + [(px_of(n - 1), cy1)]
    ad.polygon([(x * S, y * S) for x, y in poly], fill=255)
    fade = Image.new("L", (W * S, H * S), 0)
    fd = ImageDraw.Draw(fade)
    for y in range(int(cy0 * S), int(cy1 * S)):
        t = (y - cy0 * S) / max(1, (cy1 - cy0) * S)
        fd.line([0, y, W * S, y], fill=int(120 * (1 - t) ** 0.9))
    a_mask = ImageChops.multiply(area, fade)
    solid = Image.new("RGBA", (W * S, H * S), ACCENT + (255,))
    solid.putalpha(a_mask)
    canvas = Image.alpha_composite(canvas, solid)
    d = ImageDraw.Draw(canvas)

    line_layer = alpha_layer()
    ld = ImageDraw.Draw(line_layer)
    lw = int(3.2 * S)
    for i in range(n - 1):
        ld.line([pts[i][0] * S, pts[i][1] * S, pts[i + 1][0] * S, pts[i][1] * S], fill=ACCENT_HI + (255,), width=lw)
        ld.line([pts[i + 1][0] * S, pts[i][1] * S, pts[i + 1][0] * S, pts[i + 1][1] * S], fill=ACCENT_HI + (255,), width=lw)
    canvas = Image.alpha_composite(canvas, line_layer.filter(ImageFilter.GaussianBlur(5 * S)))
    canvas = Image.alpha_composite(canvas, line_layer)
    d = ImageDraw.Draw(canvas)

    for i in range(n):
        if new_stars[i] or i == n - 1:
            x, y = pts[i]
            r = 6 if new_stars[i] else 4.5
            d.ellipse([(x - r) * S, (y - r) * S, (x + r) * S, (y + r) * S],
                      fill=(22, 12, 6, 255), outline=ACCENT_HI + (255,), width=int(2.1 * S))

    first = next((i for i in range(n) if new_stars[i]), None)
    if first is not None and total_stars:
        x, y = pts[first]
        f_note = font(FONT_CN, 18)
        txt = f"{days[first].strftime('%m-%d')} 首个 Star"
        tw = d.textlength(txt, font=f_note) / S
        nx = min(x + 56, cx1 - tw - 20)
        ny = max(cy0 + 10, y - 52)
        d.line([x * S, y * S, nx * S, (ny + 13) * S], fill=ACCENT + (130,), width=max(1, int(1.1 * S)))
        d.rounded_rectangle([(nx - 10) * S, (ny - 5) * S, (nx + tw + 10) * S, (ny + 25) * S],
                            radius=7 * S, fill=(22, 12, 6, 205), outline=ACCENT + (70,), width=max(1, int(S)))
        d.text((nx * S, ny * S), txt, font=f_note, fill=ACCENT_HI + (250,))

    picks = sorted(set([0, n // 2, n - 1] + [i for i in range(n) if new_stars[i]]))
    for i in picks:
        x = px_of(i)
        t = days[i].strftime("%m-%d")
        if i == 0:
            d.text(((cx0 - 4) * S, (cy1 + 14) * S), t, font=f_axis, fill=INK_DIM + (195,), anchor="la")
        elif i == n - 1:
            d.text((x * S, (cy1 + 14) * S), t, font=f_axis, fill=INK_DIM + (195,), anchor="ra")
        else:
            d.text((x * S, (cy1 + 14) * S), t, font=f_axis, fill=INK_DIM + (195,), anchor="ma")

    d.text(((cx0 - 30) * S, (cy1 + 42) * S), f"建仓 {created.strftime('%Y-%m-%d')} · 数据 GitHub API",
           font=font(FONT_CN, 16), fill=INK_DIM + (135,))

    # ---------------- 右侧数据 ----------------
    sep_x = 1148
    d.line([sep_x * S, (py0 + 32) * S, sep_x * S, (py1 - 32) * S], fill=ACCENT + (44,), width=max(1, int(S)))

    f_lab = font(FONT_MONO, 17)
    f_num = font(FONT_MONO, 56)
    stats = [
        ("STARS", str(total_stars), ACCENT_HI),
        ("VIEWS · 14D", str(views.get("count", 0)), INK),
        ("VISITORS", str(views.get("uniques", 0)), INK),
        ("DAYS LIVE", str((now.date() - created.date()).days), INK),
    ]
    colx = [sep_x + 44, sep_x + 256]
    rowy = [py0 + 36, py0 + 152]
    for k, (label, val, col) in enumerate(stats):
        x, y = colx[k % 2], rowy[k // 2]
        d.text((x * S, y * S), label, font=f_lab, fill=INK_DIM + (165,))
        d.text((x * S, (y + 22) * S), val, font=f_num, fill=col + (255,))

    d.text(((px1 - 32) * S, (py1 - 30) * S), "每日自动更新", font=font(FONT_CN, 15), fill=INK_DIM + (110,), anchor="ra")

    out = canvas.convert("RGB").resize((W, H), Image.LANCZOS)
    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    out.save(OUT, optimize=True)
    print("saved", OUT, out.size, os.path.getsize(OUT) // 1024, "KB")


if __name__ == "__main__":
    repo, stars, views = fetch()
    build(repo, stars, views)
