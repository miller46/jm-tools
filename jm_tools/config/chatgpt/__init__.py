DEFAULT_ENGINE_ID = "gpt-5.1"

ENGINES_COST_PER_1000_TOKENS_INPUT_MAP = {
    "gpt-5.1": 1.25,
    "gpt-5": 1.25,
    "gpt-5-mini": 0.25,
    "gpt-5-nano": 0.05,
    "gpt-5.1-chat-latest": 1.25,
    "gpt-5-chat-latest": 1.25,
    "gpt-5.1-codex": 1.25,
    "gpt-5-codex": 1.25,
    "gpt-5-pro": 15.00,
    "gpt-4.1": 2.00,
    "gpt-4.1-mini": 0.40,
    "gpt-4.1-nano": 0.10,
    "gpt-4o": 2.50,
    "gpt-4o-2024-05-13": 5.00,
    "gpt-4o-mini": 0.15,
    "gpt-realtime": 4.00,
    "gpt-realtime-mini": 0.60,
    "gpt-4o-realtime-preview": 5.00,
    "gpt-4o-mini-realtime-preview": 0.60,
    "gpt-audio": 2.50,
    "gpt-audio-mini": 0.60,
    "gpt-4o-audio-preview": 2.50,
    "gpt-4o-mini-audio-preview": 0.15,
    "o1": 15.00,
    "o1-pro": 150.00,
    "o3-pro": 20.00,
    "o3": 2.00,
    "o3-deep-research": 10.00,
    "o4-mini": 1.10,
    "o4-mini-deep-research": 2.00,
    "o3-mini": 1.10,
    "o1-mini": 1.10,
    "gpt-5.1-codex-mini": 0.25,
    "codex-mini-latest": 1.50,
    "gpt-5-search-api": 1.25,
    "gpt-4o-mini-search-preview": 0.15,
    "gpt-4o-search-preview": 2.50,
    "computer-use-preview": 3.00,
    "gpt-image-1": 5.00,
    "gpt-image-1-mini": 2.00,
}


ENGINES_COST_PER_1000_TOKENS_OUTPUT_MAP = {
    "gpt-5.1": 10.00,
    "gpt-5": 10.00,
    "gpt-5-mini": 2.00,
    "gpt-5-nano": 0.40,
    "gpt-5.1-chat-latest": 10.00,
    "gpt-5-chat-latest": 10.00,
    "gpt-5.1-codex": 10.00,
    "gpt-5-codex": 10.00,
    "gpt-5-pro": 120.00,
    "gpt-4.1": 8.00,
    "gpt-4.1-mini": 1.60,
    "gpt-4.1-nano": 0.40,
    "gpt-4o": 10.00,
    "gpt-4o-2024-05-13": 15.00,
    "gpt-4o-mini": 0.60,
    "gpt-realtime": 16.00,
    "gpt-realtime-mini": 2.40,
    "gpt-4o-realtime-preview": 20.00,
    "gpt-4o-mini-realtime-preview": 2.40,
    "gpt-audio": 10.00,
    "gpt-audio-mini": 2.40,
    "gpt-4o-audio-preview": 10.00,
    "gpt-4o-mini-audio-preview": 0.60,
    "o1": 60.00,
    "o1-pro": 600.00,
    "o3-pro": 80.00,
    "o3": 8.00,
    "o3-deep-research": 40.00,
    "o4-mini": 4.40,
    "o4-mini-deep-research": 8.00,
    "o3-mini": 4.40,
    "o1-mini": 4.40,
    "gpt-5.1-codex-mini": 2.00,
    "codex-mini-latest": 6.00,
    "gpt-5-search-api": 10.00,
    "gpt-4o-mini-search-preview": 0.60,
    "gpt-4o-search-preview": 10.00,
    "computer-use-preview": 12.00,
    "gpt-image-1": None,
    "gpt-image-1-mini": None,
}


ENGINES_LIST_JSON = '{"data":[{"created":null,"id":"babbage","object":"engine","owner":"openai","permissions":null,"ready":true},{"created":null,"id":"davinci","object":"engine","owner":"openai","permissions":null,"ready":true},{"created":null,"id":"text-davinci-edit-001","object":"engine","owner":"openai","permissions":null,"ready":true},{"created":null,"id":"babbage-code-search-code","object":"engine","owner":"openai-dev","permissions":null,"ready":true},{"created":null,"id":"text-similarity-babbage-001","object":"engine","owner":"openai-dev","permissions":null,"ready":true},{"created":null,"id":"code-davinci-edit-001","object":"engine","owner":"openai","permissions":null,"ready":true},{"created":null,"id":"text-davinci-001","object":"engine","owner":"openai","permissions":null,"ready":true},{"created":null,"id":"ada","object":"engine","owner":"openai","permissions":null,"ready":true},{"created":null,"id":"babbage-code-search-text","object":"engine","owner":"openai-dev","permissions":null,"ready":true},{"created":null,"id":"babbage-similarity","object":"engine","owner":"openai-dev","permissions":null,"ready":true},{"created":null,"id":"code-search-babbage-text-001","object":"engine","owner":"openai-dev","permissions":null,"ready":true},{"created":null,"id":"text-curie-001","object":"engine","owner":"openai","permissions":null,"ready":true},{"created":null,"id":"code-search-babbage-code-001","object":"engine","owner":"openai-dev","permissions":null,"ready":true},{"created":null,"id":"text-ada-001","object":"engine","owner":"openai","permissions":null,"ready":true},{"created":null,"id":"text-embedding-ada-002","object":"engine","owner":"openai-internal","permissions":null,"ready":true},{"created":null,"id":"text-similarity-ada-001","object":"engine","owner":"openai-dev","permissions":null,"ready":true},{"created":null,"id":"curie-instruct-beta","object":"engine","owner":"openai","permissions":null,"ready":true},{"created":null,"id":"ada-code-search-code","object":"engine","owner":"openai-dev","permissions":null,"ready":true},{"created":null,"id":"ada-similarity","object":"engine","owner":"openai-dev","permissions":null,"ready":true},{"created":null,"id":"code-search-ada-text-001","object":"engine","owner":"openai-dev","permissions":null,"ready":true},{"created":null,"id":"text-search-ada-query-001","object":"engine","owner":"openai-dev","permissions":null,"ready":true},{"created":null,"id":"davinci-search-document","object":"engine","owner":"openai-dev","permissions":null,"ready":true},{"created":null,"id":"ada-code-search-text","object":"engine","owner":"openai-dev","permissions":null,"ready":true},{"created":null,"id":"text-search-ada-doc-001","object":"engine","owner":"openai-dev","permissions":null,"ready":true},{"created":null,"id":"davinci-instruct-beta","object":"engine","owner":"openai","permissions":null,"ready":true},{"created":null,"id":"gpt-3.5-turbo","object":"engine","owner":"openai","permissions":null,"ready":true},{"created":null,"id":"text-similarity-curie-001","object":"engine","owner":"openai-dev","permissions":null,"ready":true},{"created":null,"id":"code-search-ada-code-001","object":"engine","owner":"openai-dev","permissions":null,"ready":true},{"created":null,"id":"ada-search-query","object":"engine","owner":"openai-dev","permissions":null,"ready":true},{"created":null,"id":"text-search-davinci-query-001","object":"engine","owner":"openai-dev","permissions":null,"ready":true},{"created":null,"id":"curie-search-query","object":"engine","owner":"openai-dev","permissions":null,"ready":true},{"created":null,"id":"gpt-3.5-turbo-0301","object":"engine","owner":"openai","permissions":null,"ready":true},{"created":null,"id":"davinci-search-query","object":"engine","owner":"openai-dev","permissions":null,"ready":true},{"created":null,"id":"babbage-search-document","object":"engine","owner":"openai-dev","permissions":null,"ready":true},{"created":null,"id":"ada-search-document","object":"engine","owner":"openai-dev","permissions":null,"ready":true},{"created":null,"id":"text-search-curie-query-001","object":"engine","owner":"openai-dev","permissions":null,"ready":true},{"created":null,"id":"whisper-1","object":"engine","owner":"openai-internal","permissions":null,"ready":true},{"created":null,"id":"text-search-babbage-doc-001","object":"engine","owner":"openai-dev","permissions":null,"ready":true},{"created":null,"id":"curie-search-document","object":"engine","owner":"openai-dev","permissions":null,"ready":true},{"created":null,"id":"text-davinci-003","object":"engine","owner":"openai-internal","permissions":null,"ready":true},{"created":null,"id":"text-search-curie-doc-001","object":"engine","owner":"openai-dev","permissions":null,"ready":true},{"created":null,"id":"babbage-search-query","object":"engine","owner":"openai-dev","permissions":null,"ready":true},{"created":null,"id":"text-babbage-001","object":"engine","owner":"openai","permissions":null,"ready":true},{"created":null,"id":"text-search-davinci-doc-001","object":"engine","owner":"openai-dev","permissions":null,"ready":true},{"created":null,"id":"text-search-babbage-query-001","object":"engine","owner":"openai-dev","permissions":null,"ready":true},{"created":null,"id":"curie-similarity","object":"engine","owner":"openai-dev","permissions":null,"ready":true},{"created":null,"id":"curie","object":"engine","owner":"openai","permissions":null,"ready":true},{"created":null,"id":"text-similarity-davinci-001","object":"engine","owner":"openai-dev","permissions":null,"ready":true},{"created":null,"id":"text-davinci-002","object":"engine","owner":"openai","permissions":null,"ready":true},{"created":null,"id":"davinci-similarity","object":"engine","owner":"openai-dev","permissions":null,"ready":true}],"object":"list"}'

TEXT_SAMPLE = """

Authored by Susan Schmidt, Andrew Lowenthal, Tom Wyatt, Techno Fog, and 3 others via Racket News (subscribe here),



[Update: How do we know Matt and crew are over the target? Facebook won't allow this post...]

Introduction by Matt Taibbi

On January 17, 1960, outgoing President and former Supreme Allied Commander Dwight D. Eisenhower gave one of the most consequential speeches in American history. Eisenhower for eight years had been a popular president, whose appeal drew upon a reputation as a person of great personal fortitude, who’d guided the United States to victory in an existential fight for survival in World War II. Nonetheless, as he prepared to vacate the Oval Office for handsome young John F. Kennedy, he warned the country it was now at the mercy of a power eve he could not overcome. 

Until World War II, America had no permanent arms manufacturing industry. Now it did, and this new sector, Eisenhower said, was building up around itself a cultural, financial, and political support system accruing enormous power. This “conjunction of an immense military establishment and a large arms industry is new in the American experience,” he said, adding:

In the councils of government, we must guard against the acquisition of unwarranted influence, whether sought or unsought, by the military-industrial complex. The potential for the disastrous rise of misplaced power exists and will persist. 

We must never let the weight of this combination endanger our liberties or democratic processes… Only an alert and knowledgeable citizenry can compel the proper meshing of the huge industrial and military machinery of defense with our peaceful methods and goals, so that security and liberty may prosper together. 

This was the direst of warnings, but the address has tended in the popular press to be ignored. After sixty-plus years, most of America – including most of the American left, which traditionally focused the most on this issue – has lost its fear that our arms industry might conquer democracy from within. 

Now, however, we’ve unfortunately found cause to reconsider Eisenhower’s warning.

While the civilian population only in recent years began haggling over “de-platforming” incidents involving figures like Alex Jones and Milo Yiannopoulos, government agencies had already long been advancing a new theory of international conflict, in which the informational landscape is more importantly understood as a battlefield than a forum for exchanging ideas. In this view, “spammy” ads, “junk” news, and the sharing of work from “disinformation agents” like Jones aren’t inevitable features of a free Internet, but sorties in a new form of conflict called “hybrid warfare.” 

In 1996, just the Internet was becoming part of daily life in America, the U.S. Army published “Field Manual 100-6,” which spoke of “an expanding information domain termed the Global Information Environment” that contains “information processes and systems that are beyond the direct influence of the military.” Military commanders needed to understand that “information dominance” in the “GIE” would henceforth be a crucial element for “operating effectively.”

You’ll often see it implied that “information operations” are only practiced by America’s enemies, because only America’s enemies are low enough, and deprived enough of real firepower, to require the use of such tactics, needing as they do to “overcome military limitations.” We rarely hear about America’s own lengthy history with “active measures” and “information operations,” but popular media gives us space to read about the desperate tactics of the Asiatic enemy, perennially described as something like an incurable trans-continental golf cheat.

Indeed, part of the new mania surrounding “hybrid warfare” is the idea that while the American human being is accustomed to living in clear states of “war” or “peace,” the Russian, Chinese, or Iranian citizen is born into a state of constant conflict, where war is always ongoing, whether declared or not. In the face of such adversaries, America’s “open” information landscape is little more than military weakness.

In March of 2017, in a hearing of the House Armed Services Committee on hybrid war, chairman Mac Thornberry opened the session with ominous remarks, suggesting that in the wider context of history, an America built on constitutional principles of decentralized power might have been badly designed:

Americans are used to thinking of a binary state of either war or peace. That is the way our organizations, doctrine, and approaches are geared. Other countries, including Russia, China, and Iran, use a wider array of centrally controlled, or at least centrally directed, instruments of national power and influence to achieve their objectives…

Whether it is contributing to foreign political parties, targeted assassinations of opponents, infiltrating non-uniformed personnel such as the little green men, traditional media and social media, influence operations, or cyber-connected activity, all of these tactics and more are used to advance their national interests and most often to damage American national interests… 

The historical records suggest that hybrid warfare in one form or another may well be the norm for human conflict, rather than the exception.

Around that same time, i.e. shortly after the election of Donald Trump, it was becoming gospel among the future leaders of the “Censorship-Industrial Complex” that interference by “malign foreign threat actors” and the vicissitudes of Western domestic politics must be linked. Everything, from John Podesta’s emails to Trump’s Rust Belt primary victories to Brexit, were to be understood first and foremost as hybrid war events.

This is why the Trump-Russia scandal in the United States will likely be remembered as a crucial moment in 21st-century history, even though the investigation superficially ended a non-story, fake news in itself. What the Mueller investigation didn’t accomplish in ousting Trump from office, it did accomplish in birthing a vast new public-private bureaucracy devoted to stopping “mis-, dis-, and malinformation,” while smoothing public acquiescence to the emergence of a spate of new government agencies with “information warfare” missions. 

The “Censorship-Industrial Complex” is just the Military-Industrial Complex reborn for the “hybrid warfare” age.

Much like the war industry, pleased to call itself the “defense” sector, the “anti-disinformation” complex markets itself as merely defensive, designed to fend off the hostile attacks of foreign cyber-adversaries who unlike us have “military limitations.” The CIC, however, is neither wholly about defense, nor even mostly focused on foreign “disinformation.” It’s become instead a relentless, unified messaging system aimed primarily at domestic populations, who are told that political discord at home aids the enemy’s undeclared hybrid assault on democracy. 

They suggest we must rethink old conceptions about rights, and give ourselves over to new surveillance techniques like “toxicity monitoring,” replace the musty old free press with editors claiming a “nose for news” with an updated model that uses automated assignment tools like “newsworthy claim extraction,” and submit to frank thought-policing mechanisms like the “redirect method,” which sends ads at online browsers of dangerous content, pushing them toward “constructive alternative messages.”

Binding all this is a commitment to a new homogeneous politics, which the complex of public and private agencies listed below seeks to capture in something like a Unified Field Theory of neoliberal narrative, which can be perpetually tweaked and amplified online via algorithm and machine learning. This is what some of the organizations on this list mean when they talk about coming up with a “shared vocabulary” of information disorder, or “credibility,” or “media literacy.”

Anti-disinformation groups talk endlessly about building “resilience” to disinformation (which in practice means making sure the public hears approved narratives so often that anything else seems frightening or repellent), and audiences are trained to question not only the need for checks and balances, but competition. Competition is increasingly frowned upon not just in the “marketplace of ideas” (an idea itself more and more often described as outdated), but in the traditional capitalist sense. In the Twitter Files we repeatedly find documents like this unsigned “Sphere of Influence” review circulated by the Carnegie Endowment that wonders aloud if tech companies really need to be competing to “get it right”:



In place of competition, the groups we’ve been tracking favor the concept of the “shared endeavor” (one British group has even started a “Shared Endeavour” program), in which key “stakeholders” hash out their disagreements in private, but present a unified front.

Who are the leaders of these messaging campaigns? If you care to ask, the groups below are a good place to start. 

“The Top 50 List” is intended as a resource for reporters and researchers beginning their journey toward learning the scale and ambition of the “Censorship-Industrial Complex.” Written like a magazine feature, it tries to answer a few basic questions about funding, organization type, history, and especially, methodology. Many anti-disinformation groups adhere to the same formulaic approach to research, often using the same “hate-mapping,” guilt-by-association-type analysis to identify wrong-thinkers and suppressive persons. There is even a tendency to use what one Twitter Files source described as the same “hairball” graphs.

Where they compete, often, is in the area of gibberish verbiage describing their respective analytical methods. My favorite came from the Public Good Projects, which in a display of predictive skills reminiscent of the “unsinkable Titanic” described itself as the “Buzzfeed of public health.” 

Together, these groups are fast achieving what Eisenhower feared: the elimination of “balance” between the democratic need for liberalizing laws and institutions, and the vigilance required for military preparation. Democratic society requires the nourishment of free debate, disagreement, and intellectual tension, but the groups below seek instead that “shared vocabulary” to deploy on the hybrid battlefield. They propose to serve as the guardians of that “vocabulary,” which sounds very like the scenario Ike outlined in 1961, in which “public policy could itself become the captive of a scientific and technological elite.”

Without further ado, an introduction to the main players in this “CIC”:

​1.​ Information Futures Lab (IFL) at Brown University (formerly, First Draft):
Link: https://sites.brown.edu/informationfutures/ / https://First Draftnews.org/

Type: A university institute, housed within the School of Public Health, to combat “misinformation” and “outdated communications practices.” The successor to First Draft, one of the earliest and more prominent “anti-disinformation” outfits.

You may have read about them when: You first heard the terms Mis-, dis-, and malinformation. The term was coined by FD Director Claire Wardle. IFL/FD are also the only academic/non-profit organization involved in the Trusted News Initiative, a large-scale legacy media consortium established to control debate around the pandemic response. Wardle was Twitter executives’ first pick for a signal group of anti-misinformation advisors it put together. She also participated in the Aspen Institute’s Hunter Biden laptop tabletop in August 2020 (before the laptop story broke). IFL’s co-founder Stefanie Friedhoff serves on the White House Covid-19 Response Team. First Draft staffers were also revealed in the #TwitterFiles to be frequent and trusted partners to a leading public face of the Censorship-Industrial Complex, Renee DiResta, now of Stanford University.

What we know about funding: First Draft was funded by a huge number of entities including Craig Newmark, Rockefeller, the National Science Foundation, Facebook, the Ford Foundation, Google, the Knight Foundation, the Wellcome Trust, Open Society Foundations, and more. Funding for the IFL includes the Rockefeller Foundation for a “building vaccine demand” initiative.

What they do/What they are selling: IFL/First Draft position themselves as the vanguard of disinformation studies, acting as key advisors to media, technology, and public health consortiums, bringing together a wide range of academic skill sets. 

Characteristic/worldview quotes: High use of terms like coordinated inauthentic behavior, information pollution, the future Homeland Security catchwords mis-, dis-, and malinformation, and information disorder.

Gibberish verbiage: “The most accessible inoculation technique is prebunking — the process of debunking lies, tactics or sources before they strike.”

In the #TwitterFiles: First Draft is featured extensively in the files. They were the first proposed name when Twitter decided to assemble a small group of “trusted people to come together to talk about what they’re seeing,” were part of the Aspen Institute’s Burisma tabletop, and appeared in multiple emails with Pentagon officials. 



Goofy graphage: 



Closely connected to: Almost all the leading lights of the CIC, including the Stanford Internet Observatory, the Trusted News Initiative, Shorenstein Center, DFRLabs, the World Economic Forum, the Aspen Institute, Meedan, and Bellingcat.

In sum: With a strong ability to both know and direct emerging trends, and with a large array of elite networks in tow, the IFL will continue to serve as one of the key tastemakers in the “anti-disinformation” field.

2.​ Meedan
Link: https://meedan.com/

Type: Medium-sized non-profit specializing in technology and countering “disinformation.”

You may have read about them when: Meedan ran a range of Covid-19 misinformation initiatives “to support pandemic fact-checking efforts” with funding from BigTech, the Omidyar Foundation, the National Science Foundation and more. Partners included Britain’s now-disgraced Behavioural Insights Team, or “nudge unit,” known for scaring the pants off Brits about a range of medical manias. Among Meedan’s “anti-disinformation” projects is an effort to peer into private, encrypted messages. The Meedan board includes Tim Hwang (Substack General Counsel), free speech skeptic Zeynep Tufecki, and Maria Ressa, a Nobel Prize winner with very close ties to eBay founder Pierre Omidyar and the National Endowment for Democracy. Ressa believes Wikileaks “isn’t journalism.” Meedan co-founder Muna AbuSulayman was the founding Secretary General of the Saudi Alwaleed bin Talal Foundation. Alwaleed bin Talal is one of the largest shareholders in Twitter, both pre-Elon Musk and now, with Musk.

What we know about funding: Widespread public and private funding including from Omidyar, Twitter, Facebook, Google, the National Science Foundation, the Swedish International Development Cooperation Agency, and more.

What they do/What they are selling: Meedan positions itself as an NGO leader in the “anti-disinformation” field; convening networks, developing technology, and establishing new initiatives. Strong support and development are given to “fact-checking” organizations and building the technology to support them.

Characteristic/worldview quote: “Detection of controversial and hateful content.”

Gibberish verbiage: “Our work shows that there are far more matches between tipline content and public group messages on WhatsApp than between public group messages and either published fact checks or open social media content.” 

In the #TwitterFiles: Minimal in the files at hand, though Meedan is noted as one of Twitter’s four main Covid “misinformation” partners.



Connected to: Twitter, Factcheck.org, AuCoDe, the Berkman Klein Center for Internet and Society, the Behavioral Insights Team, the Oxford Internet Institute, Stanford Internet Observatory, and First Draft. 

In sum: Meedan exemplifies the NGO-to-Stasi stylistic shift, where spying and snitching on private messages in the name of “anti-disinformation” is now considered a public good.

Further reading:

Now They're Trying Censor Your Text Messages

3.​ Harvard Shorenstein Center on Media, Politics and Public Policy (Technology and Social Change Project)
Link: https://shorensteincenter.org/programs/technology-social-change/

Type: An elite academic project once regarded as one of the leading centers in the “anti-disinformation” field.

You may have read about them when: It was announced that the center would be closed in 2024 on the spurious grounds that project lead Joan Donovan lacked sufficient academic credentials to run the initiative (what was spurious is that it took that long for this realization to come about). Donovan was already widely known for partisanship and getting things wrong, in particular repeatedly claiming the Hunter Biden laptop was not genuine. The Shorenstein Center birthed two other key “anti-disinformation” initiatives, the aforementioned First Draft and the Algorithmic Transparency Initiative. Cameron Hickey, ATI’s lead, is now CEO of the much larger National Congress on Citizenship. In this video, Joan Donavan sits alongside Richard Stengel, the first head of the Global Engagement Center, an agency housed in the State Department with a remit to “counter foreign state and non-state propaganda and disinformation efforts.” The closing of the Technology and Social Change Project is a minor victory in an otherwise exploding field.

What we know about funding: Money from: the Ford Foundation, Open Society Foundations, Craig Newmark Philanthropies, Gates Foundation, Google, Facebook Journalism Project, and the W.K. Kellogg Foundation. 

What they do/What they are selling: Academic research into “disinformation,” a fellows program, field convening, and frequent media commentary. The Shorenstein Center also produces a leading “misinformation studies” journal.

Characteristic/worldview quote: Donovan’s infamous tweet, posed with an Atlantic staffer: “Me and @cwarzel Looking at the content on the Hunter Biden Laptop, the most popular straw man question at #Disinfo2022.”



Gibberish verbiage: “Examining accuracy-prompt efficacy in combination with using colored borders to differentiate news and social content online”

“Hairball” graph:



Closely connected to: First Draft, Algorithmic Transparency Initiative/NCoC, Berkman Center for Internet and Society, Data and Society, and the Aspen Institute.

In sum: An “anti-disinformation” project that got it wrong so often, even the center that housed it cut ties.

4.​ The Public Good Projects 
Link: https://www.publicgoodprojects.org/

Type: Non-profit consultancy, specializing in health communications, marketing, technology and “disinformation.”

You may have read about them when: Whilst PGP seem to do some front-facing work, they are also guns for hire for a large range of corporate and government programs. Twitter files show PGP had contracts with biotech lobby group BIO (whose members include Pfizer and Moderna) to run the Stronger campaign, which according to Lee Fang “worked w/Twitter to set content moderation rules around covid ‘misinformation.’” Jennifer McDonald of Twitter’s Public Policy team noted in an email that PGP was also among Twitter’s four “strongest information sharing partnerships” for Covid “misinformation”. PGP partnered with UNICEF on the Vaccine Demand Observatory which aims to “decrease the impact of misinformation and increase vaccine demand around the world.” The board includes the former CEO of Pepsi and Levi’s, a Morgan Stanley Vice-President, and Merck Pharmaceuticals’ Director of Public Health Partnerships.

What we know about funding: $1.25 million from BIO as well as partnerships with Google, Rockefeller, and UNICEF.

What they do/What they are selling: A suite of communications activities including marketing, research, media production, social media monitoring, vaccine promotion, and campaigns. They also use AI and natural language processing to “identify, track, and respond to narratives, trends, and urgent issues” in order to “perform fact-checking” and “power behavior change strategies."

Characteristic/worldview quote: “Think of us as the BuzzFeed of public health.”

In the #TwitterFiles: Noted as one of Twitter’s four go-to sources for supposed detection of Covid-19 misinformation.

Closely connected to: Twitter, UNICEF, Rockefeller, Kaiser Permanente, First Draft, Brown School of Public Health

In sum: A sophisticated communications and technology outfit with close BigTech and BigPharma partners, and a mission to stop “misinformation.”

Further reading:

When nudges become shoves

​5.​ Graphika 
Link: https://www.graphika.com/ 

Type: For-profit firm with defense connections specializing in “digital marketing and disinformation & analysis.”

You may have read about them when: Graphika was one of two outside groups hired in 2017 by the Senate Intelligence Committee to assess the Russian cyber menace. Graphika was also a “core four” partner to Stanford’s Election Integrity Partnership and its Virality Project, both subjects of #TwitterFiles reports. Made headlines for claiming a leak of US-UK trade discussions, publicized by Jeremy Corbyn, was part of an operation called “secondary Infektion” traceable to Russia.

Former Director of Investigations Ben Nimmo was previously a NATO press officer and DFRLabs fellow, and is now Facebook’s Global Threat Intelligence Lead. Head of Innovation Camille Francois was previously Google Jigsaw’s principal researcher.

What we know about funding: $3 million from the Department of Defense for 2020-2022, “to support and stimulate basic and applied research and technology at educational institutions”; boasts of partnerships with the Defense Advanced Partnerships Research Agency (DARPA) and the U.S. Air Force. According to USAspending.gov, defense agencies have provided almost $7 million. 

What they do/What they are selling: Long-form reports and subscription services for corporate and governmental clients, often focused on identifying “leading influencers” and “misinformation and disinformation risks,” along with highly sophisticated AI for surveilling social media.

Characteristic/worldview quote: “seeding doubt and uncertainty in authoritative voices leads to a society that finds it too challenging to identify what’s true.”

Gibberish verbiage: Tendency to impressively horrific puns (“More-troll Kombat,” “Lights, Camera, Coordinated Action!” “Step into my Parler”).

“Hairball” graph: Like pop art: 



In the #TwitterFiles: In 2017-2018, Twitter was unaware the Senate Intelligence Committee would be sharing their data on supposed Russia-linked accounts with commercial entities.

In sum: With deep Pentagon ties and a patina of public-facing commercial legitimacy, Graphika is set up to be the Rand Corporation of the Anti-Disinformation age.

Connected to: Stanford Internet Observatory, DFRLabs, Department of Defense, DARPA, Knight Foundation, Bellingcat

Further reading: https://www.foundationforfreedomonline.com/?page_id=2328

6.​ Digital Forensic Research Lab (DFRLabs) of the Atlantic Council
Link: https://www.atlanticcouncil.org/programs/digital-forensic-research-lab/

Type: Public-facing disinformation research arm of highly influential, extravagantly funded, NATO-aligned think tank, the Atlantic Council.

You may have read about them when: In May of 2018, Facebook announced a “New Election Partnership With the Atlantic Council,” to “prevent our service from being abused during elections.” The announcement was made by former National Republican Senatorial Committee Chief Digital Strategist Katie Harbath, weeks after a contentious hearing in the Senate in which Mark Zuckerberg answered questions about the “abuse of data” on Facebook. The Atlantic Council’s DFRLabs at the time included such figures as Eliot Higgins (from Bellingcat) and Ben Nimmo, future Director of Investigations at Graphika. This became a watershed moment, as Facebook soon after announced a series of purges of accounts accused of “coordinated inauthentic activity,” including small indie sites like Anti-Media, End The War on Drugs, ‘Murica Today, Reverb, and Anonymous News, beginning an era of mass deletions.

DFRLab was a core partner for Stanford’s “Election Integrity Partnership,” and the “Virality Project.” The Atlantic Council also organizes the elite 360/Open Summit whose 2018 disinformation edition included the private Vanguard-25 forum that brought together Madeleine Albright, former Swedish Prime Minister Carl Bildt, the head of the Munich Security Conference, Nobel Peace Prize winner Maria Ressa, Edelman (the world’s biggest PR company), Facebook, Twitter, Microsoft, Bellingcat, Graphika, and more.

What we know about funding: “DFRLab has received grants from the Department of State’s Global Engagement Center that support programming with an exclusively international focus,” Graham Brookie of DFRLabs told Racket. The Atlantic Council receives funding from the U.S. Army and Navy, Blackstone, Raytheon, Lockheed, the NATO STRATCOM Center of Excellence and a long list of other financial, military, and diplomatic entities.

What they do/What they are selling: Long-form reports, list-making, conference hosting, creation of reporter-friendly widgets (e.g. “Foreign Election Interference Tracker,” “Minsk Monitor”)

Characteristic/worldview quote: On “rumors about Covid-19s origins,” particularly the “disinformation” that the virus may have originated in a laboratory: “The cumulative effect of this was to distract the U.S. public’s attention away from the federal government’s disjointed approach to mitigating the virus and point the blame at China.”

Gibberish verbiage: Awesome quantities; site seethes at public’s unwillingness to popularize nom d’équipe “Digital Sherlocks”; insists so often it is relying only on “open-source information” that one doubts it; relies heavily on schlock military (“Narrative Arms Race”) and medical (“Infodemic”) metaphors to describe disinformation threat. 

“Hairball” graph: DFRLabs analysis of Wuhan rumors:



In the #TwitterFiles: Appears with frequency, with the “India List” of 40,000 names suspected of “Hindu nationalism” being a notable unfortunate episode:



In sum: DFRLabs is not only funded by the Global Engagement Center, and had initial GEC chief Richard Stengel as a fellow, but uses substantial state and corporate resources to evangelize GEC’s “ecosystem” theory of disinformation, which holds that views that overlap with foreign threat actors are themselves part of the threat.

Connected to: the Stanford Internet Observatory, University of Washington Center for an Informed Public, Graphika, Bellingcat, and the NYU Center for Social Media and Politics

​7.​ Stanford Internet Observatory 
Link: https://cyber.fsi.stanford.edu/io 

Type: Academic research institution 

You may have read about them when: The SIO is the parent of two foundational efforts at mass content surveillance and censorship: the “Election Integrity Partnership” created ahead of the 2020 presidential vote, and the “Virality Project” that created a single ticketing system for six major internet platforms for “misinformation” related to Covid-19 vaccines. As noted by head Alex Stamos, the EIP came together to “fill the gap” of things “the government could not do themselves.” Partners at DFRLabs added that the SIO’s Election Integrity Partnership “came together in June of 2020 at the encouragement of the U.S. Department of Homeland Security’s Cybersecurity and Infrastructure Security Agency, or CISA.” Research Director Renee DiResta is a former CIA fellow.

What we know about funding: Five-year grant from the National Science Foundation for $748,437. The EIP and Virality Projects also partnered with Graphika and DFRLabs, themselves recipients of funding from the Departments of Defense and State, respectively. SIO was founded with a $5 million grant from Craig Newmark and also receives funds from Omidyar, Gates, Hewlett and others.

What they do/What they are selling: As noted in two Twitter Files reports (see here and here), the twin SIO projects represented major efforts to build surveillance and flagging to scale across multiple platforms, seemingly as a proof-of-concept for a potential fully government-run enterprise like the Disinformation Governance Board, the program pushed by their partners at CISA.

Gibberish verbiage: Adept at generating imperious synonyms lauding themselves for being smart and from California (e.g. “constellation of problem solvers,” “coproducing expertise for critical infrastructure protection”). Birthed idea of “long fuse” of disinformation, suggesting speech dangers need to be cut off early.

“Hairball” graph: EIP analysis of “Glendale mail dump” rumors in 2020 Election, which incidentally were covered by CNN: 



In the #TwitterFiles: SIO perhaps appears in the TF more than any other academic, think tank or NGO partner. From an email to Twitter from the Virality Project: Twitter was told it should consider as “standard misinformation on your platform… stories of true vaccine side effects… true posts which may fuel hesitancy.” 

In sum: The Stanford Internet Observatory may or may not continue to have a high-profile role in building out the CIC, but figures like Renee DiResta and Alex Stamos have already fulfilled a substantial historical function by organizing cross-platform content sweeps for Covid-19 and the 2020 election. 

Connected to: Twitter, First Draft, Graphika, the University of Washington’s Center for an Informed Public, NYU’s Center for Politics and Social Media, the Aspen Institute, and the DHS agency CISA. 

​8.​ Poynter Institute / International Fact-Checking Network 
Link: https://www.poynter.org/; https://www.poynter.org/ifcn/

Type: Private think tank, once known as a media advocacy operation, now known more for the IFCN, which is essentially the in-house fact-checking arm of Facebook/Meta, as well as the fact-checking hub Politifact. Also produces the reporter-friendly widget MediaWise.

You may have read about them when: Trump was elected and Poynter sent an open letter to Mark Zuckerberg on behalf of “independent fact-checking organizations” telling him “Facebook should start an open conversation on the principles that could underpin a more accurate news ecosystem,” which Zuckerberg correctly interpreted as a call for his investment in those same organizations. Later Zuckerberg was challenged by Alexandria Ocasio-Cortez about the inclusion of The Daily Caller in its body of fact-checkers, and Zuckerberg tried to imply the IFCN was a fully independent body, leaving out both its funding relationship (see below) and its ability to exercise vetoes over IFCN members. Humor sidebar: Dr. Anthony Fauci was asked “Are you still confident that [Covid-19] developed naturally?” at a Poynter “Festival of Fact-Checking,” and stuns audiences by saying, “No, I’m not convinced of that.”

What we know about funding: Over $4 million a year goes from Facebook to IFCN partner organizations. Poynter and Politifact meanwhile list the Craig Newmark Foundation, the Koch Foundation, the Knight Foundation, the Omidyar Network, the National Endowment for Democracy, Microsoft, and the Washington Post as funders, among others. 

What they do/What they are selling: At-scale, enterprise effort to fact-check earth. Politifact, founded in 2007, transformed the entire idea of fact-checking, which used to be a private, in-house journalistic exercise, in which fact-checkers made sure reported statements were defensible and/or had a factual basis, a process designed to protect against litigation. Now, fact-checking is sold as an outward-facing, affirmative concept, in which things can be pronounced true/false by an institutional authority, whose judgments can then be used as the basis for algorithmic reviews. 

Characteristic/worldview quote: “Needs context.”

Gibberish verbiage: Little to none. IFCN/Politifact are mostly operated and maintained by people with relationships to journalism, and its products are designed to be consumed by broad audiences.

In the #TwitterFiles: In an election slack, the FBI asks about two tweets, and a Twitter trust and safety staffer cites Politifact as the authority for striking a piece of content, writing: “This is proven to be false via this.”

In sum: The IFCN in particular is a huge-scale fact-checking operation whose conflicted relationship with Meta/Facebook may provide a template for future truth contractors. 

​9.​ Integrity Initiative / Institute for Statecraft
Link: https://www.statecraft.org.uk/ for official page; link to Integrity Initiative documents leaked by Anonymous here.

Type: Shady-as-F spookworld surveillance and information control plan that will send you voiding in terror 

You may have read about them when: The hacker Anonymous in late 2018 published a series of documents showing the British Foreign Office funded a broad anti-disinformation scheme, centered around the construction of geographic “clusters” of anti-disinformation warriors under the guidance of Britain’s Institute for Statecraft. The initial list of cluster participants included many names who’d go on to become central players in anti-disinformation, from then-NATO press officer (and future Graphika Director of Investigations) Ben Nimmo to would-be Disinformation Governance Board chief Nina Jankowicz to ex-Obama defense official (and McCain Institute head) Evelyn Farkas to the journalist Anne Applebaum. The leak was big news in England, because it contained damning passages showing the British Foreign Office identified Jeremy Corbyn as a “useful idiot” for Russia, but made few headlines in the U.S. 

What we know about funding: The leaked documents showed 2016-2017 public funding of £296,500, with a planned increase to £1,961,000 the next year; those numbers were cited by multiple official bodies, including the UK parliament. 

What they do/What they are selling: All public traces of the Integrity Initiative, whose tweeting history showed wide interest in identifying Western figures as linked to Russia and other actors, were shut down after the Anonymous leak in late 2018. A subsequent report by the OSCR, the Scottish charity regulator, makes for frightening reading. It describes the activities of the Institute for Statecraft, technically listed as a “charity,” as “not entirely charitable,” adding that “one of its most significant activities, a project known as the Integrity Initiative, did not provide public benefit.”

Characteristic/worldview quote: “Although the principle [sic] target is Russian disinformation and influence, where appropriate clusters also consider other sources of interference where these interact with the Russians.” Also: “The cluster’s main means of influence is through select journalists.”

Gibberish verbiage: “Performance indicators” include “increased education of the younger generation on disinformation and threats.”

In the #TwitterFiles: FBI forwards to Twitter the British Parliamentary report on Russian influence: “We are grateful to those outside the Intelligence Community – in particular Anne Applebaum, William Browder, Christopher Donnelly, Edward Lucas and Christopher Steele – for volunteering their very substantial expertise on Russia.”

In sum: Straight Outta Orwell! The Integrity Initiative documents represent one of the most consequential intelligence leaks of all time — the very dirty underpants of NATO.

​10.​ National Conference on Citizenship / Algorithmic Transparency Institute 
Link: https://ncoc.org/ https://ati.io/

Type: A post-WWII, congressionally chartered civic organization that bizarrely has turned its attention to the cause of “anti-disinformation” and censorship. The Algorithmic Transparency Institute (ATI) is a sub-initiative of the NCoC.

You may have read about them when: They signed up as EIP and Virality Project partners to help “enable their analysts to monitor across networks.” Via its Junkipedia initiative, ATI contributed the creepy tactic of “civic listening” in order to “investigate narratives.” Junkipedia “enables manual and automated collection of data from across the spectrum of digital communication platforms including open social media, fringe networks, and closed messaging apps.” That’s right, they’ll even peer into your private conversations to “enable real-time situational awareness” in order to “counter problematic content.” Snitches can submit reports via “tiplines.” ATI will then “work with many newsrooms” and “pipe the resulting information into the proper state-focused channels for rapid response work.” You’ve been reported to the government. Taking it to the next level, ATI also runs the “Civic Listening Corps,” “a volunteer network of individuals trained to monitor for, critically evaluate, and report misinformation.”

Origins: ATI’s leadership emerged out of the Shorenstein Center’s soon to be closed Technology and Social Change Project. Cameron Hickey led the ATI and has since been promoted to CEO of NCoC. NCoC’s former board chair Garret Graff is director of the Aspen Institute’s cybersecurity and technology program. Graff was a key player in the Aspen Institute’s August 2020 Hunter Biden laptop “hack and dump” tabletop. As board chair, Graff’s record of following the rules is in question, given one is: “NCoC is strictly nonpartisan, and does not support or oppose any candidate or party.” 

What we know about funding: NCoC draws funding from many of the usual suspects, including Omidyar, Craig Newmark, and the Knight Foundation, as well as McArthur, Reset.tech, Rockefeller, Gates Foundation, and the Carnegie Corporation of New York.

What they do/What they are selling: Technology to monitor social media including private messaging, snitching to government and media, ethnic media coordination, training and volunteer coordination. 

Characteristic/worldview quote: “Viral misinformation is contagious and dangerous. Join the fight and stop the spread”; “centralize the collection of problematic content”; “a series of automated processes extract important data related to the content, like geographic location, engagement data, image text, and notable faces in images.”

Gibberish verbiage: “Effective inoculation messaging”

In the #TwitterFiles: Former NCoC board chair Garret Graff sent the now-infamous “Stephen was right” email outing Twitter, the New York Times, NBC News, the Washington Post, Rolling Stone, First Draft, CNN and more as having rehearsed their response in advance to the Hunter Biden laptop leak, before running their own disinformation campaign to counter what turned out to be a true story.

Other than that the only appearance is an Election Integrity Partnership “all hands” request from Stanford’s Alex Stamos that includes then Algorithmic Transparency Institute CEO Cameron Hickey.

In sum: Often the technical and “communities” partner in censorship initiatives. In promoting Cameron Hickey to NCoC CEO, the logic of ATI has now been ported to a large-scale congressionally chartered organization. 

​11.​ Park Advisors 
Link: https://www.state.gov/defeat-disinfo/

Type: For-profit firm funded by the State Department’s Global Engagement Center (GEC) specializing in “solutions to pressing issues such as Disinformation, Terrorism, Violent Extremism, Hate Speech, Human Trafficking, and Money Laundering.”

You may have read about them when: Park Advisors received funding from the GEC’s Technology Engagement Team (TET) in 2018 to develop Disinfo Cloud, a dashboard for evaluating and implementing counter-disinformation tools. In addition to Disinfo Cloud, TET commissioned the study “Weapons of Mass Distraction: Foreign State-Sponsored Disinformation in the Digital Age,” presenting vulnerabilities to disinformation on social media platforms. Park Advisors also collaborated with the Department of Homeland Security’s Cybersecurity and Infrastructure Security Agency (CISA), Dutch media group DROG, and GEC to create the game “Harmony Square,” which it claims is a “psychological ‘vaccine’ against disinformation.”

What we know about funding: Direct funding from the U.S. Department of State GEC on Disinfo Cloud and disinformation studies.

What they do/What they are selling: Created a digital database for tools and technologies aimed at countering disinformation and propaganda for corporate clients, academics, as well as U.S. and foreign government partners. Long-form reports on disinformation vulnerabilities, international policy expertise and international counter-terrorism coordination tools.

Characteristic/worldview quote: “A growing number of states, in the pursuit of geopolitical ends, are leveraging digital tools and social media networks to spread narratives, distortions, and falsehoods to shape public perceptions and undermine trust in the truth.” 

Goofy graph: 



Closely connected to: The Census Bureau, U.S. Congress, Department of Defense, Department of Energy, Department of Homeland Security, Department, Department of State, Federal Bureau of Investigation, Office of Global Affairs, Office of the Director of National Intelligence, the Treasury Department, U.S. Agency for Global Media, and the U.S. Department of Agriculture

In sum: A now defunct (and hard to find) disinformation advisory group, connected to GEC, that created a digital testbed for “counter-disinformation” tools

​12.​ New Knowledge AI, rebranded as Yonder AI, acquired by Primer
Link: https://primer.ai/products/yonder/

Type: For-profit internet company that worked for brands and national security entities searching platforms for narrative control, along with detecting narrative manipulation from malign actors. 

You may have read about them when: New Knowledge did a much publicized report for the Senate Intelligence Committee in 2018 that said Russians saturated U.S. social media with disinformation to influence the 2016 election. Days after research director Renee DiResta delivered the report, the media revealed that New Knowledge, working with a former Obama White House aide, had run an online dirty tricks operation intended to make it appear that the Kremlin supported the Republican running for Senate in Alabama. They did it by creating thousands of fake Russian Twitter followers for candidate Roy Moore, who narrowly lost the race. The operation was funded by LinkedIn founder Reid Hoffman. New Knowledge was paid $100,000 for the Alabama campaign. Tax records show its parent corporation, Popily, Inc., was paid $575,000 for research consulting by Advance Democracy, a non-profit run by oppo researcher Dan Jones, a Democratic Party liaison to Silicon Valley funders. New Knowledge created an election dashboard called Disinfo2018 for Jones’ Advance Democracy. (See entry 48.)

Also: New Knowledge founder Jonathan Morgan was one of the creators of the Hamilton 68 dashboard, under the auspices of the Alliance for Securing Democracy. Former FBI agent Clint Watts was a frontman for the dashboard and made it among the biggest sources of news in the lead up to the midterm elections. Hamilton 68 claimed to track Russian disinformation by monitoring 644 active Russian accounts. The Twitter Files have revealed that most of the accounts Hamilton 68 monitored belonged to Americans, not Russians. 

What we know about funding: Morgan founded New Knowledge in Austin in 2015. He and DiResta have told interviewers they were consulted by the Obama White House as concerns grew about the internet being used by ISIS, white supremacists, and other bad actors. Within a year, it had 50 employees, Morgan told the Austin American Statesman. Some had been analysts in the intelligence world; Morgan had worked on two open-source programs for Defense Advanced Partnerships Research Agency (DARPA), he has said; another senior official spent 15 years at the NSA. New Knowledge had $30 million in investment money. He sought more investments after the Alabama scandal led to a “rebrand” of the company in 2019 to “Yonder AI." Investors include Lux Capital, Geekdom Fund, GGV Capital, Buildgroup, Capital Factory and Kelly Perdew, co-founder of Moonshots, owner of Fast Point Games. Lux Capital advisory board member, and former SOCOM Commander Tony Thomas, also sits on the Primer advisory board. 

What they are selling: Management of brand narratives and narrative manipulation detection and analysis. New Knowledge/Yonder searched for certain words and avatars it assessed were often used by particular groups of malign users. Seeking user language that reveals “contextual narratives” helped detect subtle signs of manipulation across accounts.

Worldview quote: “Yonder is on a mission to humanize the world’s information and deliver on the promise of a more authentic internet…Yonder will talk to the industry about an ethical framework for AI.”

Gibberish verbiage: “The Yonder platform is the first to map the faction internet, finding, describing and measuring the impact of factions on conversations that matter to customers.” 

In the #TwitterFiles: Former Head of Trust and Safety at Twitter, Yoel Roth, on “Hamilton 68” account owners: 

“These accounts are neither strongly Russian nor strongly bots.”
“No evidence to support the statement that the dashboard is a finger on the pulse of Russian information ops.”
“Hardly evidence of a massive influence campaign.”
“I think we need to just call this out on the bullshit it is.”

​13.​ Moonshot CVE 
Link: https://moonshotteam.com

Type: For-profit tech company working with public and private industry partners to detect and prevent online hate.

You may have read about them when: Moonshot, working with the U.S. Military Academy, produced a report on domestic violent extremism within the military. The report included the geolocation of service members searching specific hate terms, identifying concentrated areas on military bases. The parameters of the study came under scrutiny due to the terms and phrases considered “hate speech,” including “the truth about Black Lives Matter.” Moonshot’s goal, once they identify patterns of online searches for hate and extremist ideology, is to use their “redirect method,” sending advertisements to guide people away to “constructive alternative messages.” The redirect method came under flack when it directed people to a prior-felon touting anarchist and antisemitic views. The tech company has received additional criticism based on co-founder Vidhya Ramalingam’s connection to the Obama Foundation, as a part of the Leaders Europe program.

What we know about funding: Moonshot, since its founding in 2015, has primarily been financed by venture capital firms, such as Beringea and Mercia. 

What they do/What they are selling: Online threat monitoring and reporting services, including periodic and “incident response” reporting. Moonshot also markets intervention capabilities, including counter-messaging and their aforementioned “Redirect Method.” 

Characteristic/worldview quote: “A growing number of states, in the pursuit of geopolitical ends, are leveraging digital tools and social media networks to spread narratives, distortions, and falsehoods to shape public perceptions and undermine trust in the truth.” 

Goofy graph: 



Connected to: Obama Foundation, Department of State, Wilson Center, Anti-Defamation League, Institute for Strategic Dialogue, Google Jigsaw

Worldview quote: “The lessons learned in addressing the underlying drivers to violent extremism offline simply weren’t being applied effectively online, where extremist propagandists and recruiters continue to prey on vulnerable individuals… we work to better understand and disrupt disinformation networks, gender-based violence, child sexual abuse and exploitation, and organized crime, among other harms.” 

​14.​ Annenberg Public Policy Center (home of Factcheck.org) 
Link: www.annenbergpublicpolicycenter.org

Type: Privately funded Public Policy Research Center affiliated with the Annenberg School of Communication at the University of Pennsylvania.

You may have read about them when: “APPC’s motto is ‘Research and Engagement That Matter,’ and its work has informed the policy debates around campaign finance, children’s television, internet privacy, tobacco advertising, the tone of discourse in Washington, and disinformation. Scholars at the policy center have offered guidance to journalists covering difficult stories, including terrorist threats, suicide, mental health, the Zika virus, and vaccination hesitancy.” 

What we know about funding: Seed and ongoing funding for the center came from a $2 billion bequest from Walter Annenberg, a businessman and Richard Nixon’s choice for Ambassador to the Court of Saint James (UK) from 1969-1974 who owned “Triangle Publications” which featured Seventeen Magazine, The Daily Racing Form, and TV Guide under their media umbrella.



What they do/What they are selling: A forum for discussions of key public policy issues, an educational spin-off, research in elections, child-rearing, suicide prevention, civics and mental health, and factcheck.org. 

Characteristic/worldview quote: “The Annenberg Public Policy Center community celebrates the life and mourns the passing of statesman George P. Shultz, who served as secretary of state under President Ronald Reagan and secretary of labor and treasury under President Richard Nixon, and was a close friend of Ambassadors Leonore and Walter Annenberg. Shultz was also a longtime friend of the Annenberg Public Policy Center (APPC) of the University of Pennsylvania and The Annenberg Retreat at Sunnylands, where he was a frequent guest.”

Gibberish verbiage: “The Transatlantic High Level Working Group on Content Moderation Online and Freedom of Expression is seeking to identify and encourage adoption of scalable solutions to reduce hate speech, violent extremism and viral deception online, while protecting freedom of expression and a vibrant, global internet.” (Source)

Sample graph:



Twitter Files Reference: The University of Pennsylvania Distinguished Fellow and Project Director Susan Ness, who was appointed a Commissioner at the Federal Communications Commission by President Clinton in 1994, sent Twitter’s Nick Pickles a final report from the Transatlantic Working Group’s final report on Moderating Content online and Freedom of Expression, in preparation for a “candid and off-the-record conversation.”



In Sum: The Annenberg Public Policy Center is one tentacle of the Annenberg Foundation’s larger influence operation masquerading as a think tank. Its analysis is informed by and ultimately loyal to the ghosts of Richard Nixon, Ronald Reagan, Queen Elizabeth and Walter Annenberg (the guy that used to publish the “Daily Racing Form” which is “known for being America’s Turf Authority since 1894 and provides news and data to horse racing enthusiasts).”  

​15.​ German Marshall Fund’s Alliance for Securing Democracy 
Link: democracy.gmfus.org 

Type: Public Policy Think Tank/ Grant-making institution. 

You may have read about them when: They helped fund or served as a pass-through vessel for State Department money going to Hamilton 68, a 2016 effort to “track Russian interference” that applied the “Russian influence” label to people who were not being influenced by the Russians, but were skeptical of one thing or another in the broader narrative adopted by the Atlantic Council, Stanford Internet Observatory, Brookings, or the National Endowment for Democracy. 

What we know about funding: “The German Marshall Fund of the United States was founded in 1972 through a gift from Germany as a tribute to the Marshall Plan.” Their funders at the $1 million dollar level and above include the European Commission, the Directorate General for Neighbourhood and Enlargement Negotiations, Auswaertiges Amt, the Ministry of Foreign Affairs of Norway, the U.S. Agency for International Development and the Swedish Ministry for Foreign Affairs. At the $100-999K level, funders include Google, Microsoft, Open Society, Rockefeller Foundation, the Charles Mott Foundation (who also fund Clemson University’s disinformation efforts), the Knight Foundation, Latvia’s Ministry of Defense, and the Ministry of Foreign Affairs for Belgium. 

What they do/What they are selling: In the “priorities” section of their website it’s noted that “GMF works on issues critical to transatlantic interests in the 21st century, including the future of democracy, security and geopolitics, alliances and the rise of China, and technology and innovation.”

Characteristic/worldview quote: “The surge of authoritarian threats, political polarization, and widening social inequalities continue to fuel democratic backsliding and undermine the democratic values on which our systems and institutions rest. The urgency to confront these global crises require societies to strengthen their resilience and reimagine democracy’s future.” From Future of Democracy

Gibberish verbiage: “Laissez-faire globalization is at the breaking point. The Covid-19 pandemic and Russia’s invasion of Ukraine finally exposed the fragility of the global economic system after decades of strain caused by the rise of China, and exacerbated by climate change and growing inequality. Now, U.S. leadership is needed to ensure that nationalist and authoritarian forces do not fill the resulting structural vacuum in an increasingly digital world. A new roadmap is needed for how democracies and their allies will address the technological challenges of the 21st century.” From “The New American Foreign Policy of Technology” 

Infamous “Hamilton 68” graph: 



Twitter Files Reference: The ASD-created Hamilton 68 is detailed in Twitter Files#15 and is the subject of many, many Twitter communications about suspected Russian bot accounts. Twitter executives like Carlos Monje were anxious to stay close to the “longer game” rather than confront the ASD about the Hamilton 68 problem. 

In sum: The German Marshall Fund is a large pass-through for funding from the U.S. and other NATO governments as well as the largest industrialists in those nations to try to shape public perception through front organizations. 

​16.​ Ad Council
Link: https://www.adcouncil.org/

Type: Nonprofit/Media

You may have read about them when: They started the drunk driving prevention campaign “Friends Don’t Let Friends Drive Drunk,” and also created the Smokey the Bear character. 

What we know about funding: The Ad Council is funded by the largest companies in the world. Comcast, Google and Meta all gave Ad Council more than $400K, while Adobe, Apple, Johnson & Johnson, Disney, TikTok, Verizon and Walmart gave between $300-399K. Donations in the $200-299K bracket came from Accenture, Amazon, Bank of America, Pfizer, and Twitter, among others. IBM, Fox, JP Morgan Chase kicked in at the 150K-199K level, but virtually all its funding comes from Fortune 500 corporations. 

What they do/What they are selling: The Ad Council attempts to influence large numbers of people through advertising for what it considers the public good. Initially founded in 1941, they were known as the War Advertising Council, and ran campaigns to promote women in the workplace, due to the massive influx of men into the military. 

Characteristic/worldview quote: “The Ad Council’s mission is to convene the best storytellers to educate, unite and uplift—by opening hearts, inspiring action and accelerating change. We won’t stop until we live in a society where every single person can thrive.”

Twitter Files Reference: One of Twitter’s main four Covid-19 misinfo advisors. Specifically, advanced a project to increase vaccine demand:



In sum: An advertising behemoth created by the largest corporations in WWII to sell war is still, well, doing that. 

​17.​ Clemson University Media Forensics Hub
Link: https://www.clemson.edu/centers-institutes/watt/hub/

Type: Public-Private Research Institute

You may have read about them when: They were formed in 2020 “in order to build upon the nationally recognized research performed by Clemson University faculty who were among the first to identify the organized campaign of Russian interference in the 2016 U.S. presidential election.” Clemson University Media Forensics hub scholars published “The Real Target of Authoritarian Disinformation” in Foreign Affairs about Russia’s “Internet Research Agency”; they’ve worked with the Senate Select Committee on Intelligence, the Department of Homeland Security, Federal Law Enforcement agencies and the U.S. Army Cyber Command. 

What we know about funding: $3.8 million grant from the Knight Foundation to study and fight online disinformation in November of 2022 (matched by Clemson University to bring total investment to $7.6 million). They are housed in a building constructed with a $5.5 million dollar gift from Dr. Charles Watt, who was formerly Dean of Clemson’s College of Business and Behavioral Science, a defense contractor businessman with a contract with SPAWAR Charleston (now known as NAVWARSYSCOM, the Navy’s Electronic Systems Command). One of Watt’s specialties was in what the military calls C3I—(Command, Control, Communications, Intelligence) & C4I (Command, Control, Communications, Computers, Intelligence). Before that he was the Director of Defense, Test and Evaluation in the Office of the Secretary of Defense during the Reagan Administration when the priority of that office was the Strategic Defense Initiative.

What they do/What they are selling: Multi-disciplinary research with “direct social impacts.” A mission statement full of buzzwords about the “common good”, tools for social media analysis such as Botometer (checks an account’s activity and gives it a score indicating the likelihood it is a bot) or Tweetbeaver (works at a granular level, digging out information from your or any public account) 



“Researchers with the Hub study disinformation and inauthenticity online and create tools to educate people and stop the spread of disinformation.” These tools include “help[ing] older adults recognize online scams and disinformation,” “troll spotting” and the “Convergence Accelerator” in cooperation with the USG’s National Science Foundation. “The Convergence Accelerator program model includes three phases: topic identification and convergence research phases 1 and 2. Teams that complete the convergence research phases are expected to deliver high-impact solutions that meet societal needs and continue to have an impact after NSF support ends.”

Characteristic/worldview quote: Mission Statement: “The Media Forensics Hub at Clemson University builds society’s capacity to understand the context, origins, and impact of modern media. As part of the Watt Family Innovation Center, we accomplish this by connecting scientific expertise with practical application.”

Gibberish verbiage: One study of Russian and American partisan groups “explored how their operations deviated from canonical state propaganda marked by symbols of national identity and heroic masculinity” (Russia: Strategy/Tactics/Impact 2021)

Twitter Files Reference: In 2020, Twitter’s Nick Pickles wrote that he shared Yoel Roth’s frustration that CUMFH “didn’t take any sort of guidance” on what they’ve found vis a vis the Internet Research Agency. Roth in another email added that Clemson researchers were “too chummy with HPSCI,” i.e. the House Intel Committee, and didn’t “have the chops.” 



In sum: Communications professors at Clemson managed to secure a lot of funding from a retired academic and defense contractor who played a very critical role in the Strategic Defense Initiative under the Reagan Administration for a social media analysis/disinformation center, built largely to feed information to journalists that Twitter’s own analyses consistently refuted. 

​18.​ Cybersecurity and Infrastructure Security Agency (CISA) 
Link: www.cisa.gov

Type: Government agency; a division within the Department of Homeland Security that is the “operational lead for federal cybersecurity and the national coordinator for critical infrastructure security and resilience.” Founded in 2018, it quickly took on a role in election security, declaring the electoral process critical national infrastructure. 

You may have read about them when: Their inaugural director, Christopher Krebs, was fired by President Donald Trump via tweet after CISA released a statement, saying on November 12, 2020, “The November 3rd Election was the most secure in American history.” 

What we know about funding: Reportedly, a $3 billion dollar budget.

What they do/What they are selling: CISA is supposed to be the lead agency on protecting critical infrastructure and repelling cyber-attacks; “designed for collaboration and partnership,” CISA also partners with civilian corporations, universities and research centers, notably including Stanford’s Election Integrity Partnership. 

Characteristic/worldview quote: “CISA’s cybersecurity mission is to defend and secure cyberspace by leading national efforts to drive and enable effective national cyber defense, resilience of national critical functions, and a robust technology ecosystem.” Their motto is “defend today, secure tomorrow.”

Gibberish verbiage: At the 2020 RSA Conference, Director Chris Krebs explained that the agency has an additional motto — “cybersecurity has a posse” — underscoring the role everyone plays in building resiliency and defending the nation from cyber threats.

“We send [threat information] out in an anonymized way,” Krebs explained. “What we’re trying to do here is understand the landscape — understand the conditions on top of it, and what the adversary might be doing — and get that out so the next victim might not happen. This is particularly important in the broader ransomware conversation.”

Twitter Files Reference: In an email from Special Agent Elvis M. Chan of the FBI to Yoel Roth, a formal relationship between Twitter, the FBI, and CISA is outlined:



In sum: A new sub-agency of Homeland Security with a monster budget, strong university connections, and a giant purview to the middle of a bureaucratic morass of various other federal agencies and departments, all of whom also have a piece of the Cybersecurity and Infrastructure protection portfolio; has rivals in DoD, Department of Energy, FBI, Secret Service and among the intelligence community. 

​19.​ Bellingcat 
Link: https://www.bellingcat.com/

Type: For-profit Netherlands based investigative journalism organization that seems mostly to investigate and/or denouonce the practitioners of journalism. 

You may have read about them when: Bellingcat is an independent investigative journalism organization, self-styled as an “Intelligence Agency for the People.” It was founded by former Atlantic Council DFRLabs fellow, Eliot Higgins. In the intelligence agency spirit, Bellingcat’s staff and contributors are littered with former intelligence and government officials. For instance, multiple contributors work at the Center for Information Resilience, a counter-disinformation non-profit with former “disinformation czar” Nina Jankowicz as their vice president. To add to its spook persona, the journalism collective receives funding from the National Endowment for Democracy (NED), a shadowy organization called the “sugar daddy of overt operations” by the Washington Post, doing “openly what had once been unspeakably covert – dispensing money to anti-communist forces behind the Iron Curtain.” Bellingcat was named in a proposed consortium of counter-disinformation NGOs — including the Atlantic Council’s DFRLabs — called the EXPOSE Network, organized by the Zinc Network under the UK’s Counter Disinformation and Media Development Programme. This revelation was included in the 2018 release of the Institute of Statecraft’s Integrity Initiative documents by the hacktivist group Anonymous.

What we know about funding: While Bellingcat touts that it doesn’t solicit or accept funding or contributions directly from any “national government,” NED has been a donor since at least 2017. That same year, Bellingcat received funding from Meedan, one of Twitter’s trusted Covid-19 disinformation sharing partners. In 2020, Bellingcat received €160,000 from Zinc Network, a communications network that designs “behavioral science informed interventions that change attitudes and actions.” 

What they do/What they are selling: Independent investigative journalism, relying heavily on open source intelligence (OSINT). 

Characteristic/worldview quote: “Even seemingly ‘harmless’ disinformation normalizes the distortion of reality, with potentially deadly consequences.”

Closely connected to: The Open Societies Foundation, Human Rights Foundation, NED, Zinc Network, Integrity Initiative, Graphika, Atlantic Council/DFRLabs.

In sum: The “independent” journalist consortium’s spook-a-rific investor group and malodorous contributor roster call into question its agenda-free reporting.

20.​ Center for European Policy Analysis (CEPA)
Link: https://cepa.org/

Type: CEPA is a nonprofit public policy institution based in Washington, D.C. with the mission “to ensure a strong and enduring transatlantic alliance rooted in democratic values and principles.”

You may have read about them when: CEPA employees are frequently quoted in the news about European affairs and on the Russia-Ukraine war. It said “US complicity” in the sabotage of Nord Stream pipelines was “disinformation.” On March 29, 2023 CEPA published an article concluding “Russia remains the likeliest culprit” of the destruction of the Nord Stream pipelines.

CEPA has been a proponent of escalating the war on online misinformation. It has proposed that U.S. and European sanctions against Russia should include bans of “Russian officials and oligarchs from Twitter, Facebook, and YouTube.” In an article entitled “Midterm Alert: Silicon Valley is Losing the Fight Against Misinformation,” CEPA concluded: “Social media companies acknowledge the pervasiveness of mis- and disinformation on their platforms and the threat it [sic] poses to democracy. They now need to step up their investments to combat the scourge.”

What we know about funding: CEPA’s list of supporters for the 2022 Fiscal Year includes the National Endowment for Democracy (which is heavily funded by the U.S. government), the NATO Public Policy Division, Lockheed Martin, Microsoft, Amazon Web Services, BAE Systems, Google, the Russia Strategic Initiative, U.S. European Command (Department of Defense), and the U.S. Department of State. The State Department and Department of Defense have (combined) provided over $1 million in grants to CEPA since 2016. CEPA’s December 2020 report on Democratic Offense Against Disinformation was “co-funded by the European Union.”

What they do/What they are selling: CEPA aims to further transatlantic cooperation on issues such as the support of democracy, digital regulation, and defense. One of its main goals is to “ensure the United States and its closest allies can maintain their strategic edge in an increasingly contested world.” It employs a number of “experts” who bring “innovative policy solutions to the most critical issues facing the transatlantic alliance.”

Characteristic/worldview quote: “Democracies aren’t good” at spreading disinformation. Source

Gibberish verbiage: “NATO should emphasize the role it can play in defending all humans that share transatlantic values — not necessarily through military interventions but through diplomatic, humanitarian, and political means.” Also: “Our cutting-edge analysis and timely debates galvanize communities of influence while investing in the next generation of leaders to understand and address present and future challenges to transatlantic values and principles.”

Twitter Files Reference: An e-mail from Dr. Alina Polyakova, President and CEO of CEPA, to Twitter’s Nick Pickles, hinting at info about the head of the GEC. Polyakova is also included in Twitter’s elite disinformation Signal group.



Closely connected to: Brookings Institute, Atlantic Council/DFRLabs, European Union, State Department, Department of Defense, SIO, Graphika, GEC.

In sum: CEPA seeks to advance transatlantic political “values” and strengthen transatlantic cooperation to “ensure our collective defense and future security.”

​21.​ Center for an Informed Public at the University of Washington 
Link: https://www.cip.uw.edu

Type: An academic “multidisciplinary research center” with the mission to “resist strategic misinformation, promote an informed society and strengthen democratic discourse.”

You may have read about them when: CIP co-founded the Virality Project, along with the Stanford Internet Observatory, NYU’s Center for Social Media and Politics and Tandon School of Engineering, Graphika, DFRLabs, and the National Conference on Citizenship. The Virality Project “worked with social media platforms to flag and suppress commentary on Covid vaccines, science, and policy that contradicted public health officials’ stances, even when that commentary was true.” The Virality Project also described opposition to Vaccine Passports as anti-vaccine behavior, and would describe as disinformation “events” things like a news story that "increased distrust in Fauci’s expert guidance.” CIP also participated in The Election Integrity Partnership, (EIP) along with the Stanford Internet Observatory, Graphika, and DFRLabs. The EIP, a proponent of aggressive social media censorship, partnered with the Cybersecurity and Infrastructure Security Agency in 2020 and released a report on misinformation during the 2020 election. 

What we know about funding: In 2019 The University of Washington was awarded $5 million in funding from the John S. and James L. Knight Foundation to establish the CIP. In June 2021, the CIP announced a “$1 million gift from Craig Newmark Philanthropies to support the multidisciplinary research center’s rapid-response research of election-related mis- and disinformation.” August 2021: The CIP announced a $3 million grant from the National Science Foundation “to apply collaborative, rapid-response research to mitigate online disinformation” in partnership with the Stanford Internet Observatory. The CIP received $2.25 million from that grant. Other funders include Microsoft and the University of Washington’s iSchool, Technology & Social Change Group, and Population Health Initiative.

What they do/What they are selling: CIP has undertaken projects that research misinformation and projects that look into how fact-checking can be scaled and sustained online without compromising quality. CIP researchers have written about ways to combat misinformation online, and CIP holds workshops for high schoolers on how to spot misleading information, debunk data and improve reasoning skills.

Characteristic/worldview quotes: “We have assembled world-class researchers, labs, thought leaders, and practitioners to translate research about misinformation and disinformation into policy, technology design, curriculum development, and public engagement.” From Jevin West, Center co-founder: “I study the Science of Science and worry about the spread of misinformation. My laboratory consists of millions of scholarly papers and public posts about science.” 

Gibberish verbiage: “Explore the depths of misinformation with fun and collaborative games.”

Twitter Files Reference: The Virality Project and the EIP - projects the CIP helped form and lead - were involved in flagging content and recommended social media platforms take action against “true content which might promote vaccine hesitancy.”

Closely connected to: Virality Project, Election Integrity Partnership, Stanford Internet Observatory, Graphika, NYU CSMaP and Tandon School of Engineering, the National Conference on Citizenship, DFRLabs, Aspen Institute, Information Futures Lab/First Draft.

In sum: Through public and private financing, the CIP used its academic status to help with some of the largest censorship efforts targeting speech relating to the 2020 election and Covid-19. 

​22.​ Aspen Institute 
Link: www.aspeninstitute.org 

Type: The Aspen Institute is a neoliberal global nonprofit ostensibly “committed to realizing a free, just, and equitable society” that has the rep (and the geographical profile) of an American Davos. 

You may have read about them when: The Aspen Institute holds its annual “Ideas Festival” and summits featuring state leaders and elected officials of both parties, notable bureaucrats, journalists and professors, executives and “thought leaders.” Highlights from Aspen include:

Blocking the release of then-New York City mayor Michael Bloomberg’s endorsement of stop-and-frisk tactics and the seizure of “guns from male minorities between ages 15 and 25.”

Columbia law professor Timothy Wu, before his appointment to President Biden’s National Economic Council, argued at the Aspen Ideas Festival that “traditional speech freedoms need to be rethought in the Internet/Trump era.” 

In 2020, the Aspen Institute and Stanford’s Cyber Policy Center urged journalists to “Break the Pentagon Papers principle” and not cover leaked information to prevent the spread of “disinformation.”

A 2021 “Disinfo Discussion” featured Steve Hayes, the author of “The Connection: How al Qaeda’s Collaboration with Saddam Hussein has Endangered America.”

What we know about funding: The Aspen Institute is a fundraising powerhouse, receiving over $140 million in contributions and grants in 2021. According to USAspending.gov, the Aspen Institute has received tens of millions of dollars in grants and contracts from the U.S. government, primarily from the State Department, but also from USAID.

The following entities and foundations are listed by Aspen as donors of over $500,000 or more, with many donating over $1 million: the Bill and Melinda Gates Foundation; Johnson & Johnson; JP Morgan Chase Foundation; Walmart; Blackrock; and the Open Society Foundation.

What they do/What they are selling: The Aspen Institute markets itself as a leader in bringing together leaders from a variety of fields – government, scholarship, business – “to address some of the world’s most complex problems.” The Aspen Strategy Group, co-chaired by Condoleezza Rice, holds annual forums to “provide a bipartisan forum to explore the preeminent foreign policy challenges the United States faces.”

Characteristic/worldview quote: “We’re building a more inclusive economy through our partnership with Mastercard.”

Gibberish verbiage: Nervous tic around the word “infodemic,” resulting in an infodemic video series providing a deep dive “into the costs of science misappropriation and denialism and offering solutions to the challenges science faces globally,” as well as an infodemic virtual panel led by Dr. Claire Wardle, who “offered a clear and concise picture of what disinformation is, and how we might go about protecting our society from it.” They even discussed the infodemic as a problem feeding “distrust in our institutions” that “affects all aspects of modern life.” But, good news: “The Private sector will stand up for trust and fight the infodemic.”

Twitter Files Reference: Garret Graff, Head of Aspen Digital, sent an invite email to Facebook, First Draft, Twitter, The Carnegie Endowment for International Peace, Yahoo! News, and others. He states “Bring your most devious and cynical imaginations! Please keep this document confidential to yourselves; for various reasons, we don’t want this to circulate widely.”



He also jokes after the  release of the laptop:



Closely connected to: The State Department, the Stanford Internet Observatory, First Draft/Information Futures Lab; the National Conference on Citizenship, and the Shorenstein Center on Media, Politics, and Public Policy, in addition to a boatload of mainstream media figures and international wine-set celebs like Prince Harry. 

In sum: The Aspen Institute is an influential organization that receives tens of millions of dollars in funding from the U.S. government to comprehensively advance solutions to the world’s problems so that we don’t have to.

​23.​ Trusted News Initiative 
Link: www.bbc.com/beyondfakenews/trusted-news-initiative

Institution: Trusted News Initiative

Type: Trusted News Initiative is a partnership “founded by the BBC” that includes media and technology organizations from around the world, including Google and YouTube, Microsoft, Facebook, Twitter, The CBC, The Washington Post, AP, Thomson Reuters, the Information Futures Lab/First Draft, and several more. Its members collaborate “to build audience trust and to find solutions to tackle challenges of disinformation.”

You may have read about them when: The Trusted News Initiative established an “early warning system of rapid alerts to combat the spread of disinformation” during the 2020 election. According to Variety, TNI partners would alert each other to disinformation that threatened the “integrity of the election so that content can be reviewed promptly by platforms.”

RFK Jr and a host of other plaintiffs have brought legal action against The Trusted News Initiative and many of its members, accusing them of suppressing information and debate on Covid-19.

What we know about funding: There are few details about its funding or the level of resources contributed by its members, beyond obviously the relationship to the BBC. We do know its expansion to an Asia-Pacific network was “funded by the Google News Initiative.”

What they do/What they are selling: Real-time combating of disinformation relating to issues such as elections and Covid-19.

Characteristic/worldview quote: “We’ll do everything we can, working together, to stop disinformation about Coronavirus in its tracks.”

Gibberish verbiage: Information Apocalypse. The Covid-19 pandemic brought about the “long-prophesied Information Apocalypse.” For the journalists covering disinformation: “Don’t face the Information Apocalypse alone.”

Twitter Files Reference: Claire Wardle in May 2019 mentions “BBC Media Action who were in the room told us about this ridiculous database they have. It lists the sources of information people trust around the world localized by country, region and sector of the population (farmers, teachers, etc).”



Closely connected to: Big tech and big media, and anti-disinformation groups like Information Futures Lab/First Draft.

In sum: A mammoth anti-disinformation initiative bringing together the biggest media and tech companies on the planet.

​24.​ Automated Controversy Detection 
Link: https://www.aucode.io

Type: An tech startup focused on “misinformation and controversy” emerging out of the University of Massachusetts Amherst. AuCoDe was awarded a $1 million National Science Foundation grant in November 2020 to tackle “disinformation” using artificial intelligence. They are a core partner on Meedan’s NSF-funded Fact Champ initiative to “increase collaboration between fact-checkers, academics, and community leaders to counter misinformation online.” 

You may have read about them when: AuCoDe take it to the next level, leaving countering misinformation in their wake and showing just how close the “anti-disinformation” industry is to the cultural zeitgeist. AuCoDe is concerned that “ideas are being spread uncontrollably online.” Luckily they have a “detection algorithm” that can “tell what’s important and potentially opinion-shifting before things become viral” making “communication more productive and less dangerous.” In this way they create a “new standard for nuanced community discussions.” In addition, they do “toxicity monitoring” and have a product called “Detoxify,” to help you “avoid unwanted content that triggers you.”  No misinformation, all narrative control – but done under the anti-misinformation banner. Founder Shiri Dori-Hacohen has now moved to the University of Connecticut’s Reducing Information Ecosystem Threats (RIET) Lab. The mission creep continues.

What we know about funding: The National Science Foundation has provided almost all publicly reported funding

What they do/What they are selling: AI based technology services for surveilling online conversations

Characteristic/worldview quote: “Avoid unwanted content that triggers you”

Connected to: Meedan, the Reducing Information Ecosystem Threats (RIET) Lab, Annenberg Public Policy Center/Factcheck.org, the University of Massachusetts at Amherst, the School of Communication and Information at Rutgers University-New Brunswick

In sum: Automated Controversy Detection takes anti-misinformation mission creep to the next level with its open and explicit AI-driven approach to surveilling “content that triggers you.”

​25.​ Center for Countering Digital Hate
Link: https://counterhate.com/

Type: An NGO cut-out engaged in brazen smearing, attacking of dissenting views, deplatforming, censoring and pro-active shrinkage of the Overton window.

You may have read about them when: They issued a report called the “Disinformation Dozen” which sought to “deplatform” dissident Covid thinkers from Substack, including RFK Jr, smearing them as “anti-vaxxers.” CCHD are experts in strategically conflating serious voices with the fringes, mixing them together to isolate genuine actors and squash dissent. What is unique about CCHD is its blatant distortions, vicious tone, and cynical appropriation of anti-racist, anti-sexist, and public health rhetoric. The group promotes explicitly pro-censorship and deplatforming positions, and pushes the boundaries of the new normal. Founder Imran Ahmed is connected to senior UK Labor Party figures. Current campaign work focuses on pressuring advertisers to leave Twitter due to Musk making it a “safe haven for hate and intolerance.”

What we know about funding: CCHD doesn’t declare its funding on its site, though filings show its UK registration (they are also US-registered) received almost £1m GBP in 2022.

What they do/What they are selling: Aggressive targeting of “misinformation” particularly on Covid but also related to climate, including campaigns with strong access to media outlets.

Characteristic/worldview quote: “Who are the anti-vaxx Substack millionaires?” “Science matters. Lies can kill.” “CCDH has forced social media companies to establish precedent and remove hateful or dangerous content, by holding them directly accountable for amplifying and profiting from it.​” “Campaigns such as Stop Funding Misinformation reduce the reach of websites that masquerade as real news but in fact spread conspiracy theories, lies and hateful propaganda.”

In the #TwitterFiles: 12 Attorneys General write to Twitter and Facebook on March 24, 2021, asking them to take action on the “disinformation dozen,” referencing the Center for Countering Digital Hate. They state: “As safe and effective vaccines become available, the end of this pandemic is in sight.” On April 1, days later, Twitter adds labels and gives strikes to all the accounts, and permanently suspends one person.



In sum: Institutional anger-merchant NGO with a murky background and bulldog mentality ready to attack all and sundry, to institute their regime of censorship.

​26.​ Craig Newmark Philanthropies 

Link: https://craignewmarkphilanthropies.org/

Type: A large philanthropy founded by the inventor of Craigslist, with a special focus on journalism and disinformation.

You may have read about them when: Along with Omidyar and the Knight Foundation, Craig Newmark is perhaps the most prolific private funder of projects combating “disinformation.” He provided foundational grants to a wide range of institutes including the Stanford Internet Observatory, Columbia University’s Craig Newmark Center for Journalism Ethics and Security, the Institute for Rebooting Social Media at Harvard University, Poynter’s Craig Newmark Center for Ethics and Leadership, and The Markup.

He also provided funding to the soon to be dismantled Technology and Social Change Project at Harvard’s Shorenstein Center. Newmark is the “anti-disinformation” elite of the elite. Here he is, below (back row, 7th from left) at the Aspen Institute’s Information Disorder Commission, a $3.5 million project he funded, along with Prince Harry, Alex Stamos (SIO), Kate Starbird (University of Washington), Katie Couric, Chris Krebs (Director, Cybersecurity and Infrastructure Security Agency, DHS), and several others. Full list of commissioners.



He sits on almost 40 boards, as well as many organizations he funds, including Harvard’s Shorenstein Center, Columbia Journalism Review, CUNY Graduate School of Journalism, Poynter, the Electronic Frontier Foundation, New America Foundation, Politifact and others.

What we know about funding: According to Philanthropy.com Newmark gave away USD $419m between 2018-2022, a huge portion of it to “anti-disinformation” initiatives. The list is enormous but includes Virality Project partners the Stanford Internet Observatory, University of Washington Center for an Informed Public, the Center for Social Media and Politics at NYU, and the National Conference on Citizenship, as well as First Draft, Politifact, Poynter, Pro Publica, Mother Jones and Harvard’s Shorenstein Center. In 2022 he announced a $50 million grant to the Aspen Institute to build what he calls a “cyber civil defense.” 

What they do/What they are selling: The idea that his money can be a “force multiplier” for battling disinformation. Craigslist’s free classified ads helped destroy local newspapers, but Newmark has found friends in journalism with gifts of $10 million to the Columbia Journalism School and $20 million to CUNY’s Craig Newmark Graduate School of Journalism.

Characteristic/worldview quote: “You can manipulate a person by manipulating a person’s feed. You can tell a person what to believe and maybe tell a person what to do.”

In the #TwitterFiles: Newmark is cc’d on regular emails from the Carnegie Endowment for International Peace for its monthly “sphere of influence” meetings. Other invitees include failed Disinformation Governance Board head Nina Jankowicz, the military-funded Australian Strategic Policy Institute, the Atlantic Council, and scores of others. It is not known if he attended any of the meetings.

Connected to: Almost everybody, including, probably, anyone currently in the room with you. 

In sum: A mega-fund core to power the explosive growth of the Censorship-Industrial complex.

​27.​ Omidyar Group
Link: https://omidyar.com

Type: A series of foundations from the founder of eBay providing a huge amount of funding to the Censorship-Industrial complex.

You may have read about them when: You heard of almost any “anti-disinformation” initiative. Omidyar funded projects include the incredibly creepy CryptoChat, which peers into private and encrypted messaging systems to weed out misinformation. Omidyar also funded the Algorithmic Transparency Institute which conducts “civic listening” and “automated collection of data” from “closed messaging apps” in order to combat “problematic content.” Pierre Omidyar himself is perhaps the most famous traitor to the cause of free speech in the “anti-disinformation” complex, having once stepped in to serve as the protector of Edward Snowden’s documents. Look back and you’ll see articles describing him as a Bruce Wayne-like figure, a reclusive billionaire for whom the Snowden leaks “gave him a cause — and an enemy.” 

What we know about funding: Omidyar gives funds to almost all the leading “anti-disinformation” initiatives including the Stanford Internet Observatory, the Global Disinformation Index, Full Fact, Meedan, Poynter, the National Conference on Citizenship (NCoC)/Algorithmic Transparency Institute, and University of Washington Center for an Informed Public. Omidyar is also a key funder of The Intercept. He was recently hailed for donating $100 million to “boost journalism and fight hate speech,” although only a portion of that money seems to be going to anti-disinformation efforts. Funding is distributed under several brands including Luminate, the Democracy Fund, and First Look Media. 

What they do/What they are selling: Funding for progressive causes, ostensibly.

Characteristic/worldview quote: From an Omidyar Network report: “Big tech has shown little will to truly stop…infectious and dangerous messages.”

“Hairball” graph: From an Oxford group study funded by the Omidyar Network:



In the #TwitterFiles: Twitter’s Nick Pickles reacts to an Omidyar-sponsored report on “junk news”:



In sum: Like Newmark’s group, this is a mega-fund and driving force behind the Censorship-Industrial Complex.

28.​ The Knight Foundation
Link: https://knightfoundation.org/

Type: The third in the trifecta of private foundations leading the funding of the “anti-disinformation” industry. 

You may have read about them when: The Foundation was born from the Knight Ridder company, once the largest publisher of newspapers in the United States. In 2005 it began a major course change toward digital journalism initiatives, and over the past several years made disinformation a major focus. Outgoing CEO Alberto Ibargüen served on the Council on Foreign Relations and on the boards of ProPublica, American Airlines, and the World Wide Web Foundation, among others. As an indication of the coziness of the Censorship-Industrial Complex, Vivian Schiller (Aspen Institute CEO and participant in Aspen’s Hunter Biden laptop tabletop) here co-hosts Knight’s podcast on the 2020 election and discusses the problem of misinformation. No mention is made of her work in running a misinformation operation.

In 2018 Graphika produced a report for the Knight Foundation on disinformation and Twitter during the 2016 election. The report seeks to link those supporting the journalism of Julian Assange to “anti-immigrant/anti-Muslim themes,” “conspiracy theories” and “racist and “white identity” accounts.”

What we know about funding: Like Newmark and Omidyar, Knight has given to a Who’s Who of the CIC, including NewsGuard, the University of Washington Center for an Informed Public, First Draft, the Global Disinformation Index, Poynter and the Algorithmic Transparency Institute. 

In 2019 Knight committed $50 million to “11 American universities and research institutions, including the creation of five new centers of study” including $5 million to the University of Washington’s Center for an Informed Public (of EIP and Virality Project infamy).

Total grants in 2021 were $114 million.

What they do/What they are selling: Funding for a range of media initiatives from journalism, to anti-disinformation, as well as arts and culture.

In the #TwitterFiles: In October 2018, in a classic demonstration of how CIC groups influence both content moderation and news coverage, the Washington Post writes Twitter and cites a Knight Foundation study claiming that 80% of accounts that spread disinformation in 2016 are still on the site. Twitter gets two days to respond to this query, which follows a pattern Twitter by then knew all too well: “Study X says you haven’t done enough to stop Y. We publish in Z hours…”



Characteristic/worldview quote: “We believe in freedom of expression and in the values expressed in the First Amendment to the Constitution of the United States.”

Closely connected to: almost all the NGO, think tank, and academic leaders of the “anti-disinformation” field, as well other major foundations including the Charles Koch Foundation, the Hewlett Foundation, Craig Newmark Philanthropies, and the Omidyar Network.

In sum: A leading force in developing the ecosystem of anti-disinformation organizations, particularly in the US.

​29.​ Google Jigsaw 
Link: https://jigsaw.google.com/

Type: A “think/do tank” developing technical solutions to disinformation, censorship, and violent extremism.

You may have read about them when: Jigsaw was founded in 2010 as Google Ideas under the leadership of Jared Cohen, who worked both under Condoleezza Rice and Hilary Clinton at the State Department. Cohen was seen as a rising star who could help leverage the geo-political potential of emerging digital technologies. Cohen co-wrote the book “The New Digital Age” with Google CEO Eric Schmidt and pioneered the transformation of Google into a State Department regime change proxy. Cohen is also a member of the Council on Foreign Relations.

Cohen stepped down from Jigsaw in mid-2022 to join Goldman Sachs as a Partner and as President of Global Affairs. In October he traveled to Kyiv to meet with President Zelensky. 

New CEO, Yasmin Green, is a member of the Aspen Institute’s Cybersecurity Group and Commission on Information Disorder, and on the board of the Anti-Defamation League. She is also a senior advisor on innovation to Oxford Analytica, a private intelligence firm created by former Nixon staffer David Young. Young co-founded “The Plumbers” whose members conducted the 1974 Watergate break-in. (Young did not directly participate).

Jigsaw developed the controversial Redirect Method in partnership with Moonshot. Jigsaw is training AI to combat “toxic,” “unreasonable,” “problematic,” and other language.

Camille Francois, Graphika’s current Chief Innovation Officer, was formerly the Principal Researcher at Jigsaw.

What we know about funding: Funds come from Google.

What they do/What they are selling: Highly sophisticated technology solutions to guide online discourse and selective anti-censorship work in the service of selective official goals. 

Characteristic/worldview quote: “Advancements in natural language processing and AI as a whole have enabled us to develop products with the goal of making conversations online better at scale.”

Connected to: Moonshot, Atlantic Council/DFRLabs, Graphika, Aspen Institute, the State Department. 

In sum: Perhaps the slickest and most technically sophisticated of the censorship and speech control initiatives 

​30.​ Full Fact 
Link: https://fullfact.org/

Type: A leading UK “fact-checking” “NGO” with mountains of money from Big Tech.

You may have read about them when: Founded by Michael John Samuel, the son of an aristocrat, Full Fact epitomizes the elitism and down-talking of the “fact-checking” industry. Full Fact has been explicit about collaborating with Big Tech and government, stating in a #TwitterFiles email “Full Fact has been working with a variety of organizations including Facebook, Google, Twitter, First Draft and the UK and Canadian governments to create a Framework for Information Incidents.”

In developing the framework they relied on much of the same cozy club of information police — the report drew from other leading organizations including First Draft, the Carnegie Endowment for International Peace, Ben Nimmo (NATO, Graphika, Facebook), and Joan Donovan (Data & Society, Shorenstein).

While most digital rights and free speech groups have opposed the British government’s online “safety” bill, Full Fact thinks it doesn’t go far enough, arguing “the Bill falls short of the Government’s aim to make the UK the safest place to be online.”

Full Fact was the first UK member of Facebook’s Third-Party Fact-Checking program. Characteristic of the “fact-checkers,” they get an enormous level of Covid information wrong, including claiming it is “very rare” to get Covid twice or that you “can’t be forced to get a vaccine.” While claiming they are independent they also state they “work for Facebook.” Full Fact led a successful campaign to have vaccine critic and Conservative MP Andrew Bridgen removed from the party.

As is typical, Full Fact strays dramatically from the remit of pursuing the truth, instead combating “bad” information. (It is not known if that means naughty or of poor quality; possibly, both) It would be one thing if the response was to counter with “good” information, but Full Fact’s consistent approach favors censorship-type solutions. Full Fact has even developed its own AI-driven Robocop to police speech online.

What we know about funding: Full Fact takes huge amounts of Big Tech money, almost $2.5 million between 2019-2021 from Facebook alone. Another example of corporations funding the people who supposedly keep them accountable. They also receive strong support from Google, Poynter, and Omidyar.

What they do/What they are selling: Truth policing in the service of the powerful. 

Characteristic/worldview quote: “Full Fact fights bad information”; “Bad information ruins lives.”

In the #TwitterFiles: A note via the #FakeNewsSci mailing list shows that they are working with “Facebook, Google, Twitter, First Draft and the UK and Canadian governments to create a Framework for Information Incidents.”

Connected to: Facebook, Google, Poynter, First Draft, Shorenstein Center, Graphika, and the government of the UK. 

In sum: Leading candidate for inevitable UK Big Brother award.

HONORABLE MENTIONS:
31: Media Matters For America A creature of noted political hitman David Brock, MM4A has made an effortless transition from mainstream media promulgator of political scandals like Russiagate to maker of Internet blacklists and counter of social media offenses, an example being the 927 million interactions Donald Trump’s Facebook posts earned between January 1, 2020 and January 6, 2021. 

32. Miburo/Digital Threat Analysis Center Anti-disinformation lives, even on Substack! After a departure from the Hamilton 68 project, former FBI official Clint Watts landed at a series of agencies, beginning with Miburo, a group whose goal, according to one TwitterFiles email, was to “detect bad actors in 1 hour and assess them in less than 6 hours through rapid reports, infographics, and case studies.” As far as Racket could tell, this made Miburo the only anti-disinfo group that offered a time-based, drive-thru-type service. Miburo eventually was reborn on Substack as the Digital Threat Analysis Center. 

33. Credibility Coalition An oddly vague group of researchers that has poured resources into trying to develop what it calls a “shared vocabulary for credibility.” From 30,000 feet, the CC seems to replicate a lot of what outlets like the Global Disinformation Index (see below) do, analyzing media sources and downranking for various qualities ranging from lack of fact-checking to use of “straw man” or “slippery slope” arguments. Though the group stresses it’s looking to identify content “signals” that “require human judgment and training,” the CC has worked with the media literacy platform Public Editor out of Berkeley to tout a “collaborative software” called “TextThresher” that looks suspiciously like a tool for computerized credibility analysis. The CC has also produced something like an inverse version of this list, creating a page where users can surf color-coded maps of groups that have aimed to “improve information quality.”

34. Factcheck.me/Botcheck.me Created by two ambitious whippersnappers from the Cal-Berkeley, Rohan Phadte and Ash Bhat — who once self-described as having gone from “a couple students hacking on an extended school project into an eight-person team with the mission of protecting the public” — Factcheck.me and Botcheck.me offer user-friendly tools for defending against disinformation and bots, respectively. The Democratic National Committee in 2020 hired the pair to write a report “on the spread of disinformation on social media,” as the New York Times put it. Internally, the Twitter Files show the company saw their reporter-friendly tools detecting “bot-like” activities as cousins of the infamous Hamilton 68 project, with one executive writing to a comms official handling a press inquiry about the service: “Every one of the accounts they use as an example of a bot account on their methodology page on Medium is wrong. Doesn’t publish data, does sell consultancy. Definition of monetizing the problem.” Told about the emails, Ro Bhat said, “Wow… We reached out to those guys several times and never heard back.”

35. Duke Reporters’ Lab The DRL’s tools are perfect examples of what we at Racket have termed “RFWs,” or “reporter-friendly widgets.” Funded by the usual suspects at the Newmark Foundation, the Knight Foundation, and Facebook, the Lab experiments with tools like MediaReview and ClaimReview, essentially tagging projects that allow fact-checking organizations to submit their reports of false claims or imagery to search engines and tech platforms for swifter ranking. An “experimental platform” called Squash offers “live, automated fact-checking during political events like debates and speeches,” using AI to “spot” subjects for human review. The product has already been deployed for political debates:



As with nearly all the CIC-developed tools, the DRL products seek to identify “consistent terminology” or an application that “standardizes fact-checking content in a machine-readable way.” This quest for a single fact-checking language is supported by Jigsaw, Facebook, Google, and the Washington Post. A recent Duke study purporting to show which parts of the country are sadly bereft of advanced fact-checking efforts may remind you of another color-coded state map:



36. Reveal This EU-funded “social media verification” site is, like many European anti-disinformation projects, more overtly terrifying in its dystopian aims than some of its American counterparts. This government-funded program offers a tool it calls without embarrassment the Journalist Decision Support System, or “JDDS.” Reporting is described as a government-supported team effort: “Up to 19 journalists can use JDSS simultaneously, each interactively browsing 10,000’s of posts in real-time,” and “analytics are automatically run on all posts, including sentiment analysis, fake and eyewitness media labeling and newsworthy claim extraction.” Say that loud and proud, folks: newsworthy claim extraction. The EU funding award for Reveal essentially describes an effort to automate what old-school reporters might have called the assignment desk, as the “key problem” with news is that “it takes a lot of effort to distinguish useful information from the ‘noise.’” Reveal claims to help by developing tools to “automatically judge the quality and accuracy of content.” The display portal for the JDDS looks like an interactive war game, which is probably not an accident. 



37. Global Disinformation Index The GDI should probably be higher on this list. It was the subject of one of the first true investigative features about the Censorship-Industrial Complex, a series by the Washington Examiner that focused on two key facts: the Britain-based GDI received at least $315,000 from the State Department Entity, the GEC, and engaged in “risk” scoring of news media organizations that down-ranked conservative outlets like the “American Spectator, Newsmax, the Federalist, the American Conservative, One America News, the Blaze, the Daily Wire, RealClearPolitics, Reason, and the New York Post.” As is the case with the Omidyar-funded Oxford Internet Institute and the aforementioned Credibility Coalition, the GDI’s credibility/risk/trust scoring is built atop a series of subjective variables, among them the use of “targeting language” that “demeans or belittles people or organizations,” or includes “hyperbolic,” “emotional,” and “alarmist” language. The GDI announces openly that its strategy is to push major digital marketing clients to “redirect their online ad spending.” It should be noted that two of the organizations deemed least trustworthy by the GDI are the New York Post, whose story about the Hunter Biden laptop was wrongly censored (“GDI’s study did not review specific high-profile stories,” a report quips) and Reason magazine, one of the few prominent press critics of organized censorship. Now-defunct Buzzfeed, whose editorial shipwreck will forever bear signs of hull rippage from its decision to publish a Steele dossier it knew was riddled with errors, was on GDI’s top ten safest sites list, lauded for — get this — “journalistic best practices” and  “neutral, unemotional language.”



39.  Institute for Strategic Dialogue Also funded by the U.S. State Department, the Britain-based ISD offers another smorgasbord of content-suffocation tools, including a “hate-mapper” service and a product called Beam, which “is a multi-lingual, multi-platform capability developed to expose, track and confront information threats online.” ISD identifies “bad actors” or “extremist actors” and its “shared endeavour” program seeks to build “psychosocial resilience to radicalization.” The ISD is responsible for the report saying anti-Semitic remarks soared on Twitter after Elon Musk’s purchase of the platform, a report listing “independent journalists” amplifying “Russian propaganda” that inspired an NBC report including the now-on-trial Gonzalo Lira. ISD was also a source for a USA Today report that was influential in getting not-yet-convicted people accused of participation in the January 6th protests removed from a variety of Internet services. The ISD is one of many groups that were roaring about the dangers of Discord before the “Pentagon Leaker” story, saying, “Evidence suggested that users of extreme right channels on Discord are very young,” raising questions about the role that “online games” play in “radicalization of minors.”

40. Wikipedia In June of 2021, Wikipedia’s then Executive Director Katherine Maher appeared at a conference hosted by the Atlantic Council, where she was interviewed by NBC reporter Brandy Zadrozny about “how big tech can be as trusted as Wikipedia.” The thrust of the report was that Wikipedia had refused a request by the Turkish government to take down “two pages that they did not appreciate references to President Erdogan and his family and their involvement in the Syrian civil war as a state sponsor of terrorism,” which led to a ban of the site that was overturned to great fanfare in 2020. Wikipedia, like many tech behemoths, plays the role of a defender of free speech in certain circumstances, but lately it has become perhaps the most furious grindstone of digital conformity in Western media outside Twitter, Google, and Facebook, institutionalizing a system of blockages that increasingly only let through information reported on in an approving way by large corporate or academic institutions (it has been a great struggle to get Twitter Files material on the site, for instance). Wikipedia was once seen as one of the great experiments in open-source media, and identified with legal challenges to things like the NSA’s illegal domestic surveillance program, but has become just another member of the cartel-like “industry call” that includes the FBI, Twitter, and Facebook (the Twitter Files show the exact moment in which Wikipedia asks for a “disinformation” contact at the FBI), and has taken rigid stands on ridiculous issues like the definition of “recession.”



#TwitterFiles also show Wikipedia staff invited to election tabletops with the Pentagon, and joining weekly “industry meetings” with their Big Tech brethren.

Former Executive Director Katherine Maher is a member of the Council on Foreign Relations, a World Economic Forum young global leader, a security fellow at the Truman National Security Project, and a fellow at DFRLabs at the Atlantic Council, the military-industrial complex’s favorite Think Tank. It’s amazing how far selling encyclopedias can take you.

41. EU Disinfo Lab Another anti-disinformation site that is full of features warning of the insufficiently vibrant stream of warnings about Russian aggression, climate change, and unregulated Internet spaces like Telegram. Despite being an independent non-profit, the Lab proxies for government, keenly assessing “the commitments of platform signatories of the EU Code of Practice on Disinformation.” It also seeks to weed out an “anti-system mindset,” such as the use of cryptocurrencies to fund “junk sites” seeking to cultivate a “fringe and non-conformist image.” The Lab represents the uptight tattle-tale wing of the “anti-disinformation” scene.

The EU Disinfo Lab made perhaps its biggest splash in 2019 when it claimed to have unearthed “265 Coordinated Fake Local Media Sites Serving Indian Interests.” The illustration features skull-and-crossbones icons for “zombie” sites and alien faces for “new” ones:



42. The UK 77th Brigade It should tell the reader something that the formation of an active military unit by a key NATO partner which is openly devoted to fighting online “disinformation” and has been credibly accused of mass surveillance of its own citizenry is just the 42nd entry on our list. The UK’s 77th Brigade would be rejected by any good fiction editor as too over-the-top. Big Brother Watch broke the story revealing how the speech of MPs, academics, journalists, human rights campaigners and the public was monitored under the guise of combating “misinformation.”



43. Claim Buster Another machine learning tool backed by the Knight Foundation, the National Science Foundation, Newmark Philanthropies and the Facebook Journalism Project that’s working on a key problem for any future AI-driven moderation program: how to use machine learning to identify “claims” in real-time.  “Automated live fact-checking for everyone” is easy, according to its graphics: just follow the instructions below.



44. DisinfoCloud This was a GEC-funded operation, through the beginning of 2023. It featured a “continuously updated news feed” of disinfo-related items, often with fairly far-out recommendations to the “nearly 300 organizations, including those that provide machine learning analysis of social media, media monitoring, fact-checking, media literacy, social network mapping, and more” in the organization’s “testbed.” This blogged material was available to “select government, civil society, and private sector users,” of which, fortunately for #TwitterFiles readers, Twitter was one. The company received wisdom-nuggets like the idea that the terms “color revolution” and “Russophobia” were “Pro-Kremlin” propaganda, the good news that Britain’s GHCQ might soon be using AI to combat disinformation, and much more. Not intended for your eyes, you had the honor of paying for it all, if you’re an American citizen.



45. MythDetector The fact-checking arm of the Media Development Foundation, funded by USAID and the German Marshall Fund, helps produce valuable public service messages, like a video in Georgian explaining that the so-called American doctor online who’ll cure Covid and obviate the need for masks is actually a porn star. MythDetector is a Facebook third-party fact checker, “compliant” with Poynter’s International Fact Checking Network principles, and will “measure the truth!” for you.

46. Verified The inevitable creep-tastic United Nations fact-checking initiative promises to “deliver life-saving information on Covid-19 and stories from the best of humanity.” Key insights? “Behavioral science research told us we needed to increase people’s risk perception, the feeling that there is a threat to themselves or their loved ones.” The technocrats at Verified were sure COVID-19 vaccines would “end the pandemic” by “stopping the spread of COVID-19.” Verified partnered with the World Bank, Al Jazeera, Facebook, Omidiyar, First Draft, Ikea, Spotify, Tik Tok, Twitter, and #ThisIsOurShot (also a Virality Project partner). It was built in collaboration with Purpose, a McKinsey-for-millennials whose co-founder chaired the WEF’s Global Agenda Council on Civic Participation.

47. Foreign Malign Influence Center After the public relations fiasco of the Orwellian Disinformation Governance Board that was to be housed in the Department of Homeland Security, and the erasure of the “Misinformation, Disinformation, and Malinformation” Subcommittee that appeared slated to assume the DGB’s functions, it appears the federal government is putting chips on another Truth-Ministry facsimile, moving them perhaps to this existing agency under the Office of the Director of National Intelligence. The FMIC was “activated” on September 23, 2022. The DGB closed August 24, 2022. The FMIC is headed by Jeffrey K. Wichman, who spent 30 years at the CIA.

48. Advance Democracy Inc. Not much is known about this group except that it appears as a source for a lot of USA Today stories (about Tucker Carlson’s January 6th reports, climate denialism, and “Trump allies” still on Twitter) and appeared in a strange TwitterFiles exchange, in which a comms official describes them as mysterious and the author of some “shaky” reports. As is typical of many CIC cutouts, its website lists no information regarding leadership, staff or donors. It does that at the same time as “tracking political donations” of others.



49. DisinfoWatch Who says Canadians can’t be sketchy? This group, which lists as “research partners” GEC, NATO’s STRATCOM Center of Excellence, and the Center for European Policy Analysis, is the usual mish-mash of evil Putin portraits and gibberish text about building “resilience” to threat narratives, but also offers skillful local knowledge in finding ways to blame RT for using coverage of the Canadian trucker protests to “legitimize anti-government narratives.”

50. Countering Disinformation Another USAID-funded group that promotes “information integrity” and argues for a “whole-of-society approach,” which they say will require creating a “sense of urgency” in the population about disinformation. (In anti-disinformation literature, the public is often depicted as insufficiently panicked). The group promotes a “mixed-methods approach,” which includes “fact-checking, monitoring, and other interventions.” It also offers a keen visual representation of what a “healthy information space” looks like: complete encirclement by protective institutions. Like freedom, in order words, only the opposite!
"""