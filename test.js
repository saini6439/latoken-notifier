// import * as request from 'request';
var request = require("request")
const cheerio = require('cheerio');


var options = {
    url: "https://latoken.com/exchange/USDT",
    headers: {
      'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 8_0 like Mac OS X) AppleWebKit/600.1.3 (KHTML, like Gecko) Version/8.0 Mobile/12A4345d Safari/600.1.4'
    }
  };

  request(options, function(error, response, html) {
    if (!error) {

      console.log('Scraper running on Instagram user page.');

      // Use Cheerio to load the page.
      var $ = cheerio.load(html);
      console.log($(".ReactVirtualized__Table__row jss965 jss968 jss967"))
      // Code to parse the DOM here

    }
})
  