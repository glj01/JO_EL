/* ============================================================
   Jackson Osborne — js/main.js
   Shared JavaScript for all pages
   ============================================================ */

// ── Sticky header shadow on scroll ──
const header = document.getElementById('header');
if (header) {
  window.addEventListener('scroll', () => {
    header.classList.toggle('scrolled', window.scrollY > 20);
  });
}

// ── Mobile menu open/close ──
const mobOverlay = document.getElementById('mob');
const mobOpenBtn = document.getElementById('mob-open');
const mobCloseBtn = document.getElementById('mob-close');

if (mobOpenBtn && mobOverlay) {
  mobOpenBtn.addEventListener('click', () => mobOverlay.classList.add('open'));
}
if (mobCloseBtn && mobOverlay) {
  mobCloseBtn.addEventListener('click', () => mobOverlay.classList.remove('open'));
}

// ── FAQ accordion ──
document.querySelectorAll('.faq-q').forEach(btn => {
  btn.addEventListener('click', () => {
    const item = btn.closest('.faq-item');
    const wasOpen = item.classList.contains('open');
    // Close all
    document.querySelectorAll('.faq-item.open').forEach(i => i.classList.remove('open'));
    // Open clicked one if it was closed
    if (!wasOpen) item.classList.add('open');
  });
});

// ── Mark active nav link based on current page ──
const currentPage = window.location.pathname.split('/').pop() || 'index.html';
document.querySelectorAll('nav .nl').forEach(link => {
  if (link.getAttribute('href') === currentPage) {
    link.classList.add('active');
  }
});
