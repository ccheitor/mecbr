# Animation Reference

> Cinematic motion design extracted from live DOM. Follow these specs exactly to recreate the experience.

## Motion Technology Stack

Pure CSS animations — no external animation libraries detected.

## Scroll Journey

The page is **5.344px** tall. Each frame below shows what the user sees at that scroll depth.

> **Use these screenshots to understand WHAT animates, WHEN it animates, and HOW it moves.**

### 0% — Top / Hero
Scroll position: 0px

![Scroll 0%](../screens/scroll/scroll-000.png)

### 17% — Opening Section
Scroll position: 755px

![Scroll 17%](../screens/scroll/scroll-017.png)

### 33% — First Feature Section
Scroll position: 1.467px

![Scroll 33%](../screens/scroll/scroll-033.png)

### 50% — Mid-Page
Scroll position: 2.222px

![Scroll 50%](../screens/scroll/scroll-050.png)

### 67% — Lower Content
Scroll position: 2.977px

![Scroll 67%](../screens/scroll/scroll-067.png)

### 83% — Near Footer
Scroll position: 3.689px

![Scroll 83%](../screens/scroll/scroll-083.png)

### 100% — Bottom / Footer
Scroll position: 4.444px

![Scroll 100%](../screens/scroll/scroll-100.png)

## Video Elements

| # | Role | Autoplay | Loop | Muted | Size | First Frame |
|---|------|----------|------|-------|------|-------------|
| 1 | background | ✓ | ✓ | ✓ | 1888×776 | [view](../screens/scroll/video-1-frame.png) |

**Video 1 first frame:**

![Video 1 Frame](../screens/scroll/video-1-frame.png)

- **Source:** `https://cdn.hillsong.com/wp-content/uploads/2020/03/26054238/VS20-DotCom-Header.webmhd.webm`
- **Poster:** `https://cdn.hillsong.com/wp-content/uploads/2020/03/26054614/VS20-DotCom-Header.gif`

## CSS Keyframes (5 extracted)

### `@keyframes fa-spin`

Duration: `2s` · Easing: `linear` · Delay: `0s` · Iteration: `infinite` · Fill: `none`

Used by: `.fa-spin`, `.fa-pulse`

```css
@keyframes fa-spin {
  0% {
    transform: rotate(0deg);
  }
  100% {
    transform: rotate(1turn);
  }
}
```

> Transform/motion animation

### `@keyframes fa-spin`

Duration: `2s` · Easing: `linear` · Delay: `0s` · Iteration: `infinite` · Fill: `none`

Used by: `.fa-spin`, `.fa-pulse`

```css
@keyframes fa-spin {
  0% {
    transform: rotate(0deg);
  }
  100% {
    transform: rotate(1turn);
  }
}
```

> Transform/motion animation

### `@keyframes fa-spin`

Duration: `2s` · Easing: `linear` · Delay: `0s` · Iteration: `infinite` · Fill: `none`

Used by: `.fa-spin`, `.fa-pulse`

```css
@keyframes fa-spin {
  0% {
    transform: rotate(0deg);
  }
  100% {
    transform: rotate(1turn);
  }
}
```

> Transform/motion animation

### `@keyframes fa-spin`

Duration: `2s` · Easing: `linear` · Delay: `0s` · Iteration: `infinite` · Fill: `none`

Used by: `.fa-spin`, `.fa-pulse`

```css
@keyframes fa-spin {
  0% {
    transform: rotate(0deg);
  }
  100% {
    transform: rotate(1turn);
  }
}
```

> Transform/motion animation

### `@keyframes onetrust-fade-in`

Duration: `400ms` · Easing: `ease-in-out`

Used by: `#onetrust-pc-sdk.ot-fade-in, .onetrust-pc-dark-filter.ot-fade-in, #onetrust-bann`

```css
@keyframes onetrust-fade-in {
  0% {
    opacity: 0;
  }
  100% {
    opacity: 1;
  }
}
```

> Opacity fade

## Global Transition Declarations

These `transition` values were extracted from CSS rules across the site:

```css
transition: 0.3s;
transition: opacity 0.2s;
transition: background 0.2s, width 0.2s;
transition: color 0.2s, opacity 0.2s, background 0.2s;
transition: 0.5s;
transition: 0.1s;
transition: 300ms ease-in;
transition: 0.2s ease-in;
transition: 0.4s;
transition: 150ms ease-in;
transition: 0.2s;
transition: 0.25s ease-out;
```

## How to Recreate This Motion Design

### Step 2 — Scroll-Reveal Pattern

Elements that animate into view follow this pattern:

```css
/* Initial hidden state */
.reveal {
  opacity: 0;
  transform: translateY(40px);
  transition: opacity 0.3s cubic-bezier(0.4, 0, 0.2, 1),
              transform 0.3s cubic-bezier(0.4, 0, 0.2, 1);
}
.reveal.visible {
  opacity: 1;
  transform: translateY(0);
}
```

### Step 3 — Key Motion Principles

- **Video backgrounds** — use `<video autoplay loop muted playsinline>` for background videos. Always include a poster image fallback
- **Duration scale:** `0.3s` · `0.2s` — use these values, never invent new durations
- **Always add** `@media (prefers-reduced-motion: reduce) { * { animation-duration: 0.01ms !important; transition-duration: 0.01ms !important; } }`

### Step 4 — Scroll Journey Reference

Match what happens at each scroll position:

- **0%** (`0px`) → `screens/scroll/scroll-000.png`
- **17%** (`755px`) → `screens/scroll/scroll-017.png`
- **33%** (`1467px`) → `screens/scroll/scroll-033.png`
- **50%** (`2222px`) → `screens/scroll/scroll-050.png`
- **67%** (`2977px`) → `screens/scroll/scroll-067.png`
- **83%** (`3689px`) → `screens/scroll/scroll-083.png`
- **100%** (`4444px`) → `screens/scroll/scroll-100.png`

