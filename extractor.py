# -*- coding: utf-8 -*-
"""
Created on Tue Apr 23 19:37:21 2019

@author: Anshul
"""

from bs4 import BeautifulSoup
import requests
from selenium import webdriver
import re
import time

 
dict_list=[]      
def cond(x):
    if x:
        return x.startswith("evenrow") or x.startswith("oddrow") or x.startswith("datarow")
    else:
        return False

def stl_batting_stats(url, stats_list):
    driver = webdriver.PhantomJS()
    driver.maximize_window()
    driver.set_page_load_timeout(30)
    time.sleep(20)
    driver.get(url)
    
    data = driver.find_element_by_id("team_batting")
    rows = data.find_elements_by_tag_name( "tr")
    for row in rows:
        col = row.find_elements_by_tag_name("td")
        data_list=[]
        for d in col:
            data_list.append(str(d.text).replace("*", '').replace("#", ''))
        stats_list.append(list(data_list))
    driver.quit()
    return stats_list

def json_object_building(stat_list):
    #print stat_list
    extended_lists = stat_list
    extended_lists = extended_lists[:len(extended_lists)-5]
    del extended_lists[0]
    stats_file = {}
    l=[]
    
    try:
        for extended_list in extended_lists:
            stats_file = {}
            if extended_list == [] or str(extended_list[0]) == 'P':
                pass
            else:
                #Rk	 Pos	Name	Age 	G	PA	AB	R	H	2B	3B	HR	RBI 	SB	CS	BB	SO	BA	OBP 	SLG 	OPS 	OPS+	TB	GDP 	HBP 	SH	SF	IBB
                #0   1    2     3     4   5  6 7  8   9 10 11  12    13 14 15 16 17 18     19     20    21    22  23   24    25  26 27
                if "(" in str(extended_list[1]):
                    stats_file["NAME"] = (re.sub(r" ?\([^)]+\)", "", str(extended_list[1])))
                else:
                    stats_file["NAME"] = str(extended_list[1])
                stats_file["TEAM"] = "STL"
                stats_file["G"] = str(extended_list[3])
                stats_file["AB"] = str(extended_list[5])
                stats_file["R"] = str(extended_list[6])
                stats_file["H"] = str(extended_list[7])
                stats_file["2B"] = str(extended_list[8])
                stats_file["3B"] = str(extended_list[9])
                stats_file["HR"] = str(extended_list[10])
                stats_file["RBI"] = str(extended_list[11])
                stats_file["BB"] = str(extended_list[14])
                stats_file["SO"] = str(extended_list[15])
                if int(str(extended_list[5])) == 0:
                    stats_file["AVG"] = "0"
                else:
                    stats_file["AVG"] = round(float(int(str(extended_list[7])))/(int(str(extended_list[5]))), 3)
                stats_file["OBP"] = str(extended_list[17])
                stats_file["SLG"] = str(extended_list[18])
                stats_file["OPS"] = str(extended_list[19])
                stats_file["K"] = round((float(int(str(extended_list[15])))/(int(str(extended_list[5]))*100)), 2)
                stats_file["BABIP"] = round((float(int(stats_file["H"]) - int(stats_file["HR"]))/((int(stats_file["AB"]) - int(stats_file["HR"]) - int(stats_file["SO"]) + int(str(extended_list[25]))))), 2)
                stats_file["ISO"] = round((float(int(stats_file["2B"])+(2*int(stats_file["3B"]))+(3*int(stats_file["HR"])))/int(stats_file["AB"])), 3)
                dict_list.append(stats_file)
                        
                        
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