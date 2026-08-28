# Interaction Reference

> Micro-interactions extracted from live DOM. Recreate these exactly for authentic feel.

## Coverage

| Component Type | Count | States Captured |
|----------------|-------|----------------|
| Button | 3 | default, focus, hover |
| Link | 3 | default, hover, focus |
| Input | 1 | default, focus |

## Transition System

These transition declarations were extracted from interactive elements:

```css
transition: 0.2s linear;
transition: 0.4s;
transition: all;
```

Apply these to all interactive elements. Never invent new durations or easings.

## Button Interactions

### Button 1 — `USE MY CURRENT LOCATION`

**States:**

- Default: `../screens/states/button-1-default.png`
- Focus: `../screens/states/button-1-focus.png`

**On focus:**

```css
/* outline: rgb(255, 255, 255) none 3px → */ outline: rgb(16, 16, 16) auto 1px;
/* outline-color: rgb(255, 255, 255) → */ outline-color: rgb(16, 16, 16);
```

**Transition:** `0.2s linear`

### Button 2 — `FIND A CHURCH`

**States:**

- Default: `../screens/states/button-2-default.png`
- Hover: `../screens/states/button-2-hover.png`
- Focus: `../screens/states/button-2-focus.png`

**On focus:**

```css
/* outline: rgb(255, 255, 255) none 3px → */ outline: rgb(25, 25, 25) auto 1px;
/* outline-color: rgb(255, 255, 255) → */ outline-color: rgb(25, 25, 25);
```

**Transition:** `0.4s`

### Button 3 — `Reject All`

**States:**

- Default: `../screens/states/button-3-default.png`
- Hover: `../screens/states/button-3-hover.png`
- Focus: `../screens/states/button-3-focus.png`

**On hover:**

```css
/* opacity: 1 → */ opacity: 0.7;
```

**On focus:**

```css
/* opacity: 1 → */ opacity: 0.7;
/* outline: rgb(255, 255, 255) none 3px → */ outline: rgb(255, 255, 255) solid 1px;
```

**Transition:** `all`

## Link Interactions

### Link 1 — `HILLSONG`

**States:**

- Default: `../screens/states/link-1-default.png`
- Hover: `../screens/states/link-1-hover.png`
- Focus: `../screens/states/link-1-focus.png`

**On focus:**

```css
/* outline: rgb(0, 0, 0) none 3px → */ outline: rgb(0, 0, 0) none 0px;
```

**Transition:** `all`

### Link 2 — `JESUS`

**States:**

- Default: `../screens/states/link-2-default.png`
- Hover: `../screens/states/link-2-hover.png`
- Focus: `../screens/states/link-2-focus.png`

**On focus:**

```css
/* outline: rgb(0, 0, 0) none 3px → */ outline: rgb(0, 0, 0) none 0px;
```

**Transition:** `all`

### Link 3 — `COLLEGE`

**States:**

- Default: `../screens/states/link-3-default.png`
- Hover: `../screens/states/link-3-hover.png`
- Focus: `../screens/states/link-3-focus.png`

**On focus:**

```css
/* outline: rgb(0, 0, 0) none 3px → */ outline: rgb(0, 0, 0) none 0px;
```

**Transition:** `all`

## Input Interactions

### Input 1 — `Search by City or Postcode`

**States:**

- Default: `../screens/states/input-1-default.png`
- Focus: `../screens/states/input-1-focus.png`

**On focus:**

```css
/* outline: rgb(0, 0, 0) none 3px → */ outline: rgb(0, 0, 0) none 0px;
```

**Transition:** `all`

## Interaction Rules

- Hover effects use **opacity** changes, not color shifts
- Focus states use **outline** (not box-shadow) — always match the extracted focus ring
- Transition durations in use: `0.2s`, `0.4s`
- Always respect `prefers-reduced-motion` — set all transitions to `0s` when enabled

