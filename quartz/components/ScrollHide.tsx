import { QuartzComponent, QuartzComponentConstructor } from "./types"
// @ts-ignore
import script from "./scripts/scroll-hide.inline"
import style from "./styles/scroll-hide.scss"

/**
 * Invisible helper component: bundles the scroll listener that hides the
 * top bar (logo, search, buttons) while scrolling down for reading, and
 * shows it again when scrolling up. Renders nothing itself.
 */
export default (() => {
  const ScrollHide: QuartzComponent = () => {
    return <></>
  }

  ScrollHide.css = style
  ScrollHide.afterDOMLoaded = script
  return ScrollHide
}) satisfies QuartzComponentConstructor
