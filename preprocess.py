#-*- coding: utf-8 -*-
import operator

words = set()
# open file
f1 = open("HKIB-20000_001.txt",mode='r', encoding='utf-8', errors='strict', buffering=1)
f2 = open("HKIB-20000_002.txt",mode='r', encoding='utf-8', errors='strict', buffering=1)
f3 = open("HKIB-20000_003.txt",mode='r', encoding='utf-8', errors='strict', buffering=1)
f4 = open("HKIB-20000_004.txt",mode='r', encoding='utf-8', errors='strict', buffering=1)
data = f1.read()
data = data + f2.read()
data = data + f3.read()
data = data + f4.read()
data = data.split("\n")
# dictionaries
cate0 = {'doc_count':0}
cate1 = {'doc_count':0}
cate2 = {'doc_count':0}
cate3 = {'doc_count':0}
cate4 = {'doc_count':0}
cate5 = {'doc_count':0}
cate6 = {'doc_count':0}
cate7 = {'doc_count':0}
dic_features = {}
# lists
temp_list = []
# interating for each line of file
check = 0
cate = "초기값"
for line in data:
    line = line.replace(","," ")
    line = line.replace("."," ")
    line = line.replace("-"," ")
    line = line.replace("<"," ")
    line = line.replace(">"," ")
    line = line.replace('"'," ")
    line = line.replace("["," ")
    line = line.replace("]"," ")
    line = line.replace("/"," ")
    line = line.replace("{"," ")
    line = line.replace("}"," ")
    lineWords = line.split()
    if len(lineWords) > 0:
        if lineWords[0] == "#TEXT":
            check = 1
        elif lineWords[0] == "@DOCUMENT":
            check = 0
            temp_list = []
        elif lineWords[0] == "#CAT'03:":
            cate = lineWords[1]
            if cate == "건강과":
                cate0["doc_count"] += 1
            elif cate == "경제":
                cate1["doc_count"] += 1
            elif cate == "과학":
                cate2["doc_count"] += 1
            elif cate == "교육":
                cate3["doc_count"] += 1
            elif cate == "문화와":
                cate4["doc_count"] += 1
            elif cate == "사회":
                cate5["doc_count"] += 1
            elif cate == "산업":
                cate6["doc_count"] += 1
            elif cate == "여가생활":
                cate7["doc_count"] += 1
        if check == 1 and lineWords[0] != "#TEXT":
            for word in lineWords:
                dic_features[word] = 0
                temp_list.append(word)
                if cate == "건강과":
                    if word in cate0:
                        if not(word in temp_list):
                            cate0[word] += 1
                    else:
                        cate0[word] = 1
                elif cate == "경제":
                    if word in cate1:
                        if not(word in temp_list):
                            cate1[word] += 1
                    else:
                        cate1[word] = 1
                elif cate == "과학":
                    if word in cate2:
                        if not(word in temp_list):
                            cate2[word] += 1
                    else:
                        cate2[word] = 1
                elif cate == "교육":
                    if word in cate3:
                        if not(word in temp_list):
                            cate3[word] += 1
                    else:
                        cate3[word] = 1
                elif cate == "문화와":
                    if word in cate4:
                        if not(word in temp_list):
                            cate4[word] += 1
                    else:
                        cate4[word] = 1
                elif cate == "사회":
                    if word in cate5:
                        if not(word in temp_list):
                            cate5[word] += 1
                    else:
                        cate5[word] = 1
                elif cate == "산업":
                    if word in cate6:
                        if not(word in temp_list):
                            cate6[word] += 1
                    else:
                        cate6[word] = 1
                elif cate == "여가생활":
                    if word in cate7:
                        if not(word in temp_list):
                            cate7[word] += 1
                    else:
                        cate7[word] = 1

#file.close()
f1.close()
f2.close()
f3.close()
f4.close()
# 카이제곱 구하기
for feature in dic_features:
    kai_result = []
    # category0에 대한 값
    if feature in cate0:
        A = cate0[feature]
        B = cate0["doc_count"] - cate0[feature]
    else:
        A = 0
        B = cate0["doc_count"]
    C = 0
    D = 0
    if feature in cate1:
        C += cate1[feature]
        D += (cate1["doc_count"] - cate1[feature])
    else:
        D += cate1["doc_count"]
    if feature in cate2:
        C += cate2[feature]
        D += (cate2["doc_count"] - cate2[feature])
    else:
        D += cate2["doc_count"]
    if feature in cate3:
        C += cate3[feature]
        D += (cate3["doc_count"] - cate3[feature])
    else:
        D += cate3["doc_count"]
    if feature in cate4:
        C += cate4[feature]
        D += (cate4["doc_count"] - cate4[feature])
    else:
        D += cate4["doc_count"]
    if feature in cate5:
        C += cate5[feature]
        D += (cate5["doc_count"] - cate5[feature])
    else:
        D += cate5["doc_count"]
    if feature in cate6:
        C += cate6[feature]
        D += (cate6["doc_count"] - cate6[feature])
    else:
        D += cate6["doc_count"]
    if feature in cate7:
        C += cate7[feature]
        D += (cate7["doc_count"] - cate7[feature])
    else:
        D += cate7["doc_count"]

    #print("[0] ",A," : ",B," : ",C," : ",D)
    kai_result.append( round( ( 16000 * (((A * D) - (C * B))**2) ) / ( (A + C)*(B + D)*(A + B)*(C + D) ), 6) ) 
    # category1에 대한 값
    if feature in cate1:
        A = cate1[feature]
        B = cate1["doc_count"] - cate1[feature]
    else:
        A = 0
        B = cate1["doc_count"]
    C = 0
    D = 0
    if feature in cate0:
        C += cate0[feature]
        D += (cate0["doc_count"] - cate0[feature])
    else:
        D += cate0["doc_count"]
    if feature in cate2:
        C += cate2[feature]
        D += (cate2["doc_count"] - cate2[feature])
    else:
        D += cate2["doc_count"]
    if feature in cate3:
        C += cate3[feature]
        D += (cate3["doc_count"] - cate3[feature])
    else:
        D += cate3["doc_count"]
    if feature in cate4:
        C += cate4[feature]
        D += (cate4["doc_count"] - cate4[feature])
    else:
        D += cate4["doc_count"]
    if feature in cate5:
        C += cate5[feature]
        D += (cate5["doc_count"] - cate5[feature])
    else:
        D += cate5["doc_count"]
    if feature in cate6:
        C += cate6[feature]
        D += (cate6["doc_count"] - cate6[feature])
    else:
        D += cate6["doc_count"]
    if feature in cate7:
        C += cate7[feature]
        D += (cate7["doc_count"] - cate7[feature])
    else:
        D += cate7["doc_count"]

    #print("[1] ",A," : ",B," : ",C," : ",D)
    kai_result.append( round( ( 16000 * (((A * D) - (C * B))**2) ) / ( (A + C)*(B + D)*(A + B)*(C + D) ), 6) )
    # category2에 대한 값
    if feature in cate2:
        A = cate2[feature]
        B = cate2["doc_count"] - cate2[feature]
    else:
        A = 0
        B = cate2["doc_count"]
    C = 0
    D = 0
    if feature in cate1:
        C += cate1[feature]
        D += (cate1["doc_count"] - cate1[feature])
    else:
        D += cate1["doc_count"]
    if feature in cate0:
        C += cate0[feature]
        D += (cate0["doc_count"] - cate0[feature])
    else:
        D += cate0["doc_count"]    
    if feature in cate3:
        C += cate3[feature]
        D += (cate3["doc_count"] - cate3[feature])
    else:
        D += cate3["doc_count"]
    if feature in cate4:
        C += cate4[feature]
        D += (cate4["doc_count"] - cate4[feature])
    else:
        D += cate4["doc_count"]
    if feature in cate5:
        C += cate5[feature]
        D += (cate5["doc_count"] - cate5[feature])
    else:
        D += cate5["doc_count"]
    if feature in cate6:
        C += cate6[feature]
        D += (cate6["doc_count"] - cate6[feature])
    else:
        D += cate6["doc_count"]
    if feature in cate7:
        C += cate7[feature]
        D += (cate7["doc_count"] - cate7[feature])
    else:
        D += cate7["doc_count"]

    #print("[2] ",A," : ",B," : ",C," : ",D)
    kai_result.append( round( ( 16000 * (((A * D) - (C * B))**2) ) / ( (A + C)*(B + D)*(A + B)*(C + D) ), 6) )
    # category3에 대한 값
    if feature in cate3:
        A = cate3[feature]
        B = cate3["doc_count"] - cate3[feature]
    else:
        A = 0
        B = cate3["doc_count"]
    C = 0
    D = 0
    if feature in cate1:
        C += cate1[feature]
        D += (cate1["doc_count"] - cate1[feature])
    else:
        D += cate1["doc_count"]
    if feature in cate2:
        C += cate2[feature]
        D += (cate2["doc_count"] - cate2[feature])
    else:
        D += cate2["doc_count"]
    if feature in cate0:
        C += cate0[feature]
        D += (cate0["doc_count"] - cate0[feature])
    else:
        D += cate0["doc_count"]
    if feature in cate4:
        C += cate4[feature]
        D += (cate4["doc_count"] - cate4[feature])
    else:
        D += cate4["doc_count"]
    if feature in cate5:
        C += cate5[feature]
        D += (cate5["doc_count"] - cate5[feature])
    else:
        D += cate5["doc_count"]
    if feature in cate6:
        C += cate6[feature]
        D += (cate6["doc_count"] - cate6[feature])
    else:
        D += cate6["doc_count"]
    if feature in cate7:
        C += cate7[feature]
        D += (cate7["doc_count"] - cate7[feature])
    else:
        D += cate7["doc_count"]

    #print("[3] ",A," : ",B," : ",C," : ",D)
    kai_result.append( round( ( 16000 * (((A * D) - (C * B))**2) ) / ( (A + C)*(B + D)*(A + B)*(C + D) ), 6) )
    # category4에 대한 값
    if feature in cate4:
        A = cate4[feature]
        B = cate4["doc_count"] - cate4[feature]
    else:
        A = 0
        B = cate4["doc_count"]
    C = 0
    D = 0
    if feature in cate1:
        C += cate1[feature]
        D += (cate1["doc_count"] - cate1[feature])
    else:
        D += cate1["doc_count"]
    if feature in cate2:
        C += cate2[feature]
        D += (cate2["doc_count"] - cate2[feature])
    else:
        D += cate2["doc_count"]
    if feature in cate3:
        C += cate3[feature]
        D += (cate3["doc_count"] - cate3[feature])
    else:
        D += cate3["doc_count"]
    if feature in cate0:
        C += cate0[feature]
        D += (cate0["doc_count"] - cate0[feature])
    else:
        D += cate0["doc_count"]
    if feature in cate5:
        C += cate5[feature]
        D += (cate5["doc_count"] - cate5[feature])
    else:
        D += cate5["doc_count"]
    if feature in cate6:
        C += cate6[feature]
        D += (cate6["doc_count"] - cate6[feature])
    else:
        D += cate6["doc_count"]
    if feature in cate7:
        C += cate7[feature]
        D += (cate7["doc_count"] - cate7[feature])
    else:
        D += cate7["doc_count"]

    #print("[4] ",A," : ",B," : ",C," : ",D)
    kai_result.append( round( ( 16000 * (((A * D) - (C * B))**2) ) / ( (A + C)*(B + D)*(A + B)*(C + D) ), 6) )
    # category5에 대한 값
    if feature in cate5:
        A = cate5[feature]
        B = cate5["doc_count"] - cate5[feature]
    else:
        A = 0
        B = cate5["doc_count"]
    C = 0
    D = 0
    if feature in cate1:
        C += cate1[feature]
        D += (cate1["doc_count"] - cate1[feature])
    else:
        D += cate1["doc_count"]
    if feature in cate2:
        C += cate2[feature]
        D += (cate2["doc_count"] - cate2[feature])
    else:
        D += cate2["doc_count"]
    if feature in cate3:
        C += cate3[feature]
        D += (cate3["doc_count"] - cate3[feature])
    else:
        D += cate3["doc_count"]
    if feature in cate4:
        C += cate4[feature]
        D += (cate4["doc_count"] - cate4[feature])
    else:
        D += cate4["doc_count"]
    if feature in cate0:
        C += cate0[feature]
        D += (cate0["doc_count"] - cate0[feature])
    else:
        D += cate0["doc_count"]
    if feature in cate6:
        C += cate6[feature]
        D += (cate6["doc_count"] - cate6[feature])
    else:
        D += cate6["doc_count"]
    if feature in cate7:
        C += cate7[feature]
        D += (cate7["doc_count"] - cate7[feature])
    else:
        D += cate7["doc_count"]

    #print("[5] ",A," : ",B," : ",C," : ",D)
    kai_result.append( round( ( 16000 * (((A * D) - (C * B))**2) ) / ( (A + C)*(B + D)*(A + B)*(C + D) ), 6) )
    # category6에 대한 값
    if feature in cate6:
        A = cate6[feature]
        B = cate6["doc_count"] - cate6[feature]
    else:
        A = 0
        B = cate6["doc_count"]
    C = 0
    D = 0
    if feature in cate1:
        C += cate1[feature]
        D += (cate1["doc_count"] - cate1[feature])
    else:
        D += cate1["doc_count"]
    if feature in cate2:
        C += cate2[feature]
        D += (cate2["doc_count"] - cate2[feature])
    else:
        D += cate2["doc_count"]
    if feature in cate3:
        C += cate3[feature]
        D += (cate3["doc_count"] - cate3[feature])
    else:
        D += cate3["doc_count"]
    if feature in cate4:
        C += cate4[feature]
        D += (cate4["doc_count"] - cate4[feature])
    else:
        D += cate4["doc_count"]
    if feature in cate5:
        C += cate5[feature]
        D += (cate5["doc_count"] - cate5[feature])
    else:
        D += cate5["doc_count"]
    if feature in cate0:
        C += cate0[feature]
        D += (cate0["doc_count"] - cate0[feature])
    else:
        D += cate0["doc_count"]
    if feature in cate7:
        C += cate7[feature]
        D += (cate7["doc_count"] - cate7[feature])
    else:
        D += cate7["doc_count"]

    #print("[6] ",A," : ",B," : ",C," : ",D)
    kai_result.append( round( ( 16000 * (((A * D) - (C * B))**2) ) / ( (A + C)*(B + D)*(A + B)*(C + D) ), 6) )
    # category7에 대한 값
    if feature in cate7:
        A = cate7[feature]
        B = cate7["doc_count"] - cate7[feature]
    else:
        A = 0
        B = cate7["doc_count"]
    C = 0
    D = 0
    if feature in cate1:
        C += cate1[feature]
        D += (cate1["doc_count"] - cate1[feature])
    else:
        D += cate1["doc_count"]
    if feature in cate2:
        C += cate2[feature]
        D += (cate2["doc_count"] - cate2[feature])
    else:
        D += cate2["doc_count"]
    if feature in cate3:
        C += cate3[feature]
        D += (cate3["doc_count"] - cate3[feature])
    else:
        D += cate3["doc_count"]
    if feature in cate4:
        C += cate4[feature]
        D += (cate4["doc_count"] - cate4[feature])
    else:
        D += cate4["doc_count"]
    if feature in cate5:
        C += cate5[feature]
        D += (cate5["doc_count"] - cate5[feature])
    else:
        D += cate5["doc_count"]
    if feature in cate6:
        C += cate6[feature]
        D += (cate6["doc_count"] - cate6[feature])
    else:
        D += cate6["doc_count"]
    if feature in cate0:
        C += cate0[feature]
        D += (cate0["doc_count"] - cate0[feature])
    else:
        D += cate0["doc_count"]

    #print("[7] ",A," : ",B," : ",C," : ",D)
    kai_result.append( round( ( 16000 * (((A * D) - (C * B))**2) ) / ( (A + C)*(B + D)*(A + B)*(C + D) ), 6) )
    # max값 취하기
    dic_features[feature] = max(kai_result)

print(len(dic_features))
#for feature in dic_features:
#    print(dic_features[feature]," ")
sorted_features = {}
sorted_features.update(sorted(dic_features.items(), key=operator.itemgetter(1), reverse=True))
#dic_features = sorted(dic_features.items(), key=operator.itemgetter(1))

i = 0
for feature in sorted_features:
    print(feature,sorted_features[feature])
    i += 1
    if i == 100:
        break
    
sorted_list = []
for feature in sorted_features:
    sorted_list.append(feature)

index_features = {}
index = 0
for lst in sorted_list:
    index_features[lst] = index
    index += 1
    
#alpha_sorted_features = {}
#alpha_sorted_features.update(sorted(alpha_features.items(), key=operator.itemgetter(0)))

                             
#아웃풋 적기
# open file
f1 = open("HKIB-20000_001.txt",mode='r', encoding='utf-8', errors='strict', buffering=1)
f2 = open("HKIB-20000_002.txt",mode='r', encoding='utf-8', errors='strict', buffering=1)
f3 = open("HKIB-20000_003.txt",mode='r', encoding='utf-8', errors='strict', buffering=1)
f4 = open("HKIB-20000_004.txt",mode='r', encoding='utf-8', errors='strict', buffering=1)
output = open("train.txt",mode='w', encoding='utf-8')
data = f1.read()
data = data + f2.read()
data = data + f3.read()
data = data + f4.read()
data = data.split("\n")

# interating for each line of file
list_doc = []
str_doc = ""
check = 0
for line in data:
    line = line.replace(","," ")
    line = line.replace("."," ")
    line = line.replace("-"," ")
    line = line.replace("<"," ")
    line = line.replace(">"," ")
    line = line.replace('"'," ")
    line = line.replace("["," ")
    line = line.replace("]"," ")
    line = line.replace("/"," ")
    line = line.replace("{"," ")
    line = line.replace("}"," ")
    lineWords = line.split()
    if len(lineWords) > 0:
        if lineWords[0] == "#TEXT":
            check = 1
        elif lineWords[0] == "@DOCUMENT":
            check = 0
            list_doc.sort()
            if len(list_doc) > 0:
                for now in list_doc:
                    str_doc += str(now+1) + ":" + str(sorted_features[sorted_list[now]]) + " "
                str_doc += "\n"
                output.write(str_doc)
                str_doc = ""
                list_doc = []
        elif lineWords[0] == "#CAT'03:":
            cate = lineWords[1]
            if cate == "건강과":
                str_doc += "1 "
            elif cate == "경제":
                str_doc += "2 "
            elif cate == "과학":
                str_doc += "3 "
            elif cate == "교육":
                str_doc += "4 "
            elif cate == "문화와":
                str_doc += "5 "
            elif cate == "사회":
                str_doc += "6 "
            elif cate == "산업":
                str_doc += "7 "
            elif cate == "여가생활":
                str_doc += "8 "
        if check == 1 and lineWords[0] != "#TEXT":
            for word in lineWords:
                index = index_features[word]
                #index = sorted_list.index(word)
                if list_doc.count(index) == 0:
                    list_doc.append(index)

#file.close()
f1.close()
f2.close()
f3.close()
f4.close()
output.close()

print("!!!!!!!!트레이닝 끝!")
# test file 만들기
# open file
test_file = open("HKIB-20000_005.txt",mode='r', encoding='utf-8', errors='strict', buffering=1)
test_output = open("test.txt",mode='w', encoding='utf-8')

# interating for each line of file
list_doc = []
str_doc = ""
check = 0
for line in test_file:
    line = line.replace(","," ")
    line = line.replace("."," ")
    line = line.replace("-"," ")
    line = line.replace("<"," ")
    line = line.replace(">"," ")
    line = line.replace('"'," ")
    line = line.replace("["," ")
    line = line.replace("]"," ")
    line = line.replace("/"," ")
    line = line.replace("{"," ")
    line = line.replace("}"," ")
    lineWords = line.split()
    if len(lineWords) > 0:
        if lineWords[0] == "#TEXT":
            check = 1
        elif lineWords[0] == "@DOCUMENT":
            check = 0
            list_doc.sort()
            #print(len(list_doc))
            if len(list_doc) > 0:
                for now in list_doc:
                    str_doc += str(now+1) + ":" + str(sorted_features[sorted_list[now]]) + " "
                str_doc += "\n"
                test_output.write(str_doc)
                str_doc = ""
                list_doc = []
        elif lineWords[0] == "#CAT'03:":
            cate = lineWords[1]
            if cate == "건강과":
                str_doc += "1 "
            elif cate == "경제":
                str_doc += "2 "
            elif cate == "과학":
                str_doc += "3 "
            elif cate == "교육":
                str_doc += "4 "
            elif cate == "문화와":
                str_doc += "5 "
            elif cate == "사회":
                str_doc += "6 "
            elif cate == "산업":
                str_doc += "7 "
            elif cate == "여가생활":
                str_doc += "8 "
        if check == 1 and lineWords[0] != "#TEXT":
            for word in lineWords:
                if word in index_features:
                    index = index_features[word]
                    #index = sorted_list.index(word)
                    if list_doc.count(index) == 0:
                        list_doc.append(index)

test_file.close()
test_output.close()
