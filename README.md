# Financial News Analyzer

This project uses LLMs to summarize a news page and point out the top companies and stock tickers which can be impacted based on the news.

# sample Execution of the script

Please enter the URL of the news article you'd like to analyze: https://finance.yahoo.com/news/trump-picks-scott-bessent-the-investor-favorite-for-treasury-secretary-000710469.html
## Summary

On November 22, 2024, President-elect Donald Trump announced his nomination of Scott Bessent, known as an "investor favorite," for Treasury Secretary. Bessent, the CEO of Key Square Capital Management and a prominent figure in the investment world, was selected after a contentious selection process and a series of debates concerning various candidates. Trump described Bessent as "one of the World's foremost International Investors" and a supporter of his "America First" agenda. Tasked with calming US and global markets, Bessent will also need to push forward many of Trump's economically controversial proposals, including potential tariffs and increased deficit spending. His success in this role is critical as he navigates complexities left over from tax policies and aims to promote new economic strategies.

## Impacted Company Names or Stock Tickers

### 1. **Apollo Global Management (APO)**
   - **Reasoning**: Bessent's nomination was influenced by the competitive dynamics surrounding Apollo's CEO, Marc Rowan, who was also a candidate for Treasury Secretary. Given the close involvement of Apollo in financing and investment strategies, any shifts in policies or economic strategies proposed by Bessent could directly affect the firm's operations and market perceptions.

### 2. **Key Square Capital Management**
   - **Reasoning**: As Bessent is currently the CEO of Key Square Capital, any strategic decisions or market communications from the Treasury will likely impact how his own firm invests and reallocates resources in response to federal economic policies. The reputation and performance of Key Square may also sway depending on how well Bessent performs in his new role.

### 3. **Overall Financial Services Sector**
   - **Reasoning**: Bessent's tenure as Treasury Secretary is expected to influence broader financial policies, including rates, tariffs, and spending. Companies within the financial services sector, including banks and investment firms, could experience volatility depending on the new economic initiatives he supports. Stocks in this sector may see fluctuations based on market confidence in his ability to stabilize and direct fiscal policy effectively.


# Install
```bash
conda env create -f environment.yml
conda activate llms
python financial_news_analyzer.py