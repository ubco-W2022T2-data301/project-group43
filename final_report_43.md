**Introduction**

Our research focuses on the top 1000 fastest-growing enterprises in Europe. As a group of primarily economics majors, we are very interested in following economic growth in different parts of the world and analyzing the elements that fuel this growth in the fastest-growing companies. We want to provide essential knowledge on the trends and patterns of the fastest-growing companies by utilizing data on Europe's fastest-growing enterprises. We aim to show the main growth forces to assist people in achieving their entrepreneurial goals. Analyzing the data of these organizations and finding the strategies and methods that have enabled their success is the objective of our project. As aspiring business owners, we need to understand what makes successful companies and how we can learn from them to help us in our own lives.

**How does the number of employees in small enterprises affect revenue and annual growth rates in Europe?** - **Elliott**

We were using data from the top thousand fastest-growing companies. I processed data to create visualizations that helped me answer my research question. I chose to focus specifically on small companies. In Europe, this is defined by the workforce size, and small enterprises consist of 10-50 employees. I began my analysis by removing entries with companies that had above or below this range of employees. I removed nan entries and created a new column that showed the employment growth rate of the company. With my newly processed data, I was well-armed to answer my research question.

Conducting my EDA, I expected a positive linear relationship between employment and revenue since I assumed a larger workforce could accomplish more or more significant tasks to generate more revenue. After narrowing in on small businesses, that relationship wasn't apparent.

I created a hexbin plot showing the relationship between compound annual growth rates (CAGR) and the firm size in 2020. ![Employee count and annual growth](https://github.com/ubco-W2022T2-data301/project-group43/blob/main/images/CAGR_vs._%23employees.png). The plot shows that most of the fast-growing small businesses in 2020 had around 30 employees with a compound annual growth rate of approximately 50%. This plot lets us discover a "sweet spot" for the number of employees in a small business to grow fastest. For small businesses to reach a larger scale in Europe, the size of the team is critical. Too few employees and the growth rates don't seem exceedingly high; this is likely due to discrepancies in the workforce. Too many employees and the growth rates are frequently too high, which could result from too much labor investment, which takes away from investment in other areas of the company.

After discovering the relationship above, I created another hexbin relating the growth in employees from 2017-2020 with CAGR. ![Employee and Annual Growth Rates](https://github.com/ubco-W2022T2-data301/project-group43/blob/main/images/Growth_rates%20.png). It appears that most small enterprises increased by 40-70% from 2017 to 2020; this could explain the differences in the histograms in my analysis2 file. Firms that grew less than 25% don't surpass annual growth rates above 70%. Most data for very high annual growth (50%\<) rates lay in the 40-70% change in employee range.

**What are the factors that affect growth sectors among the top 1000 companies in Europe?** - **Sebastian**

We analyzed data from the top 1000 companies in Europe and I amed to find out which of the sectors that these comapnies come from are the fastest growing. From the parameters given to me I wanted to find out which of the sectors grow the fastest.

However while doing my EDA I realized I that my first question was easily answered with one of the first few graphs I made in my EDA. Here is the graph, ![CAGR VS Revenue Change]

I first wrangled my data and cleaned it up in a manner that leaves my with only relevant data that I needed to answer my research question, and added columns with data pulled from the other columns relevant to asnwering my questions. I added the columns "Change in Revenue" and "Change % in employees"

I created a Regplot to study the relationship between CAGR of a Sector and the change in revenue of all business in that particular sector. I found out that their was a very strong positve linear relationship between the two which tells me that for a particular sector to grow, increase in revenues of a particular sector is crucial. Here is the graph, ![CAGR VS Revenue Change]

I then created another Regplot to study the relationship between Change % of employees in businesses part of a particular sector and the growth rate of that particualr sector and also saw a strong positive linear relationship. So clearly a positve % increase in the number of employees in businesses in a particular sector is directly related to a higher CAGR. Here is the graph, ![CAGR VS Change % in Employees]

**Conclusion**

Sebastian - My investigation has led me to a number of conclusions. First off, there is a correlation between firm expansion in a given area and an uptick in earnings and compound annual growth rates. Second, an increase in the number of employees is positively correlated with the expansion of businesses in a given industry. Therefore, I think that raising revenue and staff numbers is the key to expanding an organisation, and industries with enterprises that show notable revenue growth and a shift in the workforce ratio are likely to see higher growth.

Elliott - After learning about data science and conducting analysis on our data set, I was able to draw the following conclusions from the fastest-growing small companies in Europe; firms with 20-40 employees with a workforce growing at 12-20% annually (40-60% over three years) had the highest likelihood of having annual growth rates higher than 100%. Knowing what size and rate to expand a small company to have the highest chance for growth is a powerful tool to mitigate risk for entrepreneurs.


NOTE: Our third member told us last night that he had a word with Professor Moosvi and has ended school earlier due to personal reasons.