---
created: '2022-08-23'
cssclasses: ''
modified: '2023-03-14'
permalink: /🍀 Garden Tour/🧰 Library Guide/Tutorials/How to embed an access statistics
  system in this library's digital garden.md
publish: true
published: '2025-07-09T02:08:25.282+08:00'
title: How to embed an access statistics system in this library's digital garden
---
The following 3 methods are all completely free for regular use. They are progressive, and the statistical information will be more comprehensive and accurate, but it also means that it will take more time to install and deploy.

## If you use cloudflare's DNS service

[Cloudflare | Web Performance & Security](https://dash.cloudflare.com/)

Then when configuring the A record or CNAME record of the DNS, check the proxy.

At this time, all requests to this domain name will first go through the proxy service of [[Spaces/2-Area/云服务和部署/CloudFlare]], and then it will direct the request to the IP or domain name you specified.

Because this proxy middle layer is added, it can do some lightweight statistics for the network layer protocol. But it also means that all crawler or automated tool visits are also included, so it will cause the statistical data to be too high.

The official statistics panel is as follows:

![](https://img2.oldwinter.top/202208232305309.png)
![](https://img2.oldwinter.top/202208232306036.png)

![](https://img2.oldwinter.top/202208232305980.png)

## If you use google analytics' statistical service

[google analytics](https://analytics.google.com/analytics/web/)
Compared with cloudflare's proxy statistics, [[google analytics]] will load a piece of JavaScript code script on the user's browser to obtain more detailed data, such as the dwell time of each page, conversion rate, page scroll times and other information.

But there is a biggest disadvantage, that is, google statistics 1 will be blocked, resulting in the inability to count the access data of users in mainland China, and 2 will be blocked by ad blocking plugins, resulting in the inability to count the data of users who have enabled ad blocking plugins.

Based on this, it is not recommended to use google analytics, although its integration is very convenient and can be done in a few minutes.

![](https://img2.oldwinter.top/202208232313158.png)

## If you use self-built statistical analysis tools such as Umani

[umami](https://umami.is/)

I directly used the [[railway]] it recommended for one-click deployment. After deployment, I customized my own domain name umami.oldwinter.top. After logging in, I added the website to be counted, and then a piece of script code will be generated, which needs to be pasted under the head tag of the index.html file of the website's source code repository.

After deployment, I found that it is also easily blocked by ad blocking plugins. For example, the [[Spaces/3-Resource/chrome插件/uBlock Origin]] I use will block it, resulting in the inability to correctly count this access data. But at least because it is self-built, it will not be blocked.

The statistical information is less than that of [[google analytics]], probably because it emphasizes some user privacy protection policies, which leads to less user data collected.

## If you use one-stop statistical analysis tools such as Howxm

[Howxm](https://app.howxm.com/)

It is currently free, and the experience is not bad. Compared with other solutions, it also supports questionnaires and user experience collection functions. I don't know what will happen in the future. 