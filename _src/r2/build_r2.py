# Groupメンテナンス事務局Web ver1.1（2026-11-16 瀧田様「校正もどし」）
# 土台：公開中ページ https://science-web.tokyo/maintenance-g （瀧田様の添付 index.html＋GAタグ）
# 1 トップ画像をスライドショーに（images/top1.png・top2.png、約5秒ごと、枚数はJSで自動）
# 2 メールアドレス画像を g-maintenance@science-web.tokyo に（2か所の画像・mailto・alt）
# 使い方：python3 build_r2.py 入力.html 出力.html 青画像.png 白画像.png
import sys, base64, re
src, out, blue, white = sys.argv[1:5]
s = open(src, encoding='utf-8').read()

def rep(old, new, n):
    global s
    c = s.count(old)
    if c != n:
        sys.exit(f'件数が違う（期待{n}・実際{c}）：{old[:60]}')
    s = s.replace(old, new)

def b64(p):
    return 'data:image/png;base64,' + base64.b64encode(open(p, 'rb').read()).decode()

rep('BUILD_TAG: group2026_maintenance_ver1.0 / 2026-11-15', 'BUILD_TAG: group2026_maintenance_ver1.1 / 2026-11-16', 1)

# 2 メールアドレス画像（青＝見積依頼、白＝フッター）
m = re.findall(r'(<a class="g-ask-a" href="[^"]*"><img src=")(data:image/png;base64,[^"]+)(")', s)
if len(m) != 1: sys.exit('見積依頼の画像が1件でない')
s = s.replace(m[0][1], b64(blue), 1)
m = re.findall(r'(<a class="g-ft-mail" href="[^"]*"><img src=")(data:image/png;base64,[^"]+)(")', s)
if len(m) != 1: sys.exit('フッターの画像が1件でない')
s = s.replace(m[0][1], b64(white), 1)
rep('g-maintenance@science-web.co.jp', 'g-maintenance@science-web.tokyo', 4)  # mailto 2・alt 2

# 1 スライドショー
i = s.index('  <!-- 画像エリア：ご購入画像を images/ に置き')
j = s.index('</div>', s.index('<div class="media-slot mt-wide g-img"')) + len('</div>')
old_block = s[i:j]
if 'images/top1.png' not in old_block: sys.exit('画像エリアに top1.png が無い')
new_block = '''  <!-- 画像エリア（スライドショー）：約5秒ごとに切り替わります。
       画像を足すときは images/ に置き、下の mt-slide の行を写して src を変えてください（3〜5枚まで。丸のボタンは枚数に合わせて自動で出ます）。
       例 <div class="mt-slide"><img src="images/top3.png" alt="メンテナンス事務局のイメージ"></div>
       枠は左右いっぱいで、パソコンでは横長（16:7）、スマホでは 3:2 です。横幅2000px前後の画像をおすすめします。 -->
  <div class="media-slot mt-slides mt-wide g-img" id="mediaSlot" aria-label="メンテナンス事務局のイメージ">
    <div class="mt-slide on"><img src="images/top1.png" alt="メンテナンス事務局のイメージ"></div>
    <div class="mt-slide"><img src="images/top2.png" alt="メンテナンス事務局のイメージ"></div>
    <div class="mt-dots" role="group" aria-label="表示する画像"></div>
  </div>'''
s = s[:i] + new_block + s[j:]

js = '''<script>
/* トップのスライドショー（約5秒ごと。丸のボタンは画像の枚数に合わせて作る。端末が「動きを減らす」設定のときは、ふわっと切り替えずにそのまま入れ替える） */
(function(){
  var box=document.getElementById("mediaSlot"); if(!box) return;
  var sl=box.querySelectorAll(".mt-slide"), nav=box.querySelector(".mt-dots"), dt=[], i=0, tm=null;
  if(sl.length<2){ if(nav) nav.style.display="none"; return; }
  for(var k=0;k<sl.length;k++){
    var b=document.createElement("button"); b.type="button"; b.setAttribute("aria-label",(k+1)+"枚目");
    nav.appendChild(b); dt.push(b);
  }
  function show(n){
    i=(n+sl.length)%sl.length;
    for(var k=0;k<sl.length;k++){ sl[k].className=(k===i)?"mt-slide on":"mt-slide"; dt[k].className=(k===i)?"on":""; }
  }
  function stop(){ if(tm){ clearInterval(tm); tm=null; } }
  function start(){ stop(); tm=setInterval(function(){ show(i+1); },5000); }
  for(var k=0;k<dt.length;k++){ (function(n){ dt[n].addEventListener("click",function(){ show(n); start(); }); })(k); }
  show(0); start();
})();
</script>
</body>'''
rep('</body>', js, 1)
open(out, 'w', encoding='utf-8').write(s)
print('OK', out)
