// Hide the top bar (logo, search, buttons) when scrolling down for reading,
// reveal it again when scrolling up. Toggles `topbar-hidden` on <html>;
// the CSS in styles/scroll-hide.scss does the actual hiding.

// NOTE: this script is bundled at the very start of postscript.js, BEFORE the
// SPA router defines window.addCleanup. Calling addCleanup here throws and
// aborts the whole module (killing the graph/explorer/search), so we manage
// the listener ourselves with a guard flag.
const SCROLL_THRESHOLD = 80
let lastY = window.scrollY

function onScroll() {
  const y = window.scrollY
  if (y > SCROLL_THRESHOLD && y > lastY + 2) {
    document.documentElement.classList.add("topbar-hidden")
  } else if (y < lastY - 2) {
    document.documentElement.classList.remove("topbar-hidden")
  }
  lastY = y
}

// The postscript bundle re-executes on every SPA navigation, so only bind
// the listener once per page load.
const boundFlag = "__scrollHideBound"
if (!(window as unknown as Record<string, unknown>)[boundFlag]) {
  ;(window as unknown as Record<string, unknown>)[boundFlag] = true
  window.addEventListener("scroll", onScroll, { passive: true })
}
