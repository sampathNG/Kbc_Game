questions = [
"1. Former Australian captain Mark Taylor has had several nicknames over his playing career. Which of the following was NOT one of them", 
"2 . Which was the 1st non Test playing country to beat India in an international match" , 
"3 . Track and field star Carl Lewis won how many gold medals at the 1984 Olympic games" ,
 "4 . Which county did Ravi Shastri play for",
 "5 . Who was the first Indian to win the World Amateur Billiards title",
 "6 . Who is the first Indian woman to win an Asian Games gold in 400m run",
 "7. Which two counties did Kapil Dev play",
 "8. When was Amateur Athletics Federation of India established" , 
 "9. Who did Stone Cold Steve Austin wrestle at the 1998 edition of Over the Edge",
 "10. Ricky Ponting is also known as what",
 "11. How long are professional Golf Tour players allotted per shot",
 "12. Which NBA player scored 8 points in the final 7 seconds of a game to lead his team to victory",
 "13. The ratio of width of our National flag to its length is",
 "14. Rabindranath Tagore's 'Jana Gana Mana' has been adopted as India's National Anthem. How many stanzas of the said song were adopted",
 "15. Natya - Shastra the main source of India's classical dances was written by"
 ]

first_options = ["1. Tubby" , "1. Canada" , "1. Two" , "1. Leicestershire" , "1. Geet Sethi" , "1. M.L.Valsamma" , "1. Northamptonshire & Worcestershire" , "1. 1936" , "1. Cactus Jack" , "1. The Rickster" , "1. 45 seconds" ,"1. Baron Davis" , "1. 3:5" , "1. Only the first stanza" , "1. Nara Muni"]
second_options = ["2. Stodge" , "2. Sri Lanka" , "2. Three" , "2. Glamorgan" , "2. Wilson Jones" , "2. P.T.Usha" , "2. Northamptonshire & Warwickshire" , "2. 1946" , "2. Mankind" , "2. Ponts" , "2. 25 seconds" , "2. Kevin Garnett" , "2. 2:3" , "2. The whole song" , "2. Bharat Muni"]
third_options = ["3. Helium Bat" , "3. Zimbabwe" , "3. Four" , "3. Gloucestershire" , "3. Michael Ferreira" , "3. Kamaljit Sandhu" , "3. Nottinghamshire & Worcestershire" , "3. 1956" , "3. Dude Love" , "3. Ponter" , "3. 1 minute" , "3. Stephon Maurbury" , "3. 2:4" , "3. Third and Fourth stanza" , "3. Abhinav Gupt"]
fourth_options = ["4. Stumpy" , "4. East Africa" , "4. Eight" , "4. Lancashire" , "4. Manoj Kothari" ,"4. K.Malleshwari" , "4. Nottinghamshire & Warwickshire" , "4. 1966" , "4. Mick Foley" , "4. Punter" , "4. 2 minutes" , "4. Reggie Miller" , "4. 3:4" , "4. First and Second stanza", "4. Tandu Muni"]
all_options = [first_options , second_options , third_options , fourth_options]
correct_answers = 0
ans_key = [4 , 2 , 3 , 2 , 2 , 4 , 1 , 2 , 3, 4 , 1 , 4 , 2 , 1, 2]
winer_price = [1000,2000,3000,5000,10000,20000,40000,80000,160000,320000,640000,1250000,250000,5000000,10000000]
print (ans_key)
answers_list = []
list_len = len(questions)
i = 0
sum = 0
while i < list_len:
  print (questions[i])
  print("select option:-")
  print()
  print (first_options[i])
  print (second_options[i])
  print (third_options[i])
  print (fourth_options[i])
  ans = int(input(" enter correct answers "))
  answers_list.append(ans)
  if ans_key[i] == ans:
    correct_answers+=1
    print ("Congrats! your answer is corrrect " , winer_price[i] , "winer price aapko mila hai" , correct_answers , "answer sahi hey aapka")
    sum += winer_price[i]
    if i == 4:
      print ("Congrats! you cleared first round.")
    elif i == 9:
      print ("Congrats! you cleared second round.")
    elif i == 14:
      print ("Congrats! you won 1 crore ruppe in kbc." )
  else:
    print ("your answer is wrong\nyou won cash prize of" , sum ,"ruppes")
    break
  i = i + 1