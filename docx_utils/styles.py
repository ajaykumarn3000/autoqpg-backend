# styles.py
from docx.enum.style import WD_STYLE_TYPE
from docx.enum.text import WD_PARAGRAPH_ALIGNMENT
from docx.shared import Pt


def add_styles(document):
    styles = document.styles

    title_style = styles.add_style("title", WD_STYLE_TYPE.PARAGRAPH)
    title_style.font.size = Pt(14)
    title_style.font.name = "Times New Roman"
    title_style.font.bold = True
    title_style.paragraph_format.alignment = WD_PARAGRAPH_ALIGNMENT.CENTER
    title_style.paragraph_format.space_after = Pt(0)

    acad_year_style = styles.add_style("acad_year", WD_STYLE_TYPE.PARAGRAPH)
    acad_year_style.font.size = Pt(11)
    acad_year_style.font.name = "Times New Roman"
    acad_year_style.paragraph_format.alignment = WD_PARAGRAPH_ALIGNMENT.CENTER
    acad_year_style.paragraph_format.space_before = Pt(0)

    table_style = styles.add_style("table", WD_STYLE_TYPE.TABLE)
    table_style.font.size = Pt(11)
    table_style.font.name = "Times New Roman"
    table_style.paragraph_format.space_after = Pt(0)

    instruction_title_style = styles.add_style("instruction_title", WD_STYLE_TYPE.CHARACTER)
    instruction_title_style.font.size = Pt(11)
    instruction_title_style.font.name = "Times New Roman"
    instruction_title_style.font.bold = True

    instruction_body_style = styles.add_style("instruction_body", WD_STYLE_TYPE.CHARACTER)
    instruction_body_style.font.size = Pt(11)
    instruction_body_style.font.name = "Times New Roman"
    instruction_body_style.font.bold = False

    note_title_style = styles.add_style("note_title", WD_STYLE_TYPE.CHARACTER)
    note_title_style.font.size = Pt(11)
    note_title_style.font.name = "Times New Roman"
    note_title_style.font.bold = True

    note_body_style = styles.add_style("note_body", WD_STYLE_TYPE.CHARACTER)
    note_body_style.font.size = Pt(11)
    note_body_style.font.name = "Times New Roman"
    note_body_style.font.bold = False

    ques_table_heading_style = styles.add_style("ques_table_head", WD_STYLE_TYPE.PARAGRAPH)
    ques_table_heading_style.font.size = Pt(11)
    ques_table_heading_style.font.name = "Times New Roman"
    ques_table_heading_style.font.bold = True
    ques_table_heading_style.paragraph_format.alignment = WD_PARAGRAPH_ALIGNMENT.CENTER

    ques_table_body_style = styles.add_style("ques_table_body", WD_STYLE_TYPE.PARAGRAPH)
    ques_table_body_style.font.size = Pt(11)
    ques_table_body_style.font.name = "Times New Roman"
    ques_table_body_style.font.bold = False
    ques_table_body_style.paragraph_format.alignment = WD_PARAGRAPH_ALIGNMENT.LEFT

    ques_table_body_center_style = styles.add_style("ques_table_body_center", WD_STYLE_TYPE.PARAGRAPH)
    ques_table_body_center_style.font.size = Pt(11)
    ques_table_body_center_style.font.name = "Times New Roman"
    ques_table_body_center_style.font.bold = False
    ques_table_body_center_style.paragraph_format.alignment = WD_PARAGRAPH_ALIGNMENT.CENTER
