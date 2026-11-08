(function () {
  var userTs = 0;
  function mark() { userTs = Date.now(); }
  ['pointerdown', 'touchstart', 'keydown'].forEach(function (ev) {
    document.addEventListener(ev, function (e) {
      if (e.target && e.target.closest && e.target.closest('[class*="gBj_UBEJnf"]')) mark();
    }, true);
  });
  document.addEventListener('focusin', function (e) {
    var t = e.target;
    if (!t || !t.closest || !t.closest('[class*="gBj_UBEJnf"]')) return;
    if (Date.now() - userTs < 1000) return;
    var y = window.scrollY;
    window.scrollTo({ top: y, behavior: 'instant' });
    requestAnimationFrame(function () { window.scrollTo({ top: y, behavior: 'instant' }); });
    try { t.blur(); } catch (err) {}
  }, true);
})();
