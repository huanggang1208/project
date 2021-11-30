set name=daomu
scrapy startproject %name%Spider
cd %name%Spider
scrapy genspider %name% %name%.com
