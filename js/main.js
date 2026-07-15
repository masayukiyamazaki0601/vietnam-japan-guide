/* ============================================
   Vietnam Japan Guide - Main JavaScript
   デザインリニューアル対応版
   ============================================ */

'use strict';

// ---------- DOM Ready ----------
document.addEventListener('DOMContentLoaded', function() {
  initMobileMenu();
  initSearch();
  initBackToTop();
  initSmoothScroll();
  initActiveNav();
  initHeaderScroll();
  initIntersectionObserver();
});

// ---------- Mobile Menu ----------
function initMobileMenu() {
  const menuToggle = document.querySelector('.header__menu-toggle');
  const nav = document.querySelector('.header__nav');

  if (!menuToggle || !nav) return;

  menuToggle.addEventListener('click', function() {
    this.classList.toggle('active');
    nav.classList.toggle('open');
    this.setAttribute('aria-expanded', nav.classList.contains('open'));
  });

  // Close menu when clicking outside
  document.addEventListener('click', function(e) {
    if (!e.target.closest('.header__inner')) {
      menuToggle.classList.remove('active');
      nav.classList.remove('open');
      menuToggle.setAttribute('aria-expanded', 'false');
    }
  });

  // Close menu when clicking a link
  nav.querySelectorAll('.header__nav-link').forEach(function(link) {
    link.addEventListener('click', function() {
      menuToggle.classList.remove('active');
      nav.classList.remove('open');
      menuToggle.setAttribute('aria-expanded', 'false');
    });
  });
}

// ---------- Search Functionality ----------
function initSearch() {
  var searchInput = document.querySelector('.hero__search-input');
  var searchBtn = document.querySelector('.header__search-btn');

  function doSearch(query) {
    query = query.trim();
    if (query.length > 0) {
      var searchUrl = 'https://www.google.com/search?q=site:vietnam-japan-guide.com ' + encodeURIComponent(query);
      window.open(searchUrl, '_blank');
    }
  }

  if (searchInput) {
    searchInput.addEventListener('keydown', function(e) {
      if (e.key === 'Enter') {
        e.preventDefault();
        doSearch(this.value);
      }
    });
  }

  if (searchBtn) {
    searchBtn.addEventListener('click', function() {
      var input = document.querySelector('.hero__search-input');
      if (input) input.focus();
    });
  }
}

// ---------- Back to Top ----------
function initBackToTop() {
  var button = document.querySelector('.back-to-top');
  if (!button) return;

  window.addEventListener('scroll', function() {
    if (window.pageYOffset > 300) {
      button.classList.add('visible');
    } else {
      button.classList.remove('visible');
    }
  });

  button.addEventListener('click', function() {
    window.scrollTo({
      top: 0,
      behavior: 'smooth'
    });
  });
}

// ---------- Smooth Scroll ----------
function initSmoothScroll() {
  document.querySelectorAll('a[href^="#"]').forEach(function(anchor) {
    anchor.addEventListener('click', function(e) {
      var targetId = this.getAttribute('href');
      if (targetId === '#') return;

      var targetElement = document.querySelector(targetId);
      if (targetElement) {
        e.preventDefault();
        var headerOffset = 80;
        var elementPosition = targetElement.getBoundingClientRect().top;
        var offsetPosition = elementPosition + window.pageYOffset - headerOffset;

        window.scrollTo({
          top: offsetPosition,
          behavior: 'smooth'
        });
      }
    });
  });
}

// ---------- Active Navigation ----------
function initActiveNav() {
  var currentPath = window.location.pathname;

  document.querySelectorAll('.header__nav-link').forEach(function(link) {
    var href = link.getAttribute('href');
    if (currentPath === href ||
        (href !== '/' && currentPath.startsWith(href))) {
      link.classList.add('header__nav-link--active');
    }
  });
}

// ---------- Header Scroll Effect ----------
function initHeaderScroll() {
  var header = document.querySelector('.header');
  if (!header) return;

  var scrollThreshold = 100;

  window.addEventListener('scroll', function() {
    if (window.pageYOffset > scrollThreshold) {
      header.style.boxShadow = '0 2px 20px rgba(0,0,0,0.08)';
    } else {
      header.style.boxShadow = 'none';
    }
  });
}

// ---------- Intersection Observer for Animations ----------
function initIntersectionObserver() {
  if (!('IntersectionObserver' in window)) return;

  var observer = new IntersectionObserver(function(entries) {
    entries.forEach(function(entry) {
      if (entry.isIntersecting) {
        entry.target.classList.add('animate-fade-in');
        observer.unobserve(entry.target);
      }
    });
  }, { threshold: 0.1 });

  // Observe category cards and article cards
  document.querySelectorAll('.category-card, .article-card').forEach(function(el) {
    el.style.opacity = '0';
    observer.observe(el);
  });
}

// ---------- Share Buttons ----------
function shareOnTwitter(url, text) {
  var shareUrl = 'https://twitter.com/intent/tweet?text=' + encodeURIComponent(text) +
                 '&url=' + encodeURIComponent(url);
  window.open(shareUrl, '_blank', 'width=600,height=400');
}

function shareOnFacebook(url) {
  var shareUrl = 'https://www.facebook.com/sharer/sharer.php?u=' + encodeURIComponent(url);
  window.open(shareUrl, '_blank', 'width=600,height=400');
}

function shareOnLine(url, text) {
  var shareUrl = 'https://social-plugins.line.me/lineit/share?url=' + encodeURIComponent(url) +
                 '&text=' + encodeURIComponent(text);
  window.open(shareUrl, '_blank', 'width=600,height=400');
}

// ---------- Copy to Clipboard ----------
function copyToClipboard(text) {
  if (navigator.clipboard) {
    navigator.clipboard.writeText(text).then(function() {
      showToast('Đã sao chép vào clipboard');
    });
  } else {
    var textarea = document.createElement('textarea');
    textarea.value = text;
    document.body.appendChild(textarea);
    textarea.select();
    document.execCommand('copy');
    document.body.removeChild(textarea);
    showToast('Đã sao chép vào clipboard');
  }
}

// ---------- Simple Toast ----------
function showToast(message) {
  var existingToast = document.querySelector('.toast');
  if (existingToast) existingToast.remove();

  var toast = document.createElement('div');
  toast.className = 'toast';
  toast.textContent = message;
  toast.style.cssText = [
    'position: fixed',
    'bottom: 80px',
    'left: 50%',
    'transform: translateX(-50%)',
    'background: #1A365D',
    'color: #fff',
    'padding: 12px 24px',
    'border-radius: 8px',
    'font-size: 14px',
    'z-index: 9999',
    'opacity: 0',
    'transition: opacity 0.3s ease',
    'box-shadow: 0 4px 12px rgba(0,0,0,0.15)'
  ].join(';');

  document.body.appendChild(toast);
  toast.offsetHeight; // trigger reflow
  toast.style.opacity = '1';

  setTimeout(function() {
    toast.style.opacity = '0';
    setTimeout(function() { toast.remove(); }, 300);
  }, 2000);
}

// ---------- Table of Contents Generator ----------
function generateTOC() {
  var content = document.querySelector('.article-content');
  if (!content) return;

  var headings = content.querySelectorAll('h2[id], h3[id]');
  if (headings.length < 2) return;

  var tocContainer = document.querySelector('.toc__list');
  if (!tocContainer) return;

  headings.forEach(function(heading) {
    var li = document.createElement('li');
    li.className = 'toc__item';

    var a = document.createElement('a');
    a.className = 'toc__link';
    a.href = '#' + heading.id;
    a.textContent = heading.textContent.trim();

    li.appendChild(a);
    tocContainer.appendChild(li);
  });
}

// Initialize TOC on page load
if (document.querySelector('.article-content')) {
  document.addEventListener('DOMContentLoaded', generateTOC);
}