---
title: Basic Examples Test
---

# Basic Structure

::: ex
This is the most basic structure of a linguistic example. 
:::

# Example with ID and Attributes

::: {#id .ex formatGloss=false}

This is a multi-line example.
But that does not mean anything for the result
All these lines are simply treated as one paragraph.
They will become one example with one number.

:::

# Example with Preamble

:::ex
Preamble

This is an example with a preamble.
:::

# Labelled Examples

:::ex
a. This is the first example.
b. This is the second.
a. The actual letters are not important, `pandoc-ling` will put them in order.

e. Empty lines are allowed between labelled lines
Subsequent lines are again treated as one sequential paragraph.
:::

# Labelled with Preamble

:::ex
Any nice description here

a. one example sentence.
b. two
c. three
:::

# Judgements

:::ex
Throwing in a preamble for good measure

a. ^* This traditionally signals ungrammaticality.
b. ^? Question-marks indicate questionable grammaticality.
c. ^^whynot?^ But in principle any sequence can be used (here even in superscript).
d. However, such long sequences sometimes lead to undesirable effects in the layout.
:::

# Single with Preamble and Judgement

:::ex
Here is a special case with a preamble

^^???^ With a singly questionably example.
Note the alignment! Especially with this very long example
that should go over various lines in the output.
:::

# Bullet List

:::ex
- This is a lazy example.
- ^# It should return letters at the start just as before.
- ^% Also testing some unusual judgements.
:::

# Single with Judgement

::: ex
^* This traditionally signals ungrammaticality.
:::
