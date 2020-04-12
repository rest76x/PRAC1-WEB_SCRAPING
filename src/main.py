#!/usr/bin/env python
# coding: utf-8
from scraper import ACO_Scraper

fileName="ACO_PVPs.csv"

scraper = ACO_Scraper();
scraper.scrape();
scraper.data2csv(fileName);





