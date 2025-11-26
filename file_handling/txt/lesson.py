#                                                       ( txt ) <-------->

#
# a = open('hello.txt', 'w+', encoding='utf-8')
# a.write('Aisaev Izat    мен айтиде окууйм')
# a.seek(0)
# print(a.read())
# a.close()
#

# a = open('hello.txt', 'r',)
# print(a.read())
# a.close()
#
#


# with open('hello.txt', 'w+', encoding='utf-8') as a:
#     a.write('изат 2009 аркгар оыврао авлпорукшг')
#     a.seek(0)
#     print(a.readline(10))






































#                                         1-ex
# # f = open("text.txt", "r", encoding="utf-8")          # <-- okuu
# print(f.read())
# f.close()



# #                                         2-ex
# f = open("text.txt", "w", encoding="utf-8")            # <-- jazuu
# f.write("Привет мир!\nPython лучший язык!")
# f.close()


#
# #                                          3-ex
# for line in open("text.txt", encoding="utf-8"):
#     print(line.strip())


#
# #                                          4-ex
# print(len(open("text.txt", encoding="utf-8").readlines()))


#
# #                                          5-ex
# print(len(open("text.txt", encoding="utf-8").read().split()))

#
# #                                          6-ex
# print(len(open("text.txt", encoding="utf-8").read()))

#
# #                                          7-ex
# text = open("text.txt", encoding="utf-8").read().replace("Привет", "Здравствуйте")
# open("text.txt", "w", encoding="utf-8").write(text)

#
# #                                          8-ex
# lines = open('text.txt', encoding='utf-8').readlines()
# open('text.txt', 'w', encoding='utf-8').writelines([l for l in lines if 'Python' not in l])

#
# #                                          9-ex
#

#
#
# #                                          10-ex
# open('text.txt', 'w', encoding='utf-8').writelines(sorted(open('text.txt', encoding='utf-8').readlines()))
#
#





