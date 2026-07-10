// 여행지·주제별 카테고리 정의 (단일 소스).
// 글에 category frontmatter를 두지 않고 여기서 slug를 묶어 분류한다.
// 새 글을 쓰면 해당 카테고리 posts 배열에 slug만 추가하면 메뉴·목록에 자동 반영된다.

export type Category = {
	slug: string; // URL: /category/<slug>/
	label: string; // 메뉴에 노출되는 짧은 이름
	title: string; // 카테고리 페이지 제목(풀네임)
	emoji: string;
	blurb: string;
	posts: string[]; // 이 카테고리에 속한 글 slug(= 파일명, post.id)
};

export const CATEGORIES: Category[] = [
	{
		slug: 'vietnam',
		label: '베트남',
		title: '베트남 여행정보',
		emoji: '🇻🇳',
		blurb: '다낭·호치민·하노이부터 맥주·지하철·물가까지, 베트남 여행에 필요한 정보를 모았습니다.',
		posts: [
			'travel-vietnamese-phrases',
			'ho-chi-minh-map-travel-course',
			'vietnam-street-food-noodles',
			'vietnam-travel-checklist',
			'vietnam-metro-lines',
			'vietnam-beer',
			'danang-rainy-season',
			'vietnam-jobs',
			'vietnam-female-celebrities',
			'vietnam-male-celebrities',
		],
	},
	{
		slug: 'japan',
		label: '일본',
		title: '일본 여행정보',
		emoji: '🇯🇵',
		blurb: '오사카·교토 코스와 계절별 일정, 가족·솔로 여행 유형별 일본 여행 가이드입니다.',
		posts: [
			'osaka-travel-course',
			'osaka-free-travel-guide',
			'solo-japan-travel-course',
			'parents-japan-travel-course',
			'winter-japan-travel-course',
		],
	},
	{
		slug: 'tips',
		label: '여행꿀팁',
		title: '여행 준비·꿀팁',
		emoji: '🧳',
		blurb: '항공권·LCC·유심/이심·기내반입·첫 해외여행 체크리스트부터 제주 국내 코스까지, 나라 상관없이 쓰는 여행 준비 정보입니다.',
		posts: [
			'cheap-flight-tickets-tips',
			'lcc-airline-tips',
			'usim-esim-difference',
			'carry-on-prohibited-items',
			'overseas-travel-checklist-first-time',
			'jeju-3night4day-course',
		],
	},
];

export function categoryOf(id: string): Category | undefined {
	return CATEGORIES.find((c) => c.posts.includes(id));
}
