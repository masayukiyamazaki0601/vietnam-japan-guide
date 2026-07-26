import { readFileSync, writeFileSync, readdirSync } from 'fs';
import { join, dirname } from 'path';
import { fileURLToPath } from 'url';

const __dirname = dirname(fileURLToPath(import.meta.url));
const visaDir = join(__dirname, 'articles/visa');
const files = readdirSync(visaDir).filter(f => f.endsWith('.vi.html'));

// パンくずリストの第2階層のname/itemを記事パスに応じて修正
function fixBreadcrumb(html, filename) {
  // name:"Visa – Tư cách lưu trú" → "Visa / Tư cách lưu trú"
  html = html.replace(/"name":"Visa – Tư cách lưu trú"/g, '"name":"Visa / Tư cách lưu trú"');
  // パンくずのアイテムURLを.vi.htmlに修正（既にそうなっていなければ）
  // og:url が .html のままの場合 .vi.html に
  html = html.replace(/og:url" content="(.*?)\.html"/g, (m, p1) => {
    if (!p1.endsWith('.vi')) return `og:url" content="${p1}.vi.html"`;
    return m;
  });
  return html;
}

function fixHeader(html) {
  // === ナビゲーションのラベル統一 ===
  // Vĩnh trú – Nhập tịch → Thường trú / Nhập tịch
  html = html.replace(/Vĩnh trú – Nhập tịch/g, 'Thường trú / Nhập tịch');
  // Visa – Tư cách lưu trú（リンクテキスト）→ Visa / Gia hạn（但しactiveの場合は異なる）
  html = html.replace(/"Visa – Tư cách lưu trú"/g, '"Visa / Tư cách lưu trú"');
  // Đời sống – Hành chính → Cuộc sống / Hành chính
  html = html.replace(/Đời sống – Hành chính/g, 'Cuộc sống / Hành chính');
  // Việc làm – Tài chính → Việc làm / Tài chính
  html = html.replace(/Việc làm – Tài chính/g, 'Việc làm / Tài chính');

  // style="display:none" がないcong-viecに追加（visa記事でcong-viecがactiveでない場合）
  html = html.replace(
    /<li><a href="\/pages\/cong-viec\.html" class="header__nav-link"><\/li>/,
    '<li><a href="/pages/cong-viec.html" class="header__nav-link" style="display:none">'
  );
  // 既存で display:none がないものにも追加（liごと置換）
  html = html.replace(
    /(<li><a href="\/pages\/cong-viec\.html" class="header__nav-link">)([^<]*)(<\/a><\/li>)/g,
    '$1$2</a></li>'.replace('<a ', '<a style="display:none" ')
  );
  // 上記の汎用版：Việc làm / Tài chínhが含まれていてdisplay:noneがない場合
  html = html.replace(
    /(class="header__nav-link">Việc làm \/ Tài chính<\/a><\/li>)/,
    'style="display:none"$1'
  );
  // より確実に：cong-viecのliにdisplay:noneを追加
  html = html.replace(
    /<li><a href="\/pages\/cong-viec\.html" class="header__nav-link">([^<]*)<\/a><\/li>/g,
    (m, txt) => m.includes('style=') ? m : `<li><a href="/pages/cong-viec.html" class="header__nav-link" style="display:none">${txt}</a></li>`
  );

  // ヘッダーロゴの複雑な構造を簡略化
  // <a href="/" class="header__logo" aria-label="..."><span class="header__logo-icon" aria-hidden="true">VN</span><span>Vietnam Japan Guide</span></a>
  // → <a href="/" class="header__logo"><span class="header__logo-icon" aria-hidden="true">VN</span>Vietnam Japan Guide</a>
  html = html.replace(
    /<a href="\/" class="header__logo" aria-label="[^"]*">\s*<span class="header__logo-icon" aria-hidden="true">VN<\/span>\s*<span>Vietnam Japan Guide<\/span>\s*<\/a>/g,
    '<a href="/" class="header__logo"><span class="header__logo-icon" aria-hidden="true">VN</span>Vietnam Japan Guide</a>'
  );

  // nav の role="navigation" aria-label を削除
  html = html.replace(
    /<nav class="header__nav" role="navigation" aria-label="[^"]*">/g,
    '<nav class="header__nav">'
  );

  // hamburger menuのaria-expandedを削除
  html = html.replace(
    /<button class="header__menu-toggle" aria-label="Menu" aria-expanded="false">/g,
    '<button class="header__menu-toggle" aria-label="Menu">'
  );

  return html;
}

function fixFooter(html) {
  // フッターの日本語をベトナム語に統一
  html = html.replace(/当サイトについて/g, 'Về chúng tôi');
  html = html.replace(/カテゴリー/g, 'Danh mục');
  html = html.replace(/<a href="\/pages\/vinh-tru\.html">永住権<\/a>/g, '<a href="/pages/vinh-tru.html">Vĩnh trú</a>');
  html = html.replace(/<a href="\/pages\/visa\.html">ビザ<\/a>/g, '<a href="/pages/visa.html">Visa</a>');
  html = html.replace(/<a href="\/pages\/sinh-hoat\.html">生活<\/a>/g, '<a href="/pages/sinh-hoat.html">Đời sống</a>');
  html = html.replace(/<a href="\/pages\/cong-viec\.html">仕事<\/a>/g, '<a href="/pages/cong-viec.html">Công việc</a>');
  
  // footerの日本語テキスト置換
  html = html.replace(
    /Trang web này không phải là chuyên gia pháp lý\. Nội dung chỉ là thông tin tham khảo\. Để có quyết định chính xác, vui lòng xác nhận với Cục Quản lý Xuất nhập cảnh hoặc Gyoseishoshi\./g,
    ''
  );
  // 日本語フッターがあれば置換
  html = html.replace(
    /※ 当サイトは法律専門家ではありません。記載内容は参考情報であり、正確な判断については出入国在留管理庁または行政書士にご確認ください。/g,
    '※ Trang web này không phải là chuyên gia pháp lý. Nội dung chỉ là thông tin tham khảo. Để có quyết định chính xác, vui lòng xác nhận với Cục Quản lý Xuất nhập cảnh hoặc Gyoseishoshi.'
  );
  
  // footerのpタグでVietnam Japan Guideが入っているものはTrangに置換
  html = html.replace(
    /<p style="font-size:var\(--fs-sm\);">Vietnam Japan Guide<\/p>/g,
    '<p style="font-size:var(--fs-sm);">Trang thông tin tổng hợp về cuộc sống tại Nhật Bản dành cho người Việt.</p>'
  );

  // back-to-topのaria-label
  html = html.replace(/aria-label="トップに戻る"/g, 'aria-label="Lên đầu trang"');
  // フッターメニューの「Visa – Tư cách lưu trú」など
  html = html.replace(/Visa – Tư cách lưu trú/g, 'Visa / Tư cách lưu trú');

  return html;
}

let count = 0;
for (const file of files) {
  const path = join(visaDir, file);
  let html = readFileSync(path, 'utf-8');
  const before = html;
  
  html = fixBreadcrumb(html, file);
  html = fixHeader(html);
  html = fixFooter(html);
  
  if (html !== before) {
    writeFileSync(path, html, 'utf-8');
    count++;
    console.log(`✅ Fixed: ${file}`);
  }
}

// vi/pages/visa.html も修正
const visaPagePath = join(__dirname, 'vi/pages/visa.html');
let visaPage = readFileSync(visaPagePath, 'utf-8');
visaPage = fixHeader(visaPage);
visaPage = fixFooter(visaPage);
writeFileSync(visaPagePath, visaPage, 'utf-8');
console.log(`✅ Fixed: vi/pages/visa.html`);

console.log(`\n🎉 Done! ${count + 1} files updated.`);
