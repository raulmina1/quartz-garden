// Hide the top bar (logo, search, buttons) when scrolling down for reading,
// reveal it again when scrolling up. Toggles `topbar-hidden` on <html>;
// the CSS in styles/scroll-hide.scss does the actual hiding.

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

window.addEventListener("scroll", onScroll, { passive: true })
window.addCleanup(() => window.removeEventListener("scroll", onScroll))
