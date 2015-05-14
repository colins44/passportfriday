import requests
import json

headers ={
    'Host':'www.google.com',
    'origin': 'www.google.com',
    'Content-Type': 'application/json; charset=utf-8',
    'X-GWT-Permutation': '5F2895DD6DB69690093CFF1C42BEE108',
    "x-client-data":"CIS2yQEIpLbJAQiptskBCMG2yQEI7ojKAQiKksoBCLWUygEYqonKAQ==",
    "x-gwt-cctoken":"ADS25WOpHduq6uMwFGfR2mWO6GwftqrTC3jSU7VSEIP1bvupKKHz5dIClRTyTrAFAdQ6yCqQ7WRcLgruhcQiT7Spq3Zyx8FQkZ8pVIOZYWodUgW8l5LYevkMDzfs180jGvnArajw2R2I8Q1xHDuzTZhzTmrYuzBp6CU-" ,
    'X-GWT-Module-Base': 'http://www.google.com/flights/project_static/',
    'Referer': 'http://www.google.com/flights/',
    'Content-Length': 129,
    'Cookie': '_ga=GA1.3-2.1490730780.1423056129; _gat=1; PREF=ID=3cecf5ce26520198:U=4327aad536d031cc:FF=0:LD=en:TM=1402909739:LM=1423235491:S=rVTOXtG1D1rORhyo; OGPC=4061130-6:; OGP=-4061130:; GoogleAccountsLocale_session=en-GB; SID=DQAAABsBAAARC83j5L8MxxRBKaEJEaMduSHLkWFK5icF7GIFbrgrY7L8wjQXLQjslv841ZSNXzIxYY8FSR1KMuWReHvtrWlt9zmfvRfssUUYcCyflaCkCNMcKREDOygrWBLx44fWwVF0gb1OgEfj3fbAqTmKJy85IBUGPqXvS2InSrqvL3fCl_20m3gB5g7GKD_Z8FbI-poDqhRwsEm0-BJeVzvps29xaqQ0tpEoaMEcVj2lgZ7LZzj-CFfGEXP-GXdOAYskArHfeiMDaHDAaQ4jpwR44MoWQuIoHzkUPKO9FktZMcpaNae286HceueD_asAHCTNGUcThiriblXD6fslfIHpRmZIcnS1S3ognsuaHS97cq8dzR1MwXH6LTOsBtzvgnM2EX4; HSID=AOueyAYwAdmM1OFT2; SSID=ALSNUd5S4iHtprsw4; APISID=GYEocN1B1T13LLCT/A-nmTqDWeisav6p11; SAPISID=NZWHsZwhOEuOloO9/ACKJf-S3lo0dD-V2m; NID=67=ma6oC5sjhdFkn1xw2myg527JNChtnhdUlPju_R9D-QYWhoxDFkZh4J3nzU6Q_P58D7T2zUWR_7Agmp0EKwUHIcPvu3PPY4SpG45fQeLHWe05J9RXqawILlIXyWpSyBZckvHaD3JG2TUbiyPfVTO3cY-Aqf3KYhy98oqHBDefQ2XAdyOwGgabGkv-oVBOxnu8zkfuA2BTyWgxHYyqfxtL3y9FrfVzZarlNr6aEC1plEv2nBWWiWljj_TCx5T33u9d9cd0vp4tJ1yO8Vis; S=quotestreamer=2Im4eVKOdNch5tJJ-ZDIqQ:travel-flights=gPUo1uis_jx909Dv2RqY9A',
    'Pragma': 'no-cache',
    'Cache-Control': 'no-cache',
}

data = [[["fs","[,[,[\"SJC\"]\n,\"2012-04-05\",[\"EWR\",\"JFK\",\"LGA\"]\n,\"2012-04-12\"]\n]\n"]
]
,[[["b_ca","54"]
,["f_ut","search;f=SJC;t=EWR,JFK,LGA;d=2012-04-05;r=2012-04-12"]
,["b_lr","11:36"]
,["b_lr","1:1528"]
,["b_lr","2:1827"]
,["b_qu","3"]
,["b_qc","1"]
]
]
]

url ='https://www.google.com/flights/rpc'

data = json.dumps(data)
r = requests.post(url, data=data, headers=headers)
print r.status_code
print r.content


