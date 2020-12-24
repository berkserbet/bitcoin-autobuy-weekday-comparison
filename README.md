<div class="jp-Cell-inputWrapper">

<div class="jp-RenderedHTMLCommon jp-RenderedMarkdown jp-MarkdownOutput " data-mime-type="text/markdown">

### TLDR. It doesn't really matter, difference is negligible. If you had started in 2013, Wednesday would have been ideal, but as of 2014 Friday appears to be the winner.[¶](#TLDR.-It-doesn't-really-matter,-difference-is-negligible.-If-you-had-started-in-2013,-Wednesday-would-have-been-ideal,-but-as-of-2014-Friday-appears-to-be-the-winner.)

</div>

</div>

<div class="jp-Cell-inputWrapper">

<div class="jp-RenderedHTMLCommon jp-RenderedMarkdown jp-MarkdownOutput " data-mime-type="text/markdown">

### The goal is to figure out which day of the week is the best day to set up a weekly bitcoin auto-buy.[¶](#The-goal-is-to-figure-out-which-day-of-the-week-is-the-best-day-to-set-up-a-weekly-bitcoin-auto-buy.)

#### I did the calculations for 24 hour highs, lows and the average of the two in order to show a worst-case to best-case scenario.[¶](#I-did-the-calculations-for-24-hour-highs,-lows-and-the-average-of-the-two-in-order-to-show-a-worst-case-to-best-case-scenario.)

#### Some of the assumptions made.[¶](#Some-of-the-assumptions-made.)

*   No transaction costs. (This is be the same as assuming constant transaction cost)
*   Every purchase was 100 USD
*   Coindesk has correct numbers
*   Calculation are made from 2013-09-30 to 2020-12-22

</div>

</div>

<div class="jp-Cell jp-CodeCell jp-Notebook-cell jp-mod-noOutputs  ">

<div class="jp-Cell-inputWrapper">

<div class="jp-InputArea jp-Cell-inputArea">

<div class="jp-InputPrompt jp-InputArea-prompt">In [1]:</div>

<div class="jp-CodeMirrorEditor jp-Editor jp-InputArea-editor" data-type="inline">

<div class="CodeMirror cm-s-jupyter">

<div class=" highlight hl-ipython3">

<pre><span></span><span class="kn">import</span> <span class="nn">pandas</span> <span class="k">as</span> <span class="nn">pd</span>
<span class="kn">import</span> <span class="nn">datetime</span>
<span class="kn">import</span> <span class="nn">matplotlib</span>
<span class="kn">from</span> <span class="nn">helpers</span> <span class="kn">import</span> <span class="n">seperate_into_weekdays</span><span class="p">,</span> <span class="n">get_totals</span><span class="p">,</span> <span class="n">get_average</span><span class="p">,</span> <span class="n">plot_range</span><span class="p">,</span> <span class="n">show_df</span><span class="p">,</span> <span class="n">WEEKLY_BUY_USD</span>
</pre>

</div>

</div>

</div>

</div>

</div>

</div>

<div class="jp-Cell jp-CodeCell jp-Notebook-cell jp-mod-noOutputs  ">

<div class="jp-Cell-inputWrapper">

<div class="jp-InputArea jp-Cell-inputArea">

<div class="jp-InputPrompt jp-InputArea-prompt">In [2]:</div>

<div class="jp-CodeMirrorEditor jp-Editor jp-InputArea-editor" data-type="inline">

<div class="CodeMirror cm-s-jupyter">

<div class=" highlight hl-ipython3">

<pre><span></span><span class="c1"># import data</span>
<span class="n">historical_data</span> <span class="o">=</span> <span class="n">pd</span><span class="o">.</span><span class="n">read_csv</span><span class="p">(</span><span class="s1">'BTC_USD_2013-09-30_2020-12-22-CoinDesk.csv'</span><span class="p">)</span>

<span class="c1"># clean and add relevant columns</span>
<span class="n">historical_data</span><span class="p">[</span><span class="s1">'Date'</span><span class="p">]</span><span class="o">=</span> <span class="n">pd</span><span class="o">.</span><span class="n">to_datetime</span><span class="p">(</span><span class="n">historical_data</span><span class="p">[</span><span class="s1">'Date'</span><span class="p">])</span>
<span class="n">historical_data</span><span class="p">[</span><span class="s1">'24h Mid (USD)'</span><span class="p">]</span> <span class="o">=</span> <span class="p">(</span><span class="n">historical_data</span><span class="p">[</span><span class="s1">'24h Low (USD)'</span><span class="p">]</span> <span class="o">+</span> <span class="n">historical_data</span><span class="p">[</span><span class="s1">'24h High (USD)'</span><span class="p">])</span> <span class="o">/</span> <span class="mi">2</span>
<span class="n">historical_data</span><span class="p">[</span><span class="s1">'btc_at_highest_cost'</span><span class="p">]</span> <span class="o">=</span> <span class="n">WEEKLY_BUY_USD</span> <span class="o">/</span> <span class="n">historical_data</span><span class="p">[</span><span class="s1">'24h High (USD)'</span><span class="p">]</span>
<span class="n">historical_data</span><span class="p">[</span><span class="s1">'btc_at_lowest_cost'</span><span class="p">]</span> <span class="o">=</span> <span class="n">WEEKLY_BUY_USD</span> <span class="o">/</span> <span class="n">historical_data</span><span class="p">[</span><span class="s1">'24h Low (USD)'</span><span class="p">]</span>
<span class="n">historical_data</span><span class="p">[</span><span class="s1">'btc_at_average_cost'</span><span class="p">]</span> <span class="o">=</span> <span class="n">WEEKLY_BUY_USD</span> <span class="o">/</span> <span class="n">historical_data</span><span class="p">[</span><span class="s1">'24h Mid (USD)'</span><span class="p">]</span>
<span class="n">historical_data</span><span class="p">[</span><span class="s1">'week_day'</span><span class="p">]</span> <span class="o">=</span> <span class="n">historical_data</span><span class="p">[</span><span class="s1">'Date'</span><span class="p">]</span><span class="o">.</span><span class="n">dt</span><span class="o">.</span><span class="n">day_name</span><span class="p">()</span>
</pre>

</div>

</div>

</div>

</div>

</div>

</div>

<div class="jp-Cell-inputWrapper">

<div class="jp-RenderedHTMLCommon jp-RenderedMarkdown jp-MarkdownOutput " data-mime-type="text/markdown">

### Lets look at average BTC purchase for constant price in USD[¶](#Lets-look-at-average-BTC-purchase-for-constant-price-in-USD)

</div>

</div>

<div class="jp-Cell jp-CodeCell jp-Notebook-cell   ">

<div class="jp-Cell-inputWrapper">

<div class="jp-InputArea jp-Cell-inputArea">

<div class="jp-InputPrompt jp-InputArea-prompt">In [3]:</div>

<div class="jp-CodeMirrorEditor jp-Editor jp-InputArea-editor" data-type="inline">

<div class="CodeMirror cm-s-jupyter">

<div class=" highlight hl-ipython3">

<pre><span></span><span class="n">day_charts</span> <span class="o">=</span> <span class="n">seperate_into_weekdays</span><span class="p">(</span><span class="n">historical_data</span><span class="p">)</span>
<span class="n">day_of_week_vals</span> <span class="o">=</span> <span class="n">get_average</span><span class="p">(</span><span class="n">day_charts</span><span class="p">)</span>
<span class="n">plot_range</span><span class="p">(</span><span class="n">day_of_week_vals</span><span class="p">,</span> <span class="s1">'Average BTC purchase amount'</span><span class="p">)</span>
<span class="n">show_df</span><span class="p">(</span><span class="n">day_of_week_vals</span><span class="p">)</span>
</pre>

</div>

</div>

</div>

</div>

</div>

<div class="jp-Cell-outputWrapper">

<div class="jp-OutputArea jp-Cell-outputArea">

<div class="jp-OutputArea-child">

<div class="jp-OutputPrompt jp-OutputArea-prompt">Out[3]:</div>

<div class="jp-RenderedHTMLCommon jp-RenderedHTML jp-OutputArea-output jp-OutputArea-executeResult" data-mime-type="text/html"><style type="text/css">#T_9500a6be_458c_11eb_8b46_1e00621e9144row0_col1{ background-color: #b0dfaa; color: #000000; }#T_9500a6be_458c_11eb_8b46_1e00621e9144row0_col2{ background-color: #92d28f; color: #000000; }#T_9500a6be_458c_11eb_8b46_1e00621e9144row0_col3{ background-color: #99d595; color: #000000; }#T_9500a6be_458c_11eb_8b46_1e00621e9144row1_col1{ background-color: #b7e2b1; color: #000000; }#T_9500a6be_458c_11eb_8b46_1e00621e9144row1_col2{ background-color: #ceecc8; color: #000000; }#T_9500a6be_458c_11eb_8b46_1e00621e9144row1_col3{ background-color: #edf8ea; color: #000000; }#T_9500a6be_458c_11eb_8b46_1e00621e9144row2_col1,#T_9500a6be_458c_11eb_8b46_1e00621e9144row2_col2,#T_9500a6be_458c_11eb_8b46_1e00621e9144row4_col3{ background-color: #00441b; color: #f1f1f1; }#T_9500a6be_458c_11eb_8b46_1e00621e9144row2_col3{ background-color: #90d18d; color: #000000; }#T_9500a6be_458c_11eb_8b46_1e00621e9144row3_col1{ background-color: #40aa5d; color: #000000; }#T_9500a6be_458c_11eb_8b46_1e00621e9144row3_col2{ background-color: #329b51; color: #000000; }#T_9500a6be_458c_11eb_8b46_1e00621e9144row3_col3{ background-color: #acdea6; color: #000000; }#T_9500a6be_458c_11eb_8b46_1e00621e9144row4_col1{ background-color: #73c476; color: #000000; }#T_9500a6be_458c_11eb_8b46_1e00621e9144row4_col2{ background-color: #016e2d; color: #f1f1f1; }#T_9500a6be_458c_11eb_8b46_1e00621e9144row5_col1,#T_9500a6be_458c_11eb_8b46_1e00621e9144row6_col2,#T_9500a6be_458c_11eb_8b46_1e00621e9144row6_col3{ background-color: #f7fcf5; color: #000000; }#T_9500a6be_458c_11eb_8b46_1e00621e9144row5_col2{ background-color: #d4eece; color: #000000; }#T_9500a6be_458c_11eb_8b46_1e00621e9144row5_col3{ background-color: #50b264; color: #000000; }#T_9500a6be_458c_11eb_8b46_1e00621e9144row6_col1{ background-color: #eef8ea; color: #000000; }</style>

<table id="T_9500a6be_458c_11eb_8b46_1e00621e9144">

<thead>

<tr>

<th class="blank level0"></th>

<th class="col_heading level0 col0">start</th>

<th class="col_heading level0 col1">average_btc_at_lowest_cost</th>

<th class="col_heading level0 col2">average_btc_at_average_cost</th>

<th class="col_heading level0 col3">average_btc_at_highest_cost</th>

</tr>

</thead>

<tbody>

<tr>

<th id="T_9500a6be_458c_11eb_8b46_1e00621e9144level0_row0" class="row_heading level0 row0">Monday</th>

<td id="T_9500a6be_458c_11eb_8b46_1e00621e9144row0_col0" class="data row0 col0">2013-09-30</td>

<td id="T_9500a6be_458c_11eb_8b46_1e00621e9144row0_col1" class="data row0 col1">0.135853</td>

<td id="T_9500a6be_458c_11eb_8b46_1e00621e9144row0_col2" class="data row0 col2">0.132694</td>

<td id="T_9500a6be_458c_11eb_8b46_1e00621e9144row0_col3" class="data row0 col3">0.129822</td>

</tr>

<tr>

<th id="T_9500a6be_458c_11eb_8b46_1e00621e9144level0_row1" class="row_heading level0 row1">Tuesday</th>

<td id="T_9500a6be_458c_11eb_8b46_1e00621e9144row1_col0" class="data row1 col0">2013-10-01</td>

<td id="T_9500a6be_458c_11eb_8b46_1e00621e9144row1_col1" class="data row1 col1">0.135807</td>

<td id="T_9500a6be_458c_11eb_8b46_1e00621e9144row1_col2" class="data row1 col2">0.132512</td>

<td id="T_9500a6be_458c_11eb_8b46_1e00621e9144row1_col3" class="data row1 col3">0.129563</td>

</tr>

<tr>

<th id="T_9500a6be_458c_11eb_8b46_1e00621e9144level0_row2" class="row_heading level0 row2">Wednesday</th>

<td id="T_9500a6be_458c_11eb_8b46_1e00621e9144row2_col0" class="data row2 col0">2013-10-02</td>

<td id="T_9500a6be_458c_11eb_8b46_1e00621e9144row2_col1" class="data row2 col1">0.137195</td>

<td id="T_9500a6be_458c_11eb_8b46_1e00621e9144row2_col2" class="data row2 col2">0.133243</td>

<td id="T_9500a6be_458c_11eb_8b46_1e00621e9144row2_col3" class="data row2 col3">0.129844</td>

</tr>

<tr>

<th id="T_9500a6be_458c_11eb_8b46_1e00621e9144level0_row3" class="row_heading level0 row3">Thursday</th>

<td id="T_9500a6be_458c_11eb_8b46_1e00621e9144row3_col0" class="data row3 col0">2013-10-03</td>

<td id="T_9500a6be_458c_11eb_8b46_1e00621e9144row3_col1" class="data row3 col1">0.136456</td>

<td id="T_9500a6be_458c_11eb_8b46_1e00621e9144row3_col2" class="data row3 col2">0.132947</td>

<td id="T_9500a6be_458c_11eb_8b46_1e00621e9144row3_col3" class="data row3 col3">0.129778</td>

</tr>

<tr>

<th id="T_9500a6be_458c_11eb_8b46_1e00621e9144level0_row4" class="row_heading level0 row4">Friday</th>

<td id="T_9500a6be_458c_11eb_8b46_1e00621e9144row4_col0" class="data row4 col0">2013-10-04</td>

<td id="T_9500a6be_458c_11eb_8b46_1e00621e9144row4_col1" class="data row4 col1">0.136201</td>

<td id="T_9500a6be_458c_11eb_8b46_1e00621e9144row4_col2" class="data row4 col2">0.133122</td>

<td id="T_9500a6be_458c_11eb_8b46_1e00621e9144row4_col3" class="data row4 col3">0.130301</td>

</tr>

<tr>

<th id="T_9500a6be_458c_11eb_8b46_1e00621e9144level0_row5" class="row_heading level0 row5">Saturday</th>

<td id="T_9500a6be_458c_11eb_8b46_1e00621e9144row5_col0" class="data row5 col0">2013-10-05</td>

<td id="T_9500a6be_458c_11eb_8b46_1e00621e9144row5_col1" class="data row5 col1">0.135205</td>

<td id="T_9500a6be_458c_11eb_8b46_1e00621e9144row5_col2" class="data row5 col2">0.132488</td>

<td id="T_9500a6be_458c_11eb_8b46_1e00621e9144row5_col3" class="data row5 col3">0.129975</td>

</tr>

<tr>

<th id="T_9500a6be_458c_11eb_8b46_1e00621e9144level0_row6" class="row_heading level0 row6">Sunday</th>

<td id="T_9500a6be_458c_11eb_8b46_1e00621e9144row6_col0" class="data row6 col0">2013-10-06</td>

<td id="T_9500a6be_458c_11eb_8b46_1e00621e9144row6_col1" class="data row6 col1">0.135336</td>

<td id="T_9500a6be_458c_11eb_8b46_1e00621e9144row6_col2" class="data row6 col2">0.132304</td>

<td id="T_9500a6be_458c_11eb_8b46_1e00621e9144row6_col3" class="data row6 col3">0.129508</td>

</tr>

</tbody>

</table>

</div>

</div>

<div class="jp-OutputArea-child">

<div class="jp-RenderedImage jp-OutputArea-output ">![](data:image/png;base64,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1KtXj5NOOokGDRpw0UUX5XnHSkZGBiNGjOCsNs2oecwxtO0cbi0+p/9AenVsydWXDuXYE05kzGWDObXnUBq178OV192V6/QuueoS/jj4j/Ru15uqB1fN7n/mmWcyZcqUPBvEjh07ll69enHyySdTo0aNPcr69OnDs88+u8fLDu+9917mzp1LWloaPdr+juefzblNSO+Bg3lq8os0at+HT5cs48ADwuWec7q046gjDqPeaT0Zfclo6qXVo9JBlShbrix3P3E3d19/N2efdjY92/TM806jZ555hnvvvZe0tDROOeUUvv/+e3r06EFaWhqNGjWibdu23HbbbRx++OHMnDmTRo0a0bhxYyZNmsTll1/+i/UtUpJYVit/SQ1NmjTxuXPnFnj42qOn51m+rEL/PMsb1sm7jcuCgTn/Kt1bihr/jC7/5vA6h+davreq5XMTf1khXlqppXmW5/fivPj4MzMzqVSpEgC33HILK1eu5J577sk/0Fzs6/j3tl8bf+amzVQ68ADezdxM3059eXbas9Q4rMYvhktk/GmllrL46x848dXeOZan+rG7t+M3sw/dvUmhRpKEUZsTkf3I9OnTufnmm9mxYwe1atVi/PjxiQ4pJXUdeDnr1m9k444dDL9yeI6JiYgUHyUnIvuRPn367HGJIy8LFixgwIABe/QrX758dpuVX+Nv9zzG89P+m9291YyO3Tpy0ZUX5T/u3/7G888/v0e/Xr16MWbMmF8dz681c/KjQP41PwC///3veffdPZuMXX755QwaNKhYYhMpCZSciJRQDRs2ZN68eXt1mmMuH8KYy4dkdxfkyz173DFjEpKIFNW4ceMSHYLIfkcNYkVERCSpKDkRERGRpKLkRERERJKK2pxIidJ3et+9Or3ivh1TRKQkUs2JiOxh5syZdO3aNceyx+67c6/PK68HmQFccMEF2U/BjfXdd9/Rs2fPfOfxuxOO+tXxZVnxzQqm/yvv53bsDS+88EL2e4FESjIlJyIpJusx64nw2P1379XpFSQ5yc2RRx6ZY9JSHFYsV3Iisi8pOREpZn8YfC59zziNHu2aM/kf43numSe468a/ZJePnzSVEWNuAeDZf02naZcBpHfoy0VX3ZidiGTUyuD2a2/n7NPOZv6c+Tx4x4P06dCHBg0aMGzYMLKe9DxnzhzS0tJIT09n1KhRNGgQHo2/c+dO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
)</div>

</div>

</div>

</div>

</div>

<div class="jp-Cell-inputWrapper">

<div class="jp-RenderedHTMLCommon jp-RenderedMarkdown jp-MarkdownOutput " data-mime-type="text/markdown">

### Lets look at total BTC purchased for weekly autobuys of constant USD[¶](#Lets-look-at-total-BTC-purchased-for-weekly-autobuys-of-constant-USD)

</div>

</div>

<div class="jp-Cell jp-CodeCell jp-Notebook-cell   ">

<div class="jp-Cell-inputWrapper">

<div class="jp-InputArea jp-Cell-inputArea">

<div class="jp-InputPrompt jp-InputArea-prompt">In [4]:</div>

<div class="jp-CodeMirrorEditor jp-Editor jp-InputArea-editor" data-type="inline">

<div class="CodeMirror cm-s-jupyter">

<div class=" highlight hl-ipython3">

<pre><span></span><span class="n">day_charts</span> <span class="o">=</span> <span class="n">seperate_into_weekdays</span><span class="p">(</span><span class="n">historical_data</span><span class="p">)</span>
<span class="n">day_of_week_vals</span> <span class="o">=</span> <span class="n">get_totals</span><span class="p">(</span><span class="n">day_charts</span><span class="p">)</span>
<span class="n">plot_range</span><span class="p">(</span><span class="n">day_of_week_vals</span><span class="p">,</span> <span class="s1">'BTC purchased'</span><span class="p">)</span>
<span class="n">show_df</span><span class="p">(</span><span class="n">day_of_week_vals</span><span class="p">)</span>
</pre>

</div>

</div>

</div>

</div>

</div>

<div class="jp-Cell-outputWrapper">

<div class="jp-OutputArea jp-Cell-outputArea">

<div class="jp-OutputArea-child">

<div class="jp-OutputPrompt jp-OutputArea-prompt">Out[4]:</div>

<div class="jp-RenderedHTMLCommon jp-RenderedHTML jp-OutputArea-output jp-OutputArea-executeResult" data-mime-type="text/html"><style type="text/css">#T_951ac2c4_458c_11eb_8b46_1e00621e9144row0_col1{ background-color: #268e47; color: #000000; }#T_951ac2c4_458c_11eb_8b46_1e00621e9144row0_col2,#T_951ac2c4_458c_11eb_8b46_1e00621e9144row0_col3,#T_951ac2c4_458c_11eb_8b46_1e00621e9144row2_col1{ background-color: #00441b; color: #f1f1f1; }#T_951ac2c4_458c_11eb_8b46_1e00621e9144row1_col1{ background-color: #5ab769; color: #000000; }#T_951ac2c4_458c_11eb_8b46_1e00621e9144row1_col2{ background-color: #3fa95c; color: #000000; }#T_951ac2c4_458c_11eb_8b46_1e00621e9144row1_col3{ background-color: #5eb96b; color: #000000; }#T_951ac2c4_458c_11eb_8b46_1e00621e9144row2_col2{ background-color: #006729; color: #f1f1f1; }#T_951ac2c4_458c_11eb_8b46_1e00621e9144row2_col3{ background-color: #72c375; color: #000000; }#T_951ac2c4_458c_11eb_8b46_1e00621e9144row3_col1,#T_951ac2c4_458c_11eb_8b46_1e00621e9144row3_col2{ background-color: #329b51; color: #000000; }#T_951ac2c4_458c_11eb_8b46_1e00621e9144row3_col3{ background-color: #84cc83; color: #000000; }#T_951ac2c4_458c_11eb_8b46_1e00621e9144row4_col1{ background-color: #c2e7bb; color: #000000; }#T_951ac2c4_458c_11eb_8b46_1e00621e9144row4_col2{ background-color: #b2e0ac; color: #000000; }#T_951ac2c4_458c_11eb_8b46_1e00621e9144row4_col3{ background-color: #afdfa8; color: #000000; }#T_951ac2c4_458c_11eb_8b46_1e00621e9144row5_col1,#T_951ac2c4_458c_11eb_8b46_1e00621e9144row6_col2,#T_951ac2c4_458c_11eb_8b46_1e00621e9144row6_col3{ background-color: #f7fcf5; color: #000000; }#T_951ac2c4_458c_11eb_8b46_1e00621e9144row5_col2{ background-color: #e5f5e0; color: #000000; }#T_951ac2c4_458c_11eb_8b46_1e00621e9144row5_col3{ background-color: #aadda4; color: #000000; }#T_951ac2c4_458c_11eb_8b46_1e00621e9144row6_col1{ background-color: #eff9ec; color: #000000; }</style>

<table id="T_951ac2c4_458c_11eb_8b46_1e00621e9144">

<thead>

<tr>

<th class="blank level0"></th>

<th class="col_heading level0 col0">start</th>

<th class="col_heading level0 col1">total_btc_at_lowest_cost</th>

<th class="col_heading level0 col2">total_btc_at_average_cost</th>

<th class="col_heading level0 col3">total_btc_at_highest_cost</th>

</tr>

</thead>

<tbody>

<tr>

<th id="T_951ac2c4_458c_11eb_8b46_1e00621e9144level0_row0" class="row_heading level0 row0">Monday</th>

<td id="T_951ac2c4_458c_11eb_8b46_1e00621e9144row0_col0" class="data row0 col0">2013-09-30</td>

<td id="T_951ac2c4_458c_11eb_8b46_1e00621e9144row0_col1" class="data row0 col1">51.352589</td>

<td id="T_951ac2c4_458c_11eb_8b46_1e00621e9144row0_col2" class="data row0 col2">50.158449</td>

<td id="T_951ac2c4_458c_11eb_8b46_1e00621e9144row0_col3" class="data row0 col3">49.072891</td>

</tr>

<tr>

<th id="T_951ac2c4_458c_11eb_8b46_1e00621e9144level0_row1" class="row_heading level0 row1">Tuesday</th>

<td id="T_951ac2c4_458c_11eb_8b46_1e00621e9144row1_col0" class="data row1 col0">2013-10-01</td>

<td id="T_951ac2c4_458c_11eb_8b46_1e00621e9144row1_col1" class="data row1 col1">51.199204</td>

<td id="T_951ac2c4_458c_11eb_8b46_1e00621e9144row1_col2" class="data row1 col2">49.957002</td>

<td id="T_951ac2c4_458c_11eb_8b46_1e00621e9144row1_col3" class="data row1 col3">48.845227</td>

</tr>

<tr>

<th id="T_951ac2c4_458c_11eb_8b46_1e00621e9144level0_row2" class="row_heading level0 row2">Wednesday</th>

<td id="T_951ac2c4_458c_11eb_8b46_1e00621e9144row2_col0" class="data row2 col0">2013-10-02</td>

<td id="T_951ac2c4_458c_11eb_8b46_1e00621e9144row2_col1" class="data row2 col1">51.585286</td>

<td id="T_951ac2c4_458c_11eb_8b46_1e00621e9144row2_col2" class="data row2 col2">50.099402</td>

<td id="T_951ac2c4_458c_11eb_8b46_1e00621e9144row2_col3" class="data row2 col3">48.821320</td>

</tr>

<tr>

<th id="T_951ac2c4_458c_11eb_8b46_1e00621e9144level0_row3" class="row_heading level0 row3">Thursday</th>

<td id="T_951ac2c4_458c_11eb_8b46_1e00621e9144row3_col0" class="data row3 col0">2013-10-03</td>

<td id="T_951ac2c4_458c_11eb_8b46_1e00621e9144row3_col1" class="data row3 col1">51.307381</td>

<td id="T_951ac2c4_458c_11eb_8b46_1e00621e9144row3_col2" class="data row3 col2">49.987941</td>

<td id="T_951ac2c4_458c_11eb_8b46_1e00621e9144row3_col3" class="data row3 col3">48.796356</td>

</tr>

<tr>

<th id="T_951ac2c4_458c_11eb_8b46_1e00621e9144level0_row4" class="row_heading level0 row4">Friday</th>

<td id="T_951ac2c4_458c_11eb_8b46_1e00621e9144row4_col0" class="data row4 col0">2013-10-04</td>

<td id="T_951ac2c4_458c_11eb_8b46_1e00621e9144row4_col1" class="data row4 col1">50.939074</td>

<td id="T_951ac2c4_458c_11eb_8b46_1e00621e9144row4_col2" class="data row4 col2">49.787460</td>

<td id="T_951ac2c4_458c_11eb_8b46_1e00621e9144row4_col3" class="data row4 col3">48.732680</td>

</tr>

<tr>

<th id="T_951ac2c4_458c_11eb_8b46_1e00621e9144level0_row5" class="row_heading level0 row5">Saturday</th>

<td id="T_951ac2c4_458c_11eb_8b46_1e00621e9144row5_col0" class="data row5 col0">2013-10-05</td>

<td id="T_951ac2c4_458c_11eb_8b46_1e00621e9144row5_col1" class="data row5 col1">50.701932</td>

<td id="T_951ac2c4_458c_11eb_8b46_1e00621e9144row5_col2" class="data row5 col2">49.682844</td>

<td id="T_951ac2c4_458c_11eb_8b46_1e00621e9144row5_col3" class="data row5 col3">48.740703</td>

</tr>

<tr>

<th id="T_951ac2c4_458c_11eb_8b46_1e00621e9144level0_row6" class="row_heading level0 row6">Sunday</th>

<td id="T_951ac2c4_458c_11eb_8b46_1e00621e9144row6_col0" class="data row6 col0">2013-10-06</td>

<td id="T_951ac2c4_458c_11eb_8b46_1e00621e9144row6_col1" class="data row6 col1">50.750891</td>

<td id="T_951ac2c4_458c_11eb_8b46_1e00621e9144row6_col2" class="data row6 col2">49.613885</td>

<td id="T_951ac2c4_458c_11eb_8b46_1e00621e9144row6_col3" class="data row6 col3">48.565638</td>

</tr>

</tbody>

</table>

</div>

</div>

<div class="jp-OutputArea-child">

<div class="jp-RenderedImage jp-OutputArea-output ">![](data:image/png;base64,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
)</div>

</div>

</div>

</div>

</div>

<div class="jp-Cell-inputWrapper">

<div class="jp-RenderedHTMLCommon jp-RenderedMarkdown jp-MarkdownOutput " data-mime-type="text/markdown">

#### Difference between days appears to be negligible[¶](#Difference-between-days-appears-to-be-negligible)

*   Buying on wednesdays might give a benefit of 0.001% for average price.
*   Totals give much less information, especially considering that the start date was a Monday.

Since the purchases started in 2013 when BTC price was much lower compared to USD, this will give a much larger weight to the earlier days.

#### So lets explore if this holds for later[¶](#So-lets-explore-if-this-holds-for-later)

</div>

</div>

<div class="jp-Cell jp-CodeCell jp-Notebook-cell   ">

<div class="jp-Cell-inputWrapper">

<div class="jp-InputArea jp-Cell-inputArea">

<div class="jp-InputPrompt jp-InputArea-prompt">In [5]:</div>

<div class="jp-CodeMirrorEditor jp-Editor jp-InputArea-editor" data-type="inline">

<div class="CodeMirror cm-s-jupyter">

<div class=" highlight hl-ipython3">

<pre><span></span><span class="c1"># 2014 Jan 1st - today</span>
<span class="n">day_charts</span> <span class="o">=</span> <span class="n">seperate_into_weekdays</span><span class="p">(</span><span class="n">historical_data</span><span class="p">,</span> <span class="n">start_date</span><span class="o">=</span><span class="n">datetime</span><span class="o">.</span><span class="n">datetime</span><span class="p">(</span><span class="mi">2014</span><span class="p">,</span> <span class="mi">1</span><span class="p">,</span> <span class="mi">1</span><span class="p">))</span>
<span class="n">day_of_week_vals</span> <span class="o">=</span> <span class="n">get_average</span><span class="p">(</span><span class="n">day_charts</span><span class="p">)</span>
<span class="n">show_df</span><span class="p">(</span><span class="n">day_of_week_vals</span><span class="p">)</span>
</pre>

</div>

</div>

</div>

</div>

</div>

<div class="jp-Cell-outputWrapper">

<div class="jp-OutputArea jp-Cell-outputArea">

<div class="jp-OutputArea-child">

<div class="jp-OutputPrompt jp-OutputArea-prompt">Out[5]:</div>

<div class="jp-RenderedHTMLCommon jp-RenderedHTML jp-OutputArea-output jp-OutputArea-executeResult" data-mime-type="text/html"><style type="text/css">#T_952d8fee_458c_11eb_8b46_1e00621e9144row0_col1,#T_952d8fee_458c_11eb_8b46_1e00621e9144row0_col2,#T_952d8fee_458c_11eb_8b46_1e00621e9144row0_col3{ background-color: #f7fcf5; color: #000000; }#T_952d8fee_458c_11eb_8b46_1e00621e9144row1_col1{ background-color: #c8e9c1; color: #000000; }#T_952d8fee_458c_11eb_8b46_1e00621e9144row1_col2{ background-color: #e0f3db; color: #000000; }#T_952d8fee_458c_11eb_8b46_1e00621e9144row1_col3{ background-color: #ebf7e7; color: #000000; }#T_952d8fee_458c_11eb_8b46_1e00621e9144row2_col1{ background-color: #37a055; color: #000000; }#T_952d8fee_458c_11eb_8b46_1e00621e9144row2_col2{ background-color: #65bd6f; color: #000000; }#T_952d8fee_458c_11eb_8b46_1e00621e9144row2_col3{ background-color: #83cb82; color: #000000; }#T_952d8fee_458c_11eb_8b46_1e00621e9144row3_col1,#T_952d8fee_458c_11eb_8b46_1e00621e9144row5_col3{ background-color: #0c7735; color: #f1f1f1; }#T_952d8fee_458c_11eb_8b46_1e00621e9144row3_col2{ background-color: #40aa5d; color: #000000; }#T_952d8fee_458c_11eb_8b46_1e00621e9144row3_col3{ background-color: #79c67a; color: #000000; }#T_952d8fee_458c_11eb_8b46_1e00621e9144row4_col1,#T_952d8fee_458c_11eb_8b46_1e00621e9144row4_col2,#T_952d8fee_458c_11eb_8b46_1e00621e9144row4_col3{ background-color: #00441b; color: #f1f1f1; }#T_952d8fee_458c_11eb_8b46_1e00621e9144row5_col1{ background-color: #97d492; color: #000000; }#T_952d8fee_458c_11eb_8b46_1e00621e9144row5_col2{ background-color: #3aa357; color: #000000; }#T_952d8fee_458c_11eb_8b46_1e00621e9144row6_col1{ background-color: #52b365; color: #000000; }#T_952d8fee_458c_11eb_8b46_1e00621e9144row6_col2{ background-color: #3fa85b; color: #000000; }#T_952d8fee_458c_11eb_8b46_1e00621e9144row6_col3{ background-color: #38a156; color: #000000; }</style>

<table id="T_952d8fee_458c_11eb_8b46_1e00621e9144">

<thead>

<tr>

<th class="blank level0"></th>

<th class="col_heading level0 col0">start</th>

<th class="col_heading level0 col1">average_btc_at_lowest_cost</th>

<th class="col_heading level0 col2">average_btc_at_average_cost</th>

<th class="col_heading level0 col3">average_btc_at_highest_cost</th>

</tr>

</thead>

<tbody>

<tr>

<th id="T_952d8fee_458c_11eb_8b46_1e00621e9144level0_row0" class="row_heading level0 row0">Monday</th>

<td id="T_952d8fee_458c_11eb_8b46_1e00621e9144row0_col0" class="data row0 col0">2014-01-06</td>

<td id="T_952d8fee_458c_11eb_8b46_1e00621e9144row0_col1" class="data row0 col1">0.126294</td>

<td id="T_952d8fee_458c_11eb_8b46_1e00621e9144row0_col2" class="data row0 col2">0.123571</td>

<td id="T_952d8fee_458c_11eb_8b46_1e00621e9144row0_col3" class="data row0 col3">0.121055</td>

</tr>

<tr>

<th id="T_952d8fee_458c_11eb_8b46_1e00621e9144level0_row1" class="row_heading level0 row1">Tuesday</th>

<td id="T_952d8fee_458c_11eb_8b46_1e00621e9144row1_col0" class="data row1 col0">2014-01-07</td>

<td id="T_952d8fee_458c_11eb_8b46_1e00621e9144row1_col1" class="data row1 col1">0.126592</td>

<td id="T_952d8fee_458c_11eb_8b46_1e00621e9144row1_col2" class="data row1 col2">0.123765</td>

<td id="T_952d8fee_458c_11eb_8b46_1e00621e9144row1_col3" class="data row1 col3">0.121176</td>

</tr>

<tr>

<th id="T_952d8fee_458c_11eb_8b46_1e00621e9144level0_row2" class="row_heading level0 row2">Wednesday</th>

<td id="T_952d8fee_458c_11eb_8b46_1e00621e9144row2_col0" class="data row2 col0">2014-01-01</td>

<td id="T_952d8fee_458c_11eb_8b46_1e00621e9144row2_col1" class="data row2 col1">0.127098</td>

<td id="T_952d8fee_458c_11eb_8b46_1e00621e9144row2_col2" class="data row2 col2">0.124280</td>

<td id="T_952d8fee_458c_11eb_8b46_1e00621e9144row2_col3" class="data row2 col3">0.121704</td>

</tr>

<tr>

<th id="T_952d8fee_458c_11eb_8b46_1e00621e9144level0_row3" class="row_heading level0 row3">Thursday</th>

<td id="T_952d8fee_458c_11eb_8b46_1e00621e9144row3_col0" class="data row3 col0">2014-01-02</td>

<td id="T_952d8fee_458c_11eb_8b46_1e00621e9144row3_col1" class="data row3 col1">0.127296</td>

<td id="T_952d8fee_458c_11eb_8b46_1e00621e9144row3_col2" class="data row3 col2">0.124396</td>

<td id="T_952d8fee_458c_11eb_8b46_1e00621e9144row3_col3" class="data row3 col3">0.121737</td>

</tr>

<tr>

<th id="T_952d8fee_458c_11eb_8b46_1e00621e9144level0_row4" class="row_heading level0 row4">Friday</th>

<td id="T_952d8fee_458c_11eb_8b46_1e00621e9144row4_col0" class="data row4 col0">2014-01-03</td>

<td id="T_952d8fee_458c_11eb_8b46_1e00621e9144row4_col1" class="data row4 col1">0.127499</td>

<td id="T_952d8fee_458c_11eb_8b46_1e00621e9144row4_col2" class="data row4 col2">0.124890</td>

<td id="T_952d8fee_458c_11eb_8b46_1e00621e9144row4_col3" class="data row4 col3">0.122464</td>

</tr>

<tr>

<th id="T_952d8fee_458c_11eb_8b46_1e00621e9144level0_row5" class="row_heading level0 row5">Saturday</th>

<td id="T_952d8fee_458c_11eb_8b46_1e00621e9144row5_col0" class="data row5 col0">2014-01-04</td>

<td id="T_952d8fee_458c_11eb_8b46_1e00621e9144row5_col1" class="data row5 col1">0.126781</td>

<td id="T_952d8fee_458c_11eb_8b46_1e00621e9144row5_col2" class="data row5 col2">0.124436</td>

<td id="T_952d8fee_458c_11eb_8b46_1e00621e9144row5_col3" class="data row5 col3">0.122226</td>

</tr>

<tr>

<th id="T_952d8fee_458c_11eb_8b46_1e00621e9144level0_row6" class="row_heading level0 row6">Sunday</th>

<td id="T_952d8fee_458c_11eb_8b46_1e00621e9144row6_col0" class="data row6 col0">2014-01-05</td>

<td id="T_952d8fee_458c_11eb_8b46_1e00621e9144row6_col1" class="data row6 col1">0.126999</td>

<td id="T_952d8fee_458c_11eb_8b46_1e00621e9144row6_col2" class="data row6 col2">0.124407</td>

<td id="T_952d8fee_458c_11eb_8b46_1e00621e9144row6_col3" class="data row6 col3">0.121988</td>

</tr>

</tbody>

</table>

</div>

</div>

</div>

</div>

</div>

<div class="jp-Cell jp-CodeCell jp-Notebook-cell   ">

<div class="jp-Cell-inputWrapper">

<div class="jp-InputArea jp-Cell-inputArea">

<div class="jp-InputPrompt jp-InputArea-prompt">In [6]:</div>

<div class="jp-CodeMirrorEditor jp-Editor jp-InputArea-editor" data-type="inline">

<div class="CodeMirror cm-s-jupyter">

<div class=" highlight hl-ipython3">

<pre><span></span><span class="c1"># 2015 Jan 1st - today</span>
<span class="n">day_charts</span> <span class="o">=</span> <span class="n">seperate_into_weekdays</span><span class="p">(</span><span class="n">historical_data</span><span class="p">,</span> <span class="n">start_date</span><span class="o">=</span><span class="n">datetime</span><span class="o">.</span><span class="n">datetime</span><span class="p">(</span><span class="mi">2015</span><span class="p">,</span> <span class="mi">1</span><span class="p">,</span> <span class="mi">1</span><span class="p">))</span>
<span class="n">day_of_week_vals</span> <span class="o">=</span> <span class="n">get_average</span><span class="p">(</span><span class="n">day_charts</span><span class="p">)</span>
<span class="n">show_df</span><span class="p">(</span><span class="n">day_of_week_vals</span><span class="p">)</span>
</pre>

</div>

</div>

</div>

</div>

</div>

<div class="jp-Cell-outputWrapper">

<div class="jp-OutputArea jp-Cell-outputArea">

<div class="jp-OutputArea-child">

<div class="jp-OutputPrompt jp-OutputArea-prompt">Out[6]:</div>

<div class="jp-RenderedHTMLCommon jp-RenderedHTML jp-OutputArea-output jp-OutputArea-executeResult" data-mime-type="text/html"><style type="text/css">#T_95317a3c_458c_11eb_8b46_1e00621e9144row0_col1,#T_95317a3c_458c_11eb_8b46_1e00621e9144row0_col2,#T_95317a3c_458c_11eb_8b46_1e00621e9144row0_col3{ background-color: #f7fcf5; color: #000000; }#T_95317a3c_458c_11eb_8b46_1e00621e9144row1_col1{ background-color: #97d492; color: #000000; }#T_95317a3c_458c_11eb_8b46_1e00621e9144row1_col2{ background-color: #caeac3; color: #000000; }#T_95317a3c_458c_11eb_8b46_1e00621e9144row1_col3{ background-color: #e7f6e2; color: #000000; }#T_95317a3c_458c_11eb_8b46_1e00621e9144row2_col1{ background-color: #05712f; color: #f1f1f1; }#T_95317a3c_458c_11eb_8b46_1e00621e9144row2_col2{ background-color: #3fa95c; color: #000000; }#T_95317a3c_458c_11eb_8b46_1e00621e9144row2_col3{ background-color: #81ca81; color: #000000; }#T_95317a3c_458c_11eb_8b46_1e00621e9144row3_col1{ background-color: #005924; color: #f1f1f1; }#T_95317a3c_458c_11eb_8b46_1e00621e9144row3_col2{ background-color: #067230; color: #f1f1f1; }#T_95317a3c_458c_11eb_8b46_1e00621e9144row3_col3{ background-color: #18823d; color: #f1f1f1; }#T_95317a3c_458c_11eb_8b46_1e00621e9144row4_col1,#T_95317a3c_458c_11eb_8b46_1e00621e9144row4_col2,#T_95317a3c_458c_11eb_8b46_1e00621e9144row4_col3{ background-color: #00441b; color: #f1f1f1; }#T_95317a3c_458c_11eb_8b46_1e00621e9144row5_col1{ background-color: #48ae60; color: #000000; }#T_95317a3c_458c_11eb_8b46_1e00621e9144row5_col2{ background-color: #359e53; color: #000000; }#T_95317a3c_458c_11eb_8b46_1e00621e9144row5_col3{ background-color: #2a924a; color: #000000; }#T_95317a3c_458c_11eb_8b46_1e00621e9144row6_col1{ background-color: #46ae60; color: #000000; }#T_95317a3c_458c_11eb_8b46_1e00621e9144row6_col2{ background-color: #4eb264; color: #000000; }#T_95317a3c_458c_11eb_8b46_1e00621e9144row6_col3{ background-color: #56b567; color: #000000; }</style>

<table id="T_95317a3c_458c_11eb_8b46_1e00621e9144">

<thead>

<tr>

<th class="blank level0"></th>

<th class="col_heading level0 col0">start</th>

<th class="col_heading level0 col1">average_btc_at_lowest_cost</th>

<th class="col_heading level0 col2">average_btc_at_average_cost</th>

<th class="col_heading level0 col3">average_btc_at_highest_cost</th>

</tr>

</thead>

<tbody>

<tr>

<th id="T_95317a3c_458c_11eb_8b46_1e00621e9144level0_row0" class="row_heading level0 row0">Monday</th>

<td id="T_95317a3c_458c_11eb_8b46_1e00621e9144row0_col0" class="data row0 col0">2015-01-05</td>

<td id="T_95317a3c_458c_11eb_8b46_1e00621e9144row0_col1" class="data row0 col1">0.111888</td>

<td id="T_95317a3c_458c_11eb_8b46_1e00621e9144row0_col2" class="data row0 col2">0.109747</td>

<td id="T_95317a3c_458c_11eb_8b46_1e00621e9144row0_col3" class="data row0 col3">0.107746</td>

</tr>

<tr>

<th id="T_95317a3c_458c_11eb_8b46_1e00621e9144level0_row1" class="row_heading level0 row1">Tuesday</th>

<td id="T_95317a3c_458c_11eb_8b46_1e00621e9144row1_col0" class="data row1 col0">2015-01-06</td>

<td id="T_95317a3c_458c_11eb_8b46_1e00621e9144row1_col1" class="data row1 col1">0.112507</td>

<td id="T_95317a3c_458c_11eb_8b46_1e00621e9144row1_col2" class="data row1 col2">0.110120</td>

<td id="T_95317a3c_458c_11eb_8b46_1e00621e9144row1_col3" class="data row1 col3">0.107927</td>

</tr>

<tr>

<th id="T_95317a3c_458c_11eb_8b46_1e00621e9144level0_row2" class="row_heading level0 row2">Wednesday</th>

<td id="T_95317a3c_458c_11eb_8b46_1e00621e9144row2_col0" class="data row2 col0">2015-01-07</td>

<td id="T_95317a3c_458c_11eb_8b46_1e00621e9144row2_col1" class="data row2 col1">0.113204</td>

<td id="T_95317a3c_458c_11eb_8b46_1e00621e9144row2_col2" class="data row2 col2">0.110729</td>

<td id="T_95317a3c_458c_11eb_8b46_1e00621e9144row2_col3" class="data row2 col3">0.108478</td>

</tr>

<tr>

<th id="T_95317a3c_458c_11eb_8b46_1e00621e9144level0_row3" class="row_heading level0 row3">Thursday</th>

<td id="T_95317a3c_458c_11eb_8b46_1e00621e9144row3_col0" class="data row3 col0">2015-01-01</td>

<td id="T_95317a3c_458c_11eb_8b46_1e00621e9144row3_col1" class="data row3 col1">0.113328</td>

<td id="T_95317a3c_458c_11eb_8b46_1e00621e9144row3_col2" class="data row3 col2">0.111074</td>

<td id="T_95317a3c_458c_11eb_8b46_1e00621e9144row3_col3" class="data row3 col3">0.108990</td>

</tr>

<tr>

<th id="T_95317a3c_458c_11eb_8b46_1e00621e9144level0_row4" class="row_heading level0 row4">Friday</th>

<td id="T_95317a3c_458c_11eb_8b46_1e00621e9144row4_col0" class="data row4 col0">2015-01-02</td>

<td id="T_95317a3c_458c_11eb_8b46_1e00621e9144row4_col1" class="data row4 col1">0.113425</td>

<td id="T_95317a3c_458c_11eb_8b46_1e00621e9144row4_col2" class="data row4 col2">0.111303</td>

<td id="T_95317a3c_458c_11eb_8b46_1e00621e9144row4_col3" class="data row4 col3">0.109324</td>

</tr>

<tr>

<th id="T_95317a3c_458c_11eb_8b46_1e00621e9144level0_row5" class="row_heading level0 row5">Saturday</th>

<td id="T_95317a3c_458c_11eb_8b46_1e00621e9144row5_col0" class="data row5 col0">2015-01-03</td>

<td id="T_95317a3c_458c_11eb_8b46_1e00621e9144row5_col1" class="data row5 col1">0.112825</td>

<td id="T_95317a3c_458c_11eb_8b46_1e00621e9144row5_col2" class="data row5 col2">0.110795</td>

<td id="T_95317a3c_458c_11eb_8b46_1e00621e9144row5_col3" class="data row5 col3">0.108882</td>

</tr>

<tr>

<th id="T_95317a3c_458c_11eb_8b46_1e00621e9144level0_row6" class="row_heading level0 row6">Sunday</th>

<td id="T_95317a3c_458c_11eb_8b46_1e00621e9144row6_col0" class="data row6 col0">2015-01-04</td>

<td id="T_95317a3c_458c_11eb_8b46_1e00621e9144row6_col1" class="data row6 col1">0.112825</td>

<td id="T_95317a3c_458c_11eb_8b46_1e00621e9144row6_col2" class="data row6 col2">0.110669</td>

<td id="T_95317a3c_458c_11eb_8b46_1e00621e9144row6_col3" class="data row6 col3">0.108651</td>

</tr>

</tbody>

</table>

</div>

</div>

</div>

</div>

</div>

<div class="jp-Cell jp-CodeCell jp-Notebook-cell   ">

<div class="jp-Cell-inputWrapper">

<div class="jp-InputArea jp-Cell-inputArea">

<div class="jp-InputPrompt jp-InputArea-prompt">In [7]:</div>

<div class="jp-CodeMirrorEditor jp-Editor jp-InputArea-editor" data-type="inline">

<div class="CodeMirror cm-s-jupyter">

<div class=" highlight hl-ipython3">

<pre><span></span><span class="c1"># 2016 Jan 1st - today</span>
<span class="n">day_charts</span> <span class="o">=</span> <span class="n">seperate_into_weekdays</span><span class="p">(</span><span class="n">historical_data</span><span class="p">,</span> <span class="n">start_date</span><span class="o">=</span><span class="n">datetime</span><span class="o">.</span><span class="n">datetime</span><span class="p">(</span><span class="mi">2016</span><span class="p">,</span> <span class="mi">1</span><span class="p">,</span> <span class="mi">1</span><span class="p">))</span>
<span class="n">day_of_week_vals</span> <span class="o">=</span> <span class="n">get_average</span><span class="p">(</span><span class="n">day_charts</span><span class="p">)</span>
<span class="n">show_df</span><span class="p">(</span><span class="n">day_of_week_vals</span><span class="p">)</span>
</pre>

</div>

</div>

</div>

</div>

</div>

<div class="jp-Cell-outputWrapper">

<div class="jp-OutputArea jp-Cell-outputArea">

<div class="jp-OutputArea-child">

<div class="jp-OutputPrompt jp-OutputArea-prompt">Out[7]:</div>

<div class="jp-RenderedHTMLCommon jp-RenderedHTML jp-OutputArea-output jp-OutputArea-executeResult" data-mime-type="text/html"><style type="text/css">#T_95355486_458c_11eb_8b46_1e00621e9144row0_col1,#T_95355486_458c_11eb_8b46_1e00621e9144row0_col2,#T_95355486_458c_11eb_8b46_1e00621e9144row3_col3{ background-color: #f7fcf5; color: #000000; }#T_95355486_458c_11eb_8b46_1e00621e9144row0_col3,#T_95355486_458c_11eb_8b46_1e00621e9144row1_col1{ background-color: #d4eece; color: #000000; }#T_95355486_458c_11eb_8b46_1e00621e9144row1_col2{ background-color: #e4f5df; color: #000000; }#T_95355486_458c_11eb_8b46_1e00621e9144row1_col3{ background-color: #ceecc8; color: #000000; }#T_95355486_458c_11eb_8b46_1e00621e9144row2_col1{ background-color: #bbe4b4; color: #000000; }#T_95355486_458c_11eb_8b46_1e00621e9144row2_col2{ background-color: #d9f0d3; color: #000000; }#T_95355486_458c_11eb_8b46_1e00621e9144row2_col3{ background-color: #d1edcb; color: #000000; }#T_95355486_458c_11eb_8b46_1e00621e9144row3_col1{ background-color: #c9eac2; color: #000000; }#T_95355486_458c_11eb_8b46_1e00621e9144row3_col2{ background-color: #f1faee; color: #000000; }#T_95355486_458c_11eb_8b46_1e00621e9144row4_col1,#T_95355486_458c_11eb_8b46_1e00621e9144row4_col2,#T_95355486_458c_11eb_8b46_1e00621e9144row4_col3{ background-color: #00441b; color: #f1f1f1; }#T_95355486_458c_11eb_8b46_1e00621e9144row5_col1{ background-color: #56b567; color: #000000; }#T_95355486_458c_11eb_8b46_1e00621e9144row5_col2{ background-color: #39a257; color: #000000; }#T_95355486_458c_11eb_8b46_1e00621e9144row5_col3{ background-color: #107a37; color: #f1f1f1; }#T_95355486_458c_11eb_8b46_1e00621e9144row6_col1{ background-color: #9bd696; color: #000000; }#T_95355486_458c_11eb_8b46_1e00621e9144row6_col2{ background-color: #80ca80; color: #000000; }#T_95355486_458c_11eb_8b46_1e00621e9144row6_col3{ background-color: #3ca559; color: #000000; }</style>

<table id="T_95355486_458c_11eb_8b46_1e00621e9144">

<thead>

<tr>

<th class="blank level0"></th>

<th class="col_heading level0 col0">start</th>

<th class="col_heading level0 col1">average_btc_at_lowest_cost</th>

<th class="col_heading level0 col2">average_btc_at_average_cost</th>

<th class="col_heading level0 col3">average_btc_at_highest_cost</th>

</tr>

</thead>

<tbody>

<tr>

<th id="T_95355486_458c_11eb_8b46_1e00621e9144level0_row0" class="row_heading level0 row0">Monday</th>

<td id="T_95355486_458c_11eb_8b46_1e00621e9144row0_col0" class="data row0 col0">2016-01-04</td>

<td id="T_95355486_458c_11eb_8b46_1e00621e9144row0_col1" class="data row0 col1">0.056599</td>

<td id="T_95355486_458c_11eb_8b46_1e00621e9144row0_col2" class="data row0 col2">0.055711</td>

<td id="T_95355486_458c_11eb_8b46_1e00621e9144row0_col3" class="data row0 col3">0.054876</td>

</tr>

<tr>

<th id="T_95355486_458c_11eb_8b46_1e00621e9144level0_row1" class="row_heading level0 row1">Tuesday</th>

<td id="T_95355486_458c_11eb_8b46_1e00621e9144row1_col0" class="data row1 col0">2016-01-05</td>

<td id="T_95355486_458c_11eb_8b46_1e00621e9144row1_col1" class="data row1 col1">0.056866</td>

<td id="T_95355486_458c_11eb_8b46_1e00621e9144row1_col2" class="data row1 col2">0.055847</td>

<td id="T_95355486_458c_11eb_8b46_1e00621e9144row1_col3" class="data row1 col3">0.054899</td>

</tr>

<tr>

<th id="T_95355486_458c_11eb_8b46_1e00621e9144level0_row2" class="row_heading level0 row2">Wednesday</th>

<td id="T_95355486_458c_11eb_8b46_1e00621e9144row2_col0" class="data row2 col0">2016-01-06</td>

<td id="T_95355486_458c_11eb_8b46_1e00621e9144row2_col1" class="data row2 col1">0.056994</td>

<td id="T_95355486_458c_11eb_8b46_1e00621e9144row2_col2" class="data row2 col2">0.055899</td>

<td id="T_95355486_458c_11eb_8b46_1e00621e9144row2_col3" class="data row2 col3">0.054885</td>

</tr>

<tr>

<th id="T_95355486_458c_11eb_8b46_1e00621e9144level0_row3" class="row_heading level0 row3">Thursday</th>

<td id="T_95355486_458c_11eb_8b46_1e00621e9144row3_col0" class="data row3 col0">2016-01-07</td>

<td id="T_95355486_458c_11eb_8b46_1e00621e9144row3_col1" class="data row3 col1">0.056928</td>

<td id="T_95355486_458c_11eb_8b46_1e00621e9144row3_col2" class="data row3 col2">0.055757</td>

<td id="T_95355486_458c_11eb_8b46_1e00621e9144row3_col3" class="data row3 col3">0.054682</td>

</tr>

<tr>

<th id="T_95355486_458c_11eb_8b46_1e00621e9144level0_row4" class="row_heading level0 row4">Friday</th>

<td id="T_95355486_458c_11eb_8b46_1e00621e9144row4_col0" class="data row4 col0">2016-01-01</td>

<td id="T_95355486_458c_11eb_8b46_1e00621e9144row4_col1" class="data row4 col1">0.057957</td>

<td id="T_95355486_458c_11eb_8b46_1e00621e9144row4_col2" class="data row4 col2">0.056757</td>

<td id="T_95355486_458c_11eb_8b46_1e00621e9144row4_col3" class="data row4 col3">0.055659</td>

</tr>

<tr>

<th id="T_95355486_458c_11eb_8b46_1e00621e9144level0_row5" class="row_heading level0 row5">Saturday</th>

<td id="T_95355486_458c_11eb_8b46_1e00621e9144row5_col0" class="data row5 col0">2016-01-02</td>

<td id="T_95355486_458c_11eb_8b46_1e00621e9144row5_col1" class="data row5 col1">0.057374</td>

<td id="T_95355486_458c_11eb_8b46_1e00621e9144row5_col2" class="data row5 col2">0.056399</td>

<td id="T_95355486_458c_11eb_8b46_1e00621e9144row5_col3" class="data row5 col3">0.055481</td>

</tr>

<tr>

<th id="T_95355486_458c_11eb_8b46_1e00621e9144level0_row6" class="row_heading level0 row6">Sunday</th>

<td id="T_95355486_458c_11eb_8b46_1e00621e9144row6_col0" class="data row6 col0">2016-01-03</td>

<td id="T_95355486_458c_11eb_8b46_1e00621e9144row6_col1" class="data row6 col1">0.057134</td>

<td id="T_95355486_458c_11eb_8b46_1e00621e9144row6_col2" class="data row6 col2">0.056200</td>

<td id="T_95355486_458c_11eb_8b46_1e00621e9144row6_col3" class="data row6 col3">0.055315</td>

</tr>

</tbody>

</table>

</div>

</div>

</div>

</div>

</div>

<div class="jp-Cell jp-CodeCell jp-Notebook-cell   ">

<div class="jp-Cell-inputWrapper">

<div class="jp-InputArea jp-Cell-inputArea">

<div class="jp-InputPrompt jp-InputArea-prompt">In [8]:</div>

<div class="jp-CodeMirrorEditor jp-Editor jp-InputArea-editor" data-type="inline">

<div class="CodeMirror cm-s-jupyter">

<div class=" highlight hl-ipython3">

<pre><span></span><span class="c1"># 2017 Jan 1st - today</span>
<span class="n">day_charts</span> <span class="o">=</span> <span class="n">seperate_into_weekdays</span><span class="p">(</span><span class="n">historical_data</span><span class="p">,</span> <span class="n">start_date</span><span class="o">=</span><span class="n">datetime</span><span class="o">.</span><span class="n">datetime</span><span class="p">(</span><span class="mi">2017</span><span class="p">,</span> <span class="mi">1</span><span class="p">,</span> <span class="mi">1</span><span class="p">))</span>
<span class="n">day_of_week_vals</span> <span class="o">=</span> <span class="n">get_average</span><span class="p">(</span><span class="n">day_charts</span><span class="p">)</span>
<span class="n">show_df</span><span class="p">(</span><span class="n">day_of_week_vals</span><span class="p">)</span>
</pre>

</div>

</div>

</div>

</div>

</div>

<div class="jp-Cell-outputWrapper">

<div class="jp-OutputArea jp-Cell-outputArea">

<div class="jp-OutputArea-child">

<div class="jp-OutputPrompt jp-OutputArea-prompt">Out[8]:</div>

<div class="jp-RenderedHTMLCommon jp-RenderedHTML jp-OutputArea-output jp-OutputArea-executeResult" data-mime-type="text/html"><style type="text/css">#T_953930ec_458c_11eb_8b46_1e00621e9144row0_col1{ background-color: #78c679; color: #000000; }#T_953930ec_458c_11eb_8b46_1e00621e9144row0_col2{ background-color: #7fc97f; color: #000000; }#T_953930ec_458c_11eb_8b46_1e00621e9144row0_col3{ background-color: #62bb6d; color: #000000; }#T_953930ec_458c_11eb_8b46_1e00621e9144row1_col1{ background-color: #f4fbf2; color: #000000; }#T_953930ec_458c_11eb_8b46_1e00621e9144row1_col2{ background-color: #f2faef; color: #000000; }#T_953930ec_458c_11eb_8b46_1e00621e9144row1_col3{ background-color: #b6e2af; color: #000000; }#T_953930ec_458c_11eb_8b46_1e00621e9144row2_col1{ background-color: #bae3b3; color: #000000; }#T_953930ec_458c_11eb_8b46_1e00621e9144row2_col2{ background-color: #e7f6e3; color: #000000; }#T_953930ec_458c_11eb_8b46_1e00621e9144row2_col3{ background-color: #caeac3; color: #000000; }#T_953930ec_458c_11eb_8b46_1e00621e9144row3_col1{ background-color: #6ec173; color: #000000; }#T_953930ec_458c_11eb_8b46_1e00621e9144row3_col2,#T_953930ec_458c_11eb_8b46_1e00621e9144row3_col3,#T_953930ec_458c_11eb_8b46_1e00621e9144row5_col1{ background-color: #f7fcf5; color: #000000; }#T_953930ec_458c_11eb_8b46_1e00621e9144row4_col1,#T_953930ec_458c_11eb_8b46_1e00621e9144row6_col2,#T_953930ec_458c_11eb_8b46_1e00621e9144row6_col3{ background-color: #00441b; color: #f1f1f1; }#T_953930ec_458c_11eb_8b46_1e00621e9144row4_col2{ background-color: #6bc072; color: #000000; }#T_953930ec_458c_11eb_8b46_1e00621e9144row4_col3{ background-color: #abdda5; color: #000000; }#T_953930ec_458c_11eb_8b46_1e00621e9144row5_col2{ background-color: #e6f5e1; color: #000000; }#T_953930ec_458c_11eb_8b46_1e00621e9144row5_col3{ background-color: #90d18d; color: #000000; }#T_953930ec_458c_11eb_8b46_1e00621e9144row6_col1{ background-color: #1a843f; color: #000000; }</style>

<table id="T_953930ec_458c_11eb_8b46_1e00621e9144">

<thead>

<tr>

<th class="blank level0"></th>

<th class="col_heading level0 col0">start</th>

<th class="col_heading level0 col1">average_btc_at_lowest_cost</th>

<th class="col_heading level0 col2">average_btc_at_average_cost</th>

<th class="col_heading level0 col3">average_btc_at_highest_cost</th>

</tr>

</thead>

<tbody>

<tr>

<th id="T_953930ec_458c_11eb_8b46_1e00621e9144level0_row0" class="row_heading level0 row0">Monday</th>

<td id="T_953930ec_458c_11eb_8b46_1e00621e9144row0_col0" class="data row0 col0">2017-01-02</td>

<td id="T_953930ec_458c_11eb_8b46_1e00621e9144row0_col1" class="data row0 col1">0.023452</td>

<td id="T_953930ec_458c_11eb_8b46_1e00621e9144row0_col2" class="data row0 col2">0.022829</td>

<td id="T_953930ec_458c_11eb_8b46_1e00621e9144row0_col3" class="data row0 col3">0.022255</td>

</tr>

<tr>

<th id="T_953930ec_458c_11eb_8b46_1e00621e9144level0_row1" class="row_heading level0 row1">Tuesday</th>

<td id="T_953930ec_458c_11eb_8b46_1e00621e9144row1_col0" class="data row1 col0">2017-01-03</td>

<td id="T_953930ec_458c_11eb_8b46_1e00621e9144row1_col1" class="data row1 col1">0.023282</td>

<td id="T_953930ec_458c_11eb_8b46_1e00621e9144row1_col2" class="data row1 col2">0.022682</td>

<td id="T_953930ec_458c_11eb_8b46_1e00621e9144row1_col3" class="data row1 col3">0.022126</td>

</tr>

<tr>

<th id="T_953930ec_458c_11eb_8b46_1e00621e9144level0_row2" class="row_heading level0 row2">Wednesday</th>

<td id="T_953930ec_458c_11eb_8b46_1e00621e9144row2_col0" class="data row2 col0">2017-01-04</td>

<td id="T_953930ec_458c_11eb_8b46_1e00621e9144row2_col1" class="data row2 col1">0.023380</td>

<td id="T_953930ec_458c_11eb_8b46_1e00621e9144row2_col2" class="data row2 col2">0.022707</td>

<td id="T_953930ec_458c_11eb_8b46_1e00621e9144row2_col3" class="data row2 col3">0.022091</td>

</tr>

<tr>

<th id="T_953930ec_458c_11eb_8b46_1e00621e9144level0_row3" class="row_heading level0 row3">Thursday</th>

<td id="T_953930ec_458c_11eb_8b46_1e00621e9144row3_col0" class="data row3 col0">2017-01-05</td>

<td id="T_953930ec_458c_11eb_8b46_1e00621e9144row3_col1" class="data row3 col1">0.023461</td>

<td id="T_953930ec_458c_11eb_8b46_1e00621e9144row3_col2" class="data row3 col2">0.022669</td>

<td id="T_953930ec_458c_11eb_8b46_1e00621e9144row3_col3" class="data row3 col3">0.021962</td>

</tr>

<tr>

<th id="T_953930ec_458c_11eb_8b46_1e00621e9144level0_row4" class="row_heading level0 row4">Friday</th>

<td id="T_953930ec_458c_11eb_8b46_1e00621e9144row4_col0" class="data row4 col0">2017-01-06</td>

<td id="T_953930ec_458c_11eb_8b46_1e00621e9144row4_col1" class="data row4 col1">0.023637</td>

<td id="T_953930ec_458c_11eb_8b46_1e00621e9144row4_col2" class="data row4 col2">0.022846</td>

<td id="T_953930ec_458c_11eb_8b46_1e00621e9144row4_col3" class="data row4 col3">0.022145</td>

</tr>

<tr>

<th id="T_953930ec_458c_11eb_8b46_1e00621e9144level0_row5" class="row_heading level0 row5">Saturday</th>

<td id="T_953930ec_458c_11eb_8b46_1e00621e9144row5_col0" class="data row5 col0">2017-01-07</td>

<td id="T_953930ec_458c_11eb_8b46_1e00621e9144row5_col1" class="data row5 col1">0.023274</td>

<td id="T_953930ec_458c_11eb_8b46_1e00621e9144row5_col2" class="data row5 col2">0.022710</td>

<td id="T_953930ec_458c_11eb_8b46_1e00621e9144row5_col3" class="data row5 col3">0.022189</td>

</tr>

<tr>

<th id="T_953930ec_458c_11eb_8b46_1e00621e9144level0_row6" class="row_heading level0 row6">Sunday</th>

<td id="T_953930ec_458c_11eb_8b46_1e00621e9144row6_col0" class="data row6 col0">2017-01-01</td>

<td id="T_953930ec_458c_11eb_8b46_1e00621e9144row6_col1" class="data row6 col1">0.023557</td>

<td id="T_953930ec_458c_11eb_8b46_1e00621e9144row6_col2" class="data row6 col2">0.023009</td>

<td id="T_953930ec_458c_11eb_8b46_1e00621e9144row6_col3" class="data row6 col3">0.022498</td>

</tr>

</tbody>

</table>

</div>

</div>

</div>

</div>

</div>

<div class="jp-Cell jp-CodeCell jp-Notebook-cell   ">

<div class="jp-Cell-inputWrapper">

<div class="jp-InputArea jp-Cell-inputArea">

<div class="jp-InputPrompt jp-InputArea-prompt">In [9]:</div>

<div class="jp-CodeMirrorEditor jp-Editor jp-InputArea-editor" data-type="inline">

<div class="CodeMirror cm-s-jupyter">

<div class=" highlight hl-ipython3">

<pre><span></span><span class="c1"># 2018 Jan 1st - today</span>
<span class="n">day_charts</span> <span class="o">=</span> <span class="n">seperate_into_weekdays</span><span class="p">(</span><span class="n">historical_data</span><span class="p">,</span> <span class="n">start_date</span><span class="o">=</span><span class="n">datetime</span><span class="o">.</span><span class="n">datetime</span><span class="p">(</span><span class="mi">2018</span><span class="p">,</span> <span class="mi">1</span><span class="p">,</span> <span class="mi">1</span><span class="p">))</span>
<span class="n">day_of_week_vals</span> <span class="o">=</span> <span class="n">get_average</span><span class="p">(</span><span class="n">day_charts</span><span class="p">)</span>
<span class="n">show_df</span><span class="p">(</span><span class="n">day_of_week_vals</span><span class="p">)</span>
</pre>

</div>

</div>

</div>

</div>

</div>

<div class="jp-Cell-outputWrapper">

<div class="jp-OutputArea jp-Cell-outputArea">

<div class="jp-OutputArea-child">

<div class="jp-OutputPrompt jp-OutputArea-prompt">Out[9]:</div>

<div class="jp-RenderedHTMLCommon jp-RenderedHTML jp-OutputArea-output jp-OutputArea-executeResult" data-mime-type="text/html"><style type="text/css">#T_953d259e_458c_11eb_8b46_1e00621e9144row0_col1{ background-color: #137d39; color: #f1f1f1; }#T_953d259e_458c_11eb_8b46_1e00621e9144row0_col2{ background-color: #7ac77b; color: #000000; }#T_953d259e_458c_11eb_8b46_1e00621e9144row0_col3,#T_953d259e_458c_11eb_8b46_1e00621e9144row5_col1,#T_953d259e_458c_11eb_8b46_1e00621e9144row5_col2{ background-color: #f7fcf5; color: #000000; }#T_953d259e_458c_11eb_8b46_1e00621e9144row1_col1{ background-color: #4eb264; color: #000000; }#T_953d259e_458c_11eb_8b46_1e00621e9144row1_col2{ background-color: #7cc87c; color: #000000; }#T_953d259e_458c_11eb_8b46_1e00621e9144row1_col3{ background-color: #8dd08a; color: #000000; }#T_953d259e_458c_11eb_8b46_1e00621e9144row2_col1{ background-color: #38a156; color: #000000; }#T_953d259e_458c_11eb_8b46_1e00621e9144row2_col2{ background-color: #6dc072; color: #000000; }#T_953d259e_458c_11eb_8b46_1e00621e9144row2_col3{ background-color: #a3da9d; color: #000000; }#T_953d259e_458c_11eb_8b46_1e00621e9144row3_col1{ background-color: #005723; color: #f1f1f1; }#T_953d259e_458c_11eb_8b46_1e00621e9144row3_col2{ background-color: #1d8640; color: #000000; }#T_953d259e_458c_11eb_8b46_1e00621e9144row3_col3{ background-color: #79c67a; color: #000000; }#T_953d259e_458c_11eb_8b46_1e00621e9144row4_col1,#T_953d259e_458c_11eb_8b46_1e00621e9144row4_col2,#T_953d259e_458c_11eb_8b46_1e00621e9144row4_col3{ background-color: #00441b; color: #f1f1f1; }#T_953d259e_458c_11eb_8b46_1e00621e9144row5_col3{ background-color: #99d595; color: #000000; }#T_953d259e_458c_11eb_8b46_1e00621e9144row6_col1{ background-color: #daf0d4; color: #000000; }#T_953d259e_458c_11eb_8b46_1e00621e9144row6_col2{ background-color: #f1faee; color: #000000; }#T_953d259e_458c_11eb_8b46_1e00621e9144row6_col3{ background-color: #e0f3db; color: #000000; }</style>

<table id="T_953d259e_458c_11eb_8b46_1e00621e9144">

<thead>

<tr>

<th class="blank level0"></th>

<th class="col_heading level0 col0">start</th>

<th class="col_heading level0 col1">average_btc_at_lowest_cost</th>

<th class="col_heading level0 col2">average_btc_at_average_cost</th>

<th class="col_heading level0 col3">average_btc_at_highest_cost</th>

</tr>

</thead>

<tbody>

<tr>

<th id="T_953d259e_458c_11eb_8b46_1e00621e9144level0_row0" class="row_heading level0 row0">Monday</th>

<td id="T_953d259e_458c_11eb_8b46_1e00621e9144row0_col0" class="data row0 col0">2018-01-01</td>

<td id="T_953d259e_458c_11eb_8b46_1e00621e9144row0_col1" class="data row0 col1">0.014049</td>

<td id="T_953d259e_458c_11eb_8b46_1e00621e9144row0_col2" class="data row0 col2">0.013636</td>

<td id="T_953d259e_458c_11eb_8b46_1e00621e9144row0_col3" class="data row0 col3">0.013259</td>

</tr>

<tr>

<th id="T_953d259e_458c_11eb_8b46_1e00621e9144level0_row1" class="row_heading level0 row1">Tuesday</th>

<td id="T_953d259e_458c_11eb_8b46_1e00621e9144row1_col0" class="data row1 col0">2018-01-02</td>

<td id="T_953d259e_458c_11eb_8b46_1e00621e9144row1_col1" class="data row1 col1">0.013997</td>

<td id="T_953d259e_458c_11eb_8b46_1e00621e9144row1_col2" class="data row1 col2">0.013635</td>

<td id="T_953d259e_458c_11eb_8b46_1e00621e9144row1_col3" class="data row1 col3">0.013303</td>

</tr>

<tr>

<th id="T_953d259e_458c_11eb_8b46_1e00621e9144level0_row2" class="row_heading level0 row2">Wednesday</th>

<td id="T_953d259e_458c_11eb_8b46_1e00621e9144row2_col0" class="data row2 col0">2018-01-03</td>

<td id="T_953d259e_458c_11eb_8b46_1e00621e9144row2_col1" class="data row2 col1">0.014014</td>

<td id="T_953d259e_458c_11eb_8b46_1e00621e9144row2_col2" class="data row2 col2">0.013641</td>

<td id="T_953d259e_458c_11eb_8b46_1e00621e9144row2_col3" class="data row2 col3">0.013297</td>

</tr>

<tr>

<th id="T_953d259e_458c_11eb_8b46_1e00621e9144level0_row3" class="row_heading level0 row3">Thursday</th>

<td id="T_953d259e_458c_11eb_8b46_1e00621e9144row3_col0" class="data row3 col0">2018-01-04</td>

<td id="T_953d259e_458c_11eb_8b46_1e00621e9144row3_col1" class="data row3 col1">0.014080</td>

<td id="T_953d259e_458c_11eb_8b46_1e00621e9144row3_col2" class="data row3 col2">0.013676</td>

<td id="T_953d259e_458c_11eb_8b46_1e00621e9144row3_col3" class="data row3 col3">0.013309</td>

</tr>

<tr>

<th id="T_953d259e_458c_11eb_8b46_1e00621e9144level0_row4" class="row_heading level0 row4">Friday</th>

<td id="T_953d259e_458c_11eb_8b46_1e00621e9144row4_col0" class="data row4 col0">2018-01-05</td>

<td id="T_953d259e_458c_11eb_8b46_1e00621e9144row4_col1" class="data row4 col1">0.014095</td>

<td id="T_953d259e_458c_11eb_8b46_1e00621e9144row4_col2" class="data row4 col2">0.013708</td>

<td id="T_953d259e_458c_11eb_8b46_1e00621e9144row4_col3" class="data row4 col3">0.013361</td>

</tr>

<tr>

<th id="T_953d259e_458c_11eb_8b46_1e00621e9144level0_row5" class="row_heading level0 row5">Saturday</th>

<td id="T_953d259e_458c_11eb_8b46_1e00621e9144row5_col0" class="data row5 col0">2018-01-06</td>

<td id="T_953d259e_458c_11eb_8b46_1e00621e9144row5_col1" class="data row5 col1">0.013855</td>

<td id="T_953d259e_458c_11eb_8b46_1e00621e9144row5_col2" class="data row5 col2">0.013568</td>

<td id="T_953d259e_458c_11eb_8b46_1e00621e9144row5_col3" class="data row5 col3">0.013299</td>

</tr>

<tr>

<th id="T_953d259e_458c_11eb_8b46_1e00621e9144level0_row6" class="row_heading level0 row6">Sunday</th>

<td id="T_953d259e_458c_11eb_8b46_1e00621e9144row6_col0" class="data row6 col0">2018-01-07</td>

<td id="T_953d259e_458c_11eb_8b46_1e00621e9144row6_col1" class="data row6 col1">0.013897</td>

<td id="T_953d259e_458c_11eb_8b46_1e00621e9144row6_col2" class="data row6 col2">0.013574</td>

<td id="T_953d259e_458c_11eb_8b46_1e00621e9144row6_col3" class="data row6 col3">0.013274</td>

</tr>

</tbody>

</table>

</div>

</div>

</div>

</div>

</div>

<div class="jp-Cell jp-CodeCell jp-Notebook-cell   ">

<div class="jp-Cell-inputWrapper">

<div class="jp-InputArea jp-Cell-inputArea">

<div class="jp-InputPrompt jp-InputArea-prompt">In [10]:</div>

<div class="jp-CodeMirrorEditor jp-Editor jp-InputArea-editor" data-type="inline">

<div class="CodeMirror cm-s-jupyter">

<div class=" highlight hl-ipython3">

<pre><span></span><span class="c1"># 2019 Jan 1st - today</span>
<span class="n">day_charts</span> <span class="o">=</span> <span class="n">seperate_into_weekdays</span><span class="p">(</span><span class="n">historical_data</span><span class="p">,</span> <span class="n">start_date</span><span class="o">=</span><span class="n">datetime</span><span class="o">.</span><span class="n">datetime</span><span class="p">(</span><span class="mi">2019</span><span class="p">,</span> <span class="mi">1</span><span class="p">,</span> <span class="mi">1</span><span class="p">))</span>
<span class="n">day_of_week_vals</span> <span class="o">=</span> <span class="n">get_average</span><span class="p">(</span><span class="n">day_charts</span><span class="p">)</span>
<span class="n">show_df</span><span class="p">(</span><span class="n">day_of_week_vals</span><span class="p">)</span>
</pre>

</div>

</div>

</div>

</div>

</div>

<div class="jp-Cell-outputWrapper">

<div class="jp-OutputArea jp-Cell-outputArea">

<div class="jp-OutputArea-child">

<div class="jp-OutputPrompt jp-OutputArea-prompt">Out[10]:</div>

<div class="jp-RenderedHTMLCommon jp-RenderedHTML jp-OutputArea-output jp-OutputArea-executeResult" data-mime-type="text/html"><style type="text/css">#T_9540b57e_458c_11eb_8b46_1e00621e9144row0_col1{ background-color: #319a50; color: #000000; }#T_9540b57e_458c_11eb_8b46_1e00621e9144row0_col2{ background-color: #cbebc5; color: #000000; }#T_9540b57e_458c_11eb_8b46_1e00621e9144row0_col3,#T_9540b57e_458c_11eb_8b46_1e00621e9144row5_col1,#T_9540b57e_458c_11eb_8b46_1e00621e9144row5_col2{ background-color: #f7fcf5; color: #000000; }#T_9540b57e_458c_11eb_8b46_1e00621e9144row1_col1{ background-color: #40aa5d; color: #000000; }#T_9540b57e_458c_11eb_8b46_1e00621e9144row1_col2{ background-color: #2e964d; color: #000000; }#T_9540b57e_458c_11eb_8b46_1e00621e9144row1_col3{ background-color: #006328; color: #f1f1f1; }#T_9540b57e_458c_11eb_8b46_1e00621e9144row2_col1{ background-color: #2b934b; color: #000000; }#T_9540b57e_458c_11eb_8b46_1e00621e9144row2_col2{ background-color: #218944; color: #000000; }#T_9540b57e_458c_11eb_8b46_1e00621e9144row2_col3{ background-color: #097532; color: #f1f1f1; }#T_9540b57e_458c_11eb_8b46_1e00621e9144row3_col1,#T_9540b57e_458c_11eb_8b46_1e00621e9144row4_col2,#T_9540b57e_458c_11eb_8b46_1e00621e9144row4_col3{ background-color: #00441b; color: #f1f1f1; }#T_9540b57e_458c_11eb_8b46_1e00621e9144row3_col2{ background-color: #17813d; color: #f1f1f1; }#T_9540b57e_458c_11eb_8b46_1e00621e9144row3_col3{ background-color: #63bc6e; color: #000000; }#T_9540b57e_458c_11eb_8b46_1e00621e9144row4_col1{ background-color: #004e1f; color: #f1f1f1; }#T_9540b57e_458c_11eb_8b46_1e00621e9144row5_col3{ background-color: #3ca559; color: #000000; }#T_9540b57e_458c_11eb_8b46_1e00621e9144row6_col1{ background-color: #b2e0ac; color: #000000; }#T_9540b57e_458c_11eb_8b46_1e00621e9144row6_col2{ background-color: #e7f6e3; color: #000000; }#T_9540b57e_458c_11eb_8b46_1e00621e9144row6_col3{ background-color: #a8dca2; color: #000000; }</style>

<table id="T_9540b57e_458c_11eb_8b46_1e00621e9144">

<thead>

<tr>

<th class="blank level0"></th>

<th class="col_heading level0 col0">start</th>

<th class="col_heading level0 col1">average_btc_at_lowest_cost</th>

<th class="col_heading level0 col2">average_btc_at_average_cost</th>

<th class="col_heading level0 col3">average_btc_at_highest_cost</th>

</tr>

</thead>

<tbody>

<tr>

<th id="T_9540b57e_458c_11eb_8b46_1e00621e9144level0_row0" class="row_heading level0 row0">Monday</th>

<td id="T_9540b57e_458c_11eb_8b46_1e00621e9144row0_col0" class="data row0 col0">2019-01-07</td>

<td id="T_9540b57e_458c_11eb_8b46_1e00621e9144row0_col1" class="data row0 col1">0.013456</td>

<td id="T_9540b57e_458c_11eb_8b46_1e00621e9144row0_col2" class="data row0 col2">0.013090</td>

<td id="T_9540b57e_458c_11eb_8b46_1e00621e9144row0_col3" class="data row0 col3">0.012752</td>

</tr>

<tr>

<th id="T_9540b57e_458c_11eb_8b46_1e00621e9144level0_row1" class="row_heading level0 row1">Tuesday</th>

<td id="T_9540b57e_458c_11eb_8b46_1e00621e9144row1_col0" class="data row1 col0">2019-01-01</td>

<td id="T_9540b57e_458c_11eb_8b46_1e00621e9144row1_col1" class="data row1 col1">0.013443</td>

<td id="T_9540b57e_458c_11eb_8b46_1e00621e9144row1_col2" class="data row1 col2">0.013142</td>

<td id="T_9540b57e_458c_11eb_8b46_1e00621e9144row1_col3" class="data row1 col3">0.012862</td>

</tr>

<tr>

<th id="T_9540b57e_458c_11eb_8b46_1e00621e9144level0_row2" class="row_heading level0 row2">Wednesday</th>

<td id="T_9540b57e_458c_11eb_8b46_1e00621e9144row2_col0" class="data row2 col0">2019-01-02</td>

<td id="T_9540b57e_458c_11eb_8b46_1e00621e9144row2_col1" class="data row2 col1">0.013462</td>

<td id="T_9540b57e_458c_11eb_8b46_1e00621e9144row2_col2" class="data row2 col2">0.013148</td>

<td id="T_9540b57e_458c_11eb_8b46_1e00621e9144row2_col3" class="data row2 col3">0.012854</td>

</tr>

<tr>

<th id="T_9540b57e_458c_11eb_8b46_1e00621e9144level0_row3" class="row_heading level0 row3">Thursday</th>

<td id="T_9540b57e_458c_11eb_8b46_1e00621e9144row3_col0" class="data row3 col0">2019-01-03</td>

<td id="T_9540b57e_458c_11eb_8b46_1e00621e9144row3_col1" class="data row3 col1">0.013521</td>

<td id="T_9540b57e_458c_11eb_8b46_1e00621e9144row3_col2" class="data row3 col2">0.013152</td>

<td id="T_9540b57e_458c_11eb_8b46_1e00621e9144row3_col3" class="data row3 col3">0.012817</td>

</tr>

<tr>

<th id="T_9540b57e_458c_11eb_8b46_1e00621e9144level0_row4" class="row_heading level0 row4">Friday</th>

<td id="T_9540b57e_458c_11eb_8b46_1e00621e9144row4_col0" class="data row4 col0">2019-01-04</td>

<td id="T_9540b57e_458c_11eb_8b46_1e00621e9144row4_col1" class="data row4 col1">0.013515</td>

<td id="T_9540b57e_458c_11eb_8b46_1e00621e9144row4_col2" class="data row4 col2">0.013175</td>

<td id="T_9540b57e_458c_11eb_8b46_1e00621e9144row4_col3" class="data row4 col3">0.012874</td>

</tr>

<tr>

<th id="T_9540b57e_458c_11eb_8b46_1e00621e9144level0_row5" class="row_heading level0 row5">Saturday</th>

<td id="T_9540b57e_458c_11eb_8b46_1e00621e9144row5_col0" class="data row5 col0">2019-01-05</td>

<td id="T_9540b57e_458c_11eb_8b46_1e00621e9144row5_col1" class="data row5 col1">0.013311</td>

<td id="T_9540b57e_458c_11eb_8b46_1e00621e9144row5_col2" class="data row5 col2">0.013064</td>

<td id="T_9540b57e_458c_11eb_8b46_1e00621e9144row5_col3" class="data row5 col3">0.012830</td>

</tr>

<tr>

<th id="T_9540b57e_458c_11eb_8b46_1e00621e9144level0_row6" class="row_heading level0 row6">Sunday</th>

<td id="T_9540b57e_458c_11eb_8b46_1e00621e9144row6_col0" class="data row6 col0">2019-01-06</td>

<td id="T_9540b57e_458c_11eb_8b46_1e00621e9144row6_col1" class="data row6 col1">0.013378</td>

<td id="T_9540b57e_458c_11eb_8b46_1e00621e9144row6_col2" class="data row6 col2">0.013076</td>

<td id="T_9540b57e_458c_11eb_8b46_1e00621e9144row6_col3" class="data row6 col3">0.012795</td>

</tr>

</tbody>

</table>

</div>

</div>

</div>

</div>

</div>

<div class="jp-Cell jp-CodeCell jp-Notebook-cell   ">

<div class="jp-Cell-inputWrapper">

<div class="jp-InputArea jp-Cell-inputArea">

<div class="jp-InputPrompt jp-InputArea-prompt">In [11]:</div>

<div class="jp-CodeMirrorEditor jp-Editor jp-InputArea-editor" data-type="inline">

<div class="CodeMirror cm-s-jupyter">

<div class=" highlight hl-ipython3">

<pre><span></span><span class="c1"># 2020 Jan 1st - today</span>
<span class="n">day_charts</span> <span class="o">=</span> <span class="n">seperate_into_weekdays</span><span class="p">(</span><span class="n">historical_data</span><span class="p">,</span> <span class="n">start_date</span><span class="o">=</span><span class="n">datetime</span><span class="o">.</span><span class="n">datetime</span><span class="p">(</span><span class="mi">2020</span><span class="p">,</span> <span class="mi">1</span><span class="p">,</span> <span class="mi">1</span><span class="p">))</span>
<span class="n">day_of_week_vals</span> <span class="o">=</span> <span class="n">get_average</span><span class="p">(</span><span class="n">day_charts</span><span class="p">)</span>
<span class="n">show_df</span><span class="p">(</span><span class="n">day_of_week_vals</span><span class="p">)</span>
</pre>

</div>

</div>

</div>

</div>

</div>

<div class="jp-Cell-outputWrapper">

<div class="jp-OutputArea jp-Cell-outputArea">

<div class="jp-OutputArea-child">

<div class="jp-OutputPrompt jp-OutputArea-prompt">Out[11]:</div>

<div class="jp-RenderedHTMLCommon jp-RenderedHTML jp-OutputArea-output jp-OutputArea-executeResult" data-mime-type="text/html"><style type="text/css">#T_954482ee_458c_11eb_8b46_1e00621e9144row0_col1{ background-color: #005b25; color: #f1f1f1; }#T_954482ee_458c_11eb_8b46_1e00621e9144row0_col2{ background-color: #006529; color: #f1f1f1; }#T_954482ee_458c_11eb_8b46_1e00621e9144row0_col3{ background-color: #7cc87c; color: #000000; }#T_954482ee_458c_11eb_8b46_1e00621e9144row1_col1,#T_954482ee_458c_11eb_8b46_1e00621e9144row1_col2,#T_954482ee_458c_11eb_8b46_1e00621e9144row3_col3{ background-color: #f7fcf5; color: #000000; }#T_954482ee_458c_11eb_8b46_1e00621e9144row1_col3{ background-color: #d3eecd; color: #000000; }#T_954482ee_458c_11eb_8b46_1e00621e9144row2_col1,#T_954482ee_458c_11eb_8b46_1e00621e9144row5_col2{ background-color: #3aa357; color: #000000; }#T_954482ee_458c_11eb_8b46_1e00621e9144row2_col2{ background-color: #005a24; color: #f1f1f1; }#T_954482ee_458c_11eb_8b46_1e00621e9144row2_col3{ background-color: #016e2d; color: #f1f1f1; }#T_954482ee_458c_11eb_8b46_1e00621e9144row3_col1{ background-color: #006d2c; color: #f1f1f1; }#T_954482ee_458c_11eb_8b46_1e00621e9144row3_col2{ background-color: #6bc072; color: #000000; }#T_954482ee_458c_11eb_8b46_1e00621e9144row4_col1,#T_954482ee_458c_11eb_8b46_1e00621e9144row4_col2,#T_954482ee_458c_11eb_8b46_1e00621e9144row5_col3{ background-color: #00441b; color: #f1f1f1; }#T_954482ee_458c_11eb_8b46_1e00621e9144row4_col3{ background-color: #29914a; color: #000000; }#T_954482ee_458c_11eb_8b46_1e00621e9144row5_col1{ background-color: #ceecc8; color: #000000; }#T_954482ee_458c_11eb_8b46_1e00621e9144row6_col1{ background-color: #55b567; color: #000000; }#T_954482ee_458c_11eb_8b46_1e00621e9144row6_col2,#T_954482ee_458c_11eb_8b46_1e00621e9144row6_col3{ background-color: #0e7936; color: #f1f1f1; }</style>

<table id="T_954482ee_458c_11eb_8b46_1e00621e9144">

<thead>

<tr>

<th class="blank level0"></th>

<th class="col_heading level0 col0">start</th>

<th class="col_heading level0 col1">average_btc_at_lowest_cost</th>

<th class="col_heading level0 col2">average_btc_at_average_cost</th>

<th class="col_heading level0 col3">average_btc_at_highest_cost</th>

</tr>

</thead>

<tbody>

<tr>

<th id="T_954482ee_458c_11eb_8b46_1e00621e9144level0_row0" class="row_heading level0 row0">Monday</th>

<td id="T_954482ee_458c_11eb_8b46_1e00621e9144row0_col0" class="data row0 col0">2020-01-06</td>

<td id="T_954482ee_458c_11eb_8b46_1e00621e9144row0_col1" class="data row0 col1">0.010556</td>

<td id="T_954482ee_458c_11eb_8b46_1e00621e9144row0_col2" class="data row0 col2">0.010236</td>

<td id="T_954482ee_458c_11eb_8b46_1e00621e9144row0_col3" class="data row0 col3">0.009944</td>

</tr>

<tr>

<th id="T_954482ee_458c_11eb_8b46_1e00621e9144level0_row1" class="row_heading level0 row1">Tuesday</th>

<td id="T_954482ee_458c_11eb_8b46_1e00621e9144row1_col0" class="data row1 col0">2020-01-07</td>

<td id="T_954482ee_458c_11eb_8b46_1e00621e9144row1_col1" class="data row1 col1">0.010350</td>

<td id="T_954482ee_458c_11eb_8b46_1e00621e9144row1_col2" class="data row1 col2">0.010120</td>

<td id="T_954482ee_458c_11eb_8b46_1e00621e9144row1_col3" class="data row1 col3">0.009903</td>

</tr>

<tr>

<th id="T_954482ee_458c_11eb_8b46_1e00621e9144level0_row2" class="row_heading level0 row2">Wednesday</th>

<td id="T_954482ee_458c_11eb_8b46_1e00621e9144row2_col0" class="data row2 col0">2020-01-01</td>

<td id="T_954482ee_458c_11eb_8b46_1e00621e9144row2_col1" class="data row2 col1">0.010496</td>

<td id="T_954482ee_458c_11eb_8b46_1e00621e9144row2_col2" class="data row2 col2">0.010241</td>

<td id="T_954482ee_458c_11eb_8b46_1e00621e9144row2_col3" class="data row2 col3">0.010002</td>

</tr>

<tr>

<th id="T_954482ee_458c_11eb_8b46_1e00621e9144level0_row3" class="row_heading level0 row3">Thursday</th>

<td id="T_954482ee_458c_11eb_8b46_1e00621e9144row3_col0" class="data row3 col0">2020-01-02</td>

<td id="T_954482ee_458c_11eb_8b46_1e00621e9144row3_col1" class="data row3 col1">0.010544</td>

<td id="T_954482ee_458c_11eb_8b46_1e00621e9144row3_col2" class="data row3 col2">0.010188</td>

<td id="T_954482ee_458c_11eb_8b46_1e00621e9144row3_col3" class="data row3 col3">0.009873</td>

</tr>

<tr>

<th id="T_954482ee_458c_11eb_8b46_1e00621e9144level0_row4" class="row_heading level0 row4">Friday</th>

<td id="T_954482ee_458c_11eb_8b46_1e00621e9144row4_col0" class="data row4 col0">2020-01-03</td>

<td id="T_954482ee_458c_11eb_8b46_1e00621e9144row4_col1" class="data row4 col1">0.010572</td>

<td id="T_954482ee_458c_11eb_8b46_1e00621e9144row4_col2" class="data row4 col2">0.010250</td>

<td id="T_954482ee_458c_11eb_8b46_1e00621e9144row4_col3" class="data row4 col3">0.009981</td>

</tr>

<tr>

<th id="T_954482ee_458c_11eb_8b46_1e00621e9144level0_row5" class="row_heading level0 row5">Saturday</th>

<td id="T_954482ee_458c_11eb_8b46_1e00621e9144row5_col0" class="data row5 col0">2020-01-04</td>

<td id="T_954482ee_458c_11eb_8b46_1e00621e9144row5_col1" class="data row5 col1">0.010399</td>

<td id="T_954482ee_458c_11eb_8b46_1e00621e9144row5_col2" class="data row5 col2">0.010205</td>

<td id="T_954482ee_458c_11eb_8b46_1e00621e9144row5_col3" class="data row5 col3">0.010022</td>

</tr>

<tr>

<th id="T_954482ee_458c_11eb_8b46_1e00621e9144level0_row6" class="row_heading level0 row6">Sunday</th>

<td id="T_954482ee_458c_11eb_8b46_1e00621e9144row6_col0" class="data row6 col0">2020-01-05</td>

<td id="T_954482ee_458c_11eb_8b46_1e00621e9144row6_col1" class="data row6 col1">0.010478</td>

<td id="T_954482ee_458c_11eb_8b46_1e00621e9144row6_col2" class="data row6 col2">0.010227</td>

<td id="T_954482ee_458c_11eb_8b46_1e00621e9144row6_col3" class="data row6 col3">0.009995</td>

</tr>

</tbody>

</table>

</div>

</div>

</div>

</div>

</div>

<div class="jp-Cell-inputWrapper">

<div class="jp-RenderedHTMLCommon jp-RenderedMarkdown jp-MarkdownOutput " data-mime-type="text/markdown">

#### Apparently Friday is the best day to buy now.[¶](#Apparently-Friday-is-the-best-day-to-buy-now.)

</div>

</div>