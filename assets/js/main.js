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
    mealwoodKcal: 600 / 3,   // 식사나무: 3사이클마다 600kcal
    mealwoodDirt: 10,        // kg/사이클
    bristleKcal: 1600 / 6,   // 털열매 꽃: 6사이클마다 1600kcal
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
      $('cc-plant-label').textContent = '식사나무 화분';
    } else {
      var per = K.bristleKcal * ($('cc-cook').checked ? K.cookBonusBristle : 1);
      plants = Math.ceil(kcal / per);
      plantSub = '물 ' + fmt(plants * K.bristleWater, 0) + ' kg/사이클 · 빛 필요';
      $('cc-plant-label').textContent = '털열매 꽃 화분';
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
