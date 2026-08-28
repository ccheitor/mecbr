# Layout Reference

> Auto-extracted from live DOM. Use this to understand how the site is structured spatially.

## Spacing System

**Base grid:** 4px

**Scale:** `2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30` px

| Spacing | Semantic Use |
|---------|-------------|
| 4px | Tight — within a component |
| 8px | Medium — between sibling items |
| 16px | Wide — between sections |
| 32px | Vast — major section breaks |

## Flex Layouts

| Element | Direction | Justify | Align | Gap | Children |
|---------|-----------|---------|-------|-----|----------|
| `div.church-locator__search-container` | column | center | center | — | 4 |
| `div.container.medium-pad-top` | column | center | center | 20px | 1 |
| `div.footer-lower-row` | row | center | center | 20px 40px | 5 |

## Structural Containers

### `<footer>` (`footer.hillsong-footer`)

```
display:          block
children:         1
```

## Layout Rules

- **Container max-width:** `1200px` — always center with `margin: auto`
- Primary layout system: **Flexbox**
- Every spacing value must be a multiple of **4px**
- Never use arbitrary margin/padding values outside the spacing scale

