(function () {
  var MAP = {
    "Dark Gray": "https://cdn.shopify.com/s/files/1/0751/0861/4188/files/hf_20261107_092155_8540878b-9ae3-476a-b6ef-66dbf32672aa.png",
    "Navy Blue": "https://cdn.shopify.com/s/files/1/0751/0861/4188/files/hf_20261107_092158_7111e49b-78ef-4a85-a961-1ba9190adde0.png",
    "White Mesh Fabric": "https://cdn.shopify.com/s/files/1/0751/0861/4188/files/hf_20261107_092155_87a3bf4b-1454-45b0-98d7-5aac1301b0c5.png",
    "Gray And White": "https://cdn.shopify.com/s/files/1/0751/0861/4188/files/hf_20261107_092155_911001c7-f517-4ba6-9e3f-25fc26c00ce6.png",
    "Green And White": "https://cdn.shopify.com/s/files/1/0751/0861/4188/files/hf_20261107_092155_f1cb3516-a56f-4364-bdf3-094fd4be2be8.png",
    "Ice Silk Blue And White": "https://cdn.shopify.com/s/files/1/0751/0861/4188/files/hf_20261107_092155_fbc67bcc-e81f-4f26-b45f-236c584b7f2a.png",
    "Light Gray": "https://cdn.shopify.com/s/files/1/0751/0861/4188/files/hf_20261107_092155_403142d0-8cb8-4fe7-b0c8-6aa0eee6ad40.png",
    "Mesh Black And White": "https://cdn.shopify.com/s/files/1/0751/0861/4188/files/hf_20261107_092155_7fc5137c-4c10-4ae4-9abf-6b054567d3d1.png",
    "Mesh Gray And White": "https://cdn.shopify.com/s/files/1/0751/0861/4188/files/hf_20261107_092157_0e73d988-2d89-44b2-a97a-101a98d14c96.png",
    "Sky Blue": "https://cdn.shopify.com/s/files/1/0751/0861/4188/files/hf_20261107_092155_c0ca739f-6b30-46fa-b0f9-fd1e690cb7c1.png"
  };
  var tries = 0;
  function init() {
    var root = document.querySelector('[class*="g39D66BbB4"]');
    var mainEl = root && Array.prototype.find.call(root.querySelectorAll('.swiper-initialized'), function (e) {
      return e.classList.contains('swiper-horizontal') && !e.classList.contains('swiper-thumbs') && e.swiper;
    });
    if (!mainEl) { if (tries++ < 60) setTimeout(init, 250); return; }
    if (mainEl.__rmPop) return;
    mainEl.__rmPop = true;
    var sw = mainEl.swiper;
    var thumbEl = root.querySelector('.swiper-thumbs');
    var host = mainEl.parentElement;
    if (getComputedStyle(host).position === 'static') host.style.position = 'relative';
    var ov = document.createElement('div');
    ov.className = 'rm-color-pop';
    ov.innerHTML = '<img alt="">';
    host.appendChild(ov);
    var img = ov.querySelector('img');
    function preload() { Object.keys(MAP).forEach(function (k) { var i = new Image(); i.src = MAP[k] + '?width=900'; }); }
    if (document.readyState === 'complete') setTimeout(preload, 3000); else window.addEventListener('load', function () { setTimeout(preload, 3000); });
    var lastIdx = sw.realIndex || 0;
    var holding = false;
    function hide() { ov.classList.remove('on'); }
    function restore() {
      holding = true;
      try { sw.slideToLoop ? sw.slideToLoop(lastIdx, 0) : sw.slideTo(lastIdx, 0); } catch (e) {}
      try { if (thumbEl && thumbEl.swiper) thumbEl.swiper.slideTo(lastIdx, 0); } catch (e) {}
      setTimeout(function () { holding = false; }, 60);
    }
    sw.on('slideChange', function () {
      if (holding) return;
      lastIdx = sw.realIndex;
      hide();
    });
    sw.on('touchStart', hide);
    root.addEventListener('click', function (e) {
      if (e.target.closest('.swiper-thumbs') || e.target.closest('[class*="arrow"],[class*="nav"],button')) hide();
    }, true);
    document.addEventListener('change', function (e) {
      var v = e.target && e.target.value;
      if (!v || !MAP[v]) return;
      var keep = lastIdx;
      img.src = MAP[v] + '?width=900';
      ov.classList.add('on');
      [0, 120, 400, 900].forEach(function (t) {
        setTimeout(function () { lastIdx = keep; restore(); ov.classList.add('on'); }, t);
      });
    }, true);
  }
  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', init); else init();
})();
