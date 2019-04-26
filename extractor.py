# -*- coding: utf-8 -*-
"""
Created on Tue Apr 23 19:37:21 2019

@author: Anshul
"""

from bs4 import BeautifulSoup
import requests

original_stats_file = {}  
dict_list=[]      
def cond(x):
    if x:
        return x.startswith("evenrow") or x.startswith("oddrow") or x.startswith("datarow")
    else:
        return False

def stl_batting_stats(url, stats_list):
        r = requests.get(url)
        soup = BeautifulSoup(r.content, "html.parser")
        stats_table = soup.findAll("table", {"class": "tablehead"})
        for r in stats_table:
            rows = soup.findAll('tr', {'class': cond})
            for stat in rows:
                local_list = []
                data = stat.findAll("td")
                for d in data:
                    local_list.append(d.text)
                stats_list.append(local_list)
        
        return stats_list

def json_object_building(stat_list, url, url1, url2, url3):
    #print stat_list
    extended_lists = stat_list
    stats_file = {}
    l=[]
    try:
        for extended_list in extended_lists:
            stats_file = {}
            if str(extended_list[2]) == 'STL' and url == url1:
                #print str(stats_list[1])
                #print extended_list
                stats_file["NAME"] = str(extended_list[1])
                stats_file["TEAM"] = str(extended_list[2])
                stats_file["AB"] = str(extended_list[3])
                stats_file["R"] = str(extended_list[4])
                stats_file["H"] = str(extended_list[5])
                stats_file["2B"] = str(extended_list[6])
                stats_file["3B"] = str(extended_list[7])
                stats_file["HR"] = str(extended_list[8])
                stats_file["RBI"] = str(extended_list[9])
                stats_file["BB"] = str(extended_list[12])
                stats_file["SO"] = str(extended_list[13])
                stats_file["AVG"] = str(extended_list[14])
                stats_file["OBP"] = str(extended_list[15])
                stats_file["SLG"] = str(extended_list[16])
                stats_file["OPS"] = str(extended_list[17])
                stats_file["K"] = round((float(int(stats_file["SO"]))/int(stats_file["AB"]))*100, 2)
                dict_list.append(stats_file)
            if str(extended_list[2]) == 'STL' and url == url2:
                for element in dict_list:
                    if element["NAME"] == str(extended_list[1]):
                        element["G"] = str(extended_list[3])
                        SF = str(extended_list[14])
                        element["BABIP"] = round(float((int(element["H"]) - int(element["HR"])))/(int(element["AB"]) - int(element["HR"]) - int(element["SO"]) + int(SF)), 2)
            if str(extended_list[2]) == 'STL' and url == url3:
                for element in dict_list:
                    if element["NAME"] == str(extended_list[1]):
                        element["ISO"] = str(extended_list[6])
                        
                        
                l = dict_list
        return l
    except:
            pass
        
def a_team_batting_stats(stats_list, url):
    headers = requests.utils.default_headers()
    headers.update({
        'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0',
    })
    r = requests.get(url, headers=headers)
    soup = BeautifulSoup(r.content, "html.parser")
    #print soup
    
    stats_table = soup.findAll("div", {"id": "div_team_batting"})
    for div in stats_table:
        data = soup.find("table", {"id":"team_batting"}).find("tbody").findAll("tr")
        for d in data:
            td = d.findAll("td")
            data_list=[]
            for stat in td:
                data_list.append(str(stat.text).replace("*", '').replace("#", ''))
            stats_list.append(list(data_list))
    return stats_list

def minor_json_object_building(stat_list, team):
    stats_file = {}
    return_list=[]
    for i in stat_list:
        stats_file = {}
        stats_file["TEAM"] = team
        stats_file["NAME"] = str(i[0])
        stats_file["AGE"] = str(i[1])
        stats_file["G"] = str(i[2])
        stats_file["PA"] = str(i[3])
        stats_file["AB"] = str(i[4])
        stats_file["R"] = str(i[5])
        stats_file["H"] = str(i[6])
        stats_file["2B"] = str(i[7])
        stats_file["2B"] = str(i[8])
        stats_file["HR"] = str(i[9])
        stats_file["RBI"] = str(i[10])
        stats_file["SB"] = str(i[11])
        stats_file["CS"] = str(i[12])
        stats_file["BB"] = str(i[13])
        stats_file["SO"] = str(i[14])
        stats_file["BA"] = str(i[15])
        stats_file["OBP"] = str(i[16])
        stats_file["SLG"] = str(i[17])
        stats_file["OPS"] = str(i[18])
        stats_file["TB"] = str(i[19])
        stats_file["GDP"] = str(i[20])
        stats_file["HBP"] = str(i[21])
        stats_file["SH"] = str(i[22])
        stats_file["SF"] = str(i[23])
        stats_file["IBB"] = str(i[24])
        if int(stats_file["AB"]) == 0:
            stats_file["AVG"] = "0"
        else:
            stats_file["AVG"] = round(float(int(stats_file["H"]))/int(stats_file["AB"]),3)
        return_list.append(stats_file)
    return return_list 