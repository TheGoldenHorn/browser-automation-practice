from scrapy.http import HtmlResponse
import os, json, time, socket, random, sys, requests

def main():
	filename = 'linkedin.html'
	with open(filename, 'r') as in_file:
		stringLinkedin = in_file.read()
	#print stringLinkedin

	response = HtmlResponse(url='url', body=stringLinkedin, encoding='utf-8')
	for res in response.xpath('//div[@class="also-viewed module"]/ul/li/a/@href'):
		print res.extract()

	

	raw_input()
	return

if __name__ == '__main__':
	main()
