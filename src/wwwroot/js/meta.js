window.vvg = window.vvg || {};
window.vvg.updateMeta = function (meta) {
  try {
    if (meta.title) document.title = meta.title;
    const set = (name, value, attr = 'name') => {
      if (!value) return;
      let el = document.querySelector('meta[' + attr + "='" + name + "']");
      if (!el) {
        el = document.createElement('meta');
        el.setAttribute(attr, name);
        document.head.appendChild(el);
      }
      el.setAttribute('content', value);
    };
    set('description', meta.description);
    set('keywords', meta.keywords);
    set('og:title', meta.title, 'property');
    set('og:description', meta.description, 'property');
    set('og:image', meta.image, 'property');
    set('twitter:card', meta.twitterCard || 'summary_large_image', 'name');
    if (meta.jsonLd) {
      let ld = document.getElementById('vvg-jsonld');
      if (!ld) {
        ld = document.createElement('script');
        ld.type = 'application/ld+json';
        ld.id = 'vvg-jsonld';
        document.head.appendChild(ld);
      }
      ld.textContent = meta.jsonLd;
    }
  } catch (e) { console.warn(e); }
};
