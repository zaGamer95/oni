// 모바일 메뉴 토글
(function () {
  var btn = document.querySelector('.nav-toggle');
  if (btn) {
    btn.addEventListener('click', function () {
      var open = document.body.classList.toggle('nav-open');
      btn.setAttribute('aria-expanded', open ? 'true' : 'false');
    });
    document.querySelectorAll('.sidebar a').forEach(function (a) {
      a.addEventListener('click', function () { document.body.classList.remove('nav-open'); });
    });
  }
})();

// 넓은 표는 가로 스크롤 상자로 감싸기
document.querySelectorAll('.prose table').forEach(function (t) {
  var w = document.createElement('div');
  w.className = 'table-wrap';
  t.parentNode.insertBefore(w, t);
  w.appendChild(t);
});

// 장기 평형 계산기 (guide/06 페이지에 #colony-calc 가 있을 때만 동작)
(function () {
  var root = document.getElementById('colony-calc');
  if (!root) return;

  // 게임 수치 (1 사이클 = 600초). 패치로 바뀌면 여기만 고치면 됩니다.
  var K = {
    o2PerDup: 100,           // g/s 산소 소비
    kcalPerDup: 1000,        // kcal/사이클
    electrolyzerO2: 888,     // g/s
    electrolyzerWater: 1000, // g/s
    diffuserO2: 500,         // g/s (조류 550 g/s 소모)
    diffuserAlgae: 550,
    mealwoodKcal: 600 / 3,   // 끼니나무: 3사이클마다 600kcal
    mealwoodDirt: 10,        // kg/사이클
    bristleKcal: 1600 / 6,   // 센털꽃: 6사이클마다 1600kcal
    bristleWater: 20,        // kg/사이클
    cookBonusBristle: 2000 / 1600, // 구운 털열매(Gristle Berry)
    toiletGainWater: 6.7,    // kg/복제체/사이클 (수세식 화장실 순증 오염수)
  };

  var $ = function (id) { return document.getElementById(id); };
  function fmt(n, d) { return Number(n).toLocaleString('ko-KR', { maximumFractionDigits: d == null ? 1 : d }); }

  function run() {
    var dups = Math.max(1, parseInt($('cc-dups').value, 10) || 1);
    var o2src = $('cc-o2').value;
    var food = $('cc-food').value;
    var buffer = Math.max(0, parseFloat($('cc-buffer').value) || 0) / 100;

    var o2need = dups * K.o2PerDup * (1 + buffer);
    var kcal = dups * K.kcalPerDup * (1 + buffer);

    var o2text, o2sub;
    if (o2src === 'electrolyzer') {
      var n = Math.ceil(o2need / K.electrolyzerO2);
      var water = n * K.electrolyzerWater * 600 / 1000;
      o2text = '전기분해기 ' + n + '대';
      o2sub = '물 ' + fmt(water, 0) + ' kg/사이클 · 전력 ' + fmt(n * 120, 0) + ' W (+펌프)';
    } else {
      var d = Math.ceil(o2need / K.diffuserO2);
      var algae = d * K.diffuserAlgae * 600 / 1000;
      o2text = '산소 확산기 ' + d + '대';
      o2sub = '조류 ' + fmt(algae, 0) + ' kg/사이클 소모 · 전력 ' + fmt(d * 120, 0) + ' W';
    }

    var plants, plantSub;
    if (food === 'mealwood') {
      plants = Math.ceil(kcal / K.mealwoodKcal);
      plantSub = '흙 ' + fmt(plants * K.mealwoodDirt, 0) + ' kg/사이클';
      $('cc-plant-label').textContent = '끼니나무 화분';
    } else {
      var per = K.bristleKcal * ($('cc-cook').checked ? K.cookBonusBristle : 1);
      plants = Math.ceil(kcal / per);
      plantSub = '물 ' + fmt(plants * K.bristleWater, 0) + ' kg/사이클 · 빛 필요';
      $('cc-plant-label').textContent = '센털꽃 화분';
    }

    $('cc-out-o2').textContent = fmt(o2need, 0) + ' g/s';
    $('cc-out-o2src').textContent = o2text;
    $('cc-out-o2sub').textContent = o2sub;
    $('cc-out-kcal').textContent = fmt(kcal, 0) + ' kcal';
    $('cc-out-plants').textContent = plants + '개';
    $('cc-out-plantsub').textContent = plantSub;
    $('cc-out-toilet').textContent = '+' + fmt(dups * K.toiletGainWater, 1) + ' kg';
  }

  root.addEventListener('input', run);
  root.addEventListener('change', run);
  run();
})();

// 외부 이미지가 안 불러와지면 자리만 남기지 않고 대체 표시
document.querySelectorAll('img[data-fallback]').forEach(function (img) {
  function fail() { img.classList.add('img-missing'); img.removeAttribute('src'); }
  if (img.complete && img.naturalWidth === 0 && img.getAttribute('src')) fail();
  img.addEventListener('error', fail);
});

// 게임 시작 설정 마법사 (/start/)
(function () {
  var wz = document.getElementById('wizard');
  if (!wz) return;
  wz.classList.add('js');
  var steps = wz.querySelectorAll('.wz-step');
  var prog = wz.querySelectorAll('.wz-progress li');
  var total = steps.length; // 마지막은 결과
  var cur = 1;
  var picks = {};
  var notes = {
    so: 'Spaced Out!은 시작 행성이 작아서 자원이 빨리 떨어집니다. 로켓 연구를 일반보다 일찍 시작하세요.',
    qol: '모드를 켰다면 게임 업데이트 직후에는 Mod Updater로 먼저 갱신하세요.',
    on: 'DLC 콘텐츠를 켰다면 처음 보는 생물·건물은 게임 안 백과사전(코덱스)에서 확인하세요.',
    hard: '고난도 행성은 행성 고르기 페이지의 행성별 첫 행동을 꼭 먼저 읽으세요.',
    'dlc-planet': 'DLC 전용 행성 공략은 아직 정리 중입니다.'
  };

  function show(n) {
    cur = Math.max(1, Math.min(total, n));
    steps.forEach(function (s) { s.classList.toggle('on', +s.dataset.step === cur); });
    prog.forEach(function (p) {
      var k = +p.dataset.goto;
      p.classList.toggle('on', k === cur);
      p.classList.toggle('done', !!(k < cur || (k < total && picks[k])));
    });
    wz.querySelector('[data-prev]').disabled = cur === 1;
    wz.querySelector('.wz-nav').style.display = cur === total ? 'none' : '';
    if (cur === total) summary();
  }
  function pick(stepEl, btn) {
    stepEl.querySelectorAll('.wz-opt').forEach(function (b) { b.classList.toggle('sel', b === btn); b.setAttribute('aria-pressed', b === btn); });
    picks[+stepEl.dataset.step] = { value: btn.dataset.value, label: btn.dataset.label };
  }
  function pickRec(stepEl) {
    var r = stepEl.querySelector('.wz-opt[data-rec]');
    if (r) pick(stepEl, r);
  }
  function summary() {
    var msgs = [];
    for (var i = 1; i < total; i++) {
      var stepEl = wz.querySelector('.wz-step[data-step="' + i + '"]');
      if (!picks[i]) pickRec(stepEl);
      var el = wz.querySelector('[data-sum="' + i + '"]');
      var isRec = stepEl.querySelector('.wz-opt[data-rec]').dataset.value === picks[i].value;
      el.innerHTML = '';
      el.textContent = picks[i].label + (isRec ? ' ★' : '');
      if (notes[picks[i].value]) msgs.push(notes[picks[i].value]);
    }
    document.getElementById('wz-note').textContent = msgs.length ? msgs.join(' ') : '★ 추천 조합이에요. 이대로 새 게임을 만들고 다음 단계로 가세요.';
  }

  wz.addEventListener('click', function (e) {
    var opt = e.target.closest('.wz-opt');
    if (opt) { pick(opt.closest('.wz-step'), opt); show(cur + 1); return; }
    if (e.target.closest('[data-next]')) { show(cur + 1); return; }
    if (e.target.closest('[data-prev]')) { show(cur - 1); return; }
    if (e.target.closest('[data-rec-step]')) { pickRec(steps[cur - 1]); show(cur + 1); return; }
    if (e.target.closest('[data-allrec]')) { steps.forEach(function (s) { if (+s.dataset.step < total) pickRec(s); }); show(total); return; }
    var g = e.target.closest('.wz-progress li');
    if (g) show(+g.dataset.goto);
  });

  if (location.hash === '#recommended' || location.hash === '#result') {
    steps.forEach(function (s) { if (+s.dataset.step < total) pickRec(s); });
    show(total);
  } else show(1);
})();
