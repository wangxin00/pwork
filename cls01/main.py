import re  
email_re = re.compile(  
    r"(([-!#$%&'*+/=?^_`{}|~0-9A-Z]+(\.[-!#$%&'*+/=?^_`{}|~0-9A-Z]+)*"  # dot-atom  
    r'|^"([\001-\010\013\014\016-\037!#-\[\]-\177]|\\[\001-011\013\014\016-\177])*"' # quoted-string  
    r')@(?:[A-Z0-9]+(?:-*[A-Z0-9]+)*\.)+[A-Z]{2,6})', re.IGNORECASE)  # domain  
  
email_text1= "我的电子邮件tom@gmail.com。"
email_list1 = []  
  
for one in email_re.findall(email_text1):  
    email_list1.append(one[0])   
print ("我的电子邮件" )
print(email_list1)
email_text2="将什么发送到jerry123@163.com或者3123432@qq.com."
email_list2 = []    
for one in email_re.findall(email_text2):  
    email_list2.append(one[0])
print ("将什么发送到" )    
print(email_list2)
s = '若遇特殊情况打电话给182123445678.'

number=re.findall(r'\d+', s)
print("若遇特殊情况打电话给")
print(number)
