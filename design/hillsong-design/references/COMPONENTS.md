# Component Reference

> Repeated DOM patterns detected by structural analysis. Each component appeared 3+ times.

## Detected Components

| Component | Category | Instances | Key Classes |
|-----------|----------|-----------|-------------|
| **Sub Nav Item** | card | 18× | `.sub-nav-item` |
| **Footer Link Section** | unknown | 10× | `.footer-link-section` |
| **Section Title** | unknown | 10× | `.section-title` |
| **Global Nav Item** | card | 7× | `.global-nav-item` |
| **Lighttext** | unknown | 6× | `.lighttext`, `.rowtitle` |
| **Imagecomponent Image** | unknown | 6× | `.imagecomponent-image` |
| **College Image Header** | unknown | 6× | `.college-image-header`, `.imagecomponent-title` |
| **Coxytabs Control** | nav-item | 5× | `.coxytabs-control` |
| **Site Nav Item** | card | 4× | `.site-nav-item` |
| **Nav Toggle** | unknown | 4× | `.nav-toggle`, `.site-nav-link` |
| **Auto Pad Bottom** | unknown | 4× | `.auto-pad-bottom`, `.auto-pad-top`, `.section-row` |
| **Rowtext** | unknown | 4× | `.rowtext` |
| **Rowtitles** | unknown | 4× | `.rowtitles` |
| **Col** | unknown | 4× | `.col`, `.colspan_1_of_4`, `.hillsong-row` |
| **College Image Content** | unknown | 4× | `.college-image-content`, `.imagecomponent-text` |
| **Sub Nav List** | unknown | 3× | `.sub-nav-list` |
| **Site Nav Item** | card | 3× | `.site-nav-item` |
| **Site Nav Link** | unknown | 3× | `.site-nav-link` |
| **Rowtitles** | unknown | 3× | `.rowtitles` |
| **Darktext** | unknown | 3× | `.darktext`, `.rowsubtitle` |

## Cards

### Sub Nav Item

**Instances found:** 18

**CSS classes:** `.sub-nav-item`

**HTML structure:**

```html
<li class="sub-nav-item" onclick="handleSecondaryNavInteraction('AboutHillsong', event, 'click')" onmouseenter="handleSecondaryNavInteraction('AboutHillsong', event, 'mouseenter')"> <a href="#" class="sub-nav-link nav-toggle"> About Hillsong <span class="toggle-chevron toggle-chevron-right"></span> </a> </li>
```

**Base styles (from design tokens):**

```css
.sub-nav-item {
  background: #0d112f;
  border: 1px solid #585858;
  border-radius: 7px;
  padding: 8px;
}```

### Global Nav Item

**Instances found:** 7

**CSS classes:** `.global-nav-item`

**HTML structure:**

```html
<li class="global-nav-item "> <a class="global-nav-link 623535" href="/"> Hillsong …</a> </li>
```

**Base styles (from design tokens):**

```css
.global-nav-item {
  background: #0d112f;
  border: 1px solid #585858;
  border-radius: 7px;
  padding: 8px;
}```

### Site Nav Item

**Instances found:** 4

**CSS classes:** `.site-nav-item`

**HTML structure:**

```html
<li class="site-nav-item"> <div onclick="handleNavItemInteraction('About', event, 'click')" onmouseenter="handleNavItemInteraction('About', event, 'mouseenter')" style="display: inline;"> <a href="#" class="site-nav-link nav-toggle" id="AboutParentNav"> About <span class="toggle-chevron toggle-chevron-right"></span> </a> </div> <div id="AboutSubNav" class="site-sub-nav-container"> <ul class="sub-nav-list"> <li class="sub-nav-item desktop-hidden" onclick="handleNavItemInteraction('About', event, 'click')" onmouseenter="handleNavItemInteraction('About', event, 'mouseenter')"> <a href="#" class="
```

**Base styles (from design tokens):**

```css
.site-nav-item {
  background: #0d112f;
  border: 1px solid #585858;
  border-radius: 7px;
  padding: 8px;
}```

### Site Nav Item

**Instances found:** 3

**CSS classes:** `.site-nav-item`

**HTML structure:**

```html
<li class="site-nav-item"> <a href="/conference" onclick="resetSubNavsForBlank()" class="site-nav-link"> Conferences …</a> </li>
```

**Base styles (from design tokens):**

```css
.site-nav-item {
  background: #0d112f;
  border: 1px solid #585858;
  border-radius: 7px;
  padding: 8px;
}```

## Navigation Items

### Coxytabs Control

**Instances found:** 5

**CSS classes:** `.coxytabs-control`

**HTML structure:**

```html
<a href="#" class="coxytabs-control" data-coxytabs-target="#tab-EUROPE">EUROPE</a>
```

**Base styles (from design tokens):**

```css
.coxytabs-control {
  padding: 4px 8px;
  cursor: pointer;
}```

## Other Components

### Footer Link Section

**Instances found:** 10

**CSS classes:** `.footer-link-section`

**HTML structure:**

```html
<div class="footer-link-section"><h3 class="section-title">About</h3><ul><li><a href="https://hillsong.com/about/">Hillsong Church</a></li><li><a href="https://hillsong.com/leadership/">Leadership</a></li><li><a href="https://hillsong.com/what-we-believe/">What we believe</a></li><li><a href="https://hillsong.com/policies/">Governance</a></li><li><a href="/jobs">Jobs</a></li></ul></div>
```

**Base styles (from design tokens):**

```css
.footer-link-section {
  background: #0d112f;
  padding: 4px;
}```

### Section Title

**Instances found:** 10

**CSS classes:** `.section-title`

**HTML structure:**

```html
<h3 class="section-title">About</h3>
```

**Base styles (from design tokens):**

```css
.section-title {
  background: #0d112f;
  padding: 4px;
}```

### Lighttext

**Instances found:** 6

**CSS classes:** `.lighttext` `.rowtitle`

**HTML structure:**

```html
<p class="rowtitle lighttext">Hillsong is a church that believes in Jesus, a church that loves God and people.</p>
```

**Base styles (from design tokens):**

```css
.lighttext {
  background: #0d112f;
  padding: 4px;
}```

### Imagecomponent Image

**Instances found:** 6

**CSS classes:** `.imagecomponent-image`

**HTML structure:**

```html
<div class="imagecomponent-image "> <a href="http://hillsongworship.com/great-i-am"><img width="300" height="300" src="https://cdn.hillsong.com/wp-content/uploads/2025/09/26002721/HMR-GreatIAm-Cover-768x768.jpg" alt="Worship"></a> </div>
```

**Base styles (from design tokens):**

```css
.imagecomponent-image {
  background: #0d112f;
  padding: 4px;
}```

### College Image Header

**Instances found:** 6

**CSS classes:** `.college-image-header` `.imagecomponent-title`

**HTML structure:**

```html
<p class="imagecomponent-title college-image-header ">Worship</p>
```

**Base styles (from design tokens):**

```css
.college-image-header {
  background: #0d112f;
  padding: 4px;
}```

### Nav Toggle

**Instances found:** 4

**CSS classes:** `.nav-toggle` `.site-nav-link`

**HTML structure:**

```html
<a href="#" class="site-nav-link nav-toggle" id="AboutParentNav"> About <span class="toggle-chevron toggle-chevron-right"></span> </a>
```

**Base styles (from design tokens):**

```css
.nav-toggle {
  background: #0d112f;
  padding: 4px;
}```

### Auto Pad Bottom

**Instances found:** 4

**CSS classes:** `.auto-pad-bottom` `.auto-pad-top` `.section-row`

**HTML structure:**

```html
<div class="section-row auto-pad-top auto-pad-bottom"> <div class="rowtitles"> <p class="rowtitle lighttext">Hillsong is a church that believes in Je…</p> </div> <div class="rowtext"> <p>Overwhelmed by the gift of salvation we …</p> </div> </div>
```

**Base styles (from design tokens):**

```css
.auto-pad-bottom {
  background: #0d112f;
  padding: 4px;
}```

### Rowtext

**Instances found:** 4

**CSS classes:** `.rowtext`

**HTML structure:**

```html
<div class="rowtext"> <p>Overwhelmed by the gift of salvation we …</p> </div>
```

**Base styles (from design tokens):**

```css
.rowtext {
  background: #0d112f;
  padding: 4px;
}```

### Rowtitles

**Instances found:** 4

**CSS classes:** `.rowtitles`

**HTML structure:**

```html
<div class="rowtitles"> <p class="rowtitle lighttext"><img width="500" height="250" class="fluid" id="mobilemap" style="max-width:500px;" src="https://d9nqqwcssctr8.cloudfront.net/wp-content/uploads/2019/08/05021302/Asia-Pacific_Map-Gold1.png" alt="Asia Pacific"></p> <p class="rowsubtitle darktext"><br></p> </div>
```

**Base styles (from design tokens):**

```css
.rowtitles {
  background: #0d112f;
  padding: 4px;
}```

### Col

**Instances found:** 4

**CSS classes:** `.col` `.colspan_1_of_4` `.hillsong-row` `.imagecomponent`

**HTML structure:**

```html
<div id="" class="hillsong-row imagecomponent col colspan_1_of_4 "> <div class="imagecomponent-image "> <a href="http://hillsongworship.com/great-i-am"><img width="300" height="300" src="https://cdn.hillsong.com/wp-content/uploads/2025/09/26002721/HMR-GreatIAm-Cover-768x768.jpg" alt="Worship"></a> </div> <p class="imagecomponent-title college-image-header ">Worship</p> <div class="imagecomponent-text college-image-content"><p>Songs that exalt and glorify the Name of…</p> </div> </div>
```

**Base styles (from design tokens):**

```css
.col {
  background: #0d112f;
  padding: 4px;
}```

### College Image Content

**Instances found:** 4

**CSS classes:** `.college-image-content` `.imagecomponent-text`

**HTML structure:**

```html
<div class="imagecomponent-text college-image-content"><p>Songs that exalt and glorify the Name of…</p> </div>
```

**Base styles (from design tokens):**

```css
.college-image-content {
  background: #0d112f;
  padding: 4px;
}```

### Sub Nav List

**Instances found:** 3

**CSS classes:** `.sub-nav-list`

**HTML structure:**

```html
<ul class="sub-nav-list"> <li class="sub-nav-item desktop-hidden" onclick="handleNavItemInteraction('About', event, 'click')" onmouseenter="handleNavItemInteraction('About', event, 'mouseenter')"> <a href="#" class="sub-nav-link sub-nav-title"> <span class="toggle-chevron toggle-chevron-left"></span> About </a> </li> <li class="sub-nav-item" onclick="handleSecondaryNavInteraction('AboutHillsong', event, 'click')" onmouseenter="handleSecondaryNavInteraction('AboutHillsong', event, 'mouseenter')"> <a href="#" class="sub-nav-link nav-toggle"> About Hillsong <span class="toggle-chevron toggle-chev
```

**Base styles (from design tokens):**

```css
.sub-nav-list {
  background: #0d112f;
  padding: 4px;
}```

### Site Nav Link

**Instances found:** 3

**CSS classes:** `.site-nav-link`

**HTML structure:**

```html
<a href="/conference" onclick="resetSubNavsForBlank()" class="site-nav-link"> Conferences </a>
```

**Base styles (from design tokens):**

```css
.site-nav-link {
  background: #0d112f;
  padding: 4px;
}```

### Rowtitles

**Instances found:** 3

**CSS classes:** `.rowtitles`

**HTML structure:**

```html
<div class="rowtitles"> <p class="rowtitle lighttext">Hillsong is a church that believes in Je…</p> </div>
```

**Base styles (from design tokens):**

```css
.rowtitles {
  background: #0d112f;
  padding: 4px;
}```

### Darktext

**Instances found:** 3

**CSS classes:** `.darktext` `.rowsubtitle`

**HTML structure:**

```html
<p class="rowsubtitle darktext">The sound of our worship</p>
```

**Base styles (from design tokens):**

```css
.darktext {
  background: #0d112f;
  padding: 4px;
}```

## Component Rules

- Match class names exactly from the patterns above
- Each component instance must be visually identical to others of its type
- Do not add extra wrappers or change the DOM structure
- Use `#585858` for all dividers within components

