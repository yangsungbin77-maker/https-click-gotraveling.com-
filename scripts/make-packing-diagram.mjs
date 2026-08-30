import sharp from 'sharp';

const svg = `<svg width="1600" height="1000" viewBox="0 0 1600 1000" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="bg" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0" stop-color="#f6f1e7"/>
      <stop offset="1" stop-color="#efe6d4"/>
    </linearGradient>
  </defs>
  <rect width="1600" height="1000" fill="url(#bg)"/>
  <text x="800" y="86" text-anchor="middle" font-family="Malgun Gothic" font-size="52" font-weight="bold" fill="#1f3d33">캐리어 짐싸기 배치도 — 무게는 바퀴 쪽으로</text>
  <text x="800" y="140" text-anchor="middle" font-family="Malgun Gothic" font-size="30" fill="#5c6f66">세워도 안 무너지는 순서, 아래(바퀴)부터 채웁니다</text>

  <!-- suitcase body -->
  <rect x="330" y="200" width="700" height="700" rx="40" fill="#ffffff" stroke="#1f3d33" stroke-width="6"/>
  <!-- handle -->
  <rect x="600" y="150" width="160" height="50" rx="16" fill="none" stroke="#1f3d33" stroke-width="6"/>
  <!-- wheels -->
  <circle cx="420" cy="925" r="28" fill="#1f3d33"/>
  <circle cx="940" cy="925" r="28" fill="#1f3d33"/>

  <!-- zone: top light -->
  <rect x="360" y="230" width="640" height="170" rx="18" fill="#dff0e4"/>
  <text x="680" y="300" text-anchor="middle" font-family="Malgun Gothic" font-size="34" font-weight="bold" fill="#1f6b46">손잡이 쪽 — 가벼운 것</text>
  <text x="680" y="352" text-anchor="middle" font-family="Malgun Gothic" font-size="28" fill="#2c5a44">니트 · 셔츠 · 구겨지기 쉬운 옷</text>

  <!-- zone: middle -->
  <rect x="360" y="420" width="640" height="220" rx="18" fill="#fdeeca"/>
  <text x="680" y="505" text-anchor="middle" font-family="Malgun Gothic" font-size="34" font-weight="bold" fill="#8a6410">중간 — 부피 담당</text>
  <text x="680" y="557" text-anchor="middle" font-family="Malgun Gothic" font-size="28" fill="#77601f">돌돌 만 옷 · 압축팩 · 패킹큐브</text>

  <!-- zone: bottom heavy -->
  <rect x="360" y="660" width="640" height="210" rx="18" fill="#f8d9cf"/>
  <text x="680" y="740" text-anchor="middle" font-family="Malgun Gothic" font-size="34" font-weight="bold" fill="#a03a20">바퀴 쪽 — 무거운 것</text>
  <text x="680" y="792" text-anchor="middle" font-family="Malgun Gothic" font-size="28" fill="#8c4530">신발 · 세면파우치 · 드라이기 · 책</text>

  <!-- side tips -->
  <g font-family="Malgun Gothic">
    <rect x="1090" y="230" width="440" height="150" rx="18" fill="#ffffff" stroke="#c9bfa8" stroke-width="3"/>
    <text x="1115" y="285" font-size="30" font-weight="bold" fill="#1f3d33">틈새 = 양말 · 충전기</text>
    <text x="1115" y="330" font-size="26" fill="#5c6f66">신발 속과 모서리 빈틈에 채우기</text>

    <rect x="1090" y="420" width="440" height="150" rx="18" fill="#ffffff" stroke="#c9bfa8" stroke-width="3"/>
    <text x="1115" y="475" font-size="30" font-weight="bold" fill="#1f3d33">전체의 70~80%만 채우기</text>
    <text x="1115" y="520" font-size="26" fill="#5c6f66">쇼핑 · 기념품 자리 남겨두기</text>

    <rect x="1090" y="610" width="440" height="150" rx="18" fill="#ffffff" stroke="#c9bfa8" stroke-width="3"/>
    <text x="1115" y="665" font-size="30" font-weight="bold" fill="#1f3d33">액체류는 지퍼백 이중 포장</text>
    <text x="1115" y="710" font-size="26" fill="#5c6f66">터지면 옷 전체가 젖습니다</text>
  </g>
</svg>`;

await sharp(Buffer.from(svg)).png().toFile('src/assets/posts/carrier-packing-guide.png');
console.log('done');
