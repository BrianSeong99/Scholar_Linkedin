import codecs
import json
def collect_news():
    news_list = []
    dict1 = {}
    dict1["id"] = 1
    dict1["date"] = "2020-03-31 00:00:00"
    dict1["url"] = "https://www.opendemocracy.net/en/can-europe-make-it/how-data-mining-companies-are-set-gain-covid-19-pandemic/"
    dict1["fields"] = []
    dict1["fields"].append("Data_Mining")
    dict1["person"] = []
    dict1["img"] = "https://cdn-prod.opendemocracy.net/media/images/PA-49722381.max-760x504.jpg"
    text = "The current outbreak of the coronavirus pandemic may be seen as a litmus test for different institutions of contemporary society – the viability of production structures based on global value chains, the solidity of health systems built (or, rather, dismantled) in the period of neoliberalism, and, more generally, the ability of the ‘nightwatchman’ neoliberal state to ensure the security and survival of the population.\n One of the things that the Covid-19 outbreak is increasingly revealing is how pervasive the surveillance mechanisms, developed in the last decade or so, have become. In an effort to contain the spread of the virus, governments all over the world are adopting various surveillance and monitoring technologies: tracking those who have been tested positive and informing the public about their movements with ‘travel logs’ (as, for example, in South Korea); monitoring the movements of individuals to ensure their compliance with the policies of quarantine or confinement (as, for instance, in China, Israel and Singapore, as well as in Italy, Germany and Austria); or using such technologies to optimize the use of resources in hospitals (as in the UK).\nAs has always been the case with modern surveillance – and with technology more generally, which, as Melvin Kranzberg famously observed, “is neither good or bad, nor is it neutral” – it may produce positive and socially beneficial outcomes, and in the current context the adoption of such measures seems justified. However, digital surveillance has always carried with a risk of doing more harm than good – to undermine various individual rights (privacy, freedom of speech, labour rights, freedom from gender or racial discrimination, etc.) and to threaten the existence of democratic institutions and politics.\nAs Edward Snowden and number of other analysts have warned, what needs to be closely watched is whether or not the surveillance measures deployed to deal with the virus will not be kept in place by public authorities after the pandemic is over.\nIt seems that these data-mining tech companies will come out of the current crisis not just with an improved image, especially if their involvement in the containment of the Covid-19 pandemic does produce tangible results. More importantly, their status as legitimate partners of governments in the period of one of the major health crises that humanity has seen is likely to contribute to the general acceptance and normalization of their existence. In other words, their business model, ultimately based on constant privacy invasions and the monetization of the data obtained, which has been challenged by numerous activists and analysts, is likely to get further naturalized and objectified.\n"
    dict1["content"] = text
    dict1["title"] = "How data-mining companies are set to gain from the Covid-19 pandemic"
    news_list.append(dict1)
    dict2 = {}
    dict2["id"] = 2
    dict2["date"] = "2020-04-04 00:00:00"
    dict2["url"] = "https://sciencein.me/2020/04/03/automated-storage-and-retrieval-system-asrs-market-key-opportunities-and-future-demand-westfalia-technologies-inc-sencorp-white-mias-group-ihi-corporation-hanel-gmbh-co-kg-automation/"
    dict2["fields"] = []
    dict2["fields"].append("Information_Retrieval")
    dict2["person"] = []
    dict2["img"] = "https://feedroad.com/wp-content/uploads/2020/03/HPC-Data-Analysis-Storage-And-Management-Market-in-Life-Sciences.jpg"
    text = "Automated Storage and Retrieval Systems Market: Seamless Explanation on Major Growth Prospects and Growth Opportunities for Stakeholders\nXploreMR recently published a market research report titled “Automated Storage and Retrieval Systems Market Forecast, Trend Analysis and Competition Tracking – Global Review 2018-2028”. The report is a comprehensive representation of the most critical growth parameters of the automated storage and retrieval systems market. Readers can find qualitative and quantitative information on how the automated storage and retrieval systems market will grow during the forecast period 2018-2028. Readers can identify the lucrative opportunities for players in the automated storage and retrieval systems market and other factors that may influence the market growth during the assessment period. Furthermore, the report also helps readers to understand the regional outlook of the automated storage and retrieval systems market to adopt appropriate strategies to explore lucrative business opportunities in leading regional markets. The report presents critical information about the automated storage and retrieval systems market in the most seamless, chapter-wise manner for the better understanding of readers.\n"
    dict2["content"] = text
    dict2["title"] = "Automated Storage and Retrieval System (ASRS) Market Key Opportunities and Future Demand WESTFALIA TECHNOLOGIES, INC."
    news_list.append(dict2)

    dict3 = {}
    dict3["id"] = 3
    dict3["date"] = "2020-02-26 00:00:00"
    dict3["url"] = "https://www.risk.net/cutting-edge/banking/7462701/quantifying-systemic-risk-using-bayesian-networks"
    dict3["fields"] = []
    dict3["fields"].append("Bayesian_Networks")
    dict3["person"] = []
    dict3["img"] = "https://www.risk.net/sites/risk/files/styles/1905x657sc/public/2020-02/stress-break.jpg?itok=1LABvgg9"
    text = "Sumit Sourabh, Markus Hofer and Drona Kandhai develop a novel framework using Bayesian networks to capture distress dependence in the context of counterparty credit risk. Then, they apply this methodology to a wrong-way risk model and stress-scenario testing. Their results show that stress propagation in an interconnected financial system can have a significant impact on counterparty credit exposures\n"
    dict3["content"] = text
    dict3["title"] = "Quantifying systemic risk using Bayesian networks"
    news_list.append(dict3)

    dict4 = {}
    dict4["id"] = 4
    dict4["date"] = "2020-04-03 00:00:00"
    dict4["url"] = "https://securityboulevard.com/2020/04/zoom-was-mining-data-and-matching-users-with-linkedin-info/"
    dict4["fields"] = []
    dict4["fields"].append("Web_Mining")
    dict4["person"] = []
    dict4["img"] = "https://hotforsecurity.bitdefender.com/wp-content/uploads/2020/04/Capture.jpg"
    text = "Zoom has disabled a feature in its web conferencing software that allowed the company to secretly gather data and match the information with LinkedIn sources, giving some users the ability to identify participants in the conference without their knowledge.\nFollowing a New York Times investigation, Zoom decided to eliminate its LinkedIn data mining entirely, citing privacy concerns. It turns out that Zoom would send back data about participants and then used LinkedIn to match the people.\nSomeone in the active conference with a LinkedIn Sales Navigator account would be able to access LinkedIn-provided details without notifying the participants. The investigation also revealed that even users logged in as Anonymous were not safe — the data-mining feature would work just as well...\n"
    dict4["content"] = text
    dict4["title"] = "Zoom Was Mining Data and Matching Users with LinkedIn Info"
    news_list.append(dict4)


    dict5 = {}
    dict5["id"] = 5
    dict5["date"] = "2020-04-04 00:00:00"
    dict5["url"] = "https://sciencein.me/2020/04/04/machine-learning-in-financial-security-market-2020-by-industry-analysis-research-share-growth-sales-trends-supply-forecast-to-2026/"
    dict5["fields"] = []
    dict5["fields"].append("Machine_Learning")
    dict5["person"] = []
    dict5["img"] = "https://sciencein.me/wp-content/uploads/2020/04/MRI-1-300x161.png"
    text = "This report studies the Machine Learning in Financial Security Market with many aspects of the industry like the market size, market status, market trends and forecast, the report also provides brief information of the competitors and the specific growth opportunities with key market drivers. Find the complete Machine Learning in Financial Security Market analysis segmented by companies, region, type and applications in the report.\nThe final report will add the analysis of the Impact of Covid-19 in this report Machine Learning in Financial Security Industry.\n"
    dict5["content"] = text
    dict5["title"] = "Machine Learning in Financial Security Market 2020 by Industry Analysis, Research, Share, Growth, Sales, Trends, Supply, Forecast to 2026"
    news_list.append(dict5)

    dict6 = {}
    dict6["id"] = 6
    dict6["date"] = "2020-03-23 00:00:00"
    dict6[
        "url"] = "https://www.blockchaintechnology-news.com/2020/03/23/fluree-announces-seed-extension-funding-round-for-blockchain-based-data-management/"
    dict6["fields"] = []
    dict6["fields"].append("Semantic_Web")
    dict6["person"] = []
    dict6["img"] = "https://blockchaintechnology-news.com/wp-content/uploads/sites/10/2020/03/michael-longmire-lhltMGdohc8-unsplash-2048x1475.jpg"
    text = "North Carolina-based database management firm Fluree has announced a seed extension funding round led by independent venture capital company Engage.\nThe latest investment, which follows a $4.7 million seed funding round in June, allows Fluree to expand its enterprise data management platform, which acts as the foundation for emerging online architectures that include AI, microservices, machine learning, the semantic web and consortium blockchains. The platform is used by tech startups, government agencies, and Fortune 500 enterprises for sharing, securing and building services upon high-quality, trusted data.\nFluree also recently announced a strategic blockchain deployment with the United States Air Force.\nBrian Platz, co-CEO and co-founder of Fluree, said: “Organisations have been striving to secure a data-first approach for nearly a decade, and Fluree finally brings that vision to life. As the semantic web continues to dissolve data silos and build a new framework for harnessing the value of information, Fluree is becoming the backend to power that change.\n"
    dict6["content"] = text
    dict6["title"] = "Fluree announces seed extension funding round for blockchain-based data management"
    news_list.append(dict6)

    dict7 = {}
    dict7["id"] = 7
    dict7["date"] = "2020-04-08 00:00:00"
    dict7[
        "url"] = "https://sciencein.me/2020/04/05/embedded-database-management-systems-market-increasing-demand-with-leading-player-comprehensive-analysis-and-forecast-2026/"
    dict7["fields"] = []
    dict7["fields"].append("Database_Systems")
    dict7["person"] = []
    dict7[
        "img"] = "https://mk0analyticsindf35n9.kinstacdn.com/wp-content/uploads/2020/04/Mongo_guide_aim-scaled.jpg"
    text = "New Jersey, United States: The Embedded Database Management Systems Market is analyzed in depth in the report, with the primary aim of providing accurate market data and useful recommendations so that players can achieve strong growth in the future. The report is compiled by experts and experienced market analysts, which makes it very authentic and reliable. Readers have a thorough analysis of historical and future market scenarios to get a good understanding of market competition and other important issues. The report provides comprehensive information on market dynamics, key segments, key players and various regional markets. It is a complete set of in-depth analysis and research on the Embedded Database Management Systems market.\nThe authors of the report highlighted lucrative business prospects, eye-catching trends, regulatory situations and Embedded Database Management Systems market price scenarios. It is important to note that the report includes a detailed analysis of the macroeconomic and microeconomic factors affecting the growth of the Embedded Database Management Systems market. It is divided into several sections and chapters so that you can easily understand every aspect of the Embedded Database Management Systems market. Market participants can use the report to take a look at the future of the Embedded Database Management Systems market and make significant changes to their operating style and marketing tactics in order to achieve sustainable growth.\n"
    dict7["content"] = text
    dict7["title"] = "Embedded Database Management Systems Market Increasing Demand with Leading Player, Comprehensive Analysis and Forecast 2026"
    news_list.append(dict7)

    dict8 = {}
    dict8["id"] = 8
    dict8["date"] = "2020-03-23 00:00:00"
    dict8[
        "url"] = "https://www.patentlyapple.com/patently-apple/2020/04/apple-paid-former-amazon-web-services-security-engineer-big-bucks-to-successfully-hack-the-iphone-11-camera.html"
    dict8["fields"] = []
    dict8["fields"].append("Web_Services")
    dict8["person"] = []
    dict8[
        "img"] = "https://www.patentlyapple.com/.a/6a0120a5580826970c025d9b42d63f200c-pi"
    text = "Apple Paid former Amazon Web Services Security Engineer big bucks to Successfully Hack the iPhone 11 Camera\nEthical hackers, those security researchers who put their hacking talents to use in helping secure the products and services they break, can make big bucks. Work from home elite hackers participating in the recent virtual PWN2OWN event earned well over $270,000 in only 48 hours. Indeed, Google paid ethical hackers $6.5 million last year as part of its vulnerability reward programs, and Apple has a top bug bounty of $1.5 million for the most serious of iPhone hacks...\n"
    dict8["content"] = text
    dict8["title"] = "Apple Paid former Amazon Web Services Security Engineer big bucks to Successfully Hack the iPhone 11 Camera"
    news_list.append(dict8)

    dict9 = {}
    dict9["id"] = 9
    dict9["date"] = "2020-03-10 00:00:00"
    dict9[
        "url"] = "https://www.edu.cn/rd/gao_xiao_cheng_guo/gao_xiao_zi_xun/202003/t20200310_1715919.shtml"
    dict9["fields"] = []
    dict9["fields"].append("Data_Mining")
    dict9["person"] = ["Jie_Tang"]
    dict9["img"] = "http://www.cs.tsinghua.edu.cn/publish/cs/4616/20110330101939787483549/20190321114128398502759.jpg"
    text = "今天，清华大学计算机科学与技术系教授唐杰在社交媒体上宣布，他们成立了一个新期刊——《ai open》，专注 AI 的开放共享。该期刊的内容可以免费获取。此举得到了刘知远、刘群、马少平等国内研究者的支持。\n在期刊官网，我们可以看到，《ai open》隶属于北京科爱森蓝文化传播有限公司，后者由中国科技出版传媒集团有限公司和爱思唯尔这两家世界领先的科学、技术和医学出版机构共同投资成立。该期刊由唐杰教授担任主编。他是清华大学计算机科学与技术系长聘教授，研究兴趣包括社会网络分析、数据挖掘、机器学习和知识图谱等。2006 年，他还主持研发了研究者社会网络挖掘系统 AMiner。《ai open》是一个共享 AI 理论与应用知识和前瞻性观点的免费开放平台。期刊接收的内容包括研究文章、综述论文、观点、交流性短文和技术说明，范围覆盖 AI 及其应用的方方面面。\n"
    dict9["content"] = text
    dict9["title"] = "「打造中国人自己的开放 AI」:清华教授唐杰宣布成立AI新期刊"
    news_list.append(dict9)
    return news_list

if __name__ == '__main__':
    news_list = collect_news()
    fp = codecs.open('News.json', 'w', 'utf-8')
    fp.write(json.dumps(news_list, ensure_ascii=False))
    fp.close()


