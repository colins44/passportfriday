//var user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2272.104 Safari/537.36';
//var Browser = require('zombie');
//var assert = require('assert');
//
//var browser = new Browser({userAgent: user_agent, debug: true, waitFor: 10000});
//
//var url =  'http://192.168.59.103:8000/admin/login/?next=/admin/';
//
//browser.visit(url, function(e, browser){
//    console.log(browser.text('site-name'))
//})


//Browser.visit('http://192.168.59.103:8000/admin/login/?next=/admin/', function(e, browser){
////Browser.visit('https://www.google.co.uk/flights/#search;f=LHR,LGW,STN,LCY,LTN;t=BER,TXL,SXF;d=2015-04-17;r=2015-04-21', function(e, browser){
//
////    console.log(browser.html('#site-name'))
//    console.log(browser.text('#site-name'))
////    console.log(browser.cookies)
////    console.log(browser.html())
//
//
//});


var user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_3) AppleWebKit/535.20 (KHTML, like Gecko) Chrome/19.0.1036.7 Safari/535.20';
var Browser = require("zombie");
var browser = new Browser({userAgent: user_agent, debug: true, waitFor: 100000});
var fs = require('fs');

var url = 'https://www.google.co.uk/flights/';
//var url =  'http://192.168.59.103:8000/admin/login/?next=/admin/';
browser.visit(url, function() {

//    console.log(browser.text("#PNIT24B-f-w"))
//    console.log(browser.text('#site-name'))
//    console.log(document.getElementsByClassName(".PNIT24B-f-w"))
//    console.log(document.getElementsByName('colM'))
//    console.log(document.getElementById('#gbqfsb'))
    console.log(browser.text('#gbqfsb'))
    console.log(browser.html())
//    console.log(browser.html())

//    console.log(browser.html())




  });

