(function () {
    // Keep a reference to the .NET object
    let scrollDotNetRef = null;
    let scrollHandler = null;

    function getScrollY() {
        return window.scrollY || window.pageYOffset || 0;
    }

    function addScrollListener(dotNetHelper) {
        try {
            if (dotNetHelper) {
                scrollDotNetRef = dotNetHelper;
            }

            if (scrollHandler) return;

            scrollHandler = function () {
                // Throttle to avoid flooding .NET
                if (!scrollDotNetRef) return;
                // Call the instance method 'OnScroll' on the supplied DotNetObjectReference
                scrollDotNetRef.invokeMethodAsync('OnScroll').catch(() => { /* swallow */ });
            };

            window.addEventListener('scroll', scrollHandler, { passive: true });
        }
        catch (e) {
            console.warn('addScrollListener error', e);
        }
    }

    function removeScrollListener() {
        try {
            if (scrollHandler) {
                window.removeEventListener('scroll', scrollHandler);
                scrollHandler = null;
            }

            if (scrollDotNetRef) {
                try { scrollDotNetRef.dispose(); } catch (e) { /* ignore */ }
                scrollDotNetRef = null;
            }
        }
        catch (e) {
            console.warn('removeScrollListener error', e);
        }
    }

    function scrollToTop() {
        try {
            window.scrollTo({ top: 0, behavior: 'smooth' });
        }
        catch (e) {
            console.warn('scrollToTop error', e);
        }
    }

    function setTheme(theme) {
        try {
            if (!theme) return;
            document.documentElement.setAttribute('data-theme', theme);
            try { localStorage.setItem('vvg-theme', theme); } catch { }
        } catch (e) { console.warn('setTheme error', e); }
    }

    function getTheme() {
        try {
            return localStorage.getItem('vvg-theme') || null;
        } catch (e) { return null; }
    }

    // Expose to global scope
    window.addScrollListener = addScrollListener;
    window.removeScrollListener = removeScrollListener;
    window.scrollToTop = scrollToTop;
    window.getScrollY = getScrollY;
    window.setTheme = setTheme;
    window.getTheme = getTheme;
})();