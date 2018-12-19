import json
import os

nine_deck='''\\documentclass [a4paper] {article} % landscape
\\input {../../latex/packages}
\\input {../../latex/tikzcards}
\\geometry {hmargin = 5mm, vmargin = 10mm}
\\begin {document}
\\begin {center}
  \\begin {tabular}{@{}c@{\\hspace {2mm}}c@{\\hspace {2mm}}c@{}}
  \\input {./0_front.tex} &
  \\input {./1_front.tex} &
  \\input {./2_front.tex} \\\\
  \\input {./3_front.tex} &
  \\input {./4_front.tex} &
  \\input {./5_front.tex} \\\\
  \\input {./6_front.tex} &
  \\input {./7_front.tex} &
  \\input {./8_front.tex} \\\\
  \\end {tabular}
\\end {center}
\\begin {center}
  \\begin {tabular}{@{}c@{\\hspace {2mm}}c@{\\hspace {2mm}}c@{}}
  \\input {./2_back.tex} &
  \\input {./1_back.tex} &
  \\input {./0_back.tex} \\\\
  \\input {./5_back.tex} &
  \\input {./4_back.tex} &
  \\input {./3_back.tex} \\\\
  \\input {./8_back.tex} &
  \\input {./7_back.tex} &
  \\input {./6_back.tex} \\\\
  \\end {tabular}
\\end {center}
\\end {document}'''

deck_front='''\\begin{{tikzpicture}}
  \\cardborder
  \\cardtype{{rulesbg}}{{{horizontal}}}
  \\cardcontent{{}}{{{front_text}}}
\\end{{tikzpicture}}'''

deck_back='''\\begin{{tikzpicture}}
  \\cardborder
  \\cardtype{{rulesbg}}{{{horizontal}}}
  \\cardcontent{{}}{{{back_text}}}
\\end{{tikzpicture}}'''

def first_nine(list_):
     num=0
     while num < len(list_):
         yield list_[num:num+9]
         num += 9



def create_dir_write_nine_deck(subdir,items):
    path_ = os.path.join(os.getcwd(),subdir['deck_dir'])
    os.makedirs(path_,exist_ok=True)
    file_name=os.path.join(path_,'nine_deck.tex')
    f=open(file_name,'w',encoding='utf-8')
    f.write(nine_deck)
    f.close()

    for idx,x in enumerate(items):
        file_name_front = os.path.join(path_,'{0}_front.tex'.format(idx))
        file_name_back  = os.path.join(path_,'{0}_back.tex'.format(idx))
        front=open(file_name_front,'w',encoding='utf-8')
        back=open(file_name_back,'w',encoding='utf-8')
        x['back_text'] = '\n'.join(x['back'])
        x['front_text'] = '\n'.join(x['front'])
        front.write(deck_front.format(**x))
        back.write(deck_back.format(**x))
        front.close()
        back.close()
        print(idx)
    #print(nine_deck.format(**subdir))

def main():
    f=open('data.json','r',encoding='utf-8')
    data=json.load(f)

    g=first_nine(data)

    for idx,item in enumerate(g):
        print(idx)
        subdir={'deck_dir': 'tex_out/subdir_{0}'.format(idx)}
    
        create_dir_write_nine_deck(subdir,item)

if __name__ == "__main__":
    main()