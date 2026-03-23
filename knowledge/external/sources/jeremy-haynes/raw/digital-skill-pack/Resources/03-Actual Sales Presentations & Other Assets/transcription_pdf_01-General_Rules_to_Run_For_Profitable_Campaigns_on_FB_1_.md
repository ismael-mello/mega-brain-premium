# Extração: 01-General_Rules_to_Run_For_Profitable_Campaigns_on_FB_1_

- **Fonte:** 01-General_Rules_to_Run_For_Profitable_Campaigns_on_FB_1_.pdf
- **Tipo:** PDF
- **Páginas:** 0
- **Tamanho:** 0.11 MB

---

When running rules, it’s important to consider when the rules run, and what other rules might
conflict with this. Think with the below rules tactically, but also be sure to look at all rules running
from above to ensure you don’t have anything conflicting with another rule already set up or
implemented.
New users begin with the pause rules. They are probably the easiest to set up and the first to
bring value.
The hardest part is to define that best moment when you are completely certain about ad
inefficiency. May not seems tricky at a first glance, but pausing ads too early is just as bad as
too late, because you may stop a good ad that just didn’t have enough time to prove it.
Let's look at the most common pause scenarios.
Ad set or ad has already spent enough money but didn’t bring a single conversion.
Tip: You can set up similar rules for other metrics, such as CPC is too high, or
AddToCart is too expensive. This could be an earlier indicator of poor performance.
The other rule could check if the ad or ad set is performing well at first but starts to decline
over time:
Pause ad set if
Spend > $200 and Purchases > 0 and Cost per Purchase > $50
Tip: Set rules with different timeframes to monitor both longterm and shortterm
performance.
For example, check Cost per Purchase for the last 7 days and for the last 3 days including
today. This is especially important for ad sets that run on large budgets and have a lot of
conversions. By checking recent statistics, such as last 3 days, you'll be able to see if a great ad
set has recently gone bad.
Instead of Purchase, you can track any event – Click, Lead, Install, Checkout Initiated, Custom
Events, and etc. In other words, you need to select the metric that you can get enough valid
statistical data for in the selected time frame.
Use ROAS
If you run an e-commerce business where prices and quantities vary or an app with monthly and
yearly subscription plans – ROAS is the right metric to track.
Return on Ad Spend (ROAS) = Purchase Revenue / Spend
www.getwsodo.com	www.getwsodo.com

-- 1 of 4 --

The lowest point of this metric (the worst) needs to be defined empirically. Usually, business
model works if you earned 3x times more than you spent on an ad. In that case, you can make
the following rule:
Pause ad set if
Spend > $70 and ROAS < 3
Which means that for the $70 spent, you expect to get $210 in revenue.
Similar for mobile apps:
Pause ad set if
Spend > $100 and App Purchase Revenue < 3 * Spend
The time a customer needs to convert varies – oftentimes an ad set has 0 purchases, you
pause it and then a few people convert. You might have noticed it in your ad account as well.
This is especially true for zero conversions rules that we discussed first.
In most cases, you'd want to turn such ads back on:
Start ad set if
Cost per Purchase < $50 (last 12 hrs) and Purchases > 0 (last 12 hrs)
Tip: Do not exceed a 12-hour timeframe for lower $ conversions, use longer time frames
for higher product or service values or when buying cycles is longer relative to what’s
being sold.
If the ad set was on pause longer than that it loses some optimization data and might not work
well anymore.
Here is another example why you'd want to unpause an ad set. Say, a rule checks daily metrics
and pauses ad sets if Cost per Result is too high. But Facebook is infamous for its volatility and
even an exceptional ad can have a bad day. So you'd want to relaunch it the next day if it's last
7 days metrics are good.
This rule will unpause those ad sets that are off right now, were paused yesterday, but
performed well in the last 7 days.
Start ad set if
Impressions < 100 (yesterday) and Cost per Purchase < $50 (Last 7 days) and Purchases > 1
(Last 7 days)
You need to set up a custom schedule for such a rule so that it runs only at midnight.
www.getwsodo.com	www.getwsodo.com

-- 2 of 4 --

Tip: If you run pause and unpause rules make sure they don’t contradict.
As with any other investment, not only you need to pause unprofitable campaigns, but also
invest more in the best-performing ones.
Conditions are similar to the pause rules, but do the opposite.
Set budget to $500 once a day if
Purchases > 2 and Cost per Purchase < $30
Tip: For all scaling rules set a condition Time less than 12p.m. so that the budget change
does not happen too late in the day, which may affect pacing.
You can also have separate rules for when the metrics are good and when they are great – and
increase the budget correspondingly:
If your maximum cost per acquisition is $30, then you can set up the following rules:
Increase budget by 20% once a day if
Purchases > 5 and Cost per Purchase < $30 and Cost per Purchase >= $20
But if it turns out you have a killer ad set with CPA < $20, you would definitely want to pour even
more money into it.
Increase Budget by 100% once a day if
Purchases > 5 and Cost per Purchase < $20
Tip: Wait until you have at least 5-10 conversions today before doubling the budget,
otherwise you can shoot yourself in the foot.
Similarly, you can set up rules based on ROAS.
Increase Budget by 100% once a day if
Purchases > 5 and ROAS > 3
You can also add ‘increase budget’ condition only when you have already spent half of your
daily budget.
Increase Budget by 50% once a day If
ROAS >3 and Spend (today) > 0.5 * Daily Budget
www.getwsodo.com	www.getwsodo.com

-- 3 of 4 --

One more automation strategy is bid management. In most cases, Facebook does a pretty
decent job of optimizing the bid to get you the lowest cost for result. But if you want to control
your cost per optimization event in some way, we suggest adding a bid cap or setting target
cost.
Tip: Set your daily budget at least 5 times higher than your cap so you're well-positioned
to get around 50 optimization events a week.
The following rule will increase the bid if it is too low for an ad to go into the auction:
Increase bid by $0.5 every 2 hours
Impressions < 100 (last 2 hrs)
If one of your ads is doing really well, you can prioritize it in the auction by setting a higher bid
for this exact ad:
Increase ad bid by $0.25 once a day
Cost Per Lead > $10 (Today) and Leads >= 2 (Today)
Cost per Lead < Cost per Lead (ad set level)
www.getwsodo.com	www.getwsodo.com

-- 4 of 4 --

