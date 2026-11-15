# Groupメンテナンス事務局Web（https://science-web.tokyo/maintenance-9）の初校を組むスクリプト
# 土台：taka-a1111/swc2026-maintenance ver1.1 の CSS とロゴ
# 原稿：11.15 Gメンテナンス事務局Web.docx ＋ 11/15 14:45 瀧田様の回答
import base64, re, sys, os
from PIL import Image

SRC = '/home/claude/taka-a1111/swc2026-maintenance'
OUT = sys.argv[1] if len(sys.argv) > 1 else '/home/claude/group2026-maintenance'
VER = 'ver1.0'

s = open(f'{SRC}/index.html', encoding='utf-8').read()
css = s[s.index('<style>') + 7:s.index('</style>')]

def b64(path):
    return 'data:image/png;base64,' + base64.b64encode(open(path, 'rb').read()).decode()

os.makedirs(f'{OUT}/images', exist_ok=True)
# ロゴは SWC と同じ
open(f'{OUT}/images/sw-logo.png', 'wb').write(open(f'{SRC}/images/swc-logo.png', 'rb').read())
# メールアドレス画像（青）と、フッター用の白
blue = Image.open('/home/claude/gwork/mail-g-maintenance.png')
blue.save(f'{OUT}/images/mail-g-maintenance.png', optimize=True)
white = blue.copy()
px = white.load()
for y in range(white.height):
    for x in range(white.width):
        r, g, b, a = px[x, y]
        if a:
            px[x, y] = (255, 255, 255, a)
white.save(f'{OUT}/images/mail-g-maintenance-white.png', optimize=True)

LOGO = b64(f'{OUT}/images/sw-logo.png')
MAIL = b64(f'{OUT}/images/mail-g-maintenance.png')
MAILW = b64(f'{OUT}/images/mail-g-maintenance-white.png')
MAILTO = 'mailto:g-maintenance@science-web.co.jp'
W, H = blue.size

add_css = """
/* ===== Groupメンテナンス事務局Web（2026-11-15）：ここから ===== */
body{padding-bottom:0!important;}
.g-hd{justify-content:flex-start;}
.g-hero{background:#f2f8fe;padding:34px 0 30px;}
.g-catch{margin:0;font-size:clamp(14px,1.9vw,19px);font-weight:700;line-height:1.7;color:var(--navy)!important;}
.g-h1{margin:10px 0 8px;font-size:clamp(28px,8.6vw,92px);line-height:1.15;font-weight:900;color:#E65100;letter-spacing:.04em;white-space:nowrap;}
.g-lead{margin:0;font-size:clamp(15px,1.9vw,19px);font-weight:700;line-height:1.7;}
.g-three-ttl{margin:26px 0 12px;font-size:clamp(18px,2.2vw,22px);font-weight:900;color:var(--navy)!important;}
.g-three{list-style:none;margin:0;padding:0;display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:14px;}
.g-card{background:#fff;border:2px solid var(--navy);border-radius:10px;padding:16px 16px 18px;text-align:center;}
.g-badge{display:inline-block;margin:0 0 8px;padding:2px 14px;border-radius:4px;background:var(--navy);color:#fff!important;font-size:15px;font-weight:900;letter-spacing:.08em;}
.g-card-ttl{margin:0 0 6px;font-size:17px;font-weight:900;color:var(--navy-d)!important;line-height:1.5;}
.g-card-txt{margin:0;font-size:14px;line-height:1.7;}
.g-img{margin-top:26px;}
.g-body{padding:34px 0 40px;background:#fff;}
.g-2col{display:grid;grid-template-columns:minmax(0,1fr) minmax(0,1fr);gap:22px;align-items:start;}
.g-box{border:1px solid var(--line);border-radius:10px;padding:20px 22px;background:#fff;}
.g-box-ttl{margin:0 0 12px;font-size:19px;font-weight:900;color:var(--navy)!important;padding-left:12px;border-left:5px solid var(--accent);line-height:1.4;}
.g-box-note{margin:-6px 0 12px;font-size:13px;}
.g-duties{list-style:none;margin:0;padding:0;}
.g-duties li{position:relative;padding:7px 0 7px 18px;border-bottom:1px dotted #9aa7b5;font-size:15px;font-weight:700;line-height:1.6;}
.g-duties li:last-child{border-bottom:0;}
.g-duties li::before{content:"";position:absolute;left:2px;top:16px;width:8px;height:8px;border-radius:50%;background:var(--accent);}
.g-price{width:100%;border-collapse:collapse;}
.g-price th,.g-price td{padding:10px 6px;border-bottom:1px dotted #9aa7b5;text-align:left;vertical-align:middle;font-size:15px;line-height:1.5;}
.g-price th{width:30%;font-weight:900;color:var(--navy);white-space:nowrap;}
.g-price .g-yen{font-size:24px;font-weight:900;color:var(--navy);letter-spacing:-.01em;}
.g-price .g-per{font-size:14px;font-weight:700;}
.g-price .g-free{display:inline-block;margin-left:8px;padding:1px 8px;border-radius:4px;background:var(--red);color:#fff;font-size:13px;font-weight:800;white-space:nowrap;}
.g-price tr.g-sp th,.g-price tr.g-sp .g-yen{color:#D32F2F;}
.g-price .g-term{display:block;margin-top:2px;font-size:13px;font-weight:700;}
.g-tax{margin:8px 0 0;font-size:13px;text-align:right;}
.g-quote{margin-top:22px;border:2px solid var(--navy);border-radius:12px;padding:22px 24px;background:#f2f8fe;display:grid;grid-template-columns:minmax(0,1.1fr) minmax(0,.9fr);gap:20px;align-items:center;}
.g-quote-ttl{margin:0 0 6px;font-size:clamp(20px,2.4vw,26px);font-weight:900;color:var(--navy-d)!important;}
.g-quote-txt{margin:0 0 10px;font-size:15px;font-weight:700;line-height:1.7;}
.g-five{margin:0;padding:0 0 0 1.6em;font-size:15px;font-weight:700;line-height:1.9;}
.g-ask{text-align:center;}
.g-ask-lbl{margin:0 0 10px;font-size:17px;font-weight:900;color:var(--navy)!important;}
.g-ask-a{display:block;max-width:460px;margin:0 auto;background:#fff;border:2px solid var(--navy);border-radius:10px;padding:14px 16px;box-shadow:0 4px 12px rgba(15,98,180,.15);}
.g-ask-a:hover{background:var(--navy-l);}
.g-ask-a img{width:100%;height:auto;}
.g-ask-sub{margin:8px 0 0;font-size:12.5px;}
.g-footer{background:var(--navy-d);color:#fff;text-align:left;padding:28px 0 20px;font-size:14px;}
.g-footer p{color:#fff!important;}
.g-ft-grid{display:grid;grid-template-columns:minmax(0,1fr) minmax(0,1fr);gap:22px;}
.g-ft-co{margin:0 0 8px;font-size:18px;font-weight:900;letter-spacing:.04em;}
.g-ft-co small{margin-left:14px;font-size:13px;font-weight:700;letter-spacing:0;}
.g-ft-info{margin:0;}
.g-ft-info div{display:flex;gap:12px;padding:6px 0;border-bottom:1px solid rgba(255,255,255,.2);}
.g-ft-info dt{flex:0 0 9.5em;font-size:13px;font-weight:800;}
.g-ft-info dd{margin:0;font-size:14px;line-height:1.7;}
.g-ft-info a{color:#fff;}
.g-ft-mail{display:inline-block;width:min(100%,300px);vertical-align:middle;}
.g-ft-mail img{width:100%;height:auto;}
.g-ft-ttl{margin:0 0 8px;font-size:15px;font-weight:900;}
.g-ft-links{list-style:none;margin:0;padding:0;}
.g-ft-links li{padding:8px 0;border-bottom:1px solid rgba(255,255,255,.2);}
.g-ft-links .g-b{display:inline-block;min-width:3.4em;margin-right:8px;padding:0 6px;border:1px solid rgba(255,255,255,.7);border-radius:3px;font-size:12px;font-weight:900;text-align:center;}
.g-ft-links .g-n{font-weight:800;}
.g-ft-links a{display:block;margin-top:2px;color:#cfe3f7;font-size:13px;word-break:break-all;}
.g-copy{margin:18px 0 0;text-align:center;font-size:12px;opacity:.8;}
@media (max-width:900px){
  .g-three{grid-template-columns:1fr;gap:10px;}
  .g-card{display:grid;grid-template-columns:auto 1fr;gap:4px 14px;align-items:center;text-align:left;padding:14px 16px;}
  .g-badge{grid-row:1 / span 2;margin:0;}
  .g-2col,.g-quote,.g-ft-grid{grid-template-columns:1fr;}
}
@media (max-width:560px){
  .g-hero{padding:24px 0 22px;}
  .g-card{grid-template-columns:1fr;text-align:center;}
  .g-badge{grid-row:auto;justify-self:center;}
  .g-box{padding:16px 14px;}
  .g-price th{width:28%;font-size:14px;}
  .g-price .g-yen{font-size:20px;}
  .g-quote{padding:18px 14px;}
  .g-ft-info div{flex-direction:column;gap:0;}
  .g-ft-info dt{flex:none;}
}
/* ===== Groupメンテナンス事務局Web：ここまで ===== */
"""

html = f"""<!DOCTYPE html>
<!-- BUILD_TAG: group2026_maintenance_{VER} / 2026-11-15 -->
<html lang="ja">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>メンテナンス事務局｜サイエンスウェブ株式会社</title>
<meta name="description" content="PHPの脆弱性対策から、不正アクセスの早期発見、障害発生時の迅速な対応まで。サイエンスウェブの3つのメンテナンス事務局が、ホームページの安全・安心・安定を継続的に支えます。">
<meta property="og:type" content="website">
<meta property="og:locale" content="ja_JP">
<meta property="og:site_name" content="サイエンスウェブ株式会社">
<meta property="og:title" content="メンテナンス事務局｜サイエンスウェブ株式会社">
<meta property="og:description" content="研究者の現在を守り、未来の研究活動を支える。サイエンスウェブは、ホームページの安全・安心・安定を継続的に支えます。">
<meta property="og:url" content="https://science-web.tokyo/maintenance-9">
<link rel="canonical" href="https://science-web.tokyo/maintenance-9">
<meta name="twitter:card" content="summary">
<style>{css}
{add_css}</style>
</head>
<body>
<header>
  <div class="wrap hd g-hd">
    <a class="hd-logo" href="#top"><img class="hd-logo-img" src="{LOGO}" alt="サイエンスウェブ株式会社"></a>
  </div>
</header>
<main>
<div class="g-hero" id="top">
  <div class="wrap">
    <p class="g-catch"><span class="nobr">PHPの脆弱性対策から、</span><span class="nobr">不正アクセスの早期発見、</span><span class="nobr">障害発生時の迅速な対応まで。</span></p>
    <p class="g-catch"><span class="nobr">研究者の現在を守り、</span><span class="nobr">未来の研究活動を支える。</span></p>
    <h1 class="g-h1">メンテナンス事務局</h1>
    <p class="g-lead"><span class="nobr">サイエンスウェブは、</span><span class="nobr">ホームページの安全・安心・安定を</span><span class="nobr">継続的に支えます。</span></p>
    <h2 class="g-three-ttl">3つのメンテナンス事務局</h2>
    <ul class="g-three">
      <li class="g-card"><p class="g-badge">SWC</p><p class="g-card-ttl">研究紹介ホームページ制作</p><p class="g-card-txt">研究者の情報発信を支える<span class="nobr">ホームページの保守・管理</span></p></li>
      <li class="g-card"><p class="g-badge">SWT</p><p class="g-card-ttl">学術運営システムの開発</p><p class="g-card-txt">学術活動を支える<span class="nobr">システムの保守・管理</span></p></li>
      <li class="g-card"><p class="g-badge">SWO</p><p class="g-card-ttl">大会開催の準備と運営</p><p class="g-card-txt">学会大会の開催・運営を支える<span class="nobr">業務支援</span></p></li>
    </ul>
  </div>
  <!-- 画像エリア：ご購入画像を images/ に置き、下の div の中に次の行のように img を入れてください
       <img src="images/top1.jpg" alt="メンテナンス事務局のイメージ">
       img を入れると「画像エリア」の文字は自動で消えます。
       枠は左右いっぱいで、パソコンでは横長（16:7）、スマホでは 3:2 です。横幅2000px前後の画像をおすすめします。 -->
  <div class="media-slot mt-wide g-img" aria-label="メンテナンス事務局のイメージ"><span class="ms-note">画像エリア</span></div>
</div>
<div class="g-body">
  <div class="wrap">
    <div class="g-2col">
      <div class="g-box">
        <h2 class="g-box-ttl">お約束する委託業務</h2>
        <ul class="g-duties">
          <li>サーバーの保守・管理・監視</li>
          <li>サーバー障害の調査・復旧支援</li>
          <li>メールサーバーの管理</li>
          <li>メールアカウントの設定・管理</li>
          <li>グループメールの管理</li>
          <li>ドメイン・URL・DNSの管理</li>
          <li>PHP・データベースの管理</li>
          <li>セキュリティ対策、その他</li>
        </ul>
      </div>
      <div class="g-box">
        <h2 class="g-box-ttl">料金プラン</h2>
        <p class="g-box-note">年度末にて更新します</p>
        <table class="g-price">
          <tr><th>3ヶ月</th><td><span class="g-yen">30,000</span><span class="g-per">円／月額</span></td></tr>
          <tr><th>6ヶ月</th><td><span class="g-yen">25,000</span><span class="g-per">円／月額</span><span class="g-free">初月無料</span></td></tr>
          <tr><th>1年間</th><td><span class="g-yen">20,000</span><span class="g-per">円／月額</span><span class="g-free">初月無料</span></td></tr>
          <tr class="g-sp"><th>特別プラン</th><td><span class="g-yen">100,000</span><span class="g-per">円 合計</span><span class="g-term"><span class="nobr">2026/12/1〜2027/3/31</span><span class="nobr">（4ヶ月間）</span></span></td></tr>
        </table>
        <p class="g-tax">消費税別</p>
      </div>
    </div>
    <div class="g-quote">
      <div>
        <h2 class="g-quote-ttl">まずは無料見積もりから</h2>
        <p class="g-quote-txt"><span class="nobr">基本見積書は、</span><span class="nobr">着信後24時間以内に</span><span class="nobr">提出いたします。</span><br>積算に必要なのは、次の5点です。</p>
        <ol class="g-five">
          <li>ドメイン名</li>
          <li>ホームページURL</li>
          <li>サーバー会社名</li>
          <li>メール利用状況</li>
          <li>業務開始ご希望の月</li>
        </ol>
      </div>
      <div class="g-ask">
        <p class="g-ask-lbl">基本見積書ご依頼は</p>
        <a class="g-ask-a" href="{MAILTO}"><img src="{MAIL}" alt="g-maintenance@science-web.co.jp" width="{W}" height="{H}"></a>
        <p class="g-ask-sub">押すとメールソフトが起動します</p>
      </div>
    </div>
  </div>
</div>
</main>
<footer class="g-footer">
  <div class="wrap g-ft-grid">
    <div>
      <p class="g-ft-co">サイエンスウェブ株式会社<small>創業 2007年</small></p>
      <dl class="g-ft-info">
        <div><dt>メンテナンス事務局</dt><dd>丹野篤美</dd></div>
        <div><dt>所在地</dt><dd>305-0051 つくば市二の宮1-21-11</dd></div>
        <div><dt>Call</dt><dd><a href="tel:05035387006">050-3538-7006</a>　<span class="nobr">平日10：00～15：00</span></dd></div>
        <div><dt>Mail</dt><dd><a class="g-ft-mail" href="{MAILTO}"><img src="{MAILW}" alt="g-maintenance@science-web.co.jp" width="{W}" height="{H}"></a></dd></div>
      </dl>
    </div>
    <div>
      <p class="g-ft-ttl">3つのメンテナンス事務局</p>
      <ul class="g-ft-links">
        <li><span class="g-b">SWC</span><span class="g-n">研究紹介ホームページ制作</span><a href="https://www.science-web.co.jp/2026maintenance">https://www.science-web.co.jp/2026maintenance</a></li>
        <li><span class="g-b">SWT</span><span class="g-n">学術運営システムの開発</span><a href="https://www.science-web.tokyo/2026maintenance">https://www.science-web.tokyo/2026maintenance</a></li>
        <li><span class="g-b">SWO</span><span class="g-n">大会開催の準備と運営</span><a href="https://www.science-web.online/maintenance/">https://www.science-web.online/maintenance/</a></li>
      </ul>
    </div>
  </div>
  <p class="g-copy">© サイエンスウェブ株式会社 2026</p>
</footer>
</body>
</html>
"""
open(f'{OUT}/index.html', 'w', encoding='utf-8').write(html)
print('written', len(html))
