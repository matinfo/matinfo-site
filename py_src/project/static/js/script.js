/* Author: Mathieu Meylan
 * For: matinfo.ch
 */
//window.twttrCall=function(a){return window.twttr=window.twttr||(a={_e:[],ready:function(b){a._e.push(b)}})},function(a,b){var c,d,e=a.getElementsByTagName(b)[0],f=function(c,f,g){var h;if(a.getElementById(f))return;d=a.createElement(b),d.src=c,f&&(d.id=f),e.parentNode.insertBefore(d,e),g&&g(h)};f(("https:"==location.protocol?"//ssl":"//www")+".google-analytics.com/ga.js"),f("//platform.twitter.com/widgets.js","twitter-wjs",window.twttrCall)}(document,"script"),twttr.ready(function(a){a.events.bind("tweet",function(a){if(a){var b=a.target.parentNode.getAttribute("data-title");_gaq.push(["_trackSocial","twitter","tweet",b])}}),a.events.bind("follow",function(a){if(a){var b=a.region;_gaq.push(["_trackSocial","twitter","follow",b])}})});






















