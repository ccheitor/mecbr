# hillsong DESIGN.md

> Auto-generated design system — reverse-engineered via static analysis by skillui.
> Frameworks: None detected
> Colors: 20 · Fonts: 3 · Components: 10
> Icon library: not detected · State: not detected
> Primary theme: dark · Dark mode toggle: no · Motion: expressive

## Visual Reference

**Match this design exactly** — study colors, fonts, spacing, and component shapes before writing any UI code.

![hillsong Homepage](../screenshots/homepage.png)

---

## 1. Visual Theme & Atmosphere

This is a **dark-themed** interface with a neutral tone. Depth is expressed through layered shadows and subtle surface color variation. Typography pairs **hillsongv2** for display/headings with **hillsong-icons** for body text, creating clear visual hierarchy through type contrast. Spacing follows a **4px base grid** (compact density), with scale: 2, 4, 6, 8, 10, 12, 14, 16px. Motion is expressive — spring physics, layout animations, and staggered reveals are part of the visual language.

---

## 2. Color Palette & Roles

| Token | Hex | Role | Use |
|---|---|---|---|
| wp--preset--color--black | `#000000` | background | Page background, darkest surface |
| color-gray-900 | `#0d112f` | surface | Card and panel backgrounds |
| wp--preset--color--white | `#ffffff` | text-primary | Headings and body text |
| text-muted | `#464646` | text-muted | Captions, placeholders, secondary info |
| border | `#585858` | border | Dividers, card borders, outlines |
| success | `#1bc48d` | success | Success states, positive indicators |
| warning | `#aa9055` | warning | Warning states, caution indicators |
| info | `#289fd8` | info | Informational highlights |
| color-gray-700 | `#393b59` | unknown | Palette color |
| unknown | `#898989` | unknown | Palette color |
| unknown | `#666666` | unknown | Palette color |
| color-red-50 | `#f2f2f2` | unknown | Palette color |
| unknown | `#c3aa92` | unknown | Palette color |
| wp-editor-canvas-background | `#d7d7d7` | unknown | Palette color |
| unknown | `#111111` | unknown | Palette color |
| unknown | `#3c3c3c` | unknown | Palette color |
| unknown | `#3860be` | unknown | Palette color |
| unknown | `#cccccc` | unknown | Palette color |
| unknown | `#333333` | unknown | Palette color |
| color-neutral-800 | `#1f1f1f` | unknown | Palette color |

### CSS Variable Tokens

```css
--wp-editor-canvas-background: #ddd;
--wp-admin-border-width-focus: 2px;
--wp-admin-border-width-focus: 1.5px;
--wp-editor-canvas-background: #ddd;
--wp-admin-border-width-focus: 2px;
--wp-admin-border-width-focus: 1.5px;
--wp-editor-canvas-background: #ddd;
--wp-admin-border-width-focus: 2px;
--wp-admin-border-width-focus: 1.5px;
--tw-border-style: solid;
--tw-border-style: dashed;
--tw-border-style: none;
--tw-border-style: solid;
--background: #000;
--foreground: #fff;
--accent: var(--foreground);
--carousel-card-width: 8.5rem;
--carousel-resource-card-width: calc(var(--carousel-card-width)*.8);
--carousel-card-width: 10.625rem;
--background: #ffffff;
```


---

## 3. Typography Rules

**Font Stack:**
- **hillsong-icons** — Heading 1, Heading 2, Heading 3
- **hillsongv2** — Body, Caption
- **SFMono-Regular** — Code

**Font Sources:**

```css
@font-face {
  font-family: "hillsongv2";
  src: url("fonts/hillsongv2-Regular.ttf") format("truetype");
  font-weight: 400;
}
@font-face {
  font-family: "hillsong-icons";
  src: url("fonts/hillsong-icons-Regular.woff") format("woff");
  font-weight: 400;
}
@font-face {
  font-family: "proxima-nova";
  src: url("fonts/proxima-nova-700.ttf") format("woff2");
  font-weight: 700;
}
@font-face {
  font-family: "proxima-nova";
  src: url("fonts/proxima-nova-Regular.ttf") format("woff2");
  font-weight: 400;
}
@font-face {
  font-family: "Inter";
  src: url("fonts/Inter-Bold.ttf") format("truetype");
  font-weight: 700;
}
@font-face {
  font-family: "Inter";
  src: url("fonts/Inter-Regular.ttf") format("truetype");
  font-weight: 400;
}
@font-face {
  font-family: "AvenirLTPro-Light";
  src: url("fonts/AvenirLTPro-Light-Regular.woff2") format("woff2");
  font-weight: 400;
}
@font-face {
  font-family: "AvenirLTPro-LightOblique";
  src: url("fonts/AvenirLTPro-LightOblique-Regular.woff2") format("woff2");
  font-weight: 400;
}
@font-face {
  font-family: "AvenirLTPro-Book";
  src: url("fonts/AvenirLTPro-Book-Regular.woff2") format("woff2");
  font-weight: 400;
}
@font-face {
  font-family: "AvenirLTPro-BookOblique";
  src: url("fonts/AvenirLTPro-BookOblique-Regular.woff2") format("woff2");
  font-weight: 400;
}
@font-face {
  font-family: "AvenirLTPro-Roman";
  src: url("fonts/AvenirLTPro-Roman-Regular.woff2") format("woff2");
  font-weight: 400;
}
@font-face {
  font-family: "AvenirLTPro-Oblique";
  src: url("fonts/AvenirLTPro-Oblique-Regular.woff2") format("woff2");
  font-weight: 400;
}
@font-face {
  font-family: "AvenirLTPro-Medium";
  src: url("fonts/AvenirLTPro-Medium-Regular.woff2") format("woff2");
  font-weight: 400;
}
@font-face {
  font-family: "AvenirLTPro-MediumOblique";
  src: url("fonts/AvenirLTPro-MediumOblique-Regular.woff2") format("woff2");
  font-weight: 400;
}
@font-face {
  font-family: "AvenirLTPro-Heavy";
  src: url("fonts/AvenirLTPro-Heavy-Regular.woff2") format("woff2");
  font-weight: 400;
}
@font-face {
  font-family: "AvenirLTPro-HeavyOblique";
  src: url("fonts/AvenirLTPro-HeavyOblique-Regular.woff2") format("woff2");
  font-weight: 400;
}
@font-face {
  font-family: "AvenirLTPro-Black";
  src: url("fonts/AvenirLTPro-Black-Regular.woff2") format("woff2");
  font-weight: 400;
}
@font-face {
  font-family: "AvenirLTPro-BlackOblique";
  src: url("fonts/AvenirLTPro-BlackOblique-Regular.woff2") format("woff2");
  font-weight: 400;
}
@font-face {
  font-family: "inter";
  src: url("fonts/inter-100.woff2") format("woff2");
  font-weight: 100;
}
@font-face {
  font-family: "georgia";
  src: url("https://hillsong.com/app/themes/hillsong/webfonts/georgia.woff") format("woff");
  font-weight: 400;
}
```

| Role | Font | Size | Weight |
|---|---|---|---|
| Heading 1 | hillsong-icons | 100px | 700 |
| Heading 2 | hillsong-icons | 75px | 700 |
| Heading 3 | hillsong-icons | 65px | 700 |
| Body | hillsongv2 | 12px | 400 |
| Caption | hillsongv2 | 16px | 400 |
| Code | SFMono-Regular | 14px | 400 |

**Typographic Rules:**
- Limit to 3 font families max per screen
- Use **hillsong-icons** for body/UI text, **hillsongv2** for display/headings
- Maintain consistent hierarchy: no more than 3-4 font sizes per screen
- Headings use bold (600-700), body uses regular (400)
- Line height: 1.5 for body text, 1.2 for headings
- Use color and opacity for secondary hierarchy, not additional font sizes


---

## 4. Component Stylings

### Layout (1)

**Footer** — `html`

### Data Display (3)

**Card** — `html`
- Variants: `-template`, `row`

**Badge** — `html`

**List** — `html`

### Data Input (2)

**Button** — `html`
- Variants: `color)`, `bg)`
- Animation: 

**Input** — `html`
- State: :focus, :placeholder

### Overlay (1)

**Modal** — `html`

### Media (3)

**Image** — `html`

**Icon** — `html`

**Map/Canvas** — `html`



---

## 5. Layout Principles

- **Base spacing unit:** 4px
- **Spacing scale:** 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24
- **Border radius:** 0px 0px 8px 8px, .1em, .25rem, .375rem, .5rem, .75rem, 1px, 1.5em, 2px, 2em, 2rem, 2.5px, 3px, 4px, 5px, 7px, 8px, 9px, 10px, 12px, 14px, 16px, 17px, 20px, 24px, 25px, 30px, 50px, 100%, inherit, 100px
- **Max content width:** 1198px

**Spacing as Meaning:**
| Spacing | Use |
|---|---|
| 4-8px | Tight: related items within a group |
| 12-16px | Medium: between groups |
| 24-32px | Wide: between sections |
| 48px+ | Vast: major section breaks |


---

## 6. Depth & Elevation

### Flat — subtle depth hints

- `0 0 0 2px rgba(0,0,0,.1)`
- `0 0 0 2px ButtonText`
- `0 0 2px 2px #0096ff`

### Raised — cards, buttons, interactive elements

- `0 0 3px rgba(0,0,0,.1)`
- `0 0 0#666`
- `0 0 3px #666`

### Floating — dropdowns, popovers, modals

- `#0000005c 0 0 10px 2px`
- `0 2px 12px 0 rgba(0,0,0,.12)`
- `0 4px 20px rgba(0,0,0,.1)`

### Overlay — full-screen overlays, top-level dialogs

- `0 14px 35px 0 rgba(9,9,12,.4)`
- `0 8px 32px #00000059`
- `rgba(0, 0, 0, 0.1) 30px 30px 20px 0px`

### Z-Index Scale

`0, 1, 2, 5, 10, 20, 50, 100, 200, 300, 400, 420, 430, 450, 500, 520, 550, 560, 800, 900, 999, 1000, 1200, 4001, 4100, 4200, 4201, 8999, 9000, 9990, 9995, 9998, 9999, 10001, 100000`



---

## 7. Animation & Motion

This project uses **expressive motion**. Animations are an integral part of the experience.

### CSS Animations

- `@keyframes fadeup`
- `@keyframes fadein`
- `@keyframes load8`
- `@keyframes ball-spin-fade-loader`
- `@keyframes promoslideinfromleft`
- `@keyframes fa-spin`
- `@keyframes mapboxgl-spin`
- `@keyframes mapboxgl-user-location-dot-pulse`

### Animated Components

- **Button**: 

### Motion Guidelines

- Duration: 150-300ms for micro-interactions, 300-500ms for page transitions
- Easing: `ease-out` for enters, `ease-in` for exits
- Always respect `prefers-reduced-motion`


---

## 8. Do's and Don'ts

### Do's

- Use `#000000` as the primary page background
- Pair **hillsong-icons** (body) with **hillsongv2** (display) — these are the only allowed fonts
- Follow the **4px** spacing grid for all margins, padding, and gaps
- Use the defined shadow tokens for elevation — see Section 6
- Use border-radius from the scale: 0px 0px 8px 8px, .1em, .25rem, .375rem, .5rem
- Reuse existing components from Section 4 before creating new ones

### Don'ts

- Don't introduce colors outside this palette — extend the design tokens first
- Don't introduce additional font families beyond hillsong-icons and hillsongv2 and SFMono-Regular
- Don't use arbitrary spacing values — stick to multiples of 4px
- Don't create custom box-shadow values outside the system tokens
- Don't use arbitrary border-radius values — pick from the defined scale
- Don't duplicate component patterns — check Section 4 first
- Don't use backdrop-blur or blur effects

### Anti-Patterns (detected from codebase)

- No blur or backdrop-blur effects
- No zebra striping on tables/lists


---

## 9. Responsive Behavior

| Name | Value | Source |
|---|---|---|
| sm | 40rem | css |
| md | 48rem | css |
| lg | 64rem | css |
| xl | 80rem | css |
| 2xl | 96rem | css |
| xs | 320px | css |
| xs | 350px | css |
| xs | 420px | css |
| xs | 450px | css |
| sm | 500px | css |
| sm | 510px | css |
| sm | 545px | css |
| sm | 560px | css |
| sm | 561px | css |
| sm | 599px | css |
| sm | 600px | css |
| sm | 639px | css |
| sm | 640px | css |
| md | 766px | css |
| md | 767px | css |
| md | 768px | css |
| lg | 769px | css |
| lg | 770px | css |
| lg | 781px | css |
| lg | 782px | css |
| lg | 790px | css |
| lg | 800px | css |
| lg | 900px | css |
| lg | 937px | css |
| lg | 978px | css |
| lg | 979px | css |
| xl | 1198px | css |
| xl | 1199px | css |
| 2xl | 1600px | css |
| 2xl | 1680px | css |
| 2xl | 1800px | css |
| 2xl | 1900px | css |
| 2xl | 2400px | css |

**Approach:** Use `@media (min-width: ...)` queries matching the breakpoints above.


---

## 10. Agent Prompt Guide

Use these as starting points when building new UI:

### Build a Card

```
Background: #0d112f
Border: 1px solid #585858
Radius: 7px
Padding: 16px
Font: hillsong-icons
Use shadow tokens from Section 6.
```

### Build a Button

```
Primary: bg var(--accent), text white
Ghost: bg transparent, border #585858
Padding: 8px 16px
Radius: 7px
Hover: opacity 0.9 or lighter shade
Focus: ring with var(--accent)
```

### Build a Page Layout

```
Background: #000000
Max-width: 1198px, centered
Grid: 4px base
Responsive: mobile-first, breakpoints from Section 9
```

### Build a Stats Card

```
Surface: #0d112f
Label: #464646 (muted, 12px, uppercase)
Value: #ffffff (primary, 24-32px, bold)
Status: use success/warning/danger from Section 2
```

### Build a Form

```
Input bg: #000000
Input border: 1px solid #585858
Focus: border-color var(--accent)
Label: #464646 12px
Spacing: 16px between fields
Radius: 7px
```

### General Component

```
1. Read DESIGN.md Sections 2-6 for tokens
2. Colors: only from palette
3. Font: hillsong-icons, type scale from Section 3
4. Spacing: 4px grid
5. Components: match patterns from Section 4
6. Elevation: shadow tokens
```
