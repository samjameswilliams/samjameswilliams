# Migrating from Sphinx to Zensical  

I learnt how to build static websites using Sphinx at work to write documentation for internal Python libraries. I went for Sphinx because the documentation for my most used libraries are all built in Sphinx (numpy, matplotlib, scipy etc). There's definitely been a bit of a learning curve but the results are great and I've not had to learn much html and css. Having picked up the skill I thought I might as well use it to publish my own website for free on GitHub Pages. The Myst extension meant I could write pages in markdown instead of RestructuredText.  I use the iSh app on my iPhone to push changes to GitHub. I generally use Runestone to author the markdown files. I can also author from my personal or work laptop. Merging to main triggered a GitHub action which built the website to a branch and GitHub pages published it from there. The setup worked fine. 

So why change? A few reasons. I have another personal project where I was producing pdf documents from markdown files using Sphinx. A colleague at work started a discussion about producing reports using quarto. I tried it on this other project and was really pleased with the results. It was way faster, the presentation was better with less configuration and it made some nice looking HTML pages too. I wondered about switching to quarto for this site. It would probably do a great job. 

However, a podcast episode on Zensical came up and it really got my attention. At work I opted for Sphinx but I ended up being an early mover and in the time since I started, the default option has become Material for mkdocs. The Zensical episode made me glad I'd not put any time into migrating over. Basically mkdocs v2.0 is going to break Material for mkdocs, so the Material people have struck out on their own and made their own static site builder from the ground up in Rust. 

I thought my personal website would be a great way to give it a try. Since my site is predominantly markdown there wasn't much to change. Zensical doesn't need index files to create a page hierarchy, the index files were the only .rst in my site. So that's nice, no need to remember to add my new pages to the right index, just move the file from `drafts/` to `docs/...`. 

I use code blocks and MathJax so needed to add that to the toml configuration. 

I've been used to Sphinx builds taking minutes. Zensical must build in barely over 1 second. To see the Sphinx website you have to do a complete rebuild. Zensical can serve a live build to `localhost:8000` so you can view as you edit (if on a laptop, not on my iPhone). 

When you run `zensical new` it sets up the basic structure you need and it includes GitHub action `docs.yml` which builds the site and publishes it to GitHub pages. So that made it very convenient for me. It also does it the new way of saving the build to an artefact rather than the old way I was using of building to a branch. 

This makes it a very easy option for anyone starting out who wants to make their own site. 

I also used `migrate-to-uv` to switch package managers from Poetry to uv. 

I'm pleased with the new set up. It might be a while before I migrate my library docs. All the rst, addins, plots, calculations, code examples etc will surely make it a much bigger task. Sphinx  and Poetry have served me very well, but things move fast in tech and Zensical and uv are a nice upgrade.