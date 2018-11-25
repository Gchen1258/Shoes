def URLGen(model, size):
    BaseSize = 580 #For shoe size 6.5
    ShoeSize = float(size) - 6.5
    ShoeSize *= 20 #Generates our size code
    RawSize = ShoeSize + BaseSize
    SizeCode = int(RawSize)
    URL = 'https://www.adidas.com/us/' + str(model) + '.html?forceSelSize=' + str(model) + '_' + str(SizeCode)
    return URL

#Model = input('Model #:')
#Size = input('Size: ')
#print(URLGen(Model,Size))