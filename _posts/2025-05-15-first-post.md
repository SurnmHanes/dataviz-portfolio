---
title: "US Domestic Gross Box Office - Deneb Remake"
date: "2025-05-15"
layout: "single"
categories: [deneb, vega-lite, remake]
tags: [powerbi, vegalite, dataviz]
---

Inspired by a chart in *www.trendlineHQ.com* I recreated the visual using Vega-Lite inside a Deneb custom visual in Power BI.

<table>
  <tr>
    <th style="text-align: center;">Original</th>
    <th style="text-align: center;">Vega-Lite Remake</th>
  </tr>
  <tr>
    <td style="text-align: center;">
      <img src="{{ '/_images/USDomesticBoxOffice_Original.png" | relative-url }}" alt="Original Visualisation" style="width: 300px;"><br>
    </td>
    <td style="text-align: center;">
      <img src="/_images/USDomesticBoxOffice_Remake.png" alt="Vega-Lite Remake" style="width: 525px;"><br>
    </td>
  </tr>
</table>

### Tools used
- Power BI
- Vega-Lite
- Deneb custom visual
- HTML5 custom visual

Notes
- Inspiration?
- What learned?
- Any challenges
- Certain design choices?
- Reflections?

Interesting and impactful visual showing the effect of COVID-19 on cinemas.
Nice, straightforward visual to remake to start with. 
Used a bar mark to create column chart
Point marks used for left arrow and down arrow
Filtered the data *within* the visual to only show for years from 2000
Limitations
Deneb visual doesn't allow independent formatting of substrings so couldn't colour specific words. (Neither does Power BI native visuals). Had to use HTML5 custom visual to display narrative with red / green txt emphasis.

Could only have one title and one subtitle within Deneb so main title is a separate card.
