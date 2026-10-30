# 유럽 배낭여행 2주 서유럽 클래식 루트 도시 흐름 지도 — 비교표에서 지도형으로 유형 분산. PIL 자체 제작(크레딧 0).
# 사용: python3 automation/_gen_europe_route_map.py
import os
from PIL import Image, ImageDraw, ImageFont

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, "src", "assets", "posts", "europe-backpacking-route-1.png")
FONT = "/System/Library/Fonts/AppleSDGothicNeo.ttc"

PAPER = (250, 247, 240)
INK = (22, 25, 29)
JADE = (15, 110, 99)
MUTE = (110, 118, 128)
AMBER = (205, 140, 40)
BLUE = (36, 86, 138)
LAND = (238, 232, 220)
LAND_LINE = (205, 198, 184)
SEA = (223, 234, 240)


def f(size, idx=5):
    return ImageFont.truetype(FONT, size, index=idx)


w, h = 1600, 900
img = Image.new("RGB", (w, h), PAPER)
d = ImageDraw.Draw(img)

d.text((60, 42), "2주 서유럽 클래식 루트 — 도시 흐름 지도", font=f(44), fill=INK)
d.text((60, 102), "런던 → 파리 → 암스테르담 → 베를린 → 로마 · 숙박 2·3·3·3·3박 · 쉥겐 90/180일 안전권", font=f(26, idx=0), fill=MUTE)

mx, my, mw, mh = 60, 160, 1100, 680
d.rounded_rectangle((mx, my, mx + mw, my + mh), radius=22, fill=SEA, outline=(195, 210, 220), width=2)

europe_outline = [
    (100, 140), (170, 95), (260, 70), (360, 60), (460, 60), (560, 55),
    (680, 55), (790, 70), (880, 95), (960, 125), (1030, 170), (1065, 230),
    (1070, 300), (1050, 365), (1010, 420), (950, 465), (870, 495), (780, 515),
    (690, 525), (590, 530), (500, 525), (415, 510), (335, 480), (265, 440),
    (210, 385), (170, 320), (140, 240), (100, 170), (100, 140),
]
d.polygon([(mx + px, my + py) for (px, py) in europe_outline], fill=LAND, outline=LAND_LINE)

uk_outline = [
    (85, 115), (135, 95), (175, 100), (195, 125),
    (190, 170), (160, 195), (115, 195), (85, 165), (75, 135),
]
d.polygon([(mx + px, my + py) for (px, py) in uk_outline], fill=(245, 240, 225), outline=LAND_LINE)

cities = [
    ("런던", "London · 2박", (mx + 140, my + 140), BLUE, "right"),
    ("파리", "Paris · 3박", (mx + 300, my + 265), JADE, "right"),
    ("암스테르담", "Amsterdam · 3박", (mx + 430, my + 170), JADE, "left"),
    ("베를린", "Berlin · 3박", (mx + 680, my + 190), JADE, "right"),
    ("로마", "Rome · 3박", (mx + 680, my + 455), JADE, "right"),
]

route_lines = [
    (cities[0][2], cities[1][2], "유로스타 2:20", "below"),
    (cities[1][2], cities[2][2], "탈리스 3:30", "below"),
    (cities[2][2], cities[3][2], "탈리스·저가항공", "above"),
    (cities[3][2], cities[4][2], "저가항공 2:00", "right"),
]

for (a, b, label, _) in route_lines:
    d.line([a, b], fill=AMBER, width=5)

for (a, b, label, side) in route_lines:
    mx2 = (a[0] + b[0]) // 2
    my2 = (a[1] + b[1]) // 2
    if side == "above":
        my2 -= 32
    elif side == "below":
        my2 += 32
    elif side == "right":
        mx2 += 110
    tw = d.textlength(label, font=f(18, idx=0))
    d.rounded_rectangle((mx2 - tw / 2 - 10, my2 - 14, mx2 + tw / 2 + 10, my2 + 14),
                        radius=12, fill=(255, 253, 245), outline=AMBER, width=1)
    d.text((mx2, my2), label, font=f(18, idx=0), fill=AMBER, anchor="mm")

for (name, sub, (x, y), color, side) in cities:
    r = 14
    d.ellipse((x - r, y - r, x + r, y + r), fill=color, outline=(255, 255, 255), width=3)
    if side == "right":
        d.text((x + r + 10, y - 16), name, font=f(28), fill=INK)
        d.text((x + r + 10, y + 14), sub, font=f(20, idx=0), fill=MUTE)
    else:
        tw = d.textlength(name, font=f(28))
        d.text((x - r - 10 - tw, y - 16), name, font=f(28), fill=INK)
        sw = d.textlength(sub, font=f(20, idx=0))
        d.text((x - r - 10 - sw, y + 14), sub, font=f(20, idx=0), fill=MUTE)

lx, ly = 1200, 220
d.text((lx, ly), "범례", font=f(28), fill=INK)
d.rectangle((lx, ly + 60, lx + 24, ly + 84), fill=LAND, outline=JADE, width=2)
d.text((lx + 36, ly + 60), "쉥겐 29개국 영역", font=f(22), fill=JADE)
d.text((lx + 36, ly + 90), "(2025년 불가리아·루마니아 포함)", font=f(16, idx=0), fill=MUTE)

d.rectangle((lx, ly + 140, lx + 24, ly + 164), fill=(245, 240, 225), outline=MUTE, width=2)
d.text((lx + 36, ly + 140), "비쉥겐 — 영국·아일랜드", font=f(22), fill=MUTE)
d.text((lx + 36, ly + 170), "(별도 입국·2026년 영국 ETA 필요)", font=f(16, idx=0), fill=MUTE)

d.line((lx, ly + 230, lx + 24, ly + 230), fill=AMBER, width=5)
d.text((lx + 36, ly + 218), "주 이동 경로", font=f(22), fill=AMBER)
d.text((lx + 36, ly + 248), "(유로스타·탈리스·저가항공)", font=f(16, idx=0), fill=MUTE)

d.ellipse((lx + 2, ly + 298, lx + 22, ly + 318), fill=JADE, outline=(255, 255, 255), width=2)
d.text((lx + 36, ly + 300), "쉥겐 도시 거점", font=f(22), fill=JADE)
d.ellipse((lx + 2, ly + 338, lx + 22, ly + 358), fill=BLUE, outline=(255, 255, 255), width=2)
d.text((lx + 36, ly + 340), "비쉥겐 거점(런던)", font=f(22), fill=BLUE)

box_x, box_y = 60, 858
d.text((box_x, box_y), "요약 — 5개 도시, 유로스타+탈리스+저가항공 ≈ 30~40만원대(유레일 플렉시 7일 54만원보다 10~20만원 저렴) · 지도는 클릭고트래블링 자체 제작 모식도(좌표 비정확) · tali.kr·kr.trip.com 교차(2026-10)", font=f(18, idx=0), fill=MUTE)

img.save(OUT, "PNG")
print("saved", OUT, "size", os.path.getsize(OUT))
