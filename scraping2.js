var express = require('express');
var fs = require('fs');
var request = require('request');
var cheerio = require('cheerio');
var app     = express();



url = 'http://www.imdb.com/title/tt1229340/';

request(url, function(error, response, html){
    if (error) throw error;
    var $ = cheerio.load(html);
    console.log(html)
    $('a.title').each(function(){
        console.log('%s (%s)', $(this).text(), $(this).attr('href'));
    });
});