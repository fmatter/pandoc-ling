---
title: Cross-referencing Test
---

# Example with ID

::: {#test .ex}
This is a test
:::

Reference to example with ID: [@test]

# Next and Last References

::: ex
This is the first example.
:::

::: ex
This is the second example.
:::

Reference to last example: [@last]

::: ex
This will reference the next example: [@next]
:::

::: ex
This is the referenced example.
:::

Reference to last-but-one: [@llast]

Reference to last-but-eight: [@llllllllast]

# Sub-example References

:::ex
a. First sub-example.
b. Second sub-example.
c. Third sub-example.
:::

Reference to third sub-example of last-but-two: [@llast c]

Reference with custom suffix: [@last hA1l0]

# No-Format Example

::: {.ex noFormat=true}
$$\sum_{i=1}^{n}{i}=\frac{n^2-n}{2}$$
:::
