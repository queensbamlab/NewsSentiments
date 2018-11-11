import csv
import time
import requests
from bs4 import BeautifulSoup
from pattern.en import ngrams
from pattern.en import lemma, sentiment
from nltk.tokenize import sent_tokenize
import warnings

warnings.filterwarnings("ignore", category=UserWarning, module='bs4')
base_url = "http://www.moneycontrol.com"

# Build a dictionary of companies and their abbreviated names 
companies = {'cadilahealthcare':'CHC','piramalenterprises':'PH05',
             'glenmarkpharma':'GP08','glaxosmithklinepharmaceuticals':'GSK',
             'sunpharmaceuticalindustries':'SPI','lupin':'L',
             'cipla':'C','aurobindopharma':'AP',
             'drreddyslaboratories':'DRL','divislaboratories':'DL03', 'alkemlaboratories':'AL05'}
             
# Create a list of the news section urls of the respective companies 
url_list = ['http://www.moneycontrol.com/company-article/{}/news/{}#{}'.format(k,v,v) for k,v in companies.items()]

# Create an empty list which will contain the selected news articles 
List_of_links = ['https://www.moneycontrol.com/news/business/earnings/sun-pharma-q3-profit-falls-75-to-rs-365-cr-on-tax-cost-operating-income-tanks-41-2508075.html']

#https://www.moneycontrol.com/news/business/stocks/goldman-sachs-retains-buy-on-sun-pharma-after-usfda-accepts-nda-filing-for-otx-101-2470601.html
#https://www.moneycontrol.com/news/business/earnings/ciplas-post-q4-net-loss-of-rs-61-8-cr-depreciation-impairment-weigh-in-on-financials-2289081.html
#'https://www.moneycontrol.com/news/business/stocks/alkem-laboratories-falls-11-as-usfda-issues-13-observations-to-daman-plant-2538317.html'
#'http://www.moneycontrol.com/news/business/pharma-q4-earnings-preview-tough-quarter-us-pricing-pressure-domestic-sales-recovery-hold-key_10774221.html',
#'http://www.moneycontrol.com/news/buzzing-stocks/cadila-healthcare3usfda-approval-for-methylprednisolone-cinacalcet-hydrochloride-tablets_10834441.html',
#'http://www.moneycontrol.com/news/announcements/zydus-receives-final-approvalusfda-for-metoprolol-succinate-tablets_10701301.html',
#'http://www.moneycontrol.com/news/buzzing-stocks/cadila-healthcare-rises-3usfda-nod-for-metoprolol-succinate-tablets-nomura-upgrades-to-buy_10701241.html',
#'http://www.moneycontrol.com/news/brokerage-results-estimates/weak-us-sales-inr-appreciation-to-drag-earnings-dr-reddy-cadila-top-pick-edelweiss_10341221.html',
#'http://www.moneycontrol.com/news/current-affairs/glenmark-gets-usfda-nod-for-scalpskin-treatment-drug_10806261.html',
#'http://www.moneycontrol.com/news/current-affairs/glenmark-gets-usfda-nod-for-skin-ointment_10794821.html',
#'http://www.moneycontrol.com/news/business/glenmark-recalls-over-1-lakh-bottlesanti-inflammatory-drugus_10745241.html',
#'http://www.moneycontrol.com/news/business/glenmarkgets-usfda-nod-for-psoriasis-spray_10710041.html',
#'http://www.moneycontrol.com/news/buzzing-stocks/glenmark-pharma1usfda-approval-for-clobetasol-propionate-spray_10708441.html',
#'http://www.moneycontrol.com/news/buzzing-stocks/cipla-rises-2usfda-approval-for-phenylephrine-injection-exemestane-tablets_10852121.html',
#'http://www.moneycontrol.com/news/business/usfda-conducts-inspection-at-cipla39s-indore-facility_10787901.html',
#'http://www.moneycontrol.com/news/buzzing-stocks/cipla-gains-5-after-usfda-inspectionno-data-integrity-or-repeat-observations_10784941.html',
#'http://www.moneycontrol.com/news/buzzing-stocks/cipla-rises-1launching-authorized-genericaloxius-market_10703061.html',
#'http://www.moneycontrol.com/news/cnbc-tv18-comments/cipla-launches-aloxi-genericus-market-under-agreementhelsinn_10701601.html',
#'http://www.moneycontrol.com/news/results-boardroom/us-india-will-continue-to-outperform-going-ahead-cipla_10479401.html',
#'http://www.moneycontrol.com/news/result-poll/aurobindo-pharma-may-post-18-growthq3-profit-us-business-seen12_10473001.html',
#'http://www.moneycontrol.com/news/current-affairs/dr-reddy39s-gets-eirusfda-for-uk-plant_10822041.html',
#'http://www.moneycontrol.com/news/business/dr-reddy39sgets-eirusfda-for-cuernavaca-plantmexico_10764241.html',
#'http://www.moneycontrol.com/news/business/dr-reddy39s-launches-generic-nausea-drugus_10703161.html',
#'http://www.moneycontrol.com/news/results-boardroom/hope-to-resolve-srikakulamus-fda-soon-says-drl_10413301.html',
#'http://www.moneycontrol.com/news/results-boardroom/hope-to-resolve-srikakulamus-fda-soon-says-dr-reddy39s_10413281.html'

#Extract the relevant news articles weblinks from the news section of selected companies
#for urls in url_list:
#   html = requests.get(urls)
#   
#   # Create BeautifulSoup object 
#   soup = BeautifulSoup(html.text,'html.parser') 
#
#   # Retrieve a list of all the links and the titles for the respective words
#   word1,word2,word3 = "US","USA","USFDA"
#   
#   # Finds all twenty links on the page 
#   links = soup.find_all('a', class_='arial11_summ')
#   for l in links:
#      #first convert into a string
#      sp = BeautifulSoup(str(l),'html.parser')  
#      tag = sp.a
#      
#      #Check if any words exist in the given news headlines
#      if word1 in tag['title'] or word2 in tag['title'] or word3 in tag['title']:
#          #If yes then add to the list 
#          category_links = base_url + tag["href"]
#          List_of_links.append(category_links)
#          time.sleep(3)

#Remove the duplicate news articles based on News Title
unique_links = list(set(List_of_links))


# Create a dictionary of positive/negative words related to the Pharma Sector
reader = csv.reader(open('dict.csv', 'r'))
pharma_dict = dict((rows[0],rows[1]) for rows in reader)

# Creating an empty list which will be filled later with news article links, and Polarity values (pos/neg)
df =[]

# Open the choosen news articles and extract the main text  
for selected_links in unique_links:
   results_url = selected_links 
   print(results_url)
   print(">>>>")
   
   #Get each article from site
   results = requests.get(results_url)
   #Extract text
   results_text = BeautifulSoup(results.text)
   #Extract article content via class to specifically get only the text of the article
   extract_text = results_text.find(class_='arti-flow')
   
   timestamp = results_text.find(class_='arttidate')
 
   #retreive only the timestamp
   #timestamp1 = timestamp[23:50]
   
   #To handle missing / broken links
   if (extract_text == None):
       continue
       print("Skipping..")
   else:
       final_text = extract_text.get_text()
#       sentences = sent_tokenize(final_text)
#       
#       for i in sentences:
#           print(i, ">>>")
#           print(sentiment(i))
           
       # Pre-processing the extracted text using ngrams function from the pattern package to create uni/bi/trigram
       text1 = ngrams(final_text, n=1, punctuation=".,;:!?()[]{}`''\"@#$^&*+-|=~_", continuous=False)
       final_text2 = ngrams(final_text, n=2, punctuation=".,;:!?()[]{}`''\"@#$^&*+-|=~_", continuous=False)
       final_text3 = ngrams(final_text, n=3, punctuation=".,;:!?()[]{}`''\"@#$^&*+-|=~_", continuous=False)
       
       #Checking if any of the words in the news article text matches with the words in the Pharma dictionary(pos/neg)
       new_dict = {}
       new_dict1 = {}
       new_dict2 = {}
       positive_score,negative_score = 0,0
       final_text1 = []
       
       #lemmatize using lemma function of pattern
       for x in text1:
           final_text1.append(lemma(x[0]))
       
       #For loop to iterate over the unigrams in the article and check if they exist in the dictionary
       for k,v in pharma_dict.items():
           for x in final_text1:
               if x == k:
                   new_dict[x] = pharma_dict[x] 
    
       #For loop to iterate over the bigrams in the article and check if they exist in the dictionary
       for k,v in pharma_dict.items():
           for x in final_text2:
               temp = x[0] + ' ' + x[1]
               if temp == k:
                   new_dict1[x] = pharma_dict[temp]
                   
       for k,v in pharma_dict.items():
           for x in final_text3:
               temp = x[0] + ' ' + x[1] + ' ' + x[2]
               if temp == k:
                   new_dict2[x] = pharma_dict[temp]   
                   
       #Append postive and negative tag in the list               
       print(new_dict, new_dict1)
       
       positive_list = [] ; negative_list = [];
       
       for key, value in new_dict.items():
           if value == 'positive':
               positive_list.append(key)
           if value == 'negative':
               negative_list.append(key)
       
       for key, value in new_dict1.items():
           if value == 'positive':
               positive_list.append(key)
           if value == 'negative':
               negative_list.append(key)
                           
       #Compute the positive score, the negative score for each news articles
       positive_score = len(positive_list) ; negative_score = len(negative_list);
   
       #Calculating overall score
       overall_score = positive_score - negative_score
       decision = ''
       
       #Decision making
       if overall_score < 0:
           decision = 'sell'
       elif overall_score == 0:
           decision = 'hold'
       else:
           decision = 'buy'
           
       #Appending the empty list to create the final Sentiment analysis output
       var_nos = [results_url, positive_score, negative_score, overall_score, decision, timestamp]
       df.append(var_nos)
       
  
# Print the final list of the Sentiment Analysis 
print('Tagging completed >>>')
for item in df:
    print(item)
       
       
with open('scores.csv', 'w', encoding="utf-8") as csvfile:
    writer = csv.writer(csvfile) 
    writer.writerows(df)  

print("*****Completed*****")  

   