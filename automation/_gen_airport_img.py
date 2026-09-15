# 베트남 국제공항 글 본문 이미지 — 호치민 시내·떤선녓·롱탄 위치 관계 + 이전 3단계 타임라인 도식. PIL 자체 제작(크레딧 0).
# 사용: py automation/_gen_airport_img.py
import os
from PIL import Image, ImageDraw, ImageFont

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, "src", "assets", "posts", "vietnam-international-airports-long-thanh.webp")
FB, FR = r"C:\Windows\Fonts\malgunbd.ttf", r"C:\Windows\Fonts\malgun.ttf"
PAPER, INK, JADE, JADE2, MUTE, RED = (250, 247, 240), (22, 25, 29), (15, 110, 99), (210, 232, 226), (110, 118, 128), (178, 60, 50)


def f(s, b=True):
    return ImageFont.truetype(FB if b else FR, s)


w, h = 1600, 1000
img = Image.new("RGB", (w, h), PAPER)
d = ImageDraw.Draw(img)
# 은은한 격자
for x in range(0, w, 80):
    d.line((x, 0, x, h), fill=(236, 232, 224), width=1)
for y in range(0, h, 80):
    d.line((0, y, w, y), fill=(236, 232, 224), width=1)

d.text((70, 50), "호치민권 공항 위치 관계 — 떤선녓 vs 롱탄", font=f(46), fill=INK)
d.text((70, 112), "롱탄은 '2군'이 아니라 2군 방향 고속도로 끝, 동나이성에 있습니다 (거리는 대략값)", font=f(26, False), fill=MUTE)

# 지도 도식 영역
mx, my = 70, 180
d.rounded_rectangle((mx, my, mx + 1460, my + 430), radius=24, fill=(255, 255, 255), outline=(220, 214, 204), width=2)
def node(x, y, label, sub, color, r=26, above=False):
    d.ellipse((x - r, y - r, x + r, y + r), fill=color, outline=(255, 255, 255), width=4)
    if above:
        d.text((x, y - r - 60), label, font=f(30), fill=INK, anchor="ma")
        d.text((x, y - r - 22), sub, font=f(22, False), fill=MUTE, anchor="ma")
    else:
        d.text((x, y + r + 12), label, font=f(30), fill=INK, anchor="ma")
        d.text((x, y + r + 50), sub, font=f(22, False), fill=MUTE, anchor="ma")


# 노드 좌표 (라벨이 겹치지 않게 위·아래로 번갈아 배치)
tsn = (mx + 260, my + 250)     # 떤선녓 — 라벨 위
c1 = (mx + 520, my + 250)      # 1군 시내 — 라벨 아래
td = (mx + 800, my + 250)      # 2군·투득·투티엠 — 라벨 위
lt = (mx + 1320, my + 250)     # 롱탄 — 라벨 아래

# 연결선
d.line([tsn, c1], fill=JADE, width=8)
d.line([c1, td, lt], fill=(120, 130, 140), width=8)
def pill(cx, cy, text, color):
    tw = d.textlength(text, font=f(24))
    d.rounded_rectangle((cx - tw / 2 - 16, cy - 20, cx + tw / 2 + 16, cy + 20), radius=20, fill=(255, 255, 255), outline=color, width=2)
    d.text((cx, cy), text, font=f(24), fill=color, anchor="mm")


pill((tsn[0] + c1[0]) // 2, my + 250, "약 7km · 그랩 30분", JADE)
pill((td[0] + lt[0]) // 2, my + 250, "약 40km · 고속도로 1시간+", (90, 100, 110))
d.text(((td[0] + lt[0]) // 2, my + 300), "투티엠–롱탄 메트로 42km (2031년 목표, 계획 단계)", font=f(22, False), fill=MUTE, anchor="ma")

node(*tsn, "떤선녓 국제공항 (SGN)", "한국 직항 · 2027년까지 유력", JADE, above=True)
node(*c1, "호치민 1군 시내", "벤탄시장·동커이", INK, r=20)
node(*td, "2군 · 투득 · 투티엠", "고속도로 시작점 · 메트로 출발역", (90, 100, 110), r=20, above=True)
node(*lt, "롱탄 국제공항 (LTH)", "동나이성 · 2026.12.1 개항 목표", RED, r=30, above=True)

# 타임라인
ty = 660
d.text((70, ty), "떤선녓 → 롱탄 노선 이전 3단계 (굿모닝베트남·VnExpress 보도 기준)", font=f(34), fill=INK)
steps = [
    ("1단계  2026.12.1 ~ 2027.3.27", "장거리 국제선·화물·신규편", "한국편은 떤선녓"),
    ("2단계  2027.3.28 ~ 10.30", "유럽·미주·오세아니아·아프리카·중동", "동북아는 떤선녓 · 동남아 분배"),
    ("3단계  2027.10.31 ~ 2028.3.25", "롱탄이 국제선 허브", "떤선녓은 단거리·국내선"),
]
bx, by, bw, bh, gap = 70, ty + 60, 460, 200, 40
for i, (t, a, b) in enumerate(steps):
    x = bx + i * (bw + gap)
    d.rounded_rectangle((x, by, x + bw, by + bh), radius=18, fill=JADE2 if i < 2 else (240, 228, 224), outline=(210, 204, 194), width=2)
    d.text((x + 24, by + 22), t, font=f(26), fill=JADE if i < 2 else RED)
    d.text((x + 24, by + 74), a, font=f(26, False), fill=INK)
    d.text((x + 24, by + 124), "→ " + b, font=f(24), fill=MUTE)
    if i < 2:
        d.polygon([(x + bw + 8, by + bh // 2 - 14), (x + bw + 32, by + bh // 2), (x + bw + 8, by + bh // 2 + 14)], fill=MUTE)

d.text((70, 950), "정리: 클릭고트래블링 · 2026년 9월 15일 기준. 일정은 공식 발표에 따라 바뀔 수 있음", font=f(20, False), fill=MUTE)
img.save(OUT, "WEBP", quality=88)
print("saved", OUT)
