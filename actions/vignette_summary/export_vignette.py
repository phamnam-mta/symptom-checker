import os
from fpdf import FPDF, HTMLMixin
from typing import Any, Text, Dict, List

from actions.vignette_summary.constants import FONT_PATH, LOGO_PATH, REPORT_PATH, INTENT2WORD
from actions.vignette_summary.vignette_template import VS_HTML, QUESTIONNAIRE_HTML

class MyFPDF(FPDF, HTMLMixin): pass

def from_intent_to_word(intent):
    try:
        return INTENT2WORD[intent]
    except:
        return intent

def prettier_question(question):
    if '-' in question:
        question = question.replace('-','\n -')

    return question
    
def generate_report(user_info: Dict, 
                    chief_complain: Text,
                    qa_pairs: List, 
                    suggestions: Text):
    pdf=MyFPDF()
    # load the unicode font
    pdf.add_font('DejaVu', '', FONT_PATH, uni=True)
    pdf.add_page()

    name = user_info.get("name", "Nguyễn Văn A")
    age = user_info.get("age", "")
    gender = user_info.get("gender", "")
    questionnaire = "".join([QUESTIONNAIRE_HTML.format(question=p.get("question", ""), answer=from_intent_to_word(p.get("answer", ""))) 
    for p in qa_pairs])
    pdf.write_html(VS_HTML.format(logo=LOGO_PATH,
    name=name, 
    age=age, 
    gender=gender,
    chief_complain=chief_complain,
    questionnaire=questionnaire, 
    suggestions=suggestions))

    if not os.path.exists(REPORT_PATH):
        os.makedirs(REPORT_PATH)
    fn = os.path.join(REPORT_PATH, f'{name}.pdf')
    pdf.output(fn,'F')
        
    try:
        os.startfile(fn)
    except:
        os.system("xdg-open \"%s\"" % fn)