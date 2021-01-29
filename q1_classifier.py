import csv
from math import log2


test_att1= []
test_att2= []
test_att3= []
test_att4= []
test_att5= []
test_att6= []
test_att7= []
test_att8= []
test_att9= []
test_att10= []



        

def select_node(node, target):
    
    result=[]
    pos=0
    neg=0
    avg_pos=0
    avg_neg=0
    q=0
    t_target=[]
    with open('test_label.csv', newline='') as csvfile5:
            tlabeldata = csv.reader(csvfile5)
            for label in tlabeldata:
                t_target.append(int(label[0]))
    with open('test.csv', newline='') as csvfile4:
        testdata= csv.reader(csvfile4)
        for column in testdata:
                if q!=0:
                    test_att1.append(int(column[0][0]))
                    test_att2.append(int(column[0][10]))
                    test_att3.append(int(column[0][30]))
                    test_att4.append(int(column[0][40]))
                    test_att5.append(int(column[0][50]))
                    test_att6.append(int(column[0][60]))
                    test_att7.append(int(column[0][90]))
                    test_att8.append(int(column[0][100]))
                    test_att9.append(int(column[0][130]))
                    test_att10.append(int(column[0][140]))
                q=q+1
        for g in range(0,10):
            p=0
            n=0
            for c in range(0,24999):
                if (test_att1[c]==att1[c]
                and test_att2[c]==att2[c]
                and test_att3[c]==att3[c]
                and test_att4[c]==att4[c]
                and test_att5[c]==att5[c]
                and test_att6[c]==att6[c]
                and test_att7[c]==att7[c]
                and test_att8[c]==att8[c]
                and test_att9[c]==att9[c]
                and test_att10[c]==att10[c]
                and node[g]==gain10
                and t_target[c]==1):
                    p=p+1
                elif (test_att1[c]==att1[c]
                and test_att2[c]==att2[c]
                and test_att3[c]==att3[c]
                and test_att4[c]==att4[c]
                and test_att5[c]==att5[c]
                and test_att6[c]==att6[c]
                and test_att7[c]==att7[c]
                and test_att8[c]==att8[c]
                and test_att9[c]==att9[c]
                and test_att10[c]==att10[c]
                and node[g]==gain10
                and t_target[c]==0):
                    n=n+1
                else:
                    continue
                        
            
            pos=pos+p
            neg=neg+n
    good_prediction= pos+neg
    
    
    print("\n\n\n Positive while testing: ",pos)
    print(" Negative while Testing: ",neg)
    print(" Total number of perfect prediction", good_prediction)

    
    tp=0
    tn=0
    for w in range(0,25000):
        if t_target[w]==1:
            tp= tp+1
        elif t_target[w]==0:
            tn=tn+1
        w=w+1
    print("\n\n\n Number of Positive in Test Label File: ",tp)
    print(" Number of Negative in Test label File: ", tn)
    print(" Total number of prediction=", tp+tn)
    accuracy= (good_prediction/(tp+tn))*100
    accuracy_pos= (pos/tp)*100
    accuracy_neg= (neg/tn)*100
    print(" \n\n\n Accuracy for getting Positive= ", accuracy_pos, "%")
    print(" \n\n\n Accuracy for getting negative= ", accuracy_neg, "%")
    print(" \n\n\n Overall Accuracy= ", accuracy, "%")
    print("\n\n\n")
    
            
    return accuracy

def calculate(attribute, target):
    c1=attribute.count(1)
    c2=attribute.count(2)
    c3=attribute.count(3)
    c4=attribute.count(4)
    c5=attribute.count(5)
    entropy= 0
    for num in range(1,6):
        print(" For ", num, ":")
        pi=0
        ni=0
        for it1 in range(0,39999):
            if attribute[it1]==num and target[it1]==1:
                pi=pi+1
            if attribute[it1]==num and target[it1]==0:
                ni=ni+1
        print(pi)
        print(ni)
        if pi!=0 and ni!=0 :
            Infogain= ((-pi/(pi+ni))*(log2(pi/(pi+ni))))-((ni/(pi+ni))*(log2(ni/(pi+ni))))
        elif pi==0 and ni==0 :
            Infogain=0
        print(" Infogain for", num, "=", Infogain)

        insert_in_entropy= ((pi+ni)/(p+n))*Infogain
        entropy= entropy+ insert_in_entropy
    print(entropy)
    gain= class_entropy- entropy

    print("gain = ", gain)
    
    return gain


att1= []
att2= []
att3= []
att4= []
att5= []
att6= []
att7= []
att8= []
att9= []
att10= []
att_list=[]


target= []
k=0
gain_list=[]
i=0
j=0
p=0
n=0

with open('train_label.csv', newline='') as csvfile:
    data = list(csv.reader(csvfile))

    for i in range(0,40000):
        if data[i]==['1']:
            p = p + 1
        elif data[i]==['0']:
            n = n + 1
print(" Positive:", p)
print(" Negative:", n)


class_entropy =((-p/(p+n))*(log2(p/(p+n))))-((n/(p+n))*(log2(n/(p+n))))
print(" Class Entropy=", class_entropy)

with open('train_label.csv', newline='') as csvfile:
    labeldata = csv.reader(csvfile)

    for label in labeldata:
        target.append(int(label[0]))


    
with open('train.csv', newline='') as csvfile2:
        traindata= csv.reader(csvfile2)
        for column in traindata:
                if k!=0:
                    att1.append(int(column[0][0]))
                    att2.append(int(column[0][10]))
                    att3.append(int(column[0][30]))
                    att4.append(int(column[0][40]))
                    att5.append(int(column[0][50]))
                    att6.append(int(column[0][60]))
                    att7.append(int(column[0][90]))
                    att8.append(int(column[0][100]))
                    att9.append(int(column[0][130]))
                    att10.append(int(column[0][140]))
                k=k+1
        gain1 = (calculate(att1, target))
        gain2 = (calculate(att2, target))
        gain3 = (calculate(att3, target))
        gain4 = (calculate(att4, target))
        gain5 = (calculate(att5, target))
        gain6 = (calculate(att6, target))
        gain7 = (calculate(att7, target))
        gain8 = (calculate(att8, target))
        gain9 = (calculate(att9, target))
        gain10 = (calculate(att10, target))
        nodes_gain=[gain1, gain2, gain3, gain4, gain5, gain6, gain7, gain8, gain9, gain10]
        max_gain=max(nodes_gain)
        print(max_gain)
        nodes_gain.sort(reverse=True)
        print("Sorted Nodes and their Gains: ", nodes_gain)

        select_node(nodes_gain, target)
        
        
    
