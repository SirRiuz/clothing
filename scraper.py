

# Libs
from bs4 import BeautifulSoup
from requests_html import HTMLSession
import json



class DataProvider(object):

    def __init__(self) -> (None):
        self.__sessionRequest = HTMLSession()
        self.__pagination = 1
        self.__listProducts = []


    def __onRequest(self) -> (str):
        
        """
          Se encarga de obtener los datos y 
          renderizar el html
        """

        print('[I] Conectando con el servidor ...')
        print(f'[I] page={self.__pagination}')
        print(f'https://www.chollometro.com/categorias/moda-y-accesorios?page={self.__pagination}')
        response = self.__sessionRequest.get(f'https://www.chollometro.com/categorias/moda-y-accesorios?page={self.__pagination}')
        print('[I] Renderizando ... ')
        response.html.render(sleep=11)
        bsObject = BeautifulSoup(response.html.html,'html.parser')
        self.__listProducts = bsObject.html.find_all('article')

    
    def __convertToPeso(self,euro:int) -> (float):
        """ Convierte euros a peros colombianos """
        result = str(round(euro * 4.526,3))
        return result



    def __getTitle(self,itemObject:object) -> (str):
        title = itemObject.find('div',class_='threadGrid')
        title = title.find(
            'div',
            class_='threadGrid-title js-contextual-message-placeholder'
        ).strong.text
        return title

    
    def __getPrice(self,itemObject:object) -> (float):
        price = itemObject.find(
            'div',
            class_='threadGrid'
        ).find('div',class_='threadGrid-title js-contextual-message-placeholder')
        price = price.span.find('span',class_='overflow--wrap-off')

        if price:
            price = price.find(
                'span',
                class_='thread-price text--b cept-tp size--all-l size--fromW3-xl'
            )
            if price:
                price = price.text
            else:
                price = None
        else:
            price = None


        if price:
            price = (price.replace('€','')).replace(',','.')

            if price.replace('.','').isnumeric():
                price = price = self.__convertToPeso(float(price))
            else:
                price = None

        return price


    
    def __getId(self,itemObject:object) -> (str):
        itemId = ''

        if itemObject.get('id',None):
            itemId = itemObject['id'].split('_')[1]
        
        return itemId

    

    def __getImagePreview(self,itemObject:object) -> (str):
        itemObject = itemObject.find('div',class_='threadGrid')
        itemObject = itemObject.find(
            'div',
            class_='threadGrid-image space--r-3'
        ).a
        previewUrl = ''

        if itemObject:
            previewUrl = itemObject.img.get('src')

        return previewUrl


    def extractData(self) -> (None):

        while True:
            self.__onRequest()
            self.__pagination += 1
            
            for item in self.__onScractData():
                # print(item['id'])
                # print(item['title'])
                # print(item['price'])
                # print(item['origin'])
                # print(item['preview'])
                pass
    


    def __onScractData(self) -> (None):

        # TEST
        #catchData = open('result.html','r')
        #testCach = BeautifulSoup(catchData.read(),'html.parser')
        # END TEST

        #self.__listProducts = testCach.find_all('article')


        x = 0
        listData = []

        for item in self.__listProducts:

            isValid = True
            
            for classItem in item['class']:
                if classItem == 'js-telegram-widget':
                    isValid = False


            if isValid:
                price = self.__getPrice(item)
                title = self.__getTitle(item)
                data = {}
                id = self.__getId(item)

                data = {
                    'id':id,
                    'title':title,
                    'price':price,
                    'origin':f'https://www.chollometro.com/visit/thread/{id}',
                    'preview':self.__getImagePreview(item)
                }
                listData.append(data)
            x += 1


        print(json.dumps(listData,indent=3))





DataProvider().extractData()
